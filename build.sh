#!/bin/bash

set -e

# Build the package
python3 -m build

# Upload to PyPI
if twine upload dist/*; then
  echo "✅ Upload succeeded. Keeping build artifacts."
else
  echo "❌ Upload failed. Nothing deleted."
  exit 1
fi