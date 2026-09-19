# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:42:14.212626Z`  
Current process started UTC: `2026-09-19T14:38:13.450305Z`  
1-second metadata polls in this process: **220**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.20 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-102, delta=-202, z=-12.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.52 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1290, 2026-09-19T14:40:41.545811Z)
- `FUELINST|fuelType=NPSHYD|generation` = **266** (n=1290, 2026-09-19T14:40:41.545811Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1290, 2026-09-19T14:40:41.545811Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1290, 2026-09-19T14:40:41.545811Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1290, 2026-09-19T14:40:41.545811Z)
- `FUELINST|fuelType=OTHER|generation` = **1363** (n=1290, 2026-09-19T14:40:41.545811Z)
- `FUELINST|fuelType=PS|generation` = **-431** (n=1290, 2026-09-19T14:40:41.545811Z)
- `FUELINST|fuelType=WIND|generation` = **13497** (n=1290, 2026-09-19T14:40:41.545811Z)
- `IMBALNGC|TOTAL|imbalance` = **-3230** (n=212, 2026-09-19T14:25:35.374558Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=212, 2026-09-19T14:25:35.374558Z)
- `INDGEN|TOTAL|generation` = **16779** (n=212, 2026-09-19T14:25:35.374558Z)
- `MELNGC|TOTAL|margin` = **36925** (n=212, 2026-09-19T14:20:59.619875Z)
- `NDF|TOTAL|demand` = **19509** (n=217, 2026-09-19T14:18:32.720132Z)
- `TSDF|TOTAL|demand` = **20009** (n=217, 2026-09-19T14:18:32.720132Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:42:13.226136Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:12.223785Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:11.208834Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:10.193442Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:09.119133Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:08.015887Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:07.015811Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:06.001149Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:05.001075Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:03.989714Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:02.978295Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:01.138450Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:42:00.086363Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:41:59.061846Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:41:58.051793Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
