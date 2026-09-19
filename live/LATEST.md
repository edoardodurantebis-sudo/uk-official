# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T16:52:42.435654Z`  
Current process started UTC: `2026-09-19T16:48:41.615639Z`  
1-second metadata polls in this process: **226**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1316, 2026-09-19T16:50:33.333635Z)
- `FUELINST|fuelType=NPSHYD|generation` = **410** (n=1316, 2026-09-19T16:50:33.333635Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1316, 2026-09-19T16:50:33.333635Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1316, 2026-09-19T16:50:33.333635Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1316, 2026-09-19T16:50:33.333635Z)
- `FUELINST|fuelType=OTHER|generation` = **1377** (n=1316, 2026-09-19T16:50:33.333635Z)
- `FUELINST|fuelType=PS|generation` = **982** (n=1316, 2026-09-19T16:50:33.333635Z)
- `FUELINST|fuelType=WIND|generation` = **14614** (n=1316, 2026-09-19T16:50:33.333635Z)
- `IMBALNGC|TOTAL|imbalance` = **-3151** (n=216, 2026-09-19T16:25:17.651338Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=216, 2026-09-19T16:25:01.849391Z)
- `INDGEN|TOTAL|generation` = **16801** (n=216, 2026-09-19T16:25:01.849391Z)
- `MELNGC|TOTAL|margin` = **36260** (n=217, 2026-09-19T16:51:04.880682Z)
- `NDF|TOTAL|demand` = **19452** (n=222, 2026-09-19T16:48:41.615647Z)
- `TSDF|TOTAL|demand` = **19952** (n=222, 2026-09-19T16:48:41.615647Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T16:52:41.478913Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:40.478782Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:39.478671Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:38.478559Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:37.478416Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:36.478307Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:35.478158Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:34.478043Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:33.477912Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:32.477791Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:31.477670Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:30.477556Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:29.477466Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:26.912881Z` — **MID**: 0 rows; marker `2026-09-19T16:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:52:26.912881Z` — **FREQ**: 5761 rows; marker `2026-09-19T16:51:45Z`
