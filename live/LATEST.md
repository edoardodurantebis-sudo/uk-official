# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T09:35:04.777329Z`  
Current process started UTC: `2026-09-19T09:31:04.381348Z`  
1-second metadata polls in this process: **223**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-10744, delta=3052, z=1.92 -> demand pressure up
- **WINDFOR** `TOTAL` `generation` — wind forecast [TOTAL] generation: value=7845, delta=-11023, z=-4.38 -> renewable cushion down / residual-load pressure up
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=80, delta=-38, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=118, delta=27, z=6.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **560** (n=1228, 2026-09-19T09:30:22.262117Z)
- `FUELINST|fuelType=NPSHYD|generation` = **331** (n=1228, 2026-09-19T09:30:22.262117Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1228, 2026-09-19T09:30:22.262117Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1228, 2026-09-19T09:30:22.262117Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1228, 2026-09-19T09:30:22.262117Z)
- `FUELINST|fuelType=OTHER|generation` = **423** (n=1228, 2026-09-19T09:30:22.262117Z)
- `FUELINST|fuelType=PS|generation` = **-423** (n=1228, 2026-09-19T09:30:22.262117Z)
- `FUELINST|fuelType=WIND|generation` = **15208** (n=1228, 2026-09-19T09:30:22.262117Z)
- `IMBALNGC|TOTAL|imbalance` = **7771** (n=202, 2026-09-19T09:19:44.569379Z)
- `INDDEM|TOTAL|demand` = **-13216** (n=202, 2026-09-19T09:19:44.569379Z)
- `INDGEN|TOTAL|generation` = **26702** (n=202, 2026-09-19T09:19:44.569379Z)
- `MELNGC|TOTAL|margin` = **36478** (n=202, 2026-09-19T09:18:55.905783Z)
- `NDF|TOTAL|demand` = **15940** (n=207, 2026-09-19T09:17:21.692487Z)
- `TSDF|TOTAL|demand` = **18932** (n=207, 2026-09-19T09:17:21.692487Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T09:35:03.739782Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:35:02.739700Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:35:01.731055Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:35:00.730980Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:34:59.730900Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:34:58.730835Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:34:57.730726Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:34:56.730606Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:34:55.730479Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:34:54.730391Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:34:53.645213Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:34:52.645096Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:34:51.287808Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:34:50.287728Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:34:49.287650Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
