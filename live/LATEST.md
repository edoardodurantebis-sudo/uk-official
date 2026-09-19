# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T16:39:58.852769Z`  
Current process started UTC: `2026-09-19T16:35:58.775093Z`  
1-second metadata polls in this process: **170**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1313, 2026-09-19T16:35:36.873589Z)
- `FUELINST|fuelType=NPSHYD|generation` = **406** (n=1313, 2026-09-19T16:35:36.873589Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1313, 2026-09-19T16:35:36.873589Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1313, 2026-09-19T16:35:36.873589Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1313, 2026-09-19T16:35:36.873589Z)
- `FUELINST|fuelType=OTHER|generation` = **1074** (n=1313, 2026-09-19T16:35:36.873589Z)
- `FUELINST|fuelType=PS|generation` = **863** (n=1313, 2026-09-19T16:35:36.873589Z)
- `FUELINST|fuelType=WIND|generation` = **14653** (n=1313, 2026-09-19T16:35:36.873589Z)
- `IMBALNGC|TOTAL|imbalance` = **-3151** (n=216, 2026-09-19T16:25:17.651338Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=216, 2026-09-19T16:25:01.849391Z)
- `INDGEN|TOTAL|generation` = **16801** (n=216, 2026-09-19T16:25:01.849391Z)
- `MELNGC|TOTAL|margin` = **36925** (n=216, 2026-09-19T16:21:08.111780Z)
- `NDF|TOTAL|demand` = **19452** (n=221, 2026-09-19T16:19:14.104603Z)
- `TSDF|TOTAL|demand` = **19952** (n=221, 2026-09-19T16:18:57.053710Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T16:39:57.533101Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:56.222606Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:54.859153Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:53.529066Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:52.218339Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:50.143136Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:48.788293Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:47.421869Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:46.099770Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:44.774034Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:43.483568Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:42.119482Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:40.752772Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:39.454788Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:39:38.174318Z` — **MID**: 0 rows; marker `2026-09-19T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
