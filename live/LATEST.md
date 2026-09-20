# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T05:19:54.458872Z`  
Current process started UTC: `2026-09-20T05:15:54.081413Z`  
1-second metadata polls in this process: **144**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.20 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.25 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1465, 2026-09-20T05:15:27.966127Z)
- `FUELINST|fuelType=NPSHYD|generation` = **297** (n=1465, 2026-09-20T05:15:27.966127Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1465, 2026-09-20T05:15:27.966127Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1465, 2026-09-20T05:15:27.966127Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1465, 2026-09-20T05:15:27.966127Z)
- `FUELINST|fuelType=OTHER|generation` = **425** (n=1465, 2026-09-20T05:15:27.966127Z)
- `FUELINST|fuelType=PS|generation` = **-697** (n=1465, 2026-09-20T05:15:27.966127Z)
- `FUELINST|fuelType=WIND|generation` = **15453** (n=1465, 2026-09-20T05:15:27.966127Z)
- `IMBALNGC|TOTAL|imbalance` = **-6777** (n=241, 2026-09-20T04:50:32.525251Z)
- `INDDEM|TOTAL|demand` = **-12177** (n=241, 2026-09-20T04:50:32.525251Z)
- `INDGEN|TOTAL|generation` = **13175** (n=241, 2026-09-20T04:50:32.525251Z)
- `MELNGC|TOTAL|margin` = **37520** (n=242, 2026-09-20T05:19:07.535945Z)
- `NDF|TOTAL|demand` = **19452** (n=247, 2026-09-20T05:17:31.650511Z)
- `TSDF|TOTAL|demand` = **19952** (n=247, 2026-09-20T05:17:31.650511Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T05:19:52.896773Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:51.336377Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:49.507688Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:47.949068Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:46.286752Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:44.678815Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:43.094755Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:41.300625Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:39.655909Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:38.082442Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:36.530925Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:34.990941Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:33.376499Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:31.762134Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:19:30.216611Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
