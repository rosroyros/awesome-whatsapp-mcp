#!/usr/bin/env python3
"""Read a local WhatsApp TXT/ZIP export and write one JSON object per message."""

import argparse
from datetime import date, datetime
import json
from pathlib import Path
import re
import sys
import zipfile


# Remove display-direction controls, not ordinary whitespace or message content.
MARKS = str.maketrans("", "", "\u200e\u200f\ufeff")
STAMP = (
    r"(?P<date_raw>(?P<a>\d{1,2})/(?P<b>\d{1,2})/(?P<year>\d{4}|\d{2})"
    r",?\s+(?P<hour>\d{1,2}):(?P<minute>\d{2})(?::(?P<second>\d{2}))?"
    r"(?:\s*(?P<ampm>AM|PM))?)"
)
HEADERS = (
    re.compile(r"^\s*\[" + STAMP + r"\]\s*(?P<body>.*)$", re.IGNORECASE),
    re.compile(r"^\s*" + STAMP + r"\s+-\s+(?P<body>.*)$", re.IGNORECASE),
)
MEDIA = re.compile(
    r"(?:<\s*media omitted\s*>|\b(?:image|video|audio|sticker|GIF|document|contact) omitted\b)",
    re.IGNORECASE,
)


def read_export(path):
    """Choose one ZIP member and read it in memory; never extract any files."""
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as archive:
            candidates = [item for item in archive.infolist()
                          if not item.is_dir() and item.filename.lower().endswith(".txt")]
            if not candidates:
                raise ValueError("ZIP contains no .txt file")
            preferred = [item for item in candidates
                         if Path(item.filename).name.lower() == "_chat.txt"]
            chosen = sorted(preferred or candidates,
                            key=lambda item: (-item.file_size, item.filename))[0]
            print("Reading ZIP member: " + chosen.filename, file=sys.stderr)
            data = archive.read(chosen)
    elif path.suffix.lower() == ".txt":
        data = path.read_bytes()
    else:
        raise ValueError("input must be a .txt or .zip file")
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        print("Warning: invalid UTF-8 bytes replaced with U+FFFD; check the source file.",
              file=sys.stderr)
        return data.decode("utf-8-sig", errors="replace")


def header(line):
    for pattern in HEADERS:
        match = pattern.match(line)
        if match:
            return match
    return None


def detect_order(lines):
    evidence = set()
    for line in lines:
        match = header(line)
        if match:
            a, b = int(match["a"]), int(match["b"])
            if 12 < a <= 31 and 1 <= b <= 12:
                evidence.add("dmy")
            elif 12 < b <= 31 and 1 <= a <= 12:
                evidence.add("mdy")
    if len(evidence) == 1:
        return evidence.pop()
    reason = "conflicting date values" if evidence else "no date value disambiguates day/month"
    print("Warning: " + reason + "; falling back to dmy. Override with --date-order mdy or dmy.",
          file=sys.stderr)
    return "dmy"


def timestamp(match, order):
    a, b = int(match["a"]), int(match["b"])
    day, month = (a, b) if order == "dmy" else (b, a)
    year = int(match["year"])
    if len(match["year"]) == 2:
        year += 2000
    hour = int(match["hour"])
    if match["ampm"]:
        if not 1 <= hour <= 12:
            return None
        hour = hour % 12 + (12 if match["ampm"].upper() == "PM" else 0)
    try:
        return datetime(year, month, day, hour, int(match["minute"]),
                        int(match["second"] or 0)).isoformat()
    except ValueError:
        return None


def parse_export(text, order="auto"):
    lines = text.translate(MARKS).splitlines()
    if order == "auto" and lines:
        order = detect_order(lines)
    records = []
    for line in lines:
        match = header(line)
        if match:
            body = match["body"]
            sender, separator, message = body.partition(": ")
            # A sender's empty message is valid too: "Name:".
            if not separator and body.endswith(":"):
                sender, separator, message = body[:-1], ":", ""
            has_sender = bool(separator and sender.strip())
            records.append({
                "ts": timestamp(match, order), "date_raw": match["date_raw"],
                "sender": sender.strip() if has_sender else None,
                "text": message if has_sender else body, "system": not has_sender,
            })
        elif records:
            records[-1]["text"] += "\n" + line
        else:
            records.append({"ts": None, "date_raw": None, "sender": None,
                            "text": line, "system": True})
    for record in records:
        if MEDIA.search(record["text"]):
            record["media"] = True
    return records


def since_date(value):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise argparse.ArgumentTypeError("--since must be YYYY-MM-DD")
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as error:
        raise argparse.ArgumentTypeError("--since must be a valid date") from error


def last_count(value):
    try:
        number = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("--last must be a nonnegative integer") from error
    if number < 0:
        raise argparse.ArgumentTypeError("--last must be a nonnegative integer")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="local .txt or .zip WhatsApp export")
    parser.add_argument("--date-order", choices=("dmy", "mdy"), default="auto",
                        help="override automatic day/month detection")
    parser.add_argument("--since", type=since_date, metavar="YYYY-MM-DD",
                        help="keep messages on/after this date; undated messages are retained")
    parser.add_argument("--last", type=last_count, metavar="N",
                        help="keep the last N records in file order, after --since")
    args = parser.parse_args()
    try:
        records = parse_export(read_export(args.path), args.date_order)
    except (OSError, ValueError, zipfile.BadZipFile, RuntimeError, NotImplementedError) as error:
        parser.error(str(error))
    if args.since:
        records = [record for record in records
                   if record["ts"] is None or record["ts"][:10] >= args.since]
    if args.last is not None:
        records = records[-args.last:] if args.last else []
    for record in records:
        print(json.dumps(record, ensure_ascii=False))


if __name__ == "__main__":
    main()
