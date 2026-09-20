# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T00:35:53.251700Z`  
Current process started UTC: `2026-09-20T00:31:53.179147Z`  
1-second metadata polls in this process: **193**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-894, delta=-1, z=-9.54 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **956** (n=1409, 2026-09-20T00:35:38.409939Z)
- `FUELINST|fuelType=NPSHYD|generation` = **314** (n=1409, 2026-09-20T00:35:38.409939Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1409, 2026-09-20T00:35:38.409939Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1409, 2026-09-20T00:35:38.409939Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1409, 2026-09-20T00:35:38.409939Z)
- `FUELINST|fuelType=OTHER|generation` = **826** (n=1409, 2026-09-20T00:35:38.409939Z)
- `FUELINST|fuelType=PS|generation` = **-240** (n=1409, 2026-09-20T00:35:38.409939Z)
- `FUELINST|fuelType=WIND|generation` = **15700** (n=1409, 2026-09-20T00:35:38.409939Z)
- `IMBALNGC|TOTAL|imbalance` = **-3746** (n=232, 2026-09-20T00:21:29.850397Z)
- `INDDEM|TOTAL|demand` = **-11915** (n=232, 2026-09-20T00:21:13.934904Z)
- `INDGEN|TOTAL|generation` = **16206** (n=232, 2026-09-20T00:21:13.934904Z)
- `MELNGC|TOTAL|margin` = **35985** (n=232, 2026-09-20T00:19:54.139683Z)
- `NDF|TOTAL|demand` = **19452** (n=237, 2026-09-20T00:17:54.556376Z)
- `TSDF|TOTAL|demand` = **19952** (n=237, 2026-09-20T00:17:54.556376Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T00:35:52.107809Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:50.958152Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:49.773248Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:48.622825Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:47.444784Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:46.289752Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:45.162536Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:44.000710Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:42.858019Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:41.721580Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:40.550029Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:38.409939Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:38.409939Z` — **FUELINST**: 80 rows; marker `2026-09-20T00:35:00Z`
- `2026-09-20T00:35:37.252096Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:35:36.099629Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
