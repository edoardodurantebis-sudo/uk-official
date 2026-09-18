# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T10:33:39.004254Z`  
Current process started UTC: `2026-09-18T10:29:37.838001Z`  
1-second metadata polls in this process: **180**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **WINDFOR** `TOTAL` `generation` — wind forecast [TOTAL] generation: value=7845, delta=-11023, z=-4.38 -> renewable cushion down / residual-load pressure up
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=996, 2026-09-18T10:30:29.977746Z)
- `FUELINST|fuelType=NPSHYD|generation` = **334** (n=996, 2026-09-18T10:30:29.977746Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=996, 2026-09-18T10:30:29.977746Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=996, 2026-09-18T10:30:29.977746Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=996, 2026-09-18T10:30:29.977746Z)
- `FUELINST|fuelType=OTHER|generation` = **642** (n=996, 2026-09-18T10:30:29.977746Z)
- `FUELINST|fuelType=PS|generation` = **-716** (n=996, 2026-09-18T10:30:29.977746Z)
- `FUELINST|fuelType=WIND|generation` = **12228** (n=996, 2026-09-18T10:30:29.977746Z)
- `IMBALNGC|TOTAL|imbalance` = **7078** (n=164, 2026-09-18T10:19:52.073787Z)
- `INDDEM|TOTAL|demand` = **-13796** (n=164, 2026-09-18T10:19:35.912100Z)
- `INDGEN|TOTAL|generation` = **26759** (n=164, 2026-09-18T10:19:35.912100Z)
- `MELNGC|TOTAL|margin` = **36353** (n=164, 2026-09-18T10:19:03.231158Z)
- `NDF|TOTAL|demand` = **16454** (n=168, 2026-09-18T10:17:07.629865Z)
- `TSDF|TOTAL|demand` = **19681** (n=168, 2026-09-18T10:17:07.629865Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T10:33:37.470545Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:36.261215Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:35.092695Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:33.859522Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:32.638923Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:30.467819Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:29.297451Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:27.755910Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:26.518053Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:24.990940Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:23.376836Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:22.172134Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:20.991866Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:19.804507Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:33:18.175687Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
