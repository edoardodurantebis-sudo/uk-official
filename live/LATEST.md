# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T06:44:41.057631Z`  
Current process started UTC: `2026-09-20T06:40:39.946711Z`  
1-second metadata polls in this process: **136**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.72 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-988, delta=26, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.79 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=2, z=-3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-989, delta=24, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.13 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.01 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=2, z=-4.05 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1016, delta=-2, z=-4.08 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1248** (n=1482, 2026-09-20T06:40:39.946719Z)
- `FUELINST|fuelType=NPSHYD|generation` = **337** (n=1482, 2026-09-20T06:40:39.946719Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=1482, 2026-09-20T06:40:39.946719Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1482, 2026-09-20T06:40:39.946719Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1482, 2026-09-20T06:40:39.946719Z)
- `FUELINST|fuelType=OTHER|generation` = **609** (n=1482, 2026-09-20T06:40:39.946719Z)
- `FUELINST|fuelType=PS|generation` = **-805** (n=1482, 2026-09-20T06:40:39.946719Z)
- `FUELINST|fuelType=WIND|generation` = **15839** (n=1482, 2026-09-20T06:40:39.946719Z)
- `IMBALNGC|TOTAL|imbalance` = **-6854** (n=244, 2026-09-20T06:21:02.514900Z)
- `INDDEM|TOTAL|demand` = **-12306** (n=244, 2026-09-20T06:21:02.514900Z)
- `INDGEN|TOTAL|generation` = **13098** (n=244, 2026-09-20T06:21:02.514900Z)
- `MELNGC|TOTAL|margin` = **37476** (n=244, 2026-09-20T06:19:41.611361Z)
- `NDF|TOTAL|demand` = **19452** (n=249, 2026-09-20T06:17:25.387697Z)
- `TSDF|TOTAL|demand` = **19952** (n=249, 2026-09-20T06:17:42.365986Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T06:44:39.321039Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:37.599665Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:35.550392Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:33.850344Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:32.142500Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:30.436982Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:28.709592Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:27.011720Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:25.287601Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:23.564008Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:21.844155Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:19.794683Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:18.083719Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:16.379743Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:44:14.672436Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
