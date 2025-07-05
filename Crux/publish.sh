#!/bin/bash

set -e

# Clean up previous builds
rm -rf dist/
rm -rf build/
rm -rf *.egg-info/

echo "Building source and wheel distributions..."
python setup.py sdist bdist_wheel

echo "Checking distributions with twine..."
twine check dist/*

echo "
To publish to PyPI, run:"
echo "twine upload dist/*"
echo "
If you have a .pypirc file, ensure it's configured correctly."
