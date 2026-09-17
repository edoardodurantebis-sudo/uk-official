# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T01:28:14.585335Z`  
Current process started UTC: `2026-09-17T01:24:14.646767Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.72 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.77 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-286, delta=-258, z=-4.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.82 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.87 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=599, 2026-09-17T01:25:22.198640Z)
- `FUELINST|fuelType=NPSHYD|generation` = **417** (n=599, 2026-09-17T01:25:22.198640Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=599, 2026-09-17T01:25:22.198640Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=599, 2026-09-17T01:25:22.198640Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=599, 2026-09-17T01:25:22.198640Z)
- `FUELINST|fuelType=OTHER|generation` = **116** (n=599, 2026-09-17T01:25:22.198640Z)
- `FUELINST|fuelType=PS|generation` = **-317** (n=599, 2026-09-17T01:25:22.198640Z)
- `FUELINST|fuelType=WIND|generation` = **12893** (n=599, 2026-09-17T01:25:22.198640Z)
- `IMBALNGC|TOTAL|imbalance` = **6505** (n=100, 2026-09-17T01:20:34.290480Z)
- `INDDEM|TOTAL|demand` = **-11647** (n=100, 2026-09-17T01:20:34.290480Z)
- `INDGEN|TOTAL|generation` = **25626** (n=100, 2026-09-17T01:20:34.290480Z)
- `MELNGC|TOTAL|margin` = **34492** (n=100, 2026-09-17T01:19:06.062637Z)
- `NDF|TOTAL|demand` = **18621** (n=102, 2026-09-17T01:17:30.326551Z)
- `TSDF|TOTAL|demand` = **19121** (n=102, 2026-09-17T01:17:30.326551Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T01:26:09.798884Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:25:45Z`
- `2026-09-17T01:25:22.198640Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:25:00Z`
- `2026-09-17T01:24:17.647115Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:23:45Z`
- `2026-09-17T01:22:09.807018Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:21:45Z`
- `2026-09-17T01:20:34.290480Z` — **INDGEN**: 954 rows; marker `2026-09-17T01:16:00Z`
- `2026-09-17T01:20:34.290480Z` — **INDDEM**: 954 rows; marker `2026-09-17T01:16:00Z`
- `2026-09-17T01:20:34.290480Z` — **IMBALNGC**: 954 rows; marker `2026-09-17T01:16:00Z`
- `2026-09-17T01:20:34.290480Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:20:00Z`
- `2026-09-17T01:20:02.359545Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:19:45Z`
- `2026-09-17T01:19:06.062637Z` — **MELNGC**: 954 rows; marker `2026-09-17T01:16:00Z`
- `2026-09-17T01:18:18.328038Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:17:45Z`
- `2026-09-17T01:17:30.326551Z` — **TSDF**: 954 rows; marker `2026-09-17T01:16:00Z`
- `2026-09-17T01:17:30.326551Z` — **NDF**: 53 rows; marker `2026-09-17T01:16:00Z`
- `2026-09-17T01:16:26.550235Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:15:45Z`
- `2026-09-17T01:15:52.611122Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:15:00Z`
