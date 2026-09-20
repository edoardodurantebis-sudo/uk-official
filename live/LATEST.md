# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T00:56:51.477115Z`  
Current process started UTC: `2026-09-20T00:52:51.273399Z`  
1-second metadata polls in this process: **227**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.24 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-7.37 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-7.68 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.86 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1012, delta=-118, z=-9.25 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-8.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-8.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=2, z=-8.42 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-8.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-6, z=-8.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1008, delta=-111, z=-9.12 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-894, delta=-4, z=-9.66 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-897, delta=-5, z=-8.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-892, delta=1, z=-8.47 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **956** (n=1413, 2026-09-20T00:55:38.565632Z)
- `FUELINST|fuelType=NPSHYD|generation` = **313** (n=1413, 2026-09-20T00:55:38.565632Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1413, 2026-09-20T00:55:38.565632Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1413, 2026-09-20T00:55:38.565632Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1413, 2026-09-20T00:55:38.565632Z)
- `FUELINST|fuelType=OTHER|generation` = **379** (n=1413, 2026-09-20T00:55:38.565632Z)
- `FUELINST|fuelType=PS|generation` = **-252** (n=1413, 2026-09-20T00:55:38.565632Z)
- `FUELINST|fuelType=WIND|generation` = **15588** (n=1413, 2026-09-20T00:55:38.565632Z)
- `IMBALNGC|TOTAL|imbalance` = **-3763** (n=233, 2026-09-20T00:51:38.211016Z)
- `INDDEM|TOTAL|demand` = **-11949** (n=233, 2026-09-20T00:51:38.211016Z)
- `INDGEN|TOTAL|generation` = **16189** (n=233, 2026-09-20T00:51:38.211016Z)
- `MELNGC|TOTAL|margin` = **36027** (n=233, 2026-09-20T00:49:47.495939Z)
- `NDF|TOTAL|demand` = **19452** (n=238, 2026-09-20T00:47:47.229077Z)
- `TSDF|TOTAL|demand` = **19952** (n=238, 2026-09-20T00:47:47.229077Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T00:56:50.523926Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:49.523812Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:48.523693Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:47.523583Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:46.523515Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:45.523443Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:44.523318Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:43.217640Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:42.217529Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:41.217419Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:40.217305Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:39.217190Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:38.217081Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:37.217012Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:56:36.216889Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
