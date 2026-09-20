# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T05:03:10.296403Z`  
Current process started UTC: `2026-09-20T04:59:09.368642Z`  
1-second metadata polls in this process: **227**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.46 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.34 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.38 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.43 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-4.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=3, z=-4.49 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.64 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.90 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **262** (n=1462, 2026-09-20T05:00:44.598264Z)
- `FUELINST|fuelType=NPSHYD|generation` = **300** (n=1462, 2026-09-20T05:00:44.598264Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3340** (n=1462, 2026-09-20T05:00:44.598264Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1462, 2026-09-20T05:00:44.598264Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1462, 2026-09-20T05:00:44.598264Z)
- `FUELINST|fuelType=OTHER|generation` = **210** (n=1462, 2026-09-20T05:00:44.598264Z)
- `FUELINST|fuelType=PS|generation` = **-695** (n=1462, 2026-09-20T05:00:44.598264Z)
- `FUELINST|fuelType=WIND|generation` = **15449** (n=1462, 2026-09-20T05:00:44.598264Z)
- `IMBALNGC|TOTAL|imbalance` = **-6777** (n=241, 2026-09-20T04:50:32.525251Z)
- `INDDEM|TOTAL|demand` = **-12177** (n=241, 2026-09-20T04:50:32.525251Z)
- `INDGEN|TOTAL|generation` = **13175** (n=241, 2026-09-20T04:50:32.525251Z)
- `MELNGC|TOTAL|margin` = **37516** (n=241, 2026-09-20T04:49:13.726695Z)
- `NDF|TOTAL|demand` = **19452** (n=246, 2026-09-20T04:47:23.759382Z)
- `TSDF|TOTAL|demand` = **19952** (n=246, 2026-09-20T04:47:23.759382Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T05:03:09.194535Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:03:07.925786Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:03:06.694785Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:03:05.694704Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:03:04.694587Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:03:03.694478Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:03:02.694378Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:03:01.694265Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:03:00.694187Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:02:59.694056Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:02:58.448070Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:02:57.447928Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:02:56.447432Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:02:55.447294Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:02:54.447178Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
