# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T16:29:54.325449Z`  
Current process started UTC: `2026-09-16T16:25:54.123773Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3284, delta=-3, z=-4.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3287, delta=-2, z=-3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3289, delta=-4, z=-4.11 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3289, delta=-1, z=-3.74 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **164** (n=522, 2026-09-16T16:25:54.123781Z)
- `FUELINST|fuelType=NPSHYD|generation` = **515** (n=522, 2026-09-16T16:25:54.123781Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3308** (n=522, 2026-09-16T16:25:54.123781Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=522, 2026-09-16T16:25:54.123781Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=522, 2026-09-16T16:25:54.123781Z)
- `FUELINST|fuelType=OTHER|generation` = **1070** (n=522, 2026-09-16T16:25:54.123781Z)
- `FUELINST|fuelType=PS|generation` = **1099** (n=522, 2026-09-16T16:25:54.123781Z)
- `FUELINST|fuelType=WIND|generation` = **5671** (n=522, 2026-09-16T16:25:54.123781Z)
- `IMBALNGC|TOTAL|imbalance` = **6448** (n=86, 2026-09-16T16:23:03.353210Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=86, 2026-09-16T16:23:03.353210Z)
- `INDGEN|TOTAL|generation` = **25569** (n=86, 2026-09-16T16:23:03.353210Z)
- `MELNGC|TOTAL|margin` = **34170** (n=86, 2026-09-16T16:20:21.505497Z)
- `NDF|TOTAL|demand` = **18621** (n=88, 2026-09-16T16:18:04.975429Z)
- `TSDF|TOTAL|demand` = **19121** (n=88, 2026-09-16T16:18:04.975429Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T16:28:18.283644Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:27:45Z`
- `2026-09-16T16:26:10.044952Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:25:45Z`
- `2026-09-16T16:25:54.123781Z` — **FUELINST**: 80 rows; marker `2026-09-16T16:25:00Z`
- `2026-09-16T16:25:54.123781Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:23:45Z`
- `2026-09-16T16:23:03.353210Z` — **INDGEN**: 1278 rows; marker `2026-09-16T16:17:00Z`
- `2026-09-16T16:23:03.353210Z` — **INDDEM**: 1278 rows; marker `2026-09-16T16:17:00Z`
- `2026-09-16T16:23:03.353210Z` — **IMBALNGC**: 1278 rows; marker `2026-09-16T16:17:00Z`
- `2026-09-16T16:22:30.786977Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:21:45Z`
- `2026-09-16T16:20:21.505497Z` — **MELNGC**: 1278 rows; marker `2026-09-16T16:17:00Z`
- `2026-09-16T16:20:21.505497Z` — **FUELINST**: 80 rows; marker `2026-09-16T16:20:00Z`
- `2026-09-16T16:20:05.983333Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:19:45Z`
- `2026-09-16T16:18:04.975429Z` — **TSDF**: 1278 rows; marker `2026-09-16T16:17:00Z`
- `2026-09-16T16:18:04.975429Z` — **NDF**: 71 rows; marker `2026-09-16T16:17:00Z`
- `2026-09-16T16:18:04.975429Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:17:45Z`
- `2026-09-16T16:16:12.236062Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:15:45Z`
