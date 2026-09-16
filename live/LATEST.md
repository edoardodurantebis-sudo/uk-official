# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T17:11:51.809529Z`  
Current process started UTC: `2026-09-16T17:07:51.441733Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=689, delta=14, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=35, delta=25, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=675, delta=124, z=4.19 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=10, delta=20, z=4.51 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=-32, delta=138, z=4.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-10, delta=-9, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-1, delta=7, z=4.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-8, delta=24, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-32, delta=24, z=4.45 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-56, delta=26, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-82, delta=26, z=4.07 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-108, delta=25, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-133, delta=24, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=0, z=-3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=-3, z=-3.63 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **381** (n=531, 2026-09-16T17:11:22.726170Z)
- `FUELINST|fuelType=NPSHYD|generation` = **689** (n=531, 2026-09-16T17:11:22.726170Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3313** (n=531, 2026-09-16T17:11:22.726170Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=531, 2026-09-16T17:11:22.726170Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=531, 2026-09-16T17:11:22.726170Z)
- `FUELINST|fuelType=OTHER|generation` = **2670** (n=531, 2026-09-16T17:11:22.726170Z)
- `FUELINST|fuelType=PS|generation` = **1210** (n=531, 2026-09-16T17:11:22.726170Z)
- `FUELINST|fuelType=WIND|generation` = **6837** (n=531, 2026-09-16T17:11:22.726170Z)
- `IMBALNGC|TOTAL|imbalance` = **6467** (n=87, 2026-09-16T16:52:45.452564Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=87, 2026-09-16T16:52:29.961835Z)
- `INDGEN|TOTAL|generation` = **25588** (n=87, 2026-09-16T16:52:29.961835Z)
- `MELNGC|TOTAL|margin` = **34116** (n=87, 2026-09-16T16:49:49.939625Z)
- `NDF|TOTAL|demand` = **18621** (n=89, 2026-09-16T16:47:42.628101Z)
- `TSDF|TOTAL|demand` = **19121** (n=89, 2026-09-16T16:47:59.156053Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T17:11:22.726170Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:10:00Z`
- `2026-09-16T17:11:22.726170Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:09:45Z`
- `2026-09-16T17:08:10.444093Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:07:45Z`
- `2026-09-16T17:06:18.290347Z` — **MID**: 0 rows; marker `2026-09-16T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T17:06:18.290347Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:05:45Z`
- `2026-09-16T17:05:30.894450Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:05:00Z`
- `2026-09-16T17:04:10.645600Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:03:45Z`
- `2026-09-16T17:02:10.856927Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:01:45Z`
- `2026-09-16T17:00:33.339221Z` — **FUELHH**: 20 rows; marker `2026-09-16T17:00:00Z`
- `2026-09-16T17:00:33.339221Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:00:00Z`
- `2026-09-16T17:00:33.339221Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:59:45Z`
- `2026-09-16T16:58:28.608890Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:57:45Z`
- `2026-09-16T16:56:20.382105Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:55:45Z`
- `2026-09-16T16:55:48.106451Z` — **FUELINST**: 80 rows; marker `2026-09-16T16:55:00Z`
- `2026-09-16T16:54:22.577327Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:53:45Z`
