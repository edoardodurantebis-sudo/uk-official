# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T22:46:06.460969Z`  
Current process started UTC: `2026-09-19T22:42:06.437009Z`  
1-second metadata polls in this process: **146**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-684, delta=0, z=-10.86 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-684, delta=1, z=-11.36 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1226** (n=1387, 2026-09-19T22:45:36.089621Z)
- `FUELINST|fuelType=NPSHYD|generation` = **360** (n=1387, 2026-09-19T22:45:36.089621Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1387, 2026-09-19T22:45:36.089621Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1387, 2026-09-19T22:45:36.089621Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1387, 2026-09-19T22:45:36.089621Z)
- `FUELINST|fuelType=OTHER|generation` = **690** (n=1387, 2026-09-19T22:45:36.089621Z)
- `FUELINST|fuelType=PS|generation` = **-133** (n=1387, 2026-09-19T22:45:36.089621Z)
- `FUELINST|fuelType=WIND|generation` = **15239** (n=1387, 2026-09-19T22:45:36.089621Z)
- `IMBALNGC|TOTAL|imbalance` = **-3915** (n=228, 2026-09-19T22:21:37.701453Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=228, 2026-09-19T22:21:21.429295Z)
- `INDGEN|TOTAL|generation` = **16037** (n=228, 2026-09-19T22:21:21.429295Z)
- `MELNGC|TOTAL|margin` = **36068** (n=228, 2026-09-19T22:19:39.883189Z)
- `NDF|TOTAL|demand` = **19452** (n=233, 2026-09-19T22:17:44.864450Z)
- `TSDF|TOTAL|demand` = **19952** (n=233, 2026-09-19T22:17:44.864450Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T22:46:04.805799Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:46:03.278440Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:46:01.735546Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:46:00.172035Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:45:58.620358Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:45:57.086354Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:45:55.504451Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:45:53.484135Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:45:51.941709Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:45:50.396887Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:45:48.843126Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:45:47.268075Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:45:45.738647Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:45:44.202078Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:45:42.610367Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
