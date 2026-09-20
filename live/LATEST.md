# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T12:26:00.833773Z`  
Current process started UTC: `2026-09-20T12:22:00.431864Z`  
1-second metadata polls in this process: **138**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-986, delta=2, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-983, delta=3, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.72 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-988, delta=26, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.79 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=2, z=-3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-989, delta=24, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.13 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1551, 2026-09-20T12:25:36.530337Z)
- `FUELINST|fuelType=NPSHYD|generation` = **263** (n=1551, 2026-09-20T12:25:36.530337Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1551, 2026-09-20T12:25:36.530337Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1551, 2026-09-20T12:25:36.530337Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1551, 2026-09-20T12:25:36.530337Z)
- `FUELINST|fuelType=OTHER|generation` = **548** (n=1551, 2026-09-20T12:25:36.530337Z)
- `FUELINST|fuelType=PS|generation` = **-670** (n=1551, 2026-09-20T12:25:36.530337Z)
- `FUELINST|fuelType=WIND|generation` = **12524** (n=1551, 2026-09-20T12:25:36.530337Z)
- `IMBALNGC|TOTAL|imbalance` = **-5720** (n=255, 2026-09-20T12:23:23.217722Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=255, 2026-09-20T12:23:23.217722Z)
- `INDGEN|TOTAL|generation` = **15384** (n=255, 2026-09-20T12:23:23.217722Z)
- `MELNGC|TOTAL|margin` = **35780** (n=255, 2026-09-20T12:20:29.957281Z)
- `NDF|TOTAL|demand` = **20604** (n=261, 2026-09-20T12:18:20.759778Z)
- `TSDF|TOTAL|demand` = **21104** (n=261, 2026-09-20T12:18:20.759778Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T12:25:59.192698Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:57.550899Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:55.928317Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:54.284882Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:52.309497Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:50.655829Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:49.045713Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:47.424018Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:45.794221Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:44.147292Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:42.497725Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:40.865467Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:39.226497Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:36.530337Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:25:36.530337Z` — **FUELINST**: 80 rows; marker `2026-09-20T12:25:00Z`
