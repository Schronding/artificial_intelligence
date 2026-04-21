# Artificial Intelligence Workspace

This repository uses `uv` to manage the Python environment and dependencies.

## Requirements

- Python 3.11
- `uv` installed

## Quick setup on another computer

```bash
uv sync
```

This creates or updates `.venv` with all libraries defined in `pyproject.toml` and `uv.lock`.

## Run scripts or notebooks

```bash
uv run python infinite_sum_to_one.py
```

For Jupyter:

```bash
uv run jupyter lab
```

## Update dependencies

- Add package: `uv add <package>`
- Regenerate lockfile: `uv lock`

## Key files

- `pyproject.toml`: dependencies and Python version.
- `uv.lock`: exact resolved versions for reproducibility.
- `.python-version`: suggested Python version for compatible tools.
