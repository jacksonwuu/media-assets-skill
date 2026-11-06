#!/usr/bin/env python3
"""Organize downloaded media into medium folders with collision-safe names."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

MEDIUM_BY_SUFFIX = {
    ".jpg": "images", ".jpeg": "images", ".png": "images", ".webp": "images",
    ".gif": "images", ".avif": "images", ".tif": "images", ".tiff": "images",
    ".svg": "vectors",
    ".mp4": "videos", ".mov": "videos", ".webm": "videos", ".mkv": "videos", ".m4v": "videos",
    ".mp3": "audio", ".wav": "audio", ".flac": "audio", ".ogg": "audio", ".m4a": "audio",
    ".ttf": "fonts", ".otf": "fonts", ".woff": "fonts", ".woff2": "fonts",
    ".glb": "models", ".gltf": "models", ".obj": "models", ".fbx": "models", ".blend": "models",
}


def unique_destination(destination: Path) -> Path:
    if not destination.exists():
        return destination
    stem, suffix = destination.stem, destination.suffix
    counter = 2
    while True:
        candidate = destination.with_name(f"{stem}-{counter}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def organize(source: Path, target: Path, dry_run: bool) -> int:
    if not source.exists():
        raise FileNotFoundError(source)
    moved = 0
    for path in sorted(source.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in MEDIUM_BY_SUFFIX:
            continue
        medium = MEDIUM_BY_SUFFIX[path.suffix.lower()]
        destination = unique_destination(target / medium / path.name)
        print(f"{path} -> {destination}")
        if not dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(path, destination)
        moved += 1
    return moved


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Directory containing downloads")
    parser.add_argument("--target", type=Path, default=Path("assets"), help="Destination root")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without moving files")
    args = parser.parse_args()
    count = organize(args.source, args.target, args.dry_run)
    print(f"Organized {count} file(s).")


if __name__ == "__main__":
    main()
