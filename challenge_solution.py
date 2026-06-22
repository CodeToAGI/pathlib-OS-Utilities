#!/usr/bin/env python3
"""
CodeToAGI — EP40 Challenge Solution
Dataset File Inventory + Duplicate Handler
"""

from pathlib import Path
from collections import defaultdict
import shutil
from datetime import datetime

def scan_dataset(root_path: str | Path, move_duplicates: bool = False):
    root = Path(root_path).resolve()
    if not root.exists():
        print(f"❌ Folder not found: {root}")
        return

    print(f"🔍 Scanning: {root}\n")

    # Group by extension
    by_ext = defaultdict(list)
    # For duplicate detection: (name, size) -> list of paths
    duplicates_map = defaultdict(list)

    # Step 1: Recursive scan
    for file in root.rglob("*.*"):  # or rglob("*") to include files without extension
        if file.is_file():
            ext = file.suffix.lower() or ".no_extension"
            size = file.stat().st_size
            by_ext[ext].append(file)

            # Duplicate key: (filename, size)
            key = (file.name.lower(), size)
            duplicates_map[key].append(file)

    # Step 2 & 3: Print inventory
    total_files = sum(len(files) for files in by_ext.values())
    total_size_mb = sum(
        sum(f.stat().st_size for f in files) for files in by_ext.values()
    ) / (1024 * 1024)

    print(f"📊 Inventory Summary")
    print(f"   Total files: {total_files:,}")
    print(f"   Total size : {total_size_mb:.2f} MB\n")

    print("📋 Files by Extension:")
    print("-" * 60)
    for ext in sorted(by_ext.keys(), key=lambda x: len(by_ext[x]), reverse=True):
        files = by_ext[ext]
        size_mb = sum(f.stat().st_size for f in files) / (1024 * 1024)
        print(f"{ext:12} → {len(files):4,} files  ({size_mb:8.2f} MB)")

    # Step 4: Bonus - Duplicates
    dups = {k: v for k, v in duplicates_map.items() if len(v) > 1}
    if dups:
        print(f"\n⚠️  Found {len(dups)} groups of duplicate files")
        if move_duplicates:
            dup_folder = root / "duplicates"
            dup_folder.mkdir(exist_ok=True)
            moved = 0
            for key, paths in dups.items():
                # Keep the first one, move the rest
                for p in paths[1:]:
                    dest = dup_folder / p.name
                    # Avoid name collision in duplicates folder
                    counter = 1
                    while dest.exists():
                        dest = dup_folder / f"{p.stem}_{counter}{p.suffix}"
                        counter += 1
                    shutil.move(str(p), str(dest))
                    moved += 1
            print(f"   → Moved {moved} duplicate files to: {dup_folder}")
    else:
        print("\n✅ No duplicates found!")

    print(f"\n🎉 Scan completed at {datetime.now().strftime('%H:%M:%S')}")


if __name__ == "__main__":
    # === CHANGE THIS PATH ===
    target_folder = r"."  # or r"C:\path\to\your\dataset"

    scan_dataset(target_folder, move_duplicates=True)
