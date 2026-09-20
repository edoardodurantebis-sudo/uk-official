# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T05:07:21.691559Z`  
Current process started UTC: `2026-09-20T05:03:21.136156Z`  
1-second metadata polls in this process: **227**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.64 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **564** (n=1463, 2026-09-20T05:05:29.106249Z)
- `FUELINST|fuelType=NPSHYD|generation` = **305** (n=1463, 2026-09-20T05:05:29.106249Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1463, 2026-09-20T05:05:29.106249Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1463, 2026-09-20T05:05:29.106249Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1463, 2026-09-20T05:05:29.106249Z)
- `FUELINST|fuelType=OTHER|generation` = **404** (n=1463, 2026-09-20T05:05:29.106249Z)
- `FUELINST|fuelType=PS|generation` = **-693** (n=1463, 2026-09-20T05:05:29.106249Z)
- `FUELINST|fuelType=WIND|generation` = **15423** (n=1463, 2026-09-20T05:05:29.106249Z)
- `IMBALNGC|TOTAL|imbalance` = **-6777** (n=241, 2026-09-20T04:50:32.525251Z)
- `INDDEM|TOTAL|demand` = **-12177** (n=241, 2026-09-20T04:50:32.525251Z)
- `INDGEN|TOTAL|generation` = **13175** (n=241, 2026-09-20T04:50:32.525251Z)
- `MELNGC|TOTAL|margin` = **37516** (n=241, 2026-09-20T04:49:13.726695Z)
- `NDF|TOTAL|demand` = **19452** (n=246, 2026-09-20T04:47:23.759382Z)
- `TSDF|TOTAL|demand` = **19952** (n=246, 2026-09-20T04:47:23.759382Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T05:07:20.730719Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:19.730609Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:18.730479Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:17.730359Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:16.730244Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:15.730147Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:14.730007Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:13.729925Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:12.729816Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:11.729695Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:10.729583Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:09.729500Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:08.729389Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:07.729307Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:07:06.729195Z` — **MID**: 0 rows; marker `2026-09-20T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
