# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T01:34:42.777384Z`  
Current process started UTC: `2026-09-20T01:30:42.160769Z`  
1-second metadata polls in this process: **139**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-7.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.44 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-6.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-6.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=1, z=-6.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=3, z=-6.97 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-7.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1016, delta=-2, z=-7.12 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.24 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-7.37 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-7.68 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.86 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1012, delta=-118, z=-9.25 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **651** (n=1420, 2026-09-20T01:30:42.160777Z)
- `FUELINST|fuelType=NPSHYD|generation` = **323** (n=1420, 2026-09-20T01:30:42.160777Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1420, 2026-09-20T01:30:42.160777Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1420, 2026-09-20T01:30:42.160777Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1420, 2026-09-20T01:30:42.160777Z)
- `FUELINST|fuelType=OTHER|generation` = **477** (n=1420, 2026-09-20T01:30:42.160777Z)
- `FUELINST|fuelType=PS|generation` = **-822** (n=1420, 2026-09-20T01:30:42.160777Z)
- `FUELINST|fuelType=WIND|generation` = **15407** (n=1420, 2026-09-20T01:30:42.160777Z)
- `IMBALNGC|TOTAL|imbalance` = **-3751** (n=234, 2026-09-20T01:21:51.208459Z)
- `INDDEM|TOTAL|demand` = **-12198** (n=234, 2026-09-20T01:21:51.208459Z)
- `INDGEN|TOTAL|generation` = **16201** (n=234, 2026-09-20T01:21:51.208459Z)
- `MELNGC|TOTAL|margin` = **36044** (n=234, 2026-09-20T01:20:14.032301Z)
- `NDF|TOTAL|demand` = **19452** (n=239, 2026-09-20T01:18:02.718208Z)
- `TSDF|TOTAL|demand` = **19952** (n=239, 2026-09-20T01:18:02.718208Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T01:34:41.241468Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:39.674092Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:38.119580Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:36.584037Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:35.034677Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:32.805012Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:31.246680Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:29.696366Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:28.145099Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:26.599640Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:25.047896Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:23.497604Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:21.963424Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:20.321623Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:34:17.072702Z` — **MID**: 0 rows; marker `2026-09-20T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
