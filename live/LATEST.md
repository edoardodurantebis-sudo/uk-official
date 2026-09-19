# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T22:37:41.781090Z`  
Current process started UTC: `2026-09-19T22:33:41.231034Z`  
1-second metadata polls in this process: **173**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-11.96 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-626, delta=-522, z=-16.49 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-12.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-13.44 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-14.42 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=-10, z=-15.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-675, delta=-337, z=-16.96 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-338, delta=-235, z=-8.76 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=94, delta=-6, z=4.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=-378, z=-0.09 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=92, delta=-14, z=4.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.97 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=5.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=1, z=5.06 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1226** (n=1385, 2026-09-19T22:35:35.645864Z)
- `FUELINST|fuelType=NPSHYD|generation` = **366** (n=1385, 2026-09-19T22:35:35.645864Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1385, 2026-09-19T22:35:35.645864Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1385, 2026-09-19T22:35:35.645864Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1385, 2026-09-19T22:35:35.645864Z)
- `FUELINST|fuelType=OTHER|generation` = **688** (n=1385, 2026-09-19T22:35:35.645864Z)
- `FUELINST|fuelType=PS|generation` = **-137** (n=1385, 2026-09-19T22:35:35.645864Z)
- `FUELINST|fuelType=WIND|generation` = **15163** (n=1385, 2026-09-19T22:35:35.645864Z)
- `IMBALNGC|TOTAL|imbalance` = **-3915** (n=228, 2026-09-19T22:21:37.701453Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=228, 2026-09-19T22:21:21.429295Z)
- `INDGEN|TOTAL|generation` = **16037** (n=228, 2026-09-19T22:21:21.429295Z)
- `MELNGC|TOTAL|margin` = **36068** (n=228, 2026-09-19T22:19:39.883189Z)
- `NDF|TOTAL|demand` = **19452** (n=233, 2026-09-19T22:17:44.864450Z)
- `TSDF|TOTAL|demand` = **19952** (n=233, 2026-09-19T22:17:44.864450Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T22:37:40.492989Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:39.176250Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:37.850552Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:36.566641Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:35.240293Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:33.962076Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:32.692963Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:30.926148Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:29.614886Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:28.278211Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:26.991054Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:25.655128Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:24.365424Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:23.047532Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:37:21.735017Z` — **MID**: 0 rows; marker `2026-09-19T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
