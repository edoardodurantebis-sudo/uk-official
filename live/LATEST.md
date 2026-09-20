# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T01:47:18.550214Z`  
Current process started UTC: `2026-09-20T01:43:16.810822Z`  
1-second metadata polls in this process: **217**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-6.17 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-6.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.34 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-7.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.44 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-6.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-6.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=1, z=-6.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=3, z=-6.97 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-7.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1016, delta=-2, z=-7.12 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.24 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-7.37 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.53 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **651** (n=1423, 2026-09-20T01:45:44.301608Z)
- `FUELINST|fuelType=NPSHYD|generation` = **323** (n=1423, 2026-09-20T01:45:44.301608Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1423, 2026-09-20T01:45:44.301608Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1423, 2026-09-20T01:45:44.301608Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1423, 2026-09-20T01:45:44.301608Z)
- `FUELINST|fuelType=OTHER|generation` = **209** (n=1423, 2026-09-20T01:45:44.301608Z)
- `FUELINST|fuelType=PS|generation` = **-820** (n=1423, 2026-09-20T01:45:44.301608Z)
- `FUELINST|fuelType=WIND|generation` = **15321** (n=1423, 2026-09-20T01:45:44.301608Z)
- `IMBALNGC|TOTAL|imbalance` = **-3751** (n=234, 2026-09-20T01:21:51.208459Z)
- `INDDEM|TOTAL|demand` = **-12198** (n=234, 2026-09-20T01:21:51.208459Z)
- `INDGEN|TOTAL|generation` = **16201** (n=234, 2026-09-20T01:21:51.208459Z)
- `MELNGC|TOTAL|margin` = **36044** (n=234, 2026-09-20T01:20:14.032301Z)
- `NDF|TOTAL|demand` = **19452** (n=239, 2026-09-20T01:18:02.718208Z)
- `TSDF|TOTAL|demand` = **19952** (n=239, 2026-09-20T01:18:02.718208Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T01:47:16.684800Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:15.618601Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:14.430916Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:13.217107Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:11.867572Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:10.406301Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:09.006975Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:08.006884Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:06.739864Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:05.245771Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:04.195852Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:03.102255Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:01.782524Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:47:00.582545Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:46:58.978903Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
