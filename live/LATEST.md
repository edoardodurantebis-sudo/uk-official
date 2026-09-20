# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T00:44:20.078551Z`  
Current process started UTC: `2026-09-20T00:40:18.781918Z`  
1-second metadata polls in this process: **133**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-8.96 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=1, z=-9.23 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **956** (n=1410, 2026-09-20T00:40:35.836502Z)
- `FUELINST|fuelType=NPSHYD|generation` = **314** (n=1410, 2026-09-20T00:40:35.836502Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1410, 2026-09-20T00:40:35.836502Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1410, 2026-09-20T00:40:35.836502Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1410, 2026-09-20T00:40:35.836502Z)
- `FUELINST|fuelType=OTHER|generation` = **832** (n=1410, 2026-09-20T00:40:35.836502Z)
- `FUELINST|fuelType=PS|generation` = **-253** (n=1410, 2026-09-20T00:40:35.836502Z)
- `FUELINST|fuelType=WIND|generation` = **15654** (n=1410, 2026-09-20T00:40:35.836502Z)
- `IMBALNGC|TOTAL|imbalance` = **-3746** (n=232, 2026-09-20T00:21:29.850397Z)
- `INDDEM|TOTAL|demand` = **-11915** (n=232, 2026-09-20T00:21:13.934904Z)
- `INDGEN|TOTAL|generation` = **16206** (n=232, 2026-09-20T00:21:13.934904Z)
- `MELNGC|TOTAL|margin` = **35985** (n=232, 2026-09-20T00:19:54.139683Z)
- `NDF|TOTAL|demand` = **19452** (n=237, 2026-09-20T00:17:54.556376Z)
- `TSDF|TOTAL|demand` = **19952** (n=237, 2026-09-20T00:17:54.556376Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T00:44:18.376307Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:44:16.671241Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:44:14.932164Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:44:13.227068Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:44:11.520205Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:44:09.806458Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:44:08.104344Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:44:06.360220Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:44:04.351429Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:44:02.650597Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:44:00.932946Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:43:59.235314Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:43:57.541139Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:43:55.773028Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:43:54.073862Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
