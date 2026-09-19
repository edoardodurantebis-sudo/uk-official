# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T17:14:13.895810Z`  
Current process started UTC: `2026-09-19T17:10:13.877937Z`  
1-second metadata polls in this process: **146**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1320, 2026-09-19T17:10:46.957546Z)
- `FUELINST|fuelType=NPSHYD|generation` = **430** (n=1320, 2026-09-19T17:10:46.957546Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1320, 2026-09-19T17:10:46.957546Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1320, 2026-09-19T17:10:46.957546Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1320, 2026-09-19T17:10:46.957546Z)
- `FUELINST|fuelType=OTHER|generation` = **1789** (n=1320, 2026-09-19T17:10:46.957546Z)
- `FUELINST|fuelType=PS|generation` = **831** (n=1320, 2026-09-19T17:10:46.957546Z)
- `FUELINST|fuelType=WIND|generation` = **14697** (n=1320, 2026-09-19T17:10:46.957546Z)
- `IMBALNGC|TOTAL|imbalance` = **-3150** (n=217, 2026-09-19T16:53:56.891666Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=217, 2026-09-19T16:53:41.181542Z)
- `INDGEN|TOTAL|generation` = **16802** (n=217, 2026-09-19T16:53:41.181542Z)
- `MELNGC|TOTAL|margin` = **36260** (n=217, 2026-09-19T16:51:04.880682Z)
- `NDF|TOTAL|demand` = **19452** (n=222, 2026-09-19T16:48:41.615647Z)
- `TSDF|TOTAL|demand` = **19952** (n=222, 2026-09-19T16:48:41.615647Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T17:14:12.338099Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:14:10.745383Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:14:09.187350Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:14:07.536521Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:14:06.010384Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:14:04.480540Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:14:02.944554Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:14:00.890737Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:13:59.339647Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:13:57.717405Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:13:56.176988Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:13:54.607237Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:13:53.070983Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:13:51.535158Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:13:50.014486Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
