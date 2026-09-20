# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T06:19:31.351260Z`  
Current process started UTC: `2026-09-20T06:15:31.194318Z`  
1-second metadata polls in this process: **139**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.17 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.20 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1248** (n=1477, 2026-09-20T06:15:31.194329Z)
- `FUELINST|fuelType=NPSHYD|generation` = **318** (n=1477, 2026-09-20T06:15:31.194329Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1477, 2026-09-20T06:15:31.194329Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1477, 2026-09-20T06:15:31.194329Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1477, 2026-09-20T06:15:31.194329Z)
- `FUELINST|fuelType=OTHER|generation` = **497** (n=1477, 2026-09-20T06:15:31.194329Z)
- `FUELINST|fuelType=PS|generation` = **-818** (n=1477, 2026-09-20T06:15:31.194329Z)
- `FUELINST|fuelType=WIND|generation` = **15781** (n=1477, 2026-09-20T06:15:31.194329Z)
- `IMBALNGC|TOTAL|imbalance` = **-6774** (n=243, 2026-09-20T05:50:21.783913Z)
- `INDDEM|TOTAL|demand` = **-12309** (n=243, 2026-09-20T05:50:21.783913Z)
- `INDGEN|TOTAL|generation` = **13178** (n=243, 2026-09-20T05:50:21.783913Z)
- `MELNGC|TOTAL|margin` = **37465** (n=243, 2026-09-20T05:49:29.338975Z)
- `NDF|TOTAL|demand` = **19452** (n=249, 2026-09-20T06:17:25.387697Z)
- `TSDF|TOTAL|demand` = **19952** (n=249, 2026-09-20T06:17:42.365986Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T06:19:29.628611Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:27.952197Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:26.409977Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:24.796973Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:23.211259Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:21.677608Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:18.730977Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:17.078073Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:15.504170Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:13.939848Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:12.278162Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:10.644065Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:09.124032Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:07.510312Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:19:05.839276Z` — **MID**: 0 rows; marker `2026-09-20T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
