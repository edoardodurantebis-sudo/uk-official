# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T22:29:16.796197Z`  
Current process started UTC: `2026-09-19T22:25:16.610416Z`  
1-second metadata polls in this process: **133**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=-250, z=-0.07 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=100, delta=4, z=5.22 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=378, delta=4, z=13.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1226** (n=1383, 2026-09-19T22:25:33.581502Z)
- `FUELINST|fuelType=NPSHYD|generation` = **372** (n=1383, 2026-09-19T22:25:33.581502Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3340** (n=1383, 2026-09-19T22:25:33.581502Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1383, 2026-09-19T22:25:33.581502Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1383, 2026-09-19T22:25:33.581502Z)
- `FUELINST|fuelType=OTHER|generation` = **350** (n=1383, 2026-09-19T22:25:33.581502Z)
- `FUELINST|fuelType=PS|generation` = **-16** (n=1383, 2026-09-19T22:25:33.581502Z)
- `FUELINST|fuelType=WIND|generation` = **15175** (n=1383, 2026-09-19T22:25:33.581502Z)
- `IMBALNGC|TOTAL|imbalance` = **-3915** (n=228, 2026-09-19T22:21:37.701453Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=228, 2026-09-19T22:21:21.429295Z)
- `INDGEN|TOTAL|generation` = **16037** (n=228, 2026-09-19T22:21:21.429295Z)
- `MELNGC|TOTAL|margin` = **36068** (n=228, 2026-09-19T22:19:39.883189Z)
- `NDF|TOTAL|demand` = **19452** (n=233, 2026-09-19T22:17:44.864450Z)
- `TSDF|TOTAL|demand` = **19952** (n=233, 2026-09-19T22:17:44.864450Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T22:29:15.116753Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:29:13.423763Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:29:11.706842Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:29:10.014122Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:29:08.312616Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:29:06.626625Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:29:04.884695Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:29:02.742929Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:29:01.041710Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:28:59.337962Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:28:57.649964Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:28:55.953781Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:28:54.194901Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:28:52.504197Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:28:50.809307Z` — **MID**: 0 rows; marker `2026-09-19T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
