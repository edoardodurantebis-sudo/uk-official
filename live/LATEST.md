# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T23:11:19.699161Z`  
Current process started UTC: `2026-09-19T23:07:19.648726Z`  
1-second metadata polls in this process: **228**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-675, delta=-337, z=-16.96 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **992** (n=1392, 2026-09-19T23:10:36.869195Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=1392, 2026-09-19T23:10:36.869195Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1392, 2026-09-19T23:10:36.869195Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1392, 2026-09-19T23:10:36.869195Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1392, 2026-09-19T23:10:36.869195Z)
- `FUELINST|fuelType=OTHER|generation` = **742** (n=1392, 2026-09-19T23:10:36.869195Z)
- `FUELINST|fuelType=PS|generation` = **-187** (n=1392, 2026-09-19T23:10:36.869195Z)
- `FUELINST|fuelType=WIND|generation` = **15816** (n=1392, 2026-09-19T23:10:36.869195Z)
- `IMBALNGC|TOTAL|imbalance` = **-3939** (n=229, 2026-09-19T22:51:53.188955Z)
- `INDDEM|TOTAL|demand` = **-11888** (n=229, 2026-09-19T22:51:36.708891Z)
- `INDGEN|TOTAL|generation` = **16013** (n=229, 2026-09-19T22:51:36.708891Z)
- `MELNGC|TOTAL|margin` = **36059** (n=229, 2026-09-19T22:49:52.818755Z)
- `NDF|TOTAL|demand` = **19452** (n=234, 2026-09-19T22:47:40.553583Z)
- `TSDF|TOTAL|demand` = **19952** (n=234, 2026-09-19T22:47:40.553583Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T23:11:18.686241Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:17.686124Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:16.686039Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:15.685962Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:14.685853Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:13.685771Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:12.685700Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:11.685633Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:10.685503Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:09.259772Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:08.259668Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:07.259556Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:06.259440Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:05.259419Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:11:04.259338Z` — **MID**: 0 rows; marker `2026-09-19T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
