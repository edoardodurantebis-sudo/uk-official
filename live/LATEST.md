# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T17:26:48.293075Z`  
Current process started UTC: `2026-09-19T17:22:48.095392Z`  
1-second metadata polls in this process: **225**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=92, z=-0.01 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-92, delta=10, z=-8.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-31, delta=73, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.20 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-102, delta=-202, z=-12.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=-15, z=-11.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-89, delta=-179, z=-10.03 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1323, 2026-09-19T17:25:32.177900Z)
- `FUELINST|fuelType=NPSHYD|generation` = **436** (n=1323, 2026-09-19T17:25:32.177900Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1323, 2026-09-19T17:25:32.177900Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1323, 2026-09-19T17:25:32.177900Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1323, 2026-09-19T17:25:32.177900Z)
- `FUELINST|fuelType=OTHER|generation` = **1836** (n=1323, 2026-09-19T17:25:32.177900Z)
- `FUELINST|fuelType=PS|generation` = **764** (n=1323, 2026-09-19T17:25:32.177900Z)
- `FUELINST|fuelType=WIND|generation` = **14591** (n=1323, 2026-09-19T17:25:32.177900Z)
- `IMBALNGC|TOTAL|imbalance` = **-3136** (n=218, 2026-09-19T17:23:37.629192Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=218, 2026-09-19T17:23:37.629192Z)
- `INDGEN|TOTAL|generation` = **16816** (n=218, 2026-09-19T17:23:37.629192Z)
- `MELNGC|TOTAL|margin` = **36252** (n=218, 2026-09-19T17:20:30.338001Z)
- `NDF|TOTAL|demand` = **19452** (n=223, 2026-09-19T17:17:59.057425Z)
- `TSDF|TOTAL|demand` = **19952** (n=223, 2026-09-19T17:18:14.750483Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T17:26:47.322240Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:46.322165Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:45.322096Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:44.321983Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:43.321910Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:42.321793Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:41.321683Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:40.321576Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:39.321451Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:38.052004Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:37.051897Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:36.051779Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:35.051668Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:34.051549Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:26:33.047754Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
