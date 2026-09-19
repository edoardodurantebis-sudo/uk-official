# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T20:57:02.256549Z`  
Current process started UTC: `2026-09-19T20:53:00.870887Z`  
1-second metadata polls in this process: **138**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=94, delta=-6, z=4.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=-378, z=-0.09 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=92, delta=-14, z=4.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.97 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=5.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=1, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=-250, z=-0.07 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=100, delta=4, z=5.22 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=378, delta=4, z=13.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=105, delta=5, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=251, delta=-152, z=6.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=100, delta=1, z=4.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=11.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.84 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1365, 2026-09-19T20:55:26.442645Z)
- `FUELINST|fuelType=NPSHYD|generation` = **472** (n=1365, 2026-09-19T20:55:26.442645Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1365, 2026-09-19T20:55:26.442645Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1365, 2026-09-19T20:55:26.442645Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1365, 2026-09-19T20:55:26.442645Z)
- `FUELINST|fuelType=OTHER|generation` = **493** (n=1365, 2026-09-19T20:55:26.442645Z)
- `FUELINST|fuelType=PS|generation` = **823** (n=1365, 2026-09-19T20:55:26.442645Z)
- `FUELINST|fuelType=WIND|generation` = **14334** (n=1365, 2026-09-19T20:55:26.442645Z)
- `IMBALNGC|TOTAL|imbalance` = **-3851** (n=225, 2026-09-19T20:52:15.629197Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=225, 2026-09-19T20:51:59.237885Z)
- `INDGEN|TOTAL|generation` = **16101** (n=225, 2026-09-19T20:51:59.237885Z)
- `MELNGC|TOTAL|margin` = **36203** (n=225, 2026-09-19T20:49:35.992012Z)
- `NDF|TOTAL|demand` = **19452** (n=230, 2026-09-19T20:47:50.435946Z)
- `TSDF|TOTAL|demand` = **19952** (n=230, 2026-09-19T20:47:50.435946Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T20:57:00.600125Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:58.934739Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:57.292650Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:55.616465Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:53.943412Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:52.298234Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:50.626975Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:47.928938Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:46.258728Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:44.601552Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:42.902318Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:40.943116Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:39.319815Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:37.670226Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:56:35.977446Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
