#!/usr/bin/env python3
"""
Send one section of a daily AI/LLM edition to a Telegram channel.

This project runs 3 times a day. Each run writes its own section under a
run-stamped heading (`## Telegram — Run HH:MM`) and sends only that section.
Fridays also carry a `## Telegram — Take Post` (the weekly take). The
`## Notes` section is archive-only and is never sent.

Usage:
  scripts/send-to-telegram.py editions/YYYY-MM-DD.md --run HH:MM
  scripts/send-to-telegram.py editions/YYYY-MM-DD.md --section take

  --run HH:MM      send only the `## Telegram — Run HH:MM` section
  --section take   send only the `## Telegram — Take Post` section

A run section whose body is a SKIPPED stub (starts with "SKIPPED") is never
sent — the script exits 0 without calling Telegram.

Reads:
  TELEGRAM_BOT_TOKEN  -- from @BotFather
  TELEGRAM_CHAT_ID    -- channel/group ID the bot was added to (admin)

The script extracts the requested section, sends it as one message (URL on its
own line, link previews disabled), and records it in .sent-log so a re-fire of
the same (edition, section, content) is a no-op.
"""

import hashlib
import html
import os
import re
import subprocess
import sys
import time
from pathlib import Path


def load_dotenv():
    """Load .env from the project root into os.environ, if present."""
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


# Per-post hard cap: Telegram allows 4096, but the briefing format is 280
# chars excluding the URL. We pad generously for the URL line.
TELEGRAM_LIMIT = 4000

# A run section whose body begins with this marker is intentionally empty
# (no material movement this slot) and must never be sent.
SKIP_MARKER = "SKIPPED"

# Heading for the weekly take post (Friday only).
TAKE_HEADING = "## Telegram — Take Post"


def run_heading(hhmm: str) -> str:
    """Build the run-stamped section heading the skill writes."""
    return f"## Telegram — Run {hhmm}"


def extract_section(md: str, heading: str) -> str | None:
    """
    Return the body of the section starting at `heading`, stopping at the next
    "## " heading or end of file. Returns None if the heading isn't found.
    Heading match is exact on the line (after stripping).
    """
    lines = md.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == heading:
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break
    body = "\n".join(lines[start:end]).strip()
    return body or None


def md_to_html(md: str) -> str:
    """Convert a small subset of markdown to Telegram-flavoured HTML."""
    text = md.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # Links: [label](url) -> <a href="url">label</a>
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        text,
    )

    # Bold: **text** -> <b>text</b>
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)

    # Italic: *text* -> <i>text</i>  (avoid ** remnants)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<i>\1</i>", text)

    # Collapse 3+ blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def send(token: str, chat_id: str, text: str, disable_preview: bool = True):
    """POST via curl — uses the macOS system trust store, avoiding Python SSL
    issues that can occur behind corporate proxies."""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    result = subprocess.run(
        [
            "curl", "-sS", "--fail-with-body", "--max-time", "30",
            "-X", "POST", url,
            "--data-urlencode", f"chat_id={chat_id}",
            "--data-urlencode", f"text={text}",
            "--data-urlencode", "parse_mode=HTML",
            "--data-urlencode",
            f"disable_web_page_preview={'true' if disable_preview else 'false'}",
        ],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Telegram API error: {result.stdout or result.stderr}")
    return result.stdout


def parse_args(argv: list[str]) -> tuple[str, str, str]:
    """Return (path, label, heading) for the one section to send."""
    if len(argv) == 4 and argv[2] == "--run":
        hhmm = argv[3]
        if not re.fullmatch(r"\d{2}:\d{2}", hhmm):
            print("error: --run expects HH:MM (e.g. 20:00)", file=sys.stderr)
            sys.exit(2)
        return argv[1], f"Run {hhmm}", run_heading(hhmm)
    if len(argv) == 4 and argv[2] == "--section" and argv[3] == "take":
        return argv[1], "Take Post", TAKE_HEADING
    print(
        "usage: send-to-telegram.py <edition.md> (--run HH:MM | --section take)",
        file=sys.stderr,
    )
    sys.exit(2)


def main():
    path, label, heading = parse_args(sys.argv)
    load_dotenv()
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print(
            "error: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set",
            file=sys.stderr,
        )
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        md = f.read()

    body = extract_section(md, heading)
    if body is None:
        print(f"error: missing section '{heading}' in {path}", file=sys.stderr)
        sys.exit(3)

    if body.lstrip().startswith(SKIP_MARKER):
        print(f"skipped {label} (SKIPPED stub — no material movement, nothing to send)")
        return

    if len(body) > TELEGRAM_LIMIT:
        print(
            f"error: {label} section exceeds {TELEGRAM_LIMIT} chars after parsing",
            file=sys.stderr,
        )
        sys.exit(4)

    # Idempotency guard. Refuse to resend the same (edition, section, content)
    # combo. Survives stale routine prompts and accidental double-runs.
    log_path = Path(__file__).resolve().parent.parent / ".sent-log"
    sent_keys = set()
    if log_path.exists():
        sent_keys = {line.strip() for line in log_path.read_text().splitlines() if line.strip()}

    edition_name = Path(path).name
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()[:12]
    key = f"{edition_name}\t{label}\t{digest}"
    if key in sent_keys:
        print(f"skipped {label} (already sent, see .sent-log)")
        return

    send(token, chat_id, md_to_html(body))
    with log_path.open("a", encoding="utf-8") as f:
        f.write(key + "\n")
    print(f"sent {label} ({len(body)} chars)")


if __name__ == "__main__":
    main()
