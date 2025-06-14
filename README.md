# PDF Merger
_A little CLI tool to merge PDF documents_

[![CI](https://github.com/davidbossanyi/pdf-merger/actions/workflows/ci.yaml/badge.svg)](https://github.com/davidbossanyi/pdf-merger/actions/workflows/ci.yaml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)

## Usage
To merge all PDF files in a given directory, alphabetically sorted by filename:
```commandline
uv run pdf-merger "/path/to/folder/with/pdfs" -o "merged.pdf"
```

## Development
The development environment should be created and managed using [uv](https://docs.astral.sh/uv/). To create the environment:
```commandline
uv sync --all-groups
```
To run the formatting, linting and testing:
```commandline
uv run poe all
```
Or simply
```commandline
poe all
```
if you have activated the virtual environment (VSCode will do this automatically for you). For example, to activate the environment from a PowerShell prompt:
```powershell
. ".venv\Scripts\activate.ps1"
```
