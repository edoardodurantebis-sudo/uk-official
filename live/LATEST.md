# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T01:38:56.115226Z`  
Current process started UTC: `2026-09-20T01:34:55.381612Z`  
1-second metadata polls in this process: **138**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.34 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-7.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.44 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **651** (n=1421, 2026-09-20T01:35:30.841064Z)
- `FUELINST|fuelType=NPSHYD|generation` = **323** (n=1421, 2026-09-20T01:35:30.841064Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1421, 2026-09-20T01:35:30.841064Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1421, 2026-09-20T01:35:30.841064Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1421, 2026-09-20T01:35:30.841064Z)
- `FUELINST|fuelType=OTHER|generation` = **412** (n=1421, 2026-09-20T01:35:30.841064Z)
- `FUELINST|fuelType=PS|generation` = **-825** (n=1421, 2026-09-20T01:35:30.841064Z)
- `FUELINST|fuelType=WIND|generation` = **15403** (n=1421, 2026-09-20T01:35:30.841064Z)
- `IMBALNGC|TOTAL|imbalance` = **-3751** (n=234, 2026-09-20T01:21:51.208459Z)
- `INDDEM|TOTAL|demand` = **-12198** (n=234, 2026-09-20T01:21:51.208459Z)
- `INDGEN|TOTAL|generation` = **16201** (n=234, 2026-09-20T01:21:51.208459Z)
- `MELNGC|TOTAL|margin` = **36044** (n=234, 2026-09-20T01:20:14.032301Z)
- `NDF|TOTAL|demand` = **19452** (n=239, 2026-09-20T01:18:02.718208Z)
- `TSDF|TOTAL|demand` = **19952** (n=239, 2026-09-20T01:18:02.718208Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T01:38:54.046551Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:52.410217Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:50.732498Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:49.089095Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:47.475123Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:45.842655Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:44.207833Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:42.553176Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:40.888287Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:39.277548Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:37.095005Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:35.438292Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:33.807649Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:32.159575Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:38:30.535941Z` — **MID**: 0 rows; marker `2026-09-20T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
