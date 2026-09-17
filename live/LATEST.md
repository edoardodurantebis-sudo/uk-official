# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T01:57:36.525114Z`  
Current process started UTC: `2026-09-17T01:53:35.986577Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-645, delta=-22, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.75 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=605, 2026-09-17T01:55:29.041257Z)
- `FUELINST|fuelType=NPSHYD|generation` = **419** (n=605, 2026-09-17T01:55:29.041257Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=605, 2026-09-17T01:55:29.041257Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=605, 2026-09-17T01:55:29.041257Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=605, 2026-09-17T01:55:29.041257Z)
- `FUELINST|fuelType=OTHER|generation` = **357** (n=605, 2026-09-17T01:55:29.041257Z)
- `FUELINST|fuelType=PS|generation` = **-597** (n=605, 2026-09-17T01:55:29.041257Z)
- `FUELINST|fuelType=WIND|generation` = **13131** (n=605, 2026-09-17T01:55:29.041257Z)
- `IMBALNGC|TOTAL|imbalance` = **6516** (n=101, 2026-09-17T01:50:12.108296Z)
- `INDDEM|TOTAL|demand` = **-11527** (n=101, 2026-09-17T01:50:12.108296Z)
- `INDGEN|TOTAL|generation` = **25637** (n=101, 2026-09-17T01:50:12.108296Z)
- `MELNGC|TOTAL|margin` = **34561** (n=101, 2026-09-17T01:48:44.614528Z)
- `NDF|TOTAL|demand` = **18621** (n=103, 2026-09-17T01:47:23.030089Z)
- `TSDF|TOTAL|demand` = **19121** (n=103, 2026-09-17T01:47:07.443374Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T01:56:16.562302Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:55:45Z`
- `2026-09-17T01:55:29.041257Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:55:00Z`
- `2026-09-17T01:54:07.991217Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:53:45Z`
- `2026-09-17T01:52:03.329844Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:51:45Z`
- `2026-09-17T01:50:43.680370Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:50:00Z`
- `2026-09-17T01:50:28.273256Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:49:45Z`
- `2026-09-17T01:50:12.108296Z` — **INDGEN**: 936 rows; marker `2026-09-17T01:46:00Z`
- `2026-09-17T01:50:12.108296Z` — **INDDEM**: 936 rows; marker `2026-09-17T01:46:00Z`
- `2026-09-17T01:50:12.108296Z` — **IMBALNGC**: 936 rows; marker `2026-09-17T01:46:00Z`
- `2026-09-17T01:48:44.614528Z` — **MELNGC**: 936 rows; marker `2026-09-17T01:46:00Z`
- `2026-09-17T01:48:44.614528Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:47:45Z`
- `2026-09-17T01:47:23.030089Z` — **NDF**: 52 rows; marker `2026-09-17T01:46:00Z`
- `2026-09-17T01:47:07.443374Z` — **TSDF**: 936 rows; marker `2026-09-17T01:46:00Z`
- `2026-09-17T01:46:19.482117Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:45:45Z`
- `2026-09-17T01:45:31.320556Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:45:00Z`
