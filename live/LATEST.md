# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T21:43:10.660536Z`  
Current process started UTC: `2026-09-19T21:39:09.647167Z`  
1-second metadata polls in this process: **224**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1374, 2026-09-19T21:40:30.804729Z)
- `FUELINST|fuelType=NPSHYD|generation` = **454** (n=1374, 2026-09-19T21:40:30.804729Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1374, 2026-09-19T21:40:30.804729Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1374, 2026-09-19T21:40:30.804729Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1374, 2026-09-19T21:40:30.804729Z)
- `FUELINST|fuelType=OTHER|generation` = **430** (n=1374, 2026-09-19T21:40:30.804729Z)
- `FUELINST|fuelType=PS|generation` = **448** (n=1374, 2026-09-19T21:40:30.804729Z)
- `FUELINST|fuelType=WIND|generation` = **14740** (n=1374, 2026-09-19T21:40:30.804729Z)
- `IMBALNGC|TOTAL|imbalance` = **-3899** (n=226, 2026-09-19T21:22:23.160034Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=226, 2026-09-19T21:22:23.160034Z)
- `INDGEN|TOTAL|generation` = **16053** (n=226, 2026-09-19T21:22:23.160034Z)
- `MELNGC|TOTAL|margin` = **36062** (n=226, 2026-09-19T21:19:49.749521Z)
- `NDF|TOTAL|demand` = **19452** (n=231, 2026-09-19T21:18:12.331486Z)
- `TSDF|TOTAL|demand` = **19952** (n=231, 2026-09-19T21:18:12.331486Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T21:43:09.125866Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:43:08.101493Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:43:07.078136Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:43:06.078063Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:43:05.060510Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:43:04.032886Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:43:03.015865Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:43:02.006761Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:43:00.962274Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:42:59.946212Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:42:58.940070Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:42:57.910549Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:42:56.905802Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:42:55.903658Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:42:54.871574Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
