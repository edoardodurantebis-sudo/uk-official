# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T06:32:06.256095Z`  
Current process started UTC: `2026-09-20T06:28:06.192378Z`  
1-second metadata polls in this process: **169**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-4.10 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.28 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1248** (n=1480, 2026-09-20T06:30:33.007174Z)
- `FUELINST|fuelType=NPSHYD|generation` = **327** (n=1480, 2026-09-20T06:30:33.007174Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1480, 2026-09-20T06:30:33.007174Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1480, 2026-09-20T06:30:33.007174Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1480, 2026-09-20T06:30:33.007174Z)
- `FUELINST|fuelType=OTHER|generation` = **700** (n=1480, 2026-09-20T06:30:33.007174Z)
- `FUELINST|fuelType=PS|generation` = **-805** (n=1480, 2026-09-20T06:30:33.007174Z)
- `FUELINST|fuelType=WIND|generation` = **15896** (n=1480, 2026-09-20T06:30:33.007174Z)
- `IMBALNGC|TOTAL|imbalance` = **-6854** (n=244, 2026-09-20T06:21:02.514900Z)
- `INDDEM|TOTAL|demand` = **-12306** (n=244, 2026-09-20T06:21:02.514900Z)
- `INDGEN|TOTAL|generation` = **13098** (n=244, 2026-09-20T06:21:02.514900Z)
- `MELNGC|TOTAL|margin` = **37476** (n=244, 2026-09-20T06:19:41.611361Z)
- `NDF|TOTAL|demand` = **19452** (n=249, 2026-09-20T06:17:25.387697Z)
- `TSDF|TOTAL|demand` = **19952** (n=249, 2026-09-20T06:17:42.365986Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T06:32:04.969989Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:32:03.481650Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:32:02.229972Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:32:00.854895Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:31:59.502321Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:31:58.246435Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:31:56.559938Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:31:55.252113Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:31:53.989803Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:31:52.693577Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:31:51.391831Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:31:49.880413Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:31:48.577973Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:31:47.279000Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:31:45.676038Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
