# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T06:57:19.578723Z`  
Current process started UTC: `2026-09-20T06:53:18.815562Z`  
1-second metadata polls in this process: **192**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.67 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1248** (n=1485, 2026-09-20T06:55:29.239682Z)
- `FUELINST|fuelType=NPSHYD|generation` = **345** (n=1485, 2026-09-20T06:55:29.239682Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1485, 2026-09-20T06:55:29.239682Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1485, 2026-09-20T06:55:29.239682Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1485, 2026-09-20T06:55:29.239682Z)
- `FUELINST|fuelType=OTHER|generation` = **861** (n=1485, 2026-09-20T06:55:29.239682Z)
- `FUELINST|fuelType=PS|generation` = **-800** (n=1485, 2026-09-20T06:55:29.239682Z)
- `FUELINST|fuelType=WIND|generation` = **15816** (n=1485, 2026-09-20T06:55:29.239682Z)
- `IMBALNGC|TOTAL|imbalance` = **-6802** (n=245, 2026-09-20T06:51:13.366134Z)
- `INDDEM|TOTAL|demand` = **-12302** (n=245, 2026-09-20T06:50:57.374716Z)
- `INDGEN|TOTAL|generation` = **13150** (n=245, 2026-09-20T06:50:57.374716Z)
- `MELNGC|TOTAL|margin` = **37681** (n=245, 2026-09-20T06:49:53.401212Z)
- `NDF|TOTAL|demand` = **19452** (n=250, 2026-09-20T06:47:34.462781Z)
- `TSDF|TOTAL|demand` = **19952** (n=250, 2026-09-20T06:47:34.462781Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T06:57:18.377080Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:17.173540Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:15.945277Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:14.665088Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:13.469755Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:12.242320Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:11.073114Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:09.858577Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:08.640899Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:07.110596Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:05.891645Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:04.710503Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:03.497396Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:02.292317Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:57:01.096603Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
