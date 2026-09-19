# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T23:44:56.144306Z`  
Current process started UTC: `2026-09-19T23:40:56.062444Z`  
1-second metadata polls in this process: **229**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-684, delta=0, z=-10.86 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-684, delta=1, z=-11.36 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **992** (n=1398, 2026-09-19T23:40:30.087298Z)
- `FUELINST|fuelType=NPSHYD|generation` = **347** (n=1398, 2026-09-19T23:40:30.087298Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1398, 2026-09-19T23:40:30.087298Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1398, 2026-09-19T23:40:30.087298Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1398, 2026-09-19T23:40:30.087298Z)
- `FUELINST|fuelType=OTHER|generation` = **768** (n=1398, 2026-09-19T23:40:30.087298Z)
- `FUELINST|fuelType=PS|generation` = **-251** (n=1398, 2026-09-19T23:40:30.087298Z)
- `FUELINST|fuelType=WIND|generation` = **16000** (n=1398, 2026-09-19T23:40:30.087298Z)
- `IMBALNGC|TOTAL|imbalance` = **-3940** (n=230, 2026-09-19T23:21:44.790794Z)
- `INDDEM|TOTAL|demand` = **-11888** (n=230, 2026-09-19T23:21:11.961383Z)
- `INDGEN|TOTAL|generation` = **16012** (n=230, 2026-09-19T23:21:11.961383Z)
- `MELNGC|TOTAL|margin` = **36070** (n=230, 2026-09-19T23:19:52.106383Z)
- `NDF|TOTAL|demand` = **19452** (n=235, 2026-09-19T23:17:17.399852Z)
- `TSDF|TOTAL|demand` = **19952** (n=235, 2026-09-19T23:17:33.708117Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-19T23:44:55.175353Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:54.175238Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:53.175150Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:52.175057Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:51.174929Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:50.174769Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:49.174631Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:47.734090Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:46.733951Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:45.733831Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:44.733706Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:43.733593Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:42.733461Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:41.732032Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:44:40.731958Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
