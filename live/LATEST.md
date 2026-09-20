# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T03:34:04.392369Z`  
Current process started UTC: `2026-09-20T03:30:03.361189Z`  
1-second metadata polls in this process: **176**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-5.46 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.90 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1444, 2026-09-20T03:30:21.497328Z)
- `FUELINST|fuelType=NPSHYD|generation` = **296** (n=1444, 2026-09-20T03:30:21.497328Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1444, 2026-09-20T03:30:21.497328Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1444, 2026-09-20T03:30:21.497328Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1444, 2026-09-20T03:30:21.497328Z)
- `FUELINST|fuelType=OTHER|generation` = **492** (n=1444, 2026-09-20T03:30:21.497328Z)
- `FUELINST|fuelType=PS|generation` = **-699** (n=1444, 2026-09-20T03:30:21.497328Z)
- `FUELINST|fuelType=WIND|generation` = **15204** (n=1444, 2026-09-20T03:30:21.497328Z)
- `IMBALNGC|TOTAL|imbalance` = **-3815** (n=238, 2026-09-20T03:20:58.508066Z)
- `INDDEM|TOTAL|demand` = **-12287** (n=238, 2026-09-20T03:20:58.508066Z)
- `INDGEN|TOTAL|generation` = **16137** (n=238, 2026-09-20T03:20:58.508066Z)
- `MELNGC|TOTAL|margin` = **37545** (n=238, 2026-09-20T03:19:19.206204Z)
- `NDF|TOTAL|demand` = **19452** (n=243, 2026-09-20T03:17:24.742276Z)
- `TSDF|TOTAL|demand` = **19952** (n=243, 2026-09-20T03:17:24.742276Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T03:34:03.085027Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:34:00.956136Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:59.662828Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:58.383670Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:57.074483Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:55.813366Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:54.543092Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:53.278562Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:52.022047Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:50.631175Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:49.335895Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:48.069878Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:46.807394Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:45.024472Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:33:43.255458Z` — **MID**: 0 rows; marker `2026-09-20T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
