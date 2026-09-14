# UK data contract

`uk-official` is the code/control repository. Raw `master_wide` and `exante_wide` are intentionally **not committed** here.

## Frozen historical baseline recovered 2026-09-14

| dataset | rows | columns | SHA256 | source range |
|---|---:|---:|---|---|
| `master_wide.csv` | 81,398 | 195 | `31701eae21fa2c1453e605b9ef5bbd8fb4f5128de4431230a33886abc3cd8542` | 2022-01-01 → 2026-08-23 |
| `exante_wide.csv` | 81,456 | 45 | `7ad10429a2c30473ac39eee467aa140f914c08a8cd31a6ef9fe14e6bb08f53c1` | 2022-01-01 → 2026-08-24 |

The files are retained outside GitHub in the project/private file store.

## Time identity

The legacy `datetime_tz` is a naive Europe/Rome wall-clock field. Legacy `date` and `settlement_period` are not GB physical identity. `gb_legacy_canonicalizer.py` converts the wall clock to UTC, derives London delivery date and sequential GB SP, and certifies only complete physical days.

On the frozen master this currently gives **81,158 certified rows across 1,691 complete GB delivery days**. Autumn DST fold days in the legacy wide file cannot be reconstructed uniquely because the repeated wall-clock hour was collapsed; they are excluded fail-closed. Edge partial days are excluded too.

## Granularity rule

The scanner processes every observation at its **native** resolution. PT30 data remain PT30. PT15, PT60, minute/tick/MATS data are kept at their real timestamps; the system must never upsample PT30 values and pretend they are minute observations.

## PIT / gates

Gate policy is explicit in code and will move to the Feature Availability Registry as certification matures:

- DA: D-1 forecast vintages available by the DA gate (current conservative baseline: v7/v8).
- IDA1: D-1 vintages through v16 plus certified DA/ex-ante fields.
- IDA2: D-1 vintages plus D0 vintages strictly before 09:00 (current conservative baseline: v7/v8 D0) plus certified DA/ex-ante fields.
- Ex-post/actual/error/BOA/NIV/imbalance-price fields are targets/audit only, never discovery inputs.

## Outputs

Candidate discovery output is not a trading instruction. Machine promotion is capped at review-ready; rulebook promotion remains a separate validation step. Sensitive derived results should stay outside the public repository unless explicitly approved.
