# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T20:19:18.899804Z`  
Current process started UTC: `2026-09-19T20:15:18.696011Z`  
1-second metadata polls in this process: **220**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.93 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1357, 2026-09-19T20:15:34.971792Z)
- `FUELINST|fuelType=NPSHYD|generation` = **488** (n=1357, 2026-09-19T20:15:34.971792Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1357, 2026-09-19T20:15:34.971792Z)
- `FUELINST|fuelType=OCGT|generation` = **106** (n=1357, 2026-09-19T20:15:34.971792Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1357, 2026-09-19T20:15:34.971792Z)
- `FUELINST|fuelType=OTHER|generation` = **874** (n=1357, 2026-09-19T20:15:34.971792Z)
- `FUELINST|fuelType=PS|generation` = **823** (n=1357, 2026-09-19T20:15:34.971792Z)
- `FUELINST|fuelType=WIND|generation` = **14089** (n=1357, 2026-09-19T20:15:34.971792Z)
- `IMBALNGC|TOTAL|imbalance` = **-3790** (n=223, 2026-09-19T19:52:47.570321Z)
- `INDDEM|TOTAL|demand` = **-11873** (n=223, 2026-09-19T19:52:31.555589Z)
- `INDGEN|TOTAL|generation` = **16162** (n=223, 2026-09-19T19:52:47.570321Z)
- `MELNGC|TOTAL|margin` = **36216** (n=223, 2026-09-19T19:50:05.899376Z)
- `NDF|TOTAL|demand` = **19452** (n=229, 2026-09-19T20:17:59.606414Z)
- `TSDF|TOTAL|demand` = **19952** (n=229, 2026-09-19T20:17:59.606414Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T20:19:17.893094Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:16.856815Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:15.809404Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:14.802456Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:13.800897Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:12.787405Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:11.773932Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:10.761644Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:09.693669Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:08.609905Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:07.287170Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:06.267865Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:04.197385Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:03.163341Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:19:02.134717Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
