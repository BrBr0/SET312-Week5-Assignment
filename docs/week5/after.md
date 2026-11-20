# Before / After — Refactoring report

The baseline values below are supplied by the lab. **After** tool results must be measured on your own computer; do not submit unverified numbers.

| Measure | Before (legacy_fees.py) | After (fees.py) |
|---|---|---|
| Ruff issues (total) | 16 (handout) | **RUN RUFF** |
| Highest cyclomatic complexity | 9 (`calc`, handout) | **MEASURE** |
| Arguments of main fee function | 6 | 5 (`tuition_fee`) |
| Pylint score (/10) | **RUN PYLINT** | **RUN PYLINT** |
| Tests passing | 0 (no tests before lab) | **RUN PYTEST** |

## Why the new implementation is safer

- `legacy_fees.py` remains untouched for characterization comparisons.
- `tuition_fee` preserves the calculation order, with constants, an enum, a frozen dataclass and a rate table.
- `process_all` handles scholarship students explicitly, avoiding a stale or unbound `fee`.
- `report` returns text rather than printing it.

## Pair-programming reflection — COMPLETE WITH YOUR ACTUAL EXPERIENCE

Write 3–4 sentences after working with your partner. Mention who was Driver/Navigator, when you switched, what the navigator noticed, and what was harder or easier than working alone. Do not claim pairing or a review occurred if it did not.
