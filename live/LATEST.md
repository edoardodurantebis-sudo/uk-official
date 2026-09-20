# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T03:46:44.692158Z`  
Current process started UTC: `2026-09-20T03:42:43.694976Z`  
1-second metadata polls in this process: **184**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.87 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.95 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-5.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.09 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.14 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.19 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.24 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-5.29 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-5.35 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1447, 2026-09-20T03:45:33.949012Z)
- `FUELINST|fuelType=NPSHYD|generation` = **298** (n=1447, 2026-09-20T03:45:33.949012Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1447, 2026-09-20T03:45:33.949012Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1447, 2026-09-20T03:45:33.949012Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1447, 2026-09-20T03:45:33.949012Z)
- `FUELINST|fuelType=OTHER|generation` = **482** (n=1447, 2026-09-20T03:45:33.949012Z)
- `FUELINST|fuelType=PS|generation` = **-695** (n=1447, 2026-09-20T03:45:33.949012Z)
- `FUELINST|fuelType=WIND|generation` = **15081** (n=1447, 2026-09-20T03:45:33.949012Z)
- `IMBALNGC|TOTAL|imbalance` = **-3815** (n=238, 2026-09-20T03:20:58.508066Z)
- `INDDEM|TOTAL|demand` = **-12287** (n=238, 2026-09-20T03:20:58.508066Z)
- `INDGEN|TOTAL|generation` = **16137** (n=238, 2026-09-20T03:20:58.508066Z)
- `MELNGC|TOTAL|margin` = **37545** (n=238, 2026-09-20T03:19:19.206204Z)
- `NDF|TOTAL|demand` = **19452** (n=243, 2026-09-20T03:17:24.742276Z)
- `TSDF|TOTAL|demand` = **19952** (n=243, 2026-09-20T03:17:24.742276Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T03:46:43.464952Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:42.178538Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:40.897466Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:39.414203Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:38.154518Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:36.639847Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:35.406089Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:34.162588Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:32.889648Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:31.613587Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:30.364722Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:29.132191Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:27.919452Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:26.603374Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:46:25.331143Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
