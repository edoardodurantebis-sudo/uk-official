# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T22:54:32.248320Z`  
Current process started UTC: `2026-09-19T22:50:30.983785Z`  
1-second metadata polls in this process: **130**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-338, delta=-235, z=-8.76 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=94, delta=-6, z=4.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=-378, z=-0.09 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=92, delta=-14, z=4.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.92 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1226** (n=1388, 2026-09-19T22:50:30.983792Z)
- `FUELINST|fuelType=NPSHYD|generation` = **360** (n=1388, 2026-09-19T22:50:30.983792Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1388, 2026-09-19T22:50:30.983792Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1388, 2026-09-19T22:50:30.983792Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1388, 2026-09-19T22:50:30.983792Z)
- `FUELINST|fuelType=OTHER|generation` = **722** (n=1388, 2026-09-19T22:50:30.983792Z)
- `FUELINST|fuelType=PS|generation` = **-134** (n=1388, 2026-09-19T22:50:30.983792Z)
- `FUELINST|fuelType=WIND|generation` = **15287** (n=1388, 2026-09-19T22:50:30.983792Z)
- `IMBALNGC|TOTAL|imbalance` = **-3939** (n=229, 2026-09-19T22:51:53.188955Z)
- `INDDEM|TOTAL|demand` = **-11888** (n=229, 2026-09-19T22:51:36.708891Z)
- `INDGEN|TOTAL|generation` = **16013** (n=229, 2026-09-19T22:51:36.708891Z)
- `MELNGC|TOTAL|margin` = **36059** (n=229, 2026-09-19T22:49:52.818755Z)
- `NDF|TOTAL|demand` = **19452** (n=234, 2026-09-19T22:47:40.553583Z)
- `TSDF|TOTAL|demand` = **19952** (n=234, 2026-09-19T22:47:40.553583Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T22:54:30.535385Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:28.839432Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:27.143962Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:25.451994Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:23.747438Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:22.048399Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:20.350162Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:17.110910Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:15.426662Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:13.720785Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:11.812192Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:10.120123Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:08.415597Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:06.679796Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T22:54:04.998376Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
