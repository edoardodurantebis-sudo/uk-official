# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T02:26:53.114438Z`  
Current process started UTC: `2026-09-17T02:22:52.511965Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=0, z=-3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=0, z=-3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=-24, z=-3.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-783, delta=-46, z=-3.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-737, delta=-46, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-638, delta=-42, z=-3.94 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-691, delta=-46, z=-3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-645, delta=-22, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.90 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-596, delta=-258, z=-4.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-3.96 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-623, delta=0, z=-4.01 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=611, 2026-09-17T02:25:32.711782Z)
- `FUELINST|fuelType=NPSHYD|generation` = **423** (n=611, 2026-09-17T02:25:32.711782Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=611, 2026-09-17T02:25:32.711782Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=611, 2026-09-17T02:25:32.711782Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=611, 2026-09-17T02:25:32.711782Z)
- `FUELINST|fuelType=OTHER|generation` = **256** (n=611, 2026-09-17T02:25:32.711782Z)
- `FUELINST|fuelType=PS|generation` = **-538** (n=611, 2026-09-17T02:25:32.711782Z)
- `FUELINST|fuelType=WIND|generation` = **13437** (n=611, 2026-09-17T02:25:32.711782Z)
- `IMBALNGC|TOTAL|imbalance` = **6512** (n=102, 2026-09-17T02:20:53.960752Z)
- `INDDEM|TOTAL|demand` = **-11527** (n=102, 2026-09-17T02:20:38.099754Z)
- `INDGEN|TOTAL|generation` = **25633** (n=102, 2026-09-17T02:20:38.099754Z)
- `MELNGC|TOTAL|margin` = **35851** (n=102, 2026-09-17T02:19:02.355909Z)
- `NDF|TOTAL|demand` = **18621** (n=104, 2026-09-17T02:17:42.741584Z)
- `TSDF|TOTAL|demand` = **19121** (n=104, 2026-09-17T02:17:42.741584Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T02:26:04.179191Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:25:45Z`
- `2026-09-17T02:25:32.711782Z` — **FUELINST**: 80 rows; marker `2026-09-17T02:25:00Z`
- `2026-09-17T02:24:12.521657Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:23:45Z`
- `2026-09-17T02:22:30.239229Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:21:45Z`
- `2026-09-17T02:20:53.960752Z` — **IMBALNGC**: 918 rows; marker `2026-09-17T02:17:00Z`
- `2026-09-17T02:20:38.099754Z` — **INDGEN**: 918 rows; marker `2026-09-17T02:17:00Z`
- `2026-09-17T02:20:38.099754Z` — **INDDEM**: 918 rows; marker `2026-09-17T02:17:00Z`
- `2026-09-17T02:20:38.099754Z` — **FUELINST**: 80 rows; marker `2026-09-17T02:20:00Z`
- `2026-09-17T02:20:21.938080Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:19:45Z`
- `2026-09-17T02:19:02.355909Z` — **MELNGC**: 918 rows; marker `2026-09-17T02:17:00Z`
- `2026-09-17T02:18:14.305113Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:17:45Z`
- `2026-09-17T02:17:42.741584Z` — **TSDF**: 918 rows; marker `2026-09-17T02:17:00Z`
- `2026-09-17T02:17:42.741584Z` — **NDF**: 51 rows; marker `2026-09-17T02:17:00Z`
- `2026-09-17T02:16:22.799667Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:15:45Z`
- `2026-09-17T02:15:34.790664Z` — **FUELINST**: 80 rows; marker `2026-09-17T02:15:00Z`
