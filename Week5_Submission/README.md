# Week 5 — Pair Programming & Static Analysis

This is a **prepared code-and-documentation package**, not a claim that the required real-life pairing, git history, review, or local Ruff/Pylint runs have occurred.

## Folder layout

- `week5/grades.py`, `week5/test_grades.py`: grading kata and tests.
- `week5/legacy_fees.py`: unchanged source from the handout.
- `week5/fees.py`, `week5/test_fees.py`: refactoring and regression tests.
- `week5/pyproject.toml`: final Ruff config; excludes the unchanged legacy sample from project-wide lint.
- `week5/pyproject.before.toml`: original lint config to measure legacy code.
- `docs/week5/before.txt`, `findings.md`, `after.md`: requested documentation.

## Run locally (VS Code terminal, from repository root)

```powershell
cd week5
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pytest ruff pylint
python -m pytest -v
ruff check --config pyproject.before.toml legacy_fees.py
ruff check --config pyproject.before.toml legacy_fees.py --statistics
pylint legacy_fees.py
ruff check .
ruff format --check .
pylint fees.py
```

Paste the **real** Ruff and Pylint baseline outputs into `docs/week5/before.txt`, and update the measured cells in `docs/week5/after.md`. Run Ruff before and after, and resolve any new warnings; versions can differ. `ruff format .` will change formatting, so run it only when ready to review the diff.

## Git and pair-work requirements

Use the existing team repository and create `week5-quality` from `main`. Do the actual 12-minute Driver/Navigator rotations, make at least two kata commits (including a genuine `Co-authored-by:` trailer), and commit each refactoring step as the lab requires. These historical events cannot be recreated merely by unzipping a completed solution. Ask your real partner to review the GitHub pull request, then submit the PR URL to LMS. Do not use placeholder names or fabricated commits/reviews.

## Note

The PDF is headed **Lab 5 — Week 5**, even though its uploaded filename contains `Lab6`.
