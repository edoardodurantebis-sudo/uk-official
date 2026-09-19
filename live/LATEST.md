# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T20:52:48.366471Z`  
Current process started UTC: `2026-09-19T20:48:47.776800Z`  
1-second metadata polls in this process: **220**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=94, delta=-6, z=4.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=-378, z=-0.09 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=92, delta=-14, z=4.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.97 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=5.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=1, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=-250, z=-0.07 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=100, delta=4, z=5.22 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=378, delta=4, z=13.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=105, delta=5, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=251, delta=-152, z=6.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=100, delta=1, z=4.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=11.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.84 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1364, 2026-09-19T20:50:39.280648Z)
- `FUELINST|fuelType=NPSHYD|generation` = **475** (n=1364, 2026-09-19T20:50:39.280648Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1364, 2026-09-19T20:50:39.280648Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1364, 2026-09-19T20:50:39.280648Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1364, 2026-09-19T20:50:39.280648Z)
- `FUELINST|fuelType=OTHER|generation` = **571** (n=1364, 2026-09-19T20:50:39.280648Z)
- `FUELINST|fuelType=PS|generation` = **823** (n=1364, 2026-09-19T20:50:39.280648Z)
- `FUELINST|fuelType=WIND|generation` = **14335** (n=1364, 2026-09-19T20:50:39.280648Z)
- `IMBALNGC|TOTAL|imbalance` = **-3851** (n=225, 2026-09-19T20:52:15.629197Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=225, 2026-09-19T20:51:59.237885Z)
- `INDGEN|TOTAL|generation` = **16101** (n=225, 2026-09-19T20:51:59.237885Z)
- `MELNGC|TOTAL|margin` = **36203** (n=225, 2026-09-19T20:49:35.992012Z)
- `NDF|TOTAL|demand` = **19452** (n=230, 2026-09-19T20:47:50.435946Z)
- `TSDF|TOTAL|demand` = **19952** (n=230, 2026-09-19T20:47:50.435946Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T20:52:47.361861Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:46.337673Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:45.325079Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:44.239346Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:43.195376Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:42.095480Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:41.067523Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:40.067454Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:39.039149Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:38.019891Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:37.010875Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:35.978933Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:34.941914Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:33.894221Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:52:32.450820Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
