# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T02:07:13.124178Z`  
Current process started UTC: `2026-09-15T02:03:12.770657Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=542, delta=109, z=4.43 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-366** (n=62, 2026-09-15T02:05:27.104908Z)
- `FUELINST|fuelType=NPSHYD|generation` = **336** (n=62, 2026-09-15T02:05:27.104908Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=62, 2026-09-15T02:05:27.104908Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=62, 2026-09-15T02:05:27.104908Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=62, 2026-09-15T02:05:27.104908Z)
- `FUELINST|fuelType=OTHER|generation` = **147** (n=62, 2026-09-15T02:05:27.104908Z)
- `FUELINST|fuelType=PS|generation` = **-7** (n=62, 2026-09-15T02:05:27.104908Z)
- `FUELINST|fuelType=WIND|generation` = **12553** (n=62, 2026-09-15T02:05:27.104908Z)
- `IMBALNGC|TOTAL|imbalance` = **244** (n=11, 2026-09-15T01:51:27.629381Z)
- `INDDEM|TOTAL|demand` = **-12315** (n=11, 2026-09-15T01:51:27.629381Z)
- `INDGEN|TOTAL|generation` = **20729** (n=11, 2026-09-15T01:51:43.194597Z)
- `MELNGC|TOTAL|margin` = **32734** (n=11, 2026-09-15T01:49:28.964755Z)
- `NDF|TOTAL|demand` = **19934** (n=11, 2026-09-15T01:47:04.701005Z)
- `TSDF|TOTAL|demand` = **20485** (n=11, 2026-09-15T01:47:20.702925Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-15T02:06:33.192231Z` — **MID**: 0 rows; marker `2026-09-15T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T02:06:16.058272Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:05:45Z`
- `2026-09-15T02:05:27.104908Z` — **FUELINST**: 80 rows; marker `2026-09-15T02:05:00Z`
- `2026-09-15T02:04:22.948214Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:03:45Z`
- `2026-09-15T02:02:13.733662Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:01:45Z`
- `2026-09-15T02:00:21.862091Z` — **FUELHH**: 20 rows; marker `2026-09-15T02:00:00Z`
- `2026-09-15T02:00:21.862091Z` — **FUELINST**: 80 rows; marker `2026-09-15T02:00:00Z`
- `2026-09-15T02:00:21.862091Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:59:45Z`
- `2026-09-15T01:58:06.172894Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:57:45Z`
- `2026-09-15T01:56:30.283760Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:55:45Z`
- `2026-09-15T01:55:26.022953Z` — **FUELINST**: 80 rows; marker `2026-09-15T01:55:00Z`
- `2026-09-15T01:54:06.794387Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:53:45Z`
- `2026-09-15T01:52:14.811733Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:51:45Z`
- `2026-09-15T01:51:43.194597Z` — **INDGEN**: 936 rows; marker `2026-09-15T01:46:00Z`
- `2026-09-15T01:51:27.629381Z` — **INDDEM**: 936 rows; marker `2026-09-15T01:46:00Z`
