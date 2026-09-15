# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T08:28:45.105137Z`  
Current process started UTC: `2026-09-15T08:24:45.240737Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=3.92 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=4.18 -> generation-mix component moved
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=20619, delta=1396, z=0.72 -> demand pressure up
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=20069, delta=1346, z=0.74 -> demand pressure up
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=4.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=162, z=4.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=538, delta=280, z=3.81 -> generation-mix component moved
- **FUELHH** `fuelType=INTNEM` `generation` — half-hour generation mix [fuelType=INTNEM] generation: value=824, delta=70, z=4.21 -> generation-mix component moved
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=19223, delta=-1261, z=-2941.66 -> demand pressure easing
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=0, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=0, z=3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=0, z=4.07 -> generation-mix component moved
- **FUELHH** `fuelType=INTVKL` `generation` — half-hour generation mix [fuelType=INTVKL] generation: value=1336, delta=1030, z=3.74 -> generation-mix component moved
- **FUELHH** `fuelType=INTNEM` `generation` — half-hour generation mix [fuelType=INTNEM] generation: value=754, delta=1138, z=8.18 -> generation-mix component moved
- **FUELHH** `fuelType=INTEW` `generation` — half-hour generation mix [fuelType=INTEW] generation: value=-424, delta=-132, z=-4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=138, 2026-09-15T08:25:33.250501Z)
- `FUELINST|fuelType=NPSHYD|generation` = **430** (n=138, 2026-09-15T08:25:33.250501Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3314** (n=138, 2026-09-15T08:25:33.250501Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=138, 2026-09-15T08:25:33.250501Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=138, 2026-09-15T08:25:33.250501Z)
- `FUELINST|fuelType=OTHER|generation` = **626** (n=138, 2026-09-15T08:25:33.250501Z)
- `FUELINST|fuelType=PS|generation` = **-307** (n=138, 2026-09-15T08:25:33.250501Z)
- `FUELINST|fuelType=WIND|generation` = **12643** (n=138, 2026-09-15T08:25:33.250501Z)
- `IMBALNGC|TOTAL|imbalance` = **-475** (n=23, 2026-09-15T08:19:48.895221Z)
- `INDDEM|TOTAL|demand` = **-12308** (n=23, 2026-09-15T08:19:48.895221Z)
- `INDGEN|TOTAL|generation` = **20144** (n=23, 2026-09-15T08:19:48.895221Z)
- `MELNGC|TOTAL|margin` = **34045** (n=23, 2026-09-15T08:19:16.718059Z)
- `NDF|TOTAL|demand` = **20069** (n=24, 2026-09-15T08:17:09.102894Z)
- `TSDF|TOTAL|demand` = **20619** (n=24, 2026-09-15T08:17:25.048682Z)
- `WINDFOR|TOTAL|generation` = **17059** (n=3, 2026-09-15T05:30:39.125309Z)

## Latest publication events

- `2026-09-15T08:28:12.918764Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:27:45Z`
- `2026-09-15T08:26:21.336889Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:25:45Z`
- `2026-09-15T08:25:33.250501Z` — **FUELINST**: 80 rows; marker `2026-09-15T08:25:00Z`
- `2026-09-15T08:24:22.948930Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:23:45Z`
- `2026-09-15T08:22:14.882532Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:21:45Z`
- `2026-09-15T08:20:37.700628Z` — **FUELINST**: 80 rows; marker `2026-09-15T08:20:00Z`
- `2026-09-15T08:20:21.337244Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:19:45Z`
- `2026-09-15T08:19:48.895221Z` — **INDGEN**: 702 rows; marker `2026-09-15T08:16:00Z`
- `2026-09-15T08:19:48.895221Z` — **INDDEM**: 702 rows; marker `2026-09-15T08:16:00Z`
- `2026-09-15T08:19:48.895221Z` — **IMBALNGC**: 702 rows; marker `2026-09-15T08:16:00Z`
- `2026-09-15T08:19:16.718059Z` — **MELNGC**: 702 rows; marker `2026-09-15T08:16:00Z`
- `2026-09-15T08:18:12.992870Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:17:45Z`
- `2026-09-15T08:17:25.048682Z` — **TSDF**: 702 rows; marker `2026-09-15T08:16:00Z`
- `2026-09-15T08:17:09.102894Z` — **NDF**: 39 rows; marker `2026-09-15T08:16:00Z`
- `2026-09-15T08:16:21.357184Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:15:45Z`
