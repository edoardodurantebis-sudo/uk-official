# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T07:34:09.644650Z`  
Current process started UTC: `2026-09-15T07:30:09.964664Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTVKL` `generation` — half-hour generation mix [fuelType=INTVKL] generation: value=1336, delta=1030, z=3.74 -> generation-mix component moved
- **FUELHH** `fuelType=INTNEM` `generation` — half-hour generation mix [fuelType=INTNEM] generation: value=754, delta=1138, z=8.18 -> generation-mix component moved
- **FUELHH** `fuelType=INTEW` `generation` — half-hour generation mix [fuelType=INTEW] generation: value=-424, delta=-132, z=-4.12 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=0, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=0, z=4.79 -> generation-mix component moved
- **FUELINST** `fuelType=INTEW` `generation` — instantaneous generation mix [fuelType=INTEW] generation: value=-453, delta=1, z=-3.59 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=0, z=5.33 -> generation-mix component moved
- **FUELINST** `fuelType=INTEW` `generation` — instantaneous generation mix [fuelType=INTEW] generation: value=-454, delta=-24, z=-3.82 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=20, z=6.11 -> generation-mix component moved
- **FUELINST** `fuelType=INTEW` `generation` — instantaneous generation mix [fuelType=INTEW] generation: value=-430, delta=-26, z=-3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTVKL` `generation` — instantaneous generation mix [fuelType=INTVKL] generation: value=1366, delta=336, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=802, delta=366, z=7.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTEW` `generation` — instantaneous generation mix [fuelType=INTEW] generation: value=-404, delta=-25, z=-3.77 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=436, delta=500, z=5.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTEW` `generation` — instantaneous generation mix [fuelType=INTEW] generation: value=-379, delta=-26, z=-3.71 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1404** (n=127, 2026-09-15T07:30:28.783389Z)
- `FUELINST|fuelType=NPSHYD|generation` = **455** (n=127, 2026-09-15T07:30:28.783389Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=127, 2026-09-15T07:30:28.783389Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=127, 2026-09-15T07:30:28.783389Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=127, 2026-09-15T07:30:28.783389Z)
- `FUELINST|fuelType=OTHER|generation` = **1683** (n=127, 2026-09-15T07:30:28.783389Z)
- `FUELINST|fuelType=PS|generation` = **-258** (n=127, 2026-09-15T07:30:28.783389Z)
- `FUELINST|fuelType=WIND|generation` = **12461** (n=127, 2026-09-15T07:30:28.783389Z)
- `IMBALNGC|TOTAL|imbalance` = **-454** (n=22, 2026-09-15T07:20:16.723769Z)
- `INDDEM|TOTAL|demand` = **-12285** (n=22, 2026-09-15T07:20:00.229572Z)
- `INDGEN|TOTAL|generation` = **20030** (n=22, 2026-09-15T07:20:16.723769Z)
- `MELNGC|TOTAL|margin` = **34133** (n=22, 2026-09-15T07:18:40.859983Z)
- `NDF|TOTAL|demand` = **19934** (n=22, 2026-09-15T07:17:10.602011Z)
- `TSDF|TOTAL|demand` = **20484** (n=22, 2026-09-15T07:16:54.235813Z)
- `WINDFOR|TOTAL|generation` = **17059** (n=3, 2026-09-15T05:30:39.125309Z)

## Latest publication events

- `2026-09-15T07:32:19.333355Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:31:45Z`
- `2026-09-15T07:30:28.783389Z` — **FUELHH**: 20 rows; marker `2026-09-15T07:30:00Z`
- `2026-09-15T07:30:28.783389Z` — **FUELINST**: 80 rows; marker `2026-09-15T07:30:00Z`
- `2026-09-15T07:30:12.965105Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:29:45Z`
- `2026-09-15T07:28:21.765879Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:27:45Z`
- `2026-09-15T07:26:14.124099Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:25:45Z`
- `2026-09-15T07:25:36.362211Z` — **FUELINST**: 80 rows; marker `2026-09-15T07:25:00Z`
- `2026-09-15T07:24:16.376432Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:23:45Z`
- `2026-09-15T07:22:08.848419Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:21:45Z`
- `2026-09-15T07:20:32.548006Z` — **FUELINST**: 80 rows; marker `2026-09-15T07:20:00Z`
- `2026-09-15T07:20:16.723769Z` — **INDGEN**: 738 rows; marker `2026-09-15T07:16:00Z`
- `2026-09-15T07:20:16.723769Z` — **IMBALNGC**: 738 rows; marker `2026-09-15T07:16:00Z`
- `2026-09-15T07:20:16.723769Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:19:45Z`
- `2026-09-15T07:20:00.229572Z` — **INDDEM**: 738 rows; marker `2026-09-15T07:16:00Z`
- `2026-09-15T07:18:40.859983Z` — **MELNGC**: 738 rows; marker `2026-09-15T07:16:00Z`
