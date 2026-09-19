# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T23:57:34.025071Z`  
Current process started UTC: `2026-09-19T23:53:33.782690Z`  
1-second metadata polls in this process: **226**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-892, delta=1, z=-8.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-8.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-8.96 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=1, z=-9.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-894, delta=-1, z=-9.54 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-890, delta=-204, z=-12.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-9.86 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=-1, z=-10.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-892, delta=1, z=-10.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=-2, z=-11.11 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-891, delta=-12, z=-11.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-879, delta=-185, z=-12.04 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-686, delta=-60, z=-12.25 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-694, delta=-9, z=-9.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=-1, z=-10.05 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **992** (n=1401, 2026-09-19T23:55:29.416806Z)
- `FUELINST|fuelType=NPSHYD|generation` = **345** (n=1401, 2026-09-19T23:55:29.416806Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1401, 2026-09-19T23:55:29.416806Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1401, 2026-09-19T23:55:29.416806Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1401, 2026-09-19T23:55:29.416806Z)
- `FUELINST|fuelType=OTHER|generation` = **426** (n=1401, 2026-09-19T23:55:29.416806Z)
- `FUELINST|fuelType=PS|generation` = **-253** (n=1401, 2026-09-19T23:55:29.416806Z)
- `FUELINST|fuelType=WIND|generation` = **16176** (n=1401, 2026-09-19T23:55:29.416806Z)
- `IMBALNGC|TOTAL|imbalance` = **-3708** (n=231, 2026-09-19T23:51:59.807396Z)
- `INDDEM|TOTAL|demand` = **-11889** (n=231, 2026-09-19T23:51:59.807396Z)
- `INDGEN|TOTAL|generation` = **16244** (n=231, 2026-09-19T23:51:59.807396Z)
- `MELNGC|TOTAL|margin` = **35994** (n=231, 2026-09-19T23:49:51.036521Z)
- `NDF|TOTAL|demand` = **19452** (n=236, 2026-09-19T23:47:47.316209Z)
- `TSDF|TOTAL|demand` = **19952** (n=236, 2026-09-19T23:47:47.316209Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-19T23:57:33.065243Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:32.065090Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:31.065011Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:30.064894Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:29.064777Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:27.614195Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:26.614052Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:25.613936Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:24.613817Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:23.613691Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:22.613573Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:21.613452Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:20.613335Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:19.613197Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:57:18.613119Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
