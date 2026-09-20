# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T00:23:21.734672Z`  
Current process started UTC: `2026-09-20T00:19:21.598780Z`  
1-second metadata polls in this process: **221**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=2, z=-8.42 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-8.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-6, z=-8.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1008, delta=-111, z=-9.12 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-894, delta=-4, z=-9.66 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-897, delta=-5, z=-8.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-892, delta=1, z=-8.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-8.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-8.96 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=1, z=-9.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-894, delta=-1, z=-9.54 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-890, delta=-204, z=-12.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-9.86 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=-1, z=-10.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-892, delta=1, z=-10.63 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **956** (n=1406, 2026-09-20T00:20:41.500279Z)
- `FUELINST|fuelType=NPSHYD|generation` = **316** (n=1406, 2026-09-20T00:20:41.500279Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1406, 2026-09-20T00:20:41.500279Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1406, 2026-09-20T00:20:41.500279Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1406, 2026-09-20T00:20:41.500279Z)
- `FUELINST|fuelType=OTHER|generation` = **668** (n=1406, 2026-09-20T00:20:41.500279Z)
- `FUELINST|fuelType=PS|generation` = **-130** (n=1406, 2026-09-20T00:20:41.500279Z)
- `FUELINST|fuelType=WIND|generation` = **15624** (n=1406, 2026-09-20T00:20:41.500279Z)
- `IMBALNGC|TOTAL|imbalance` = **-3746** (n=232, 2026-09-20T00:21:29.850397Z)
- `INDDEM|TOTAL|demand` = **-11915** (n=232, 2026-09-20T00:21:13.934904Z)
- `INDGEN|TOTAL|generation` = **16206** (n=232, 2026-09-20T00:21:13.934904Z)
- `MELNGC|TOTAL|margin` = **35985** (n=232, 2026-09-20T00:19:54.139683Z)
- `NDF|TOTAL|demand` = **19452** (n=237, 2026-09-20T00:17:54.556376Z)
- `TSDF|TOTAL|demand` = **19952** (n=237, 2026-09-20T00:17:54.556376Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T00:23:20.229947Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:19.212135Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:18.207220Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:17.177334Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:16.166704Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:15.163946Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:14.151786Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:13.138453Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:12.138383Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:11.137745Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:10.108935Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:09.078594Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:08.078526Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:07.049345Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:23:06.026099Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
