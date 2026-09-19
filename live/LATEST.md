# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:29:36.627263Z`  
Current process started UTC: `2026-09-19T14:25:35.374550Z`  
1-second metadata polls in this process: **138**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=-15, z=-11.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-89, delta=-179, z=-10.03 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=100, delta=26, z=19.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=90, delta=-13, z=10.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=12.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=13.38 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=14.43 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=15.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=1, z=17.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=74, delta=74, z=126.77 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=102, delta=0, z=19.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=102, delta=0, z=24.13 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1287, 2026-09-19T14:25:35.374558Z)
- `FUELINST|fuelType=NPSHYD|generation` = **282** (n=1287, 2026-09-19T14:25:35.374558Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1287, 2026-09-19T14:25:35.374558Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1287, 2026-09-19T14:25:35.374558Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1287, 2026-09-19T14:25:35.374558Z)
- `FUELINST|fuelType=OTHER|generation` = **774** (n=1287, 2026-09-19T14:25:35.374558Z)
- `FUELINST|fuelType=PS|generation` = **-255** (n=1287, 2026-09-19T14:25:35.374558Z)
- `FUELINST|fuelType=WIND|generation` = **13975** (n=1287, 2026-09-19T14:25:35.374558Z)
- `IMBALNGC|TOTAL|imbalance` = **-3230** (n=212, 2026-09-19T14:25:35.374558Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=212, 2026-09-19T14:25:35.374558Z)
- `INDGEN|TOTAL|generation` = **16779** (n=212, 2026-09-19T14:25:35.374558Z)
- `MELNGC|TOTAL|margin` = **36925** (n=212, 2026-09-19T14:20:59.619875Z)
- `NDF|TOTAL|demand` = **19509** (n=217, 2026-09-19T14:18:32.720132Z)
- `TSDF|TOTAL|demand` = **20009** (n=217, 2026-09-19T14:18:32.720132Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:29:35.077370Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:33.484066Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:31.853032Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:30.316894Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:28.343452Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:26.746996Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:25.039897Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:23.431677Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:21.886188Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:20.290478Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:18.636247Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:16.153281Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:14.606519Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:12.141548Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:29:10.601569Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
