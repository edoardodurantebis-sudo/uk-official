# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T01:49:11.433274Z`  
Current process started UTC: `2026-09-17T01:45:11.318126Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.90 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-596, delta=-258, z=-4.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.96 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-4.01 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-4.07 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=-41, z=-4.13 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-582, delta=-78, z=-4.09 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-504, delta=-78, z=-3.96 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-338, delta=-52, z=-3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-426, delta=-78, z=-3.82 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-348, delta=-36, z=-3.68 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.68 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=603, 2026-09-17T01:45:31.320556Z)
- `FUELINST|fuelType=NPSHYD|generation` = **419** (n=603, 2026-09-17T01:45:31.320556Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=603, 2026-09-17T01:45:31.320556Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=603, 2026-09-17T01:45:31.320556Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=603, 2026-09-17T01:45:31.320556Z)
- `FUELINST|fuelType=OTHER|generation` = **266** (n=603, 2026-09-17T01:45:31.320556Z)
- `FUELINST|fuelType=PS|generation` = **-308** (n=603, 2026-09-17T01:45:31.320556Z)
- `FUELINST|fuelType=WIND|generation` = **13063** (n=603, 2026-09-17T01:45:31.320556Z)
- `IMBALNGC|TOTAL|imbalance` = **6505** (n=100, 2026-09-17T01:20:34.290480Z)
- `INDDEM|TOTAL|demand` = **-11647** (n=100, 2026-09-17T01:20:34.290480Z)
- `INDGEN|TOTAL|generation` = **25626** (n=100, 2026-09-17T01:20:34.290480Z)
- `MELNGC|TOTAL|margin` = **34561** (n=101, 2026-09-17T01:48:44.614528Z)
- `NDF|TOTAL|demand` = **18621** (n=103, 2026-09-17T01:47:23.030089Z)
- `TSDF|TOTAL|demand` = **19121** (n=103, 2026-09-17T01:47:07.443374Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T01:48:44.614528Z` — **MELNGC**: 936 rows; marker `2026-09-17T01:46:00Z`
- `2026-09-17T01:48:44.614528Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:47:45Z`
- `2026-09-17T01:47:23.030089Z` — **NDF**: 52 rows; marker `2026-09-17T01:46:00Z`
- `2026-09-17T01:47:07.443374Z` — **TSDF**: 936 rows; marker `2026-09-17T01:46:00Z`
- `2026-09-17T01:46:19.482117Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:45:45Z`
- `2026-09-17T01:45:31.320556Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:45:00Z`
- `2026-09-17T01:44:28.045676Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:43:45Z`
- `2026-09-17T01:42:20.440379Z` — **MID**: 0 rows; marker `2026-09-17T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T01:42:20.440379Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:41:45Z`
- `2026-09-17T01:40:33.376966Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:40:00Z`
- `2026-09-17T01:40:17.896800Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:39:45Z`
- `2026-09-17T01:38:25.239091Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:37:45Z`
- `2026-09-17T01:36:48.846881Z` — **MID**: 0 rows; marker `2026-09-17T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T01:36:22.973845Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:35:45Z`
- `2026-09-17T01:35:50.270836Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:35:00Z`
