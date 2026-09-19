# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T18:04:37.829562Z`  
Current process started UTC: `2026-09-19T18:00:37.807862Z`  
1-second metadata polls in this process: **136**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1330, 2026-09-19T18:00:37.807871Z)
- `FUELINST|fuelType=NPSHYD|generation` = **440** (n=1330, 2026-09-19T18:00:37.807871Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=1330, 2026-09-19T18:00:37.807871Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1330, 2026-09-19T18:00:37.807871Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1330, 2026-09-19T18:00:37.807871Z)
- `FUELINST|fuelType=OTHER|generation` = **1518** (n=1330, 2026-09-19T18:00:37.807871Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1330, 2026-09-19T18:00:37.807871Z)
- `FUELINST|fuelType=WIND|generation` = **14283** (n=1330, 2026-09-19T18:00:37.807871Z)
- `IMBALNGC|TOTAL|imbalance` = **-3139** (n=219, 2026-09-19T17:53:18.380714Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=219, 2026-09-19T17:53:18.380714Z)
- `INDGEN|TOTAL|generation` = **16813** (n=219, 2026-09-19T17:53:18.380714Z)
- `MELNGC|TOTAL|margin` = **36302** (n=219, 2026-09-19T17:51:00.750598Z)
- `NDF|TOTAL|demand` = **19452** (n=224, 2026-09-19T17:48:18.539367Z)
- `TSDF|TOTAL|demand` = **19952** (n=224, 2026-09-19T17:48:18.539367Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T18:04:34.696986Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:33.073564Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:31.407350Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:29.731148Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:28.124835Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:26.491217Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:24.823864Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:23.167521Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:21.532641Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:17.919778Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:17.919778Z` — **FREQ**: 5761 rows; marker `2026-09-19T18:03:45Z`
- `2026-09-19T18:04:16.273091Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:14.631955Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:12.975797Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:04:11.314902Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
