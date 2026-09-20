# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T00:27:32.380124Z`  
Current process started UTC: `2026-09-20T00:23:32.179747Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-890, delta=-204, z=-12.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-9.86 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=-1, z=-10.23 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **956** (n=1407, 2026-09-20T00:25:30.042716Z)
- `FUELINST|fuelType=NPSHYD|generation` = **312** (n=1407, 2026-09-20T00:25:30.042716Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1407, 2026-09-20T00:25:30.042716Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1407, 2026-09-20T00:25:30.042716Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1407, 2026-09-20T00:25:30.042716Z)
- `FUELINST|fuelType=OTHER|generation` = **636** (n=1407, 2026-09-20T00:25:30.042716Z)
- `FUELINST|fuelType=PS|generation` = **-132** (n=1407, 2026-09-20T00:25:30.042716Z)
- `FUELINST|fuelType=WIND|generation` = **15588** (n=1407, 2026-09-20T00:25:30.042716Z)
- `IMBALNGC|TOTAL|imbalance` = **-3746** (n=232, 2026-09-20T00:21:29.850397Z)
- `INDDEM|TOTAL|demand` = **-11915** (n=232, 2026-09-20T00:21:13.934904Z)
- `INDGEN|TOTAL|generation` = **16206** (n=232, 2026-09-20T00:21:13.934904Z)
- `MELNGC|TOTAL|margin` = **35985** (n=232, 2026-09-20T00:19:54.139683Z)
- `NDF|TOTAL|demand` = **19452** (n=237, 2026-09-20T00:17:54.556376Z)
- `TSDF|TOTAL|demand` = **19952** (n=237, 2026-09-20T00:17:54.556376Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T00:27:31.414833Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:30.414759Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:29.414692Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:28.414608Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:27.414523Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:26.414446Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:25.414339Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:24.145523Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:23.145429Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:22.145322Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:21.145213Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:20.145115Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:19.145015Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:18.144914Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:27:17.144809Z` — **MID**: 0 rows; marker `2026-09-20T00:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
