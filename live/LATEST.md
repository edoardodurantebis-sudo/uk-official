# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T06:27:53.571773Z`  
Current process started UTC: `2026-09-20T06:23:52.494967Z`  
1-second metadata polls in this process: **161**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-4.10 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.13 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.15 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1248** (n=1479, 2026-09-20T06:25:29.681723Z)
- `FUELINST|fuelType=NPSHYD|generation` = **320** (n=1479, 2026-09-20T06:25:29.681723Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1479, 2026-09-20T06:25:29.681723Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1479, 2026-09-20T06:25:29.681723Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1479, 2026-09-20T06:25:29.681723Z)
- `FUELINST|fuelType=OTHER|generation` = **678** (n=1479, 2026-09-20T06:25:29.681723Z)
- `FUELINST|fuelType=PS|generation` = **-805** (n=1479, 2026-09-20T06:25:29.681723Z)
- `FUELINST|fuelType=WIND|generation` = **15813** (n=1479, 2026-09-20T06:25:29.681723Z)
- `IMBALNGC|TOTAL|imbalance` = **-6854** (n=244, 2026-09-20T06:21:02.514900Z)
- `INDDEM|TOTAL|demand` = **-12306** (n=244, 2026-09-20T06:21:02.514900Z)
- `INDGEN|TOTAL|generation` = **13098** (n=244, 2026-09-20T06:21:02.514900Z)
- `MELNGC|TOTAL|margin` = **37476** (n=244, 2026-09-20T06:19:41.611361Z)
- `NDF|TOTAL|demand` = **19452** (n=249, 2026-09-20T06:17:25.387697Z)
- `TSDF|TOTAL|demand` = **19952** (n=249, 2026-09-20T06:17:42.365986Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T06:27:52.119653Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:50.699917Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:49.262990Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:47.783918Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:46.322555Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:44.885331Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:43.425178Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:41.974922Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:40.543463Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:37.902731Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:36.467287Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:35.042723Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:33.612614Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:32.135306Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:27:30.705291Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
