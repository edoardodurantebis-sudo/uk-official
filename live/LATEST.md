# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T02:16:37.983698Z`  
Current process started UTC: `2026-09-20T02:12:37.798099Z`  
1-second metadata polls in this process: **230**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-5.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-6.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.08 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-6.17 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-6.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.34 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-7.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.44 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-6.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-6.75 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **329** (n=1429, 2026-09-20T02:15:42.612005Z)
- `FUELINST|fuelType=NPSHYD|generation` = **308** (n=1429, 2026-09-20T02:15:42.612005Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1429, 2026-09-20T02:15:42.612005Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1429, 2026-09-20T02:15:42.612005Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1429, 2026-09-20T02:15:42.612005Z)
- `FUELINST|fuelType=OTHER|generation` = **250** (n=1429, 2026-09-20T02:15:42.612005Z)
- `FUELINST|fuelType=PS|generation` = **-698** (n=1429, 2026-09-20T02:15:42.612005Z)
- `FUELINST|fuelType=WIND|generation` = **15375** (n=1429, 2026-09-20T02:15:42.612005Z)
- `IMBALNGC|TOTAL|imbalance` = **-3757** (n=235, 2026-09-20T01:51:00.792913Z)
- `INDDEM|TOTAL|demand` = **-12197** (n=235, 2026-09-20T01:51:00.792913Z)
- `INDGEN|TOTAL|generation` = **16195** (n=235, 2026-09-20T01:51:00.792913Z)
- `MELNGC|TOTAL|margin` = **36018** (n=235, 2026-09-20T01:49:39.512104Z)
- `NDF|TOTAL|demand` = **19452** (n=240, 2026-09-20T01:47:46.889825Z)
- `TSDF|TOTAL|demand` = **19952** (n=240, 2026-09-20T01:47:46.889825Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T02:16:37.029321Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:36.029214Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:35.029090Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:34.028966Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:33.028852Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:32.028735Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:31.028607Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:29.740806Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:28.740689Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:27.740572Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:26.740446Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:25.720046Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:24.719919Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:23.719806Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:16:22.719682Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
