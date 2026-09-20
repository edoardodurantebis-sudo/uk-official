# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T00:15:00.046262Z`  
Current process started UTC: `2026-09-20T00:10:58.911731Z`  
1-second metadata polls in this process: **195**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=-2, z=-11.11 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-891, delta=-12, z=-11.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **956** (n=1404, 2026-09-20T00:10:58.911738Z)
- `FUELINST|fuelType=NPSHYD|generation` = **340** (n=1404, 2026-09-20T00:10:58.911738Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1404, 2026-09-20T00:10:58.911738Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1404, 2026-09-20T00:10:58.911738Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1404, 2026-09-20T00:10:58.911738Z)
- `FUELINST|fuelType=OTHER|generation` = **736** (n=1404, 2026-09-20T00:10:58.911738Z)
- `FUELINST|fuelType=PS|generation` = **-129** (n=1404, 2026-09-20T00:10:58.911738Z)
- `FUELINST|fuelType=WIND|generation` = **15878** (n=1404, 2026-09-20T00:10:58.911738Z)
- `IMBALNGC|TOTAL|imbalance` = **-3708** (n=231, 2026-09-19T23:51:59.807396Z)
- `INDDEM|TOTAL|demand` = **-11889** (n=231, 2026-09-19T23:51:59.807396Z)
- `INDGEN|TOTAL|generation` = **16244** (n=231, 2026-09-19T23:51:59.807396Z)
- `MELNGC|TOTAL|margin` = **35994** (n=231, 2026-09-19T23:49:51.036521Z)
- `NDF|TOTAL|demand` = **19452** (n=236, 2026-09-19T23:47:47.316209Z)
- `TSDF|TOTAL|demand` = **19952** (n=236, 2026-09-19T23:47:47.316209Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T00:14:58.877575Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:57.255203Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:56.066274Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:54.898762Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:53.733271Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:52.565617Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:51.380637Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:50.185079Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:49.024076Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:47.884355Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:46.713698Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:45.528495Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:44.346661Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:43.169780Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:14:41.613028Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
