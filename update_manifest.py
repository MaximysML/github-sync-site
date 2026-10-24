#!/usr/bin/env python3
"""Обновляет updates.json после замены установщиков в downloads/."""

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True, help="Например: 2.2.0")
    parser.add_argument("--android-code", required=True, type=int, help="Новый versionCode APK")
    parser.add_argument("--notes", default="", help="Описание обновления")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    downloads = root / "downloads"
    windows = downloads / "GitHubSync-Setup.exe"
    android = downloads / "GitHubSync-Remote.apk"
    for path in (windows, android):
        if not path.is_file():
            raise SystemExit(f"Файл не найден: {path}")

    manifest = {
        "schemaVersion": 1,
        "windows": {
            "version": args.version,
            "url": "downloads/GitHubSync-Setup.exe",
            "sha256": sha256(windows),
            "notes": args.notes,
        },
        "android": {
            "version": args.version,
            "versionCode": args.android_code,
            "url": "downloads/GitHubSync-Remote.apk",
            "sha256": sha256(android),
            "notes": args.notes,
        },
    }
    output = root / "updates.json"
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Обновлён {output}")


if __name__ == "__main__":
    main()
