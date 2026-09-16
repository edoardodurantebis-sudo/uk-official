# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T16:46:42.654650Z`  
Current process started UTC: `2026-09-16T16:42:42.851259Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-32, delta=24, z=4.45 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-56, delta=26, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-82, delta=26, z=4.07 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-108, delta=25, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-133, delta=24, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=0, z=-3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=-3, z=-3.63 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3286, delta=2, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3285, delta=6, z=-3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3279, delta=-1, z=-4.31 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3284, delta=-5, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3280, delta=-3, z=-4.29 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3283, delta=-4, z=-4.06 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3287, delta=3, z=-3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3284, delta=0, z=-4.09 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **164** (n=526, 2026-09-16T16:45:40.747152Z)
- `FUELINST|fuelType=NPSHYD|generation` = **516** (n=526, 2026-09-16T16:45:40.747152Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3307** (n=526, 2026-09-16T16:45:40.747152Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=526, 2026-09-16T16:45:40.747152Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=526, 2026-09-16T16:45:40.747152Z)
- `FUELINST|fuelType=OTHER|generation` = **1055** (n=526, 2026-09-16T16:45:40.747152Z)
- `FUELINST|fuelType=PS|generation` = **1207** (n=526, 2026-09-16T16:45:40.747152Z)
- `FUELINST|fuelType=WIND|generation` = **6149** (n=526, 2026-09-16T16:45:40.747152Z)
- `IMBALNGC|TOTAL|imbalance` = **6448** (n=86, 2026-09-16T16:23:03.353210Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=86, 2026-09-16T16:23:03.353210Z)
- `INDGEN|TOTAL|generation` = **25569** (n=86, 2026-09-16T16:23:03.353210Z)
- `MELNGC|TOTAL|margin` = **34170** (n=86, 2026-09-16T16:20:21.505497Z)
- `NDF|TOTAL|demand` = **18621** (n=88, 2026-09-16T16:18:04.975429Z)
- `TSDF|TOTAL|demand` = **19121** (n=88, 2026-09-16T16:18:04.975429Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T16:46:12.753290Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:45:45Z`
- `2026-09-16T16:45:40.747152Z` — **FUELINST**: 80 rows; marker `2026-09-16T16:45:00Z`
- `2026-09-16T16:44:19.983191Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:43:45Z`
- `2026-09-16T16:42:17.318784Z` — **MID**: 0 rows; marker `2026-09-16T16:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T16:42:17.318784Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:41:45Z`
- `2026-09-16T16:40:25.335274Z` — **FUELINST**: 80 rows; marker `2026-09-16T16:40:00Z`
- `2026-09-16T16:40:25.335274Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:39:45Z`
- `2026-09-16T16:38:17.430265Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:37:45Z`
- `2026-09-16T16:37:29.821721Z` — **MID**: 0 rows; marker `2026-09-16T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T16:36:08.804925Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:35:45Z`
- `2026-09-16T16:35:37.515282Z` — **FUELINST**: 80 rows; marker `2026-09-16T16:35:00Z`
- `2026-09-16T16:34:17.561485Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:33:45Z`
- `2026-09-16T16:32:17.090984Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:31:45Z`
- `2026-09-16T16:30:25.726572Z` — **WINDFOR**: 73 rows; marker `2026-09-16T16:30:00Z`
- `2026-09-16T16:30:25.726572Z` — **FUELHH**: 20 rows; marker `2026-09-16T16:30:00Z`
