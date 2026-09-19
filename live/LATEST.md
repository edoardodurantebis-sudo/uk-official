# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T16:27:08.483955Z`  
Current process started UTC: `2026-09-19T16:23:07.768434Z`  
1-second metadata polls in this process: **228**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1311, 2026-09-19T16:25:33.850313Z)
- `FUELINST|fuelType=NPSHYD|generation` = **383** (n=1311, 2026-09-19T16:25:33.850313Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1311, 2026-09-19T16:25:33.850313Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1311, 2026-09-19T16:25:33.850313Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1311, 2026-09-19T16:25:33.850313Z)
- `FUELINST|fuelType=OTHER|generation` = **1243** (n=1311, 2026-09-19T16:25:33.850313Z)
- `FUELINST|fuelType=PS|generation` = **557** (n=1311, 2026-09-19T16:25:33.850313Z)
- `FUELINST|fuelType=WIND|generation` = **14490** (n=1311, 2026-09-19T16:25:33.850313Z)
- `IMBALNGC|TOTAL|imbalance` = **-3151** (n=216, 2026-09-19T16:25:17.651338Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=216, 2026-09-19T16:25:01.849391Z)
- `INDGEN|TOTAL|generation` = **16801** (n=216, 2026-09-19T16:25:01.849391Z)
- `MELNGC|TOTAL|margin` = **36925** (n=216, 2026-09-19T16:21:08.111780Z)
- `NDF|TOTAL|demand` = **19452** (n=221, 2026-09-19T16:19:14.104603Z)
- `TSDF|TOTAL|demand` = **19952** (n=221, 2026-09-19T16:18:57.053710Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T16:27:07.529859Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:27:06.529731Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:27:05.529614Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:27:04.529534Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:27:03.529414Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:27:02.519537Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:27:01.519415Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:27:00.519333Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:26:59.519211Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:26:58.519096Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:26:57.519006Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:26:56.518878Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:26:55.369380Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:26:53.906512Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:26:52.906433Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
