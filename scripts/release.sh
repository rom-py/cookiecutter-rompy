#!/bin/bash
# Release script for cookiecutter-rompy
set -e

# Determine version bump type
if [ -z "$1" ]; then
  echo "Usage: $0 <major|minor|patch>"
  exit 1
fi

# Bump version
bump2version $1

# Push changes and tags
git push && git push --tags

# GitHub release
gh release create $(python -c "import toml; print(toml.load('pyproject.toml')['project']['version'])") --title "Release $(python -c "import toml; print(toml.load('pyproject.toml')['project']['version'])")" --notes "Automated release via script."

# Publish to PyPI
python -m build
twine upload dist/*

# Cleanup
echo "Release successful."