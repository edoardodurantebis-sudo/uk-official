# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T01:09:28.742536Z`  
Current process started UTC: `2026-09-20T01:05:28.604133Z`  
1-second metadata polls in this process: **210**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1008, delta=-111, z=-9.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **730** (n=1415, 2026-09-20T01:05:45.859862Z)
- `FUELINST|fuelType=NPSHYD|generation` = **321** (n=1415, 2026-09-20T01:05:45.859862Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1415, 2026-09-20T01:05:45.859862Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1415, 2026-09-20T01:05:45.859862Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1415, 2026-09-20T01:05:45.859862Z)
- `FUELINST|fuelType=OTHER|generation` = **427** (n=1415, 2026-09-20T01:05:45.859862Z)
- `FUELINST|fuelType=PS|generation` = **-476** (n=1415, 2026-09-20T01:05:45.859862Z)
- `FUELINST|fuelType=WIND|generation` = **15582** (n=1415, 2026-09-20T01:05:45.859862Z)
- `IMBALNGC|TOTAL|imbalance` = **-3763** (n=233, 2026-09-20T00:51:38.211016Z)
- `INDDEM|TOTAL|demand` = **-11949** (n=233, 2026-09-20T00:51:38.211016Z)
- `INDGEN|TOTAL|generation` = **16189** (n=233, 2026-09-20T00:51:38.211016Z)
- `MELNGC|TOTAL|margin` = **36027** (n=233, 2026-09-20T00:49:47.495939Z)
- `NDF|TOTAL|demand` = **19452** (n=238, 2026-09-20T00:47:47.229077Z)
- `TSDF|TOTAL|demand` = **19952** (n=238, 2026-09-20T00:47:47.229077Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T01:09:27.734737Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:26.711044Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:25.707054Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:24.672359Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:23.655913Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:22.604225Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:21.604149Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:19.873481Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:18.870893Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:17.836303Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:16.817734Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:15.817655Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:14.813504Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:13.813406Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:09:12.813328Z` — **MID**: 0 rows; marker `2026-09-20T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
