# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T08:03:35.437608Z`  
Current process started UTC: `2026-09-15T07:59:35.204535Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNEM` `generation` — half-hour generation mix [fuelType=INTNEM] generation: value=824, delta=70, z=4.21 -> generation-mix component moved
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=19223, delta=-1261, z=-2941.66 -> demand pressure easing
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=0, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=0, z=3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=0, z=4.07 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1409** (n=133, 2026-09-15T08:00:41.181118Z)
- `FUELINST|fuelType=NPSHYD|generation` = **456** (n=133, 2026-09-15T08:00:41.181118Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3319** (n=133, 2026-09-15T08:00:41.181118Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=133, 2026-09-15T08:00:41.181118Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=133, 2026-09-15T08:00:41.181118Z)
- `FUELINST|fuelType=OTHER|generation` = **1085** (n=133, 2026-09-15T08:00:41.181118Z)
- `FUELINST|fuelType=PS|generation` = **-264** (n=133, 2026-09-15T08:00:41.181118Z)
- `FUELINST|fuelType=WIND|generation` = **12618** (n=133, 2026-09-15T08:00:41.181118Z)
- `IMBALNGC|TOTAL|imbalance` = **-454** (n=22, 2026-09-15T07:20:16.723769Z)
- `INDDEM|TOTAL|demand` = **-12285** (n=22, 2026-09-15T07:20:00.229572Z)
- `INDGEN|TOTAL|generation` = **20030** (n=22, 2026-09-15T07:20:16.723769Z)
- `MELNGC|TOTAL|margin` = **34133** (n=22, 2026-09-15T07:18:40.859983Z)
- `NDF|TOTAL|demand` = **18723** (n=23, 2026-09-15T07:45:46.867197Z)
- `TSDF|TOTAL|demand` = **19223** (n=23, 2026-09-15T07:45:46.867197Z)
- `WINDFOR|TOTAL|generation` = **17059** (n=3, 2026-09-15T05:30:39.125309Z)

## Latest publication events

- `2026-09-15T08:02:17.654322Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:01:45Z`
- `2026-09-15T08:00:41.181118Z` — **FUELHH**: 20 rows; marker `2026-09-15T08:00:00Z`
- `2026-09-15T08:00:41.181118Z` — **FUELINST**: 80 rows; marker `2026-09-15T08:00:00Z`
- `2026-09-15T08:00:08.259230Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:59:45Z`
- `2026-09-15T07:58:16.064327Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:57:45Z`
- `2026-09-15T07:56:08.061077Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:55:45Z`
- `2026-09-15T07:55:36.667004Z` — **FUELINST**: 80 rows; marker `2026-09-15T07:55:00Z`
- `2026-09-15T07:54:25.248738Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:53:45Z`
- `2026-09-15T07:52:17.856473Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:51:45Z`
- `2026-09-15T07:50:42.197603Z` — **FUELINST**: 80 rows; marker `2026-09-15T07:50:00Z`
- `2026-09-15T07:50:26.598676Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:49:45Z`
- `2026-09-15T07:48:18.661230Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:47:45Z`
- `2026-09-15T07:46:18.183262Z` — **FREQ**: 5761 rows; marker `2026-09-15T07:45:45Z`
- `2026-09-15T07:45:46.867197Z` — **TSDF**: 864 rows; marker `2026-09-15T07:45:00Z`
- `2026-09-15T07:45:46.867197Z` — **NDF**: 48 rows; marker `2026-09-15T07:45:00Z`
