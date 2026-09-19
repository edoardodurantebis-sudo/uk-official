# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:46:26.364085Z`  
Current process started UTC: `2026-09-19T14:42:24.781903Z`  
1-second metadata polls in this process: **174**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=100, delta=26, z=19.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=90, delta=-13, z=10.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=12.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=13.38 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=14.43 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1291, 2026-09-19T14:45:35.984144Z)
- `FUELINST|fuelType=NPSHYD|generation` = **265** (n=1291, 2026-09-19T14:45:35.984144Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1291, 2026-09-19T14:45:35.984144Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1291, 2026-09-19T14:45:35.984144Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1291, 2026-09-19T14:45:35.984144Z)
- `FUELINST|fuelType=OTHER|generation` = **1388** (n=1291, 2026-09-19T14:45:35.984144Z)
- `FUELINST|fuelType=PS|generation` = **-259** (n=1291, 2026-09-19T14:45:35.984144Z)
- `FUELINST|fuelType=WIND|generation` = **13425** (n=1291, 2026-09-19T14:45:35.984144Z)
- `IMBALNGC|TOTAL|imbalance` = **-3230** (n=212, 2026-09-19T14:25:35.374558Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=212, 2026-09-19T14:25:35.374558Z)
- `INDGEN|TOTAL|generation` = **16779** (n=212, 2026-09-19T14:25:35.374558Z)
- `MELNGC|TOTAL|margin` = **36925** (n=212, 2026-09-19T14:20:59.619875Z)
- `NDF|TOTAL|demand` = **19509** (n=217, 2026-09-19T14:18:32.720132Z)
- `TSDF|TOTAL|demand` = **20009** (n=217, 2026-09-19T14:18:32.720132Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:46:24.385564Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:23.111248Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:21.839819Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:20.534183Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:19.244983Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:17.962997Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:16.645341Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:15.400682Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:14.123936Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:12.884847Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:11.536272Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:08.263422Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:08.263422Z` — **FREQ**: 5761 rows; marker `2026-09-19T14:45:45Z`
- `2026-09-19T14:46:06.816489Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:46:05.080727Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
