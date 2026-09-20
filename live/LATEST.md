# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T00:19:12.486882Z`  
Current process started UTC: `2026-09-20T00:15:11.533393Z`  
1-second metadata polls in this process: **192**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=-2, z=-11.11 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **956** (n=1405, 2026-09-20T00:15:29.321536Z)
- `FUELINST|fuelType=NPSHYD|generation` = **326** (n=1405, 2026-09-20T00:15:29.321536Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3321** (n=1405, 2026-09-20T00:15:29.321536Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1405, 2026-09-20T00:15:29.321536Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1405, 2026-09-20T00:15:29.321536Z)
- `FUELINST|fuelType=OTHER|generation` = **770** (n=1405, 2026-09-20T00:15:29.321536Z)
- `FUELINST|fuelType=PS|generation` = **-131** (n=1405, 2026-09-20T00:15:29.321536Z)
- `FUELINST|fuelType=WIND|generation` = **15729** (n=1405, 2026-09-20T00:15:29.321536Z)
- `IMBALNGC|TOTAL|imbalance` = **-3708** (n=231, 2026-09-19T23:51:59.807396Z)
- `INDDEM|TOTAL|demand` = **-11889** (n=231, 2026-09-19T23:51:59.807396Z)
- `INDGEN|TOTAL|generation` = **16244** (n=231, 2026-09-19T23:51:59.807396Z)
- `MELNGC|TOTAL|margin` = **35994** (n=231, 2026-09-19T23:49:51.036521Z)
- `NDF|TOTAL|demand` = **19452** (n=237, 2026-09-20T00:17:54.556376Z)
- `TSDF|TOTAL|demand` = **19952** (n=237, 2026-09-20T00:17:54.556376Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T00:19:11.319611Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:19:10.133479Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:19:08.969072Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:19:07.580474Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:19:06.351289Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:19:05.139941Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:19:03.967740Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:19:02.778643Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:19:01.585650Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:19:00.423637Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:18:59.243217Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:18:57.813563Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:18:56.640903Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:18:55.454680Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:18:54.289216Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
