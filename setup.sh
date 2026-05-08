#!/bin/bash
cp -r ./skills/* $HOME/.gemini/skills/
python3 -m pip install -q PyMuPDF Pillow pdfplumber
mkdir -p ./data
