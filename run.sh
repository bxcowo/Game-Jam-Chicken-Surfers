#!/bin/sh

uv run main.py
find . -name "__pycache__" -exec rm -r {} +
