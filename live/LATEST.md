# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T18:13:00.815914Z`  
Current process started UTC: `2026-09-19T18:09:00.301636Z`  
1-second metadata polls in this process: **143**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=92, z=-0.01 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-92, delta=10, z=-8.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-31, delta=73, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.20 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-102, delta=-202, z=-12.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=-15, z=-11.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-89, delta=-179, z=-10.03 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1332, 2026-09-19T18:10:24.023629Z)
- `FUELINST|fuelType=NPSHYD|generation` = **477** (n=1332, 2026-09-19T18:10:24.023629Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1332, 2026-09-19T18:10:24.023629Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1332, 2026-09-19T18:10:24.023629Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1332, 2026-09-19T18:10:24.023629Z)
- `FUELINST|fuelType=OTHER|generation` = **1039** (n=1332, 2026-09-19T18:10:24.023629Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1332, 2026-09-19T18:10:24.023629Z)
- `FUELINST|fuelType=WIND|generation` = **14346** (n=1332, 2026-09-19T18:10:24.023629Z)
- `IMBALNGC|TOTAL|imbalance` = **-3139** (n=219, 2026-09-19T17:53:18.380714Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=219, 2026-09-19T17:53:18.380714Z)
- `INDGEN|TOTAL|generation` = **16813** (n=219, 2026-09-19T17:53:18.380714Z)
- `MELNGC|TOTAL|margin` = **36302** (n=219, 2026-09-19T17:51:00.750598Z)
- `NDF|TOTAL|demand` = **19452** (n=224, 2026-09-19T17:48:18.539367Z)
- `TSDF|TOTAL|demand` = **19952** (n=224, 2026-09-19T17:48:18.539367Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T18:12:59.191447Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:57.646347Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:56.082412Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:54.476128Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:52.333069Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:50.767520Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:49.197356Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:47.680117Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:46.120489Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:44.570836Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:42.957410Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:41.387381Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:39.836516Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:38.295591Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:12:36.148932Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
