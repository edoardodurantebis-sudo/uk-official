# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T18:00:27.072361Z`  
Current process started UTC: `2026-09-19T17:56:26.561462Z`  
1-second metadata polls in this process: **229**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1329, 2026-09-19T17:55:26.109403Z)
- `FUELINST|fuelType=NPSHYD|generation` = **435** (n=1329, 2026-09-19T17:55:26.109403Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=1329, 2026-09-19T17:55:26.109403Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1329, 2026-09-19T17:55:26.109403Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1329, 2026-09-19T17:55:26.109403Z)
- `FUELINST|fuelType=OTHER|generation` = **1717** (n=1329, 2026-09-19T17:55:26.109403Z)
- `FUELINST|fuelType=PS|generation` = **806** (n=1329, 2026-09-19T17:55:26.109403Z)
- `FUELINST|fuelType=WIND|generation` = **14282** (n=1329, 2026-09-19T17:55:26.109403Z)
- `IMBALNGC|TOTAL|imbalance` = **-3139** (n=219, 2026-09-19T17:53:18.380714Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=219, 2026-09-19T17:53:18.380714Z)
- `INDGEN|TOTAL|generation` = **16813** (n=219, 2026-09-19T17:53:18.380714Z)
- `MELNGC|TOTAL|margin` = **36302** (n=219, 2026-09-19T17:51:00.750598Z)
- `NDF|TOTAL|demand` = **19452** (n=224, 2026-09-19T17:48:18.539367Z)
- `TSDF|TOTAL|demand` = **19952** (n=224, 2026-09-19T17:48:18.539367Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T18:00:26.114687Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:25.114549Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:24.114405Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:23.114275Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:22.096350Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:21.096185Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:20.094945Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:19.094870Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:15.592665Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:15.592665Z` — **FREQ**: 5761 rows; marker `2026-09-19T17:59:45Z`
- `2026-09-19T18:00:14.592583Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:13.592435Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:12.592359Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:11.592262Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:00:10.592130Z` — **MID**: 0 rows; marker `2026-09-19T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
