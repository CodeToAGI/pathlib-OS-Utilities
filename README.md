# CodeToAGI — Episode 40: pathlib & OS Utilities

**Python pathlib, os, shutil, glob, and dataset management explained.**

## 📁 Files

- `manim_ep40.py` — Manim animation scenes
- `generate_ep40.py` — Full episode builder (voice + video + thumbnail)
- `dataset_inventory.py` — **Challenge solution**

## 🎯 Challenge

Build a dataset file inventory script that:
1. Recursively scans a folder with `Path.rglob()`
2. Groups files by extension
3. Reports count + total size per type
4. (Bonus) Moves duplicates to a separate folder

**Solution included**: `dataset_inventory.py`

## 🛠️ Key Topics Covered

- `pathlib.Path` — modern cross-platform paths
- `Path.rglob()` vs `os.walk()`
- `os.makedirs(..., exist_ok=True)`
- `shutil.copy/move/rmtree`
- Glob patterns (`**/*.png`)

## Next Episode

**EP41 — JSON & REST APIs**

---

Made with ❤️ for the CodeToAGI community
