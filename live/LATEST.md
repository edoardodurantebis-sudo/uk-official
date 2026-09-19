# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T23:19:40.872277Z`  
Current process started UTC: `2026-09-19T23:15:40.573233Z`  
1-second metadata polls in this process: **169**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=-2, z=-11.11 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-891, delta=-12, z=-11.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-879, delta=-185, z=-12.04 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-686, delta=-60, z=-12.25 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-694, delta=-9, z=-9.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=-1, z=-10.05 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-684, delta=0, z=-10.42 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-684, delta=0, z=-10.86 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-684, delta=1, z=-11.36 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-11.96 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-626, delta=-522, z=-16.49 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-12.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-13.44 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-14.42 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=-10, z=-15.65 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **992** (n=1393, 2026-09-19T23:15:40.573241Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=1393, 2026-09-19T23:15:40.573241Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1393, 2026-09-19T23:15:40.573241Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1393, 2026-09-19T23:15:40.573241Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1393, 2026-09-19T23:15:40.573241Z)
- `FUELINST|fuelType=OTHER|generation` = **624** (n=1393, 2026-09-19T23:15:40.573241Z)
- `FUELINST|fuelType=PS|generation` = **-259** (n=1393, 2026-09-19T23:15:40.573241Z)
- `FUELINST|fuelType=WIND|generation` = **15954** (n=1393, 2026-09-19T23:15:40.573241Z)
- `IMBALNGC|TOTAL|imbalance` = **-3939** (n=229, 2026-09-19T22:51:53.188955Z)
- `INDDEM|TOTAL|demand` = **-11888** (n=229, 2026-09-19T22:51:36.708891Z)
- `INDGEN|TOTAL|generation` = **16013** (n=229, 2026-09-19T22:51:36.708891Z)
- `MELNGC|TOTAL|margin` = **36059** (n=229, 2026-09-19T22:49:52.818755Z)
- `NDF|TOTAL|demand` = **19452** (n=235, 2026-09-19T23:17:17.399852Z)
- `TSDF|TOTAL|demand` = **19952** (n=235, 2026-09-19T23:17:33.708117Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T23:19:39.558254Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:38.272572Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:37.018004Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:35.732407Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:34.415503Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:33.116609Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:31.811416Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:30.241881Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:28.317422Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:27.011838Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:25.720965Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:24.456021Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:23.155358Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:21.846544Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:19:20.569793Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
