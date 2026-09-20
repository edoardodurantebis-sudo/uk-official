# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T06:48:53.760959Z`  
Current process started UTC: `2026-09-20T06:44:53.264157Z`  
1-second metadata polls in this process: **147**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.69 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1248** (n=1483, 2026-09-20T06:45:25.103136Z)
- `FUELINST|fuelType=NPSHYD|generation` = **339** (n=1483, 2026-09-20T06:45:25.103136Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1483, 2026-09-20T06:45:25.103136Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1483, 2026-09-20T06:45:25.103136Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1483, 2026-09-20T06:45:25.103136Z)
- `FUELINST|fuelType=OTHER|generation` = **627** (n=1483, 2026-09-20T06:45:25.103136Z)
- `FUELINST|fuelType=PS|generation` = **-805** (n=1483, 2026-09-20T06:45:25.103136Z)
- `FUELINST|fuelType=WIND|generation` = **15856** (n=1483, 2026-09-20T06:45:25.103136Z)
- `IMBALNGC|TOTAL|imbalance` = **-6854** (n=244, 2026-09-20T06:21:02.514900Z)
- `INDDEM|TOTAL|demand` = **-12306** (n=244, 2026-09-20T06:21:02.514900Z)
- `INDGEN|TOTAL|generation` = **13098** (n=244, 2026-09-20T06:21:02.514900Z)
- `MELNGC|TOTAL|margin` = **37476** (n=244, 2026-09-20T06:19:41.611361Z)
- `NDF|TOTAL|demand` = **19452** (n=250, 2026-09-20T06:47:34.462781Z)
- `TSDF|TOTAL|demand` = **19952** (n=250, 2026-09-20T06:47:34.462781Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T06:48:52.177953Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:50.631457Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:49.101136Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:47.559251Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:46.032972Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:44.475645Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:42.942649Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:41.405810Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:39.868033Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:38.080805Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:36.540481Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:34.989508Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:33.419425Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:31.610188Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:48:30.063332Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
