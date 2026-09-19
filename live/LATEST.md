# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T20:23:29.572705Z`  
Current process started UTC: `2026-09-19T20:19:29.129387Z`  
1-second metadata polls in this process: **221**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=11.75 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=404, delta=1, z=12.44 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1358, 2026-09-19T20:20:34.414958Z)
- `FUELINST|fuelType=NPSHYD|generation` = **487** (n=1358, 2026-09-19T20:20:34.414958Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1358, 2026-09-19T20:20:34.414958Z)
- `FUELINST|fuelType=OCGT|generation` = **106** (n=1358, 2026-09-19T20:20:34.414958Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1358, 2026-09-19T20:20:34.414958Z)
- `FUELINST|fuelType=OTHER|generation` = **651** (n=1358, 2026-09-19T20:20:34.414958Z)
- `FUELINST|fuelType=PS|generation` = **823** (n=1358, 2026-09-19T20:20:34.414958Z)
- `FUELINST|fuelType=WIND|generation` = **14107** (n=1358, 2026-09-19T20:20:34.414958Z)
- `IMBALNGC|TOTAL|imbalance` = **-3820** (n=224, 2026-09-19T20:22:42.485438Z)
- `INDDEM|TOTAL|demand` = **-11873** (n=224, 2026-09-19T20:22:26.195138Z)
- `INDGEN|TOTAL|generation` = **16132** (n=224, 2026-09-19T20:22:26.195138Z)
- `MELNGC|TOTAL|margin` = **36251** (n=224, 2026-09-19T20:20:18.046700Z)
- `NDF|TOTAL|demand` = **19452** (n=229, 2026-09-19T20:17:59.606414Z)
- `TSDF|TOTAL|demand` = **19952** (n=229, 2026-09-19T20:17:59.606414Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T20:23:28.527513Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:27.508867Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:26.486208Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:25.472551Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:24.460010Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:23.377209Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:22.360069Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:21.307477Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:20.282636Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:19.281621Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:18.275266Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:17.237447Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:16.237379Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:15.207506Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:23:13.839777Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
