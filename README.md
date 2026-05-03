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

## Troubleshooting

- First run can take several minutes, especially while downloading heavy packages (for example, TensorFlow).
- If the command appears to stall in an editor terminal, wait longer or run `uv sync` again; downloads are resumed and installation completes normally.
- Verify everything is ready with:

```bash
uv run python infinite_sum_to_one.py
```

## Run scripts or notebooks

```bash
uv run python infinite_sum_to_one.py
```

For Jupyter:

```bash
uv run jupyter lab
```

## GPU setup (TensorFlow + NVIDIA)

If `tf.config.list_physical_devices("GPU")` returns an empty list but `nvidia-smi` shows a GPU, install TensorFlow CUDA dependencies in this project:

```bash
uv add "tensorflow[and-cuda]==2.20.0"
uv sync
```

Then verify:

```bash
uv run python -c "import tensorflow as tf; print(tf.__version__); print(tf.config.list_physical_devices('GPU'))"
```

Notes for Windows:

- On recent TensorFlow versions, the most reliable path is WSL2 with NVIDIA driver support for WSL.
- Keep your NVIDIA driver updated on Windows (check with `nvidia-smi`).
- After dependency changes, restart the Jupyter kernel before rechecking GPU detection.

## Update dependencies

- Add package: `uv add <package>`
- Regenerate lockfile: `uv lock`

## Key files

- `pyproject.toml`: dependencies and Python version.
- `uv.lock`: exact resolved versions for reproducibility.
- `.python-version`: suggested Python version for compatible tools.
