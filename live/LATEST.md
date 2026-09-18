# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T10:29:28.168137Z`  
Current process started UTC: `2026-09-18T10:25:27.876780Z`  
1-second metadata polls in this process: **225**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=995, 2026-09-18T10:25:43.554447Z)
- `FUELINST|fuelType=NPSHYD|generation` = **321** (n=995, 2026-09-18T10:25:43.554447Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=995, 2026-09-18T10:25:43.554447Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=995, 2026-09-18T10:25:43.554447Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=995, 2026-09-18T10:25:43.554447Z)
- `FUELINST|fuelType=OTHER|generation` = **705** (n=995, 2026-09-18T10:25:43.554447Z)
- `FUELINST|fuelType=PS|generation` = **-716** (n=995, 2026-09-18T10:25:43.554447Z)
- `FUELINST|fuelType=WIND|generation` = **12115** (n=995, 2026-09-18T10:25:43.554447Z)
- `IMBALNGC|TOTAL|imbalance` = **7078** (n=164, 2026-09-18T10:19:52.073787Z)
- `INDDEM|TOTAL|demand` = **-13796** (n=164, 2026-09-18T10:19:35.912100Z)
- `INDGEN|TOTAL|generation` = **26759** (n=164, 2026-09-18T10:19:35.912100Z)
- `MELNGC|TOTAL|margin` = **36353** (n=164, 2026-09-18T10:19:03.231158Z)
- `NDF|TOTAL|demand` = **16454** (n=168, 2026-09-18T10:17:07.629865Z)
- `TSDF|TOTAL|demand` = **19681** (n=168, 2026-09-18T10:17:07.629865Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T10:29:27.167417Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:25.861615Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:24.822026Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:23.806091Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:22.757630Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:21.744719Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:20.707025Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:19.671945Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:18.670438Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:17.658759Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:16.639985Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:15.639912Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:14.639841Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:13.568181Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:29:12.518776Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
