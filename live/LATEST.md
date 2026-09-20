# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T01:13:41.379883Z`  
Current process started UTC: `2026-09-20T01:09:39.544631Z`  
1-second metadata polls in this process: **134**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=1, z=-6.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=3, z=-6.97 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-7.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1016, delta=-2, z=-7.12 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.24 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-7.37 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-7.68 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.86 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1012, delta=-118, z=-9.25 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-8.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-8.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=2, z=-8.42 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-8.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-6, z=-8.91 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **651** (n=1416, 2026-09-20T01:10:43.648296Z)
- `FUELINST|fuelType=NPSHYD|generation` = **322** (n=1416, 2026-09-20T01:10:43.648296Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1416, 2026-09-20T01:10:43.648296Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1416, 2026-09-20T01:10:43.648296Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1416, 2026-09-20T01:10:43.648296Z)
- `FUELINST|fuelType=OTHER|generation` = **605** (n=1416, 2026-09-20T01:10:43.648296Z)
- `FUELINST|fuelType=PS|generation` = **-730** (n=1416, 2026-09-20T01:10:43.648296Z)
- `FUELINST|fuelType=WIND|generation` = **15583** (n=1416, 2026-09-20T01:10:43.648296Z)
- `IMBALNGC|TOTAL|imbalance` = **-3763** (n=233, 2026-09-20T00:51:38.211016Z)
- `INDDEM|TOTAL|demand` = **-11949** (n=233, 2026-09-20T00:51:38.211016Z)
- `INDGEN|TOTAL|generation` = **16189** (n=233, 2026-09-20T00:51:38.211016Z)
- `MELNGC|TOTAL|margin` = **36027** (n=233, 2026-09-20T00:49:47.495939Z)
- `NDF|TOTAL|demand` = **19452** (n=238, 2026-09-20T00:47:47.229077Z)
- `TSDF|TOTAL|demand` = **19952** (n=238, 2026-09-20T00:47:47.229077Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T01:13:39.114047Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:37.406063Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:35.690078Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:33.935339Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:32.212762Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:30.526113Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:28.810125Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:27.118663Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:25.426214Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:23.218842Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:21.497767Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:19.789172Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:18.081562Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:16.381032Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:13:14.683240Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
