# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T01:50:29.009106Z`  
Current process started UTC: `2026-09-15T01:46:29.490890Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-359** (n=58, 2026-09-15T01:45:45.184301Z)
- `FUELINST|fuelType=NPSHYD|generation` = **334** (n=58, 2026-09-15T01:45:45.184301Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=58, 2026-09-15T01:45:45.184301Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=58, 2026-09-15T01:45:45.184301Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=58, 2026-09-15T01:45:45.184301Z)
- `FUELINST|fuelType=OTHER|generation` = **175** (n=58, 2026-09-15T01:45:45.184301Z)
- `FUELINST|fuelType=PS|generation` = **-7** (n=58, 2026-09-15T01:45:45.184301Z)
- `FUELINST|fuelType=WIND|generation` = **12590** (n=58, 2026-09-15T01:45:45.184301Z)
- `IMBALNGC|TOTAL|imbalance` = **246** (n=10, 2026-09-15T01:21:35.962228Z)
- `INDDEM|TOTAL|demand` = **-12315** (n=10, 2026-09-15T01:21:19.808966Z)
- `INDGEN|TOTAL|generation` = **20731** (n=10, 2026-09-15T01:21:19.808966Z)
- `MELNGC|TOTAL|margin` = **32734** (n=11, 2026-09-15T01:49:28.964755Z)
- `NDF|TOTAL|demand` = **19934** (n=11, 2026-09-15T01:47:04.701005Z)
- `TSDF|TOTAL|demand` = **20485** (n=11, 2026-09-15T01:47:20.702925Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-15T01:50:17.342187Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:49:45Z`
- `2026-09-15T01:49:28.964755Z` — **MELNGC**: 936 rows; marker `2026-09-15T01:46:00Z`
- `2026-09-15T01:48:08.958372Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:47:45Z`
- `2026-09-15T01:47:20.702925Z` — **TSDF**: 936 rows; marker `2026-09-15T01:46:00Z`
- `2026-09-15T01:47:04.701005Z` — **NDF**: 52 rows; marker `2026-09-15T01:46:00Z`
- `2026-09-15T01:46:00.851081Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:45:45Z`
- `2026-09-15T01:45:45.184301Z` — **FUELINST**: 80 rows; marker `2026-09-15T01:45:00Z`
- `2026-09-15T01:44:09.711664Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:43:45Z`
- `2026-09-15T01:42:18.217722Z` — **MID**: 0 rows; marker `2026-09-15T01:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T01:42:18.217722Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:41:45Z`
- `2026-09-15T01:40:35.281654Z` — **FUELINST**: 80 rows; marker `2026-09-15T01:40:00Z`
- `2026-09-15T01:40:19.060576Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:39:45Z`
- `2026-09-15T01:38:27.060270Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:37:45Z`
- `2026-09-15T01:36:19.459114Z` — **MID**: 0 rows; marker `2026-09-15T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T01:36:19.459114Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:35:45Z`
