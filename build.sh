#!/bin/bash

set -e

echo "[INFO] Building package..."
python3 -m build

echo "[INFO] Uploading package to PyPI..."
twine upload dist/* || echo "[ERROR] Upload failed. Artifacts still cleaned up."

echo "[INFO] Cleaning up build artifacts..."
rm -rf build dist *.egg-info

echo "[INFO] Done."