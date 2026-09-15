# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T02:28:08.329701Z`  
Current process started UTC: `2026-09-15T02:24:08.175145Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **MELNGC** `TOTAL` `margin` — indicated margin [TOTAL] margin: value=34104, delta=1370, z=NA -> margin/tightness state changed
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=0, z=3.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=1, z=4.75 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=3.56 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=3.86 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=-299, delta=8, z=3.95 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=4.25 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=4.80 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=5.62 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=-307, delta=170, z=4.89 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=7.11 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0.004, z=11.23 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2683, delta=11, z=5.04 -> generation-mix component moved
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2672, delta=95, z=11.64 -> generation-mix component moved
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2560, delta=-26, z=-2.39 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-367** (n=66, 2026-09-15T02:25:29.614620Z)
- `FUELINST|fuelType=NPSHYD|generation` = **336** (n=66, 2026-09-15T02:25:29.614620Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=66, 2026-09-15T02:25:29.614620Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=66, 2026-09-15T02:25:29.614620Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=66, 2026-09-15T02:25:29.614620Z)
- `FUELINST|fuelType=OTHER|generation` = **183** (n=66, 2026-09-15T02:25:29.614620Z)
- `FUELINST|fuelType=PS|generation` = **-8** (n=66, 2026-09-15T02:25:29.614620Z)
- `FUELINST|fuelType=WIND|generation` = **12389** (n=66, 2026-09-15T02:25:29.614620Z)
- `IMBALNGC|TOTAL|imbalance` = **247** (n=12, 2026-09-15T02:20:48.688934Z)
- `INDDEM|TOTAL|demand` = **-12319** (n=12, 2026-09-15T02:20:32.984280Z)
- `INDGEN|TOTAL|generation` = **20732** (n=12, 2026-09-15T02:20:32.984280Z)
- `MELNGC|TOTAL|margin` = **34104** (n=12, 2026-09-15T02:19:28.123721Z)
- `NDF|TOTAL|demand` = **19934** (n=12, 2026-09-15T02:17:36.288258Z)
- `TSDF|TOTAL|demand` = **20485** (n=12, 2026-09-15T02:17:36.288258Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-15T02:26:16.957076Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:25:45Z`
- `2026-09-15T02:25:29.614620Z` — **FUELINST**: 80 rows; marker `2026-09-15T02:25:00Z`
- `2026-09-15T02:24:24.176877Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:23:45Z`
- `2026-09-15T02:22:24.924585Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:21:45Z`
- `2026-09-15T02:20:48.688934Z` — **IMBALNGC**: 918 rows; marker `2026-09-15T02:17:00Z`
- `2026-09-15T02:20:32.984280Z` — **INDGEN**: 918 rows; marker `2026-09-15T02:17:00Z`
- `2026-09-15T02:20:32.984280Z` — **INDDEM**: 918 rows; marker `2026-09-15T02:17:00Z`
- `2026-09-15T02:20:32.984280Z` — **FUELINST**: 80 rows; marker `2026-09-15T02:20:00Z`
- `2026-09-15T02:20:17.252441Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:19:45Z`
- `2026-09-15T02:19:28.123721Z` — **MELNGC**: 918 rows; marker `2026-09-15T02:17:00Z`
- `2026-09-15T02:18:24.131625Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:17:45Z`
- `2026-09-15T02:17:36.288258Z` — **TSDF**: 918 rows; marker `2026-09-15T02:17:00Z`
- `2026-09-15T02:17:36.288258Z` — **NDF**: 51 rows; marker `2026-09-15T02:17:00Z`
- `2026-09-15T02:16:16.589045Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:15:45Z`
- `2026-09-15T02:15:44.716743Z` — **FUELINST**: 80 rows; marker `2026-09-15T02:15:00Z`
