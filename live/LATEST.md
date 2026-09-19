# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T17:05:49.701804Z`  
Current process started UTC: `2026-09-19T17:01:49.164796Z`  
1-second metadata polls in this process: **212**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1319, 2026-09-19T17:05:19.689604Z)
- `FUELINST|fuelType=NPSHYD|generation` = **436** (n=1319, 2026-09-19T17:05:19.689604Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1319, 2026-09-19T17:05:19.689604Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1319, 2026-09-19T17:05:19.689604Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1319, 2026-09-19T17:05:19.689604Z)
- `FUELINST|fuelType=OTHER|generation` = **1491** (n=1319, 2026-09-19T17:05:19.689604Z)
- `FUELINST|fuelType=PS|generation` = **916** (n=1319, 2026-09-19T17:05:19.689604Z)
- `FUELINST|fuelType=WIND|generation` = **14731** (n=1319, 2026-09-19T17:05:19.689604Z)
- `IMBALNGC|TOTAL|imbalance` = **-3150** (n=217, 2026-09-19T16:53:56.891666Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=217, 2026-09-19T16:53:41.181542Z)
- `INDGEN|TOTAL|generation` = **16802** (n=217, 2026-09-19T16:53:41.181542Z)
- `MELNGC|TOTAL|margin` = **36260** (n=217, 2026-09-19T16:51:04.880682Z)
- `NDF|TOTAL|demand` = **19452** (n=222, 2026-09-19T16:48:41.615647Z)
- `TSDF|TOTAL|demand` = **19952** (n=222, 2026-09-19T16:48:41.615647Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T17:05:48.692767Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:47.692669Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:46.664505Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:45.651721Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:44.613697Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:43.601551Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:42.579326Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:41.568759Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:40.538126Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:39.489600Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:38.478382Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:37.439609Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:35.911853Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:34.895790Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:05:33.870245Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
