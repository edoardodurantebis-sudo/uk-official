# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T20:17:50.037221Z`  
Current process started UTC: `2026-09-17T20:13:49.866597Z`  
1-second metadata polls in this process: **229**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=80, delta=-38, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=118, delta=27, z=6.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **728** (n=825, 2026-09-17T20:15:24.386866Z)
- `FUELINST|fuelType=NPSHYD|generation` = **563** (n=825, 2026-09-17T20:15:24.386866Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=825, 2026-09-17T20:15:24.386866Z)
- `FUELINST|fuelType=OCGT|generation` = **38** (n=825, 2026-09-17T20:15:24.386866Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=825, 2026-09-17T20:15:24.386866Z)
- `FUELINST|fuelType=OTHER|generation` = **732** (n=825, 2026-09-17T20:15:24.386866Z)
- `FUELINST|fuelType=PS|generation` = **503** (n=825, 2026-09-17T20:15:24.386866Z)
- `FUELINST|fuelType=WIND|generation` = **15862** (n=825, 2026-09-17T20:15:24.386866Z)
- `IMBALNGC|TOTAL|imbalance` = **9708** (n=136, 2026-09-17T19:53:01.099555Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=136, 2026-09-17T19:52:45.276545Z)
- `INDGEN|TOTAL|generation` = **26522** (n=136, 2026-09-17T19:52:45.276545Z)
- `MELNGC|TOTAL|margin` = **36519** (n=136, 2026-09-17T19:50:44.130170Z)
- `NDF|TOTAL|demand` = **16314** (n=139, 2026-09-17T19:48:10.710850Z)
- `TSDF|TOTAL|demand` = **16814** (n=139, 2026-09-17T19:48:10.710850Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T20:17:49.079334Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:47.761401Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:46.761301Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:45.761191Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:44.761120Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:43.756742Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:42.756617Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:41.756506Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:40.756431Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:39.756310Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:38.756195Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:37.756072Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:36.755957Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:35.755841Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:17:34.755722Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
