# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T05:53:50.252531Z`  
Current process started UTC: `2026-09-20T05:49:49.885855Z`  
1-second metadata polls in this process: **226**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.46 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.34 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1472, 2026-09-20T05:50:37.909732Z)
- `FUELINST|fuelType=NPSHYD|generation` = **297** (n=1472, 2026-09-20T05:50:37.909732Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1472, 2026-09-20T05:50:37.909732Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1472, 2026-09-20T05:50:37.909732Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1472, 2026-09-20T05:50:37.909732Z)
- `FUELINST|fuelType=OTHER|generation` = **497** (n=1472, 2026-09-20T05:50:37.909732Z)
- `FUELINST|fuelType=PS|generation` = **-818** (n=1472, 2026-09-20T05:50:37.909732Z)
- `FUELINST|fuelType=WIND|generation` = **15675** (n=1472, 2026-09-20T05:50:37.909732Z)
- `IMBALNGC|TOTAL|imbalance` = **-6774** (n=243, 2026-09-20T05:50:21.783913Z)
- `INDDEM|TOTAL|demand` = **-12309** (n=243, 2026-09-20T05:50:21.783913Z)
- `INDGEN|TOTAL|generation` = **13178** (n=243, 2026-09-20T05:50:21.783913Z)
- `MELNGC|TOTAL|margin` = **37465** (n=243, 2026-09-20T05:49:29.338975Z)
- `NDF|TOTAL|demand` = **19452** (n=248, 2026-09-20T05:47:19.313557Z)
- `TSDF|TOTAL|demand` = **19952** (n=248, 2026-09-20T05:47:19.313557Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T05:53:49.231848Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:48.205471Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:47.192286Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:45.862113Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:44.855443Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:43.847209Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:42.831473Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:41.812686Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:40.795562Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:39.766940Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:38.760047Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:37.753401Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:36.740045Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:35.731461Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:53:34.701129Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
