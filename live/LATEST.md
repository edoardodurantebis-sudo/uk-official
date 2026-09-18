# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T08:13:40.371250Z`  
Current process started UTC: `2026-09-18T08:09:40.038859Z`  
1-second metadata polls in this process: **171**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=968, 2026-09-18T08:10:30.041017Z)
- `FUELINST|fuelType=NPSHYD|generation` = **379** (n=968, 2026-09-18T08:10:30.041017Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=968, 2026-09-18T08:10:30.041017Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=968, 2026-09-18T08:10:30.041017Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=968, 2026-09-18T08:10:30.041017Z)
- `FUELINST|fuelType=OTHER|generation` = **1539** (n=968, 2026-09-18T08:10:30.041017Z)
- `FUELINST|fuelType=PS|generation` = **370** (n=968, 2026-09-18T08:10:30.041017Z)
- `FUELINST|fuelType=WIND|generation` = **12467** (n=968, 2026-09-18T08:10:30.041017Z)
- `IMBALNGC|TOTAL|imbalance` = **10218** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDDEM|TOTAL|demand` = **-11739** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDGEN|TOTAL|generation` = **27722** (n=159, 2026-09-18T07:19:58.374346Z)
- `MELNGC|TOTAL|margin` = **37765** (n=159, 2026-09-18T07:19:09.419948Z)
- `NDF|TOTAL|demand` = **15870** (n=163, 2026-09-18T07:46:04.858619Z)
- `TSDF|TOTAL|demand` = **16370** (n=163, 2026-09-18T07:46:04.858619Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T08:13:38.964760Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:37.647202Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:36.314495Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:34.987132Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:33.646947Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:32.288478Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:30.657115Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:29.325501Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:27.998434Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:26.630955Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:25.301542Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:23.995670Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:22.643656Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:21.320933Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:13:20.012299Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
