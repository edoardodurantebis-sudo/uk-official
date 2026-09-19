# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T23:53:21.204032Z`  
Current process started UTC: `2026-09-19T23:49:19.441227Z`  
1-second metadata polls in this process: **132**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-684, delta=0, z=-10.42 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **992** (n=1400, 2026-09-19T23:50:39.558525Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=1400, 2026-09-19T23:50:39.558525Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1400, 2026-09-19T23:50:39.558525Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1400, 2026-09-19T23:50:39.558525Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1400, 2026-09-19T23:50:39.558525Z)
- `FUELINST|fuelType=OTHER|generation` = **561** (n=1400, 2026-09-19T23:50:39.558525Z)
- `FUELINST|fuelType=PS|generation` = **-251** (n=1400, 2026-09-19T23:50:39.558525Z)
- `FUELINST|fuelType=WIND|generation` = **16099** (n=1400, 2026-09-19T23:50:39.558525Z)
- `IMBALNGC|TOTAL|imbalance` = **-3708** (n=231, 2026-09-19T23:51:59.807396Z)
- `INDDEM|TOTAL|demand` = **-11889** (n=231, 2026-09-19T23:51:59.807396Z)
- `INDGEN|TOTAL|generation` = **16244** (n=231, 2026-09-19T23:51:59.807396Z)
- `MELNGC|TOTAL|margin` = **35994** (n=231, 2026-09-19T23:49:51.036521Z)
- `NDF|TOTAL|demand` = **19452** (n=236, 2026-09-19T23:47:47.316209Z)
- `TSDF|TOTAL|demand` = **19952** (n=236, 2026-09-19T23:47:47.316209Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-19T23:53:19.149303Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:53:17.470232Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:53:15.776521Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:53:14.082324Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:53:12.394936Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:53:10.691521Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:53:08.993518Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:53:07.309010Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:53:05.631461Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:53:03.354087Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:53:01.655556Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:52:59.961515Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:52:58.285613Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:52:56.598935Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:52:54.907032Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
