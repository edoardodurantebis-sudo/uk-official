# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T00:52:41.292990Z`  
Current process started UTC: `2026-09-20T00:48:41.173093Z`  
1-second metadata polls in this process: **188**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-8.71 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **956** (n=1412, 2026-09-20T00:50:34.637380Z)
- `FUELINST|fuelType=NPSHYD|generation` = **313** (n=1412, 2026-09-20T00:50:34.637380Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1412, 2026-09-20T00:50:34.637380Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1412, 2026-09-20T00:50:34.637380Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1412, 2026-09-20T00:50:34.637380Z)
- `FUELINST|fuelType=OTHER|generation` = **535** (n=1412, 2026-09-20T00:50:34.637380Z)
- `FUELINST|fuelType=PS|generation` = **-254** (n=1412, 2026-09-20T00:50:34.637380Z)
- `FUELINST|fuelType=WIND|generation` = **15630** (n=1412, 2026-09-20T00:50:34.637380Z)
- `IMBALNGC|TOTAL|imbalance` = **-3763** (n=233, 2026-09-20T00:51:38.211016Z)
- `INDDEM|TOTAL|demand` = **-11949** (n=233, 2026-09-20T00:51:38.211016Z)
- `INDGEN|TOTAL|generation` = **16189** (n=233, 2026-09-20T00:51:38.211016Z)
- `MELNGC|TOTAL|margin` = **36027** (n=233, 2026-09-20T00:49:47.495939Z)
- `NDF|TOTAL|demand` = **19452** (n=238, 2026-09-20T00:47:47.229077Z)
- `TSDF|TOTAL|demand` = **19952** (n=238, 2026-09-20T00:47:47.229077Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T00:52:40.090256Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:38.882295Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:37.714320Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:36.506650Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:35.307135Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:34.130941Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:32.935722Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:31.766234Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:30.593795Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:29.396060Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:28.221109Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:26.602892Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:25.401832Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:24.224461Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:52:23.031858Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
