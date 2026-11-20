# Static-analysis findings — legacy_fees.py

The following **expected** Ruff counts come from the lab handout (page 5). Confirm with the actual local Ruff output before submitting; tool versions can differ.

| Ruff rule | Expected count | Code smell | Proposed refactoring |
|---|---:|---|---|
| F401 | 2 | Dead code: unused imports | Remove `os` and `math` |
| PLR2004 | 6 | Magic numbers / type codes | Introduce constants and `StudentType` enum |
| C901 | 1 | Excessive cyclomatic complexity | Replace conditional chains with a rate lookup |
| PLR0913 | 1 | Too many arguments | Simplify API and remove unused `y`; consider a value object |
| ARG001 | 1 | Unused parameter | Remove `y` |
| B006 | 1 | Mutable default argument | Use `extras=()` |
| E711 / E712 | 2 | Explicit comparisons with `None` / `True` | Use `is not None` and truthiness |
| F841 | 1 | Dead assignment | Delete `tmp` |
| N802 | 1 | Non-PEP8 function name | Rename `ProcessAll` to `process_all` |
| **Total** | **16** | | |

## Three additional smells not captured by the listed Ruff warnings

1. **Mysterious names:** `d`, `t`, `s`, `disc`, `x` obscure the meaning of data and business rules.
2. **Duplicated logic:** `ProcessAll` calls `calc` separately for student types 1 and 2, duplicating almost identical code.
3. **Mixed responsibilities:** `report` calculates the fee and prints output, coupling business logic to console presentation.
4. **Primitive obsession:** course credit hours are represented as dictionaries with the cryptic key `"h"` rather than a dedicated `Course` object.

## Hidden bug in `ProcessAll`

`ProcessAll` only assigns `fee` for types 1 and 2. When Omar (type 3, scholarship) follows Sara, Omar prints Sara's previous `fee` (1050), because the variable remains bound from the preceding loop iteration. If Omar appears first, the function raises `UnboundLocalError` instead. The corrected `process_all` calculates a fee for every student; a scholarship student with no summer fee pays 0.
