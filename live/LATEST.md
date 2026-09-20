# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T01:05:18.108767Z`  
Current process started UTC: `2026-09-20T01:01:16.549160Z`  
1-second metadata polls in this process: **181**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1008, delta=-111, z=-9.12 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-894, delta=-4, z=-9.66 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **882** (n=1414, 2026-09-20T01:00:34.722046Z)
- `FUELINST|fuelType=NPSHYD|generation` = **312** (n=1414, 2026-09-20T01:00:34.722046Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1414, 2026-09-20T01:00:34.722046Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1414, 2026-09-20T01:00:34.722046Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1414, 2026-09-20T01:00:34.722046Z)
- `FUELINST|fuelType=OTHER|generation` = **297** (n=1414, 2026-09-20T01:00:34.722046Z)
- `FUELINST|fuelType=PS|generation` = **-254** (n=1414, 2026-09-20T01:00:34.722046Z)
- `FUELINST|fuelType=WIND|generation` = **15567** (n=1414, 2026-09-20T01:00:34.722046Z)
- `IMBALNGC|TOTAL|imbalance` = **-3763** (n=233, 2026-09-20T00:51:38.211016Z)
- `INDDEM|TOTAL|demand` = **-11949** (n=233, 2026-09-20T00:51:38.211016Z)
- `INDGEN|TOTAL|generation` = **16189** (n=233, 2026-09-20T00:51:38.211016Z)
- `MELNGC|TOTAL|margin` = **36027** (n=233, 2026-09-20T00:49:47.495939Z)
- `NDF|TOTAL|demand` = **19452** (n=238, 2026-09-20T00:47:47.229077Z)
- `TSDF|TOTAL|demand` = **19952** (n=238, 2026-09-20T00:47:47.229077Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T01:05:16.538358Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:05:15.183135Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:05:14.069761Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:05:12.865209Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:05:11.649029Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:05:10.474371Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:05:09.304247Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:05:08.182315Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:05:06.976718Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:05:04.874104Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:05:03.312506Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:05:01.358660Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:04:59.779499Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:04:58.627131Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:04:57.468987Z` — **MID**: 0 rows; marker `2026-09-20T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
