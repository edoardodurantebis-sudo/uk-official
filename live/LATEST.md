# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T01:04:20.751624Z`  
Current process started UTC: `2026-09-15T01:00:21.125764Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=542, delta=109, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=1193, delta=90, z=3.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-187** (n=49, 2026-09-15T01:00:36.705016Z)
- `FUELINST|fuelType=NPSHYD|generation` = **362** (n=49, 2026-09-15T01:00:36.705016Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=49, 2026-09-15T01:00:36.705016Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=49, 2026-09-15T01:00:36.705016Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=49, 2026-09-15T01:00:36.705016Z)
- `FUELINST|fuelType=OTHER|generation` = **154** (n=49, 2026-09-15T01:00:36.705016Z)
- `FUELINST|fuelType=PS|generation` = **-7** (n=49, 2026-09-15T01:00:36.705016Z)
- `FUELINST|fuelType=WIND|generation` = **12076** (n=49, 2026-09-15T01:00:36.705016Z)
- `IMBALNGC|TOTAL|imbalance` = **272** (n=9, 2026-09-15T00:50:48.386336Z)
- `INDDEM|TOTAL|demand` = **-12347** (n=9, 2026-09-15T00:50:48.386336Z)
- `INDGEN|TOTAL|generation` = **20756** (n=9, 2026-09-15T00:50:48.386336Z)
- `MELNGC|TOTAL|margin` = **32669** (n=9, 2026-09-15T00:49:12.420351Z)
- `NDF|TOTAL|demand` = **19934** (n=9, 2026-09-15T00:47:35.530009Z)
- `TSDF|TOTAL|demand` = **20485** (n=9, 2026-09-15T00:47:35.530009Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-15T01:02:31.072666Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:01:45Z`
- `2026-09-15T01:00:36.705016Z` — **FUELHH**: 20 rows; marker `2026-09-15T01:00:00Z`
- `2026-09-15T01:00:36.705016Z` — **FUELINST**: 80 rows; marker `2026-09-15T01:00:00Z`
- `2026-09-15T01:00:21.125773Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:59:45Z`
- `2026-09-15T00:58:27.533975Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:57:45Z`
- `2026-09-15T00:56:26.905699Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:55:45Z`
- `2026-09-15T00:55:44.442285Z` — **FUELINST**: 80 rows; marker `2026-09-15T00:55:00Z`
- `2026-09-15T00:54:24.342168Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:53:45Z`
- `2026-09-15T00:52:16.068439Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:51:45Z`
- `2026-09-15T00:50:48.386336Z` — **INDGEN**: 972 rows; marker `2026-09-15T00:47:00Z`
- `2026-09-15T00:50:48.386336Z` — **INDDEM**: 972 rows; marker `2026-09-15T00:47:00Z`
- `2026-09-15T00:50:48.386336Z` — **IMBALNGC**: 972 rows; marker `2026-09-15T00:47:00Z`
- `2026-09-15T00:50:31.907378Z` — **FUELINST**: 80 rows; marker `2026-09-15T00:50:00Z`
- `2026-09-15T00:50:16.122121Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:49:45Z`
- `2026-09-15T00:49:12.420351Z` — **MELNGC**: 972 rows; marker `2026-09-15T00:47:00Z`
