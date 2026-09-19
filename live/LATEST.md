# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T19:03:21.250882Z`  
Current process started UTC: `2026-09-19T18:59:19.905861Z`  
1-second metadata polls in this process: **169**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1342, 2026-09-19T19:00:41.665923Z)
- `FUELINST|fuelType=NPSHYD|generation` = **502** (n=1342, 2026-09-19T19:00:41.665923Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1342, 2026-09-19T19:00:41.665923Z)
- `FUELINST|fuelType=OCGT|generation` = **20** (n=1342, 2026-09-19T19:00:41.665923Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1342, 2026-09-19T19:00:41.665923Z)
- `FUELINST|fuelType=OTHER|generation` = **1174** (n=1342, 2026-09-19T19:00:41.665923Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1342, 2026-09-19T19:00:41.665923Z)
- `FUELINST|fuelType=WIND|generation` = **14210** (n=1342, 2026-09-19T19:00:41.665923Z)
- `IMBALNGC|TOTAL|imbalance` = **-3742** (n=221, 2026-09-19T18:54:47.042884Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=221, 2026-09-19T18:54:31.530560Z)
- `INDGEN|TOTAL|generation` = **16210** (n=221, 2026-09-19T18:54:31.530560Z)
- `MELNGC|TOTAL|margin` = **36202** (n=221, 2026-09-19T18:51:13.295596Z)
- `NDF|TOTAL|demand` = **19452** (n=226, 2026-09-19T18:48:41.702714Z)
- `TSDF|TOTAL|demand` = **19952** (n=226, 2026-09-19T18:48:41.702714Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T19:03:19.578385Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:18.311898Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:16.565487Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:15.315275Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:13.498553Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:11.876959Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:10.536700Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:08.002716Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:06.276558Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:04.888776Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:03.614429Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:02.206991Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:03:00.429083Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:02:58.937861Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:02:57.603121Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
