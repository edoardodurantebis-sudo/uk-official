# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T02:46:43.226895Z`  
Current process started UTC: `2026-09-20T02:42:41.643330Z`  
1-second metadata polls in this process: **136**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-5.35 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-5.46 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-5.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-5.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-6.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.08 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-6.17 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **329** (n=1435, 2026-09-20T02:45:33.075372Z)
- `FUELINST|fuelType=NPSHYD|generation` = **307** (n=1435, 2026-09-20T02:45:33.075372Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1435, 2026-09-20T02:45:33.075372Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1435, 2026-09-20T02:45:33.075372Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1435, 2026-09-20T02:45:33.075372Z)
- `FUELINST|fuelType=OTHER|generation` = **370** (n=1435, 2026-09-20T02:45:33.075372Z)
- `FUELINST|fuelType=PS|generation` = **-697** (n=1435, 2026-09-20T02:45:33.075372Z)
- `FUELINST|fuelType=WIND|generation` = **15326** (n=1435, 2026-09-20T02:45:33.075372Z)
- `IMBALNGC|TOTAL|imbalance` = **-3755** (n=236, 2026-09-20T02:21:16.829176Z)
- `INDDEM|TOTAL|demand` = **-12197** (n=236, 2026-09-20T02:21:16.829176Z)
- `INDGEN|TOTAL|generation` = **16197** (n=236, 2026-09-20T02:21:16.829176Z)
- `MELNGC|TOTAL|margin` = **37606** (n=236, 2026-09-20T02:19:46.154039Z)
- `NDF|TOTAL|demand` = **19452** (n=241, 2026-09-20T02:17:36.584473Z)
- `TSDF|TOTAL|demand` = **19952** (n=241, 2026-09-20T02:17:36.584473Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T02:46:41.505184Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:39.800582Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:38.091487Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:36.153572Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:34.470872Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:32.763091Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:31.060506Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:29.341959Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:27.644428Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:25.961223Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:24.262822Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:20.891885Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:20.891885Z` — **FREQ**: 5761 rows; marker `2026-09-20T02:45:45Z`
- `2026-09-20T02:46:19.169181Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:46:17.482685Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
