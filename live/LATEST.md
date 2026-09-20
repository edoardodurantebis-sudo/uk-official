# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T06:06:21.395668Z`  
Current process started UTC: `2026-09-20T06:02:19.614613Z`  
1-second metadata polls in this process: **181**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.25 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1108** (n=1475, 2026-09-20T06:05:31.906862Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1475, 2026-09-20T06:05:31.906862Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1475, 2026-09-20T06:05:31.906862Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1475, 2026-09-20T06:05:31.906862Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1475, 2026-09-20T06:05:31.906862Z)
- `FUELINST|fuelType=OTHER|generation` = **555** (n=1475, 2026-09-20T06:05:31.906862Z)
- `FUELINST|fuelType=PS|generation` = **-818** (n=1475, 2026-09-20T06:05:31.906862Z)
- `FUELINST|fuelType=WIND|generation` = **15728** (n=1475, 2026-09-20T06:05:31.906862Z)
- `IMBALNGC|TOTAL|imbalance` = **-6774** (n=243, 2026-09-20T05:50:21.783913Z)
- `INDDEM|TOTAL|demand` = **-12309** (n=243, 2026-09-20T05:50:21.783913Z)
- `INDGEN|TOTAL|generation` = **13178** (n=243, 2026-09-20T05:50:21.783913Z)
- `MELNGC|TOTAL|margin` = **37465** (n=243, 2026-09-20T05:49:29.338975Z)
- `NDF|TOTAL|demand` = **19452** (n=248, 2026-09-20T05:47:19.313557Z)
- `TSDF|TOTAL|demand` = **19952** (n=248, 2026-09-20T05:47:19.313557Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T06:06:18.804513Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:18.804513Z` — **FREQ**: 5761 rows; marker `2026-09-20T06:05:45Z`
- `2026-09-20T06:06:17.650198Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:16.458477Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:15.304511Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:14.126900Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:12.941375Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:11.759137Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:10.575810Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:09.400252Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:08.239865Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:07.058271Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:05.887048Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:04.693962Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:06:02.933007Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
