# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T23:23:52.637803Z`  
Current process started UTC: `2026-09-19T23:19:52.106377Z`  
1-second metadata polls in this process: **145**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-892, delta=1, z=-10.63 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **992** (n=1394, 2026-09-19T23:20:23.651882Z)
- `FUELINST|fuelType=NPSHYD|generation` = **345** (n=1394, 2026-09-19T23:20:23.651882Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1394, 2026-09-19T23:20:23.651882Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1394, 2026-09-19T23:20:23.651882Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1394, 2026-09-19T23:20:23.651882Z)
- `FUELINST|fuelType=OTHER|generation` = **576** (n=1394, 2026-09-19T23:20:23.651882Z)
- `FUELINST|fuelType=PS|generation` = **-257** (n=1394, 2026-09-19T23:20:23.651882Z)
- `FUELINST|fuelType=WIND|generation` = **16063** (n=1394, 2026-09-19T23:20:23.651882Z)
- `IMBALNGC|TOTAL|imbalance` = **-3940** (n=230, 2026-09-19T23:21:44.790794Z)
- `INDDEM|TOTAL|demand` = **-11888** (n=230, 2026-09-19T23:21:11.961383Z)
- `INDGEN|TOTAL|generation` = **16012** (n=230, 2026-09-19T23:21:11.961383Z)
- `MELNGC|TOTAL|margin` = **36070** (n=230, 2026-09-19T23:19:52.106383Z)
- `NDF|TOTAL|demand` = **19452** (n=235, 2026-09-19T23:17:17.399852Z)
- `TSDF|TOTAL|demand` = **19952** (n=235, 2026-09-19T23:17:33.708117Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T23:23:51.101844Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:49.512773Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:47.980759Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:46.455073Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:44.757177Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:43.202903Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:41.667029Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:40.114294Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:38.183160Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:36.643895Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:35.074266Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:33.550081Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:32.018805Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:30.476255Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:23:28.903726Z` — **MID**: 0 rows; marker `2026-09-19T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
