# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T01:26:15.918889Z`  
Current process started UTC: `2026-09-20T01:22:15.910146Z`  
1-second metadata polls in this process: **197**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-6.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-6.75 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **651** (n=1419, 2026-09-20T01:25:34.422478Z)
- `FUELINST|fuelType=NPSHYD|generation` = **323** (n=1419, 2026-09-20T01:25:34.422478Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1419, 2026-09-20T01:25:34.422478Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1419, 2026-09-20T01:25:34.422478Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1419, 2026-09-20T01:25:34.422478Z)
- `FUELINST|fuelType=OTHER|generation` = **541** (n=1419, 2026-09-20T01:25:34.422478Z)
- `FUELINST|fuelType=PS|generation` = **-820** (n=1419, 2026-09-20T01:25:34.422478Z)
- `FUELINST|fuelType=WIND|generation` = **15456** (n=1419, 2026-09-20T01:25:34.422478Z)
- `IMBALNGC|TOTAL|imbalance` = **-3751** (n=234, 2026-09-20T01:21:51.208459Z)
- `INDDEM|TOTAL|demand` = **-12198** (n=234, 2026-09-20T01:21:51.208459Z)
- `INDGEN|TOTAL|generation` = **16201** (n=234, 2026-09-20T01:21:51.208459Z)
- `MELNGC|TOTAL|margin` = **36044** (n=234, 2026-09-20T01:20:14.032301Z)
- `NDF|TOTAL|demand` = **19452** (n=239, 2026-09-20T01:18:02.718208Z)
- `TSDF|TOTAL|demand` = **19952** (n=239, 2026-09-20T01:18:02.718208Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T01:26:14.775519Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:26:13.639814Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:26:12.490296Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:26:11.355393Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:26:07.027832Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:26:07.027832Z` — **FREQ**: 5761 rows; marker `2026-09-20T01:25:45Z`
- `2026-09-20T01:26:05.891783Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:26:04.735943Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:26:03.607219Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:26:02.453077Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:26:01.298678Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:26:00.137656Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:25:58.993853Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:25:57.867463Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:25:56.725139Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
