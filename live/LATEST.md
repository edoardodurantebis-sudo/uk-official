# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T00:39:11.598479Z`  
Current process started UTC: `2026-09-15T00:35:11.556934Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-889, delta=-56, z=-4.14 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-134** (n=44, 2026-09-15T00:35:27.800431Z)
- `FUELINST|fuelType=NPSHYD|generation` = **364** (n=44, 2026-09-15T00:35:27.800431Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3313** (n=44, 2026-09-15T00:35:27.800431Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=44, 2026-09-15T00:35:27.800431Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=44, 2026-09-15T00:35:27.800431Z)
- `FUELINST|fuelType=OTHER|generation` = **259** (n=44, 2026-09-15T00:35:27.800431Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=44, 2026-09-15T00:35:27.800431Z)
- `FUELINST|fuelType=WIND|generation` = **11900** (n=44, 2026-09-15T00:35:27.800431Z)
- `IMBALNGC|TOTAL|imbalance` = **264** (n=8, 2026-09-15T00:21:24.227589Z)
- `INDDEM|TOTAL|demand` = **-12271** (n=8, 2026-09-15T00:20:52.338789Z)
- `INDGEN|TOTAL|generation` = **20748** (n=8, 2026-09-15T00:20:52.338789Z)
- `MELNGC|TOTAL|margin` = **32698** (n=8, 2026-09-15T00:19:15.734525Z)
- `NDF|TOTAL|demand` = **19934** (n=8, 2026-09-15T00:17:29.827613Z)
- `TSDF|TOTAL|demand` = **20485** (n=8, 2026-09-15T00:17:29.827613Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-15T00:38:22.640594Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:37:45Z`
- `2026-09-15T00:37:18.687378Z` — **MID**: 0 rows; marker `2026-09-15T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T00:36:15.338219Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:35:45Z`
- `2026-09-15T00:35:27.800431Z` — **FUELINST**: 80 rows; marker `2026-09-15T00:35:00Z`
- `2026-09-15T00:34:11.201061Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:33:45Z`
- `2026-09-15T00:32:19.028558Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:31:45Z`
- `2026-09-15T00:30:31.822197Z` — **FUELHH**: 20 rows; marker `2026-09-15T00:30:00Z`
- `2026-09-15T00:30:31.822197Z` — **FUELINST**: 80 rows; marker `2026-09-15T00:30:00Z`
- `2026-09-15T00:30:15.496579Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:29:45Z`
- `2026-09-15T00:28:07.651859Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:27:45Z`
- `2026-09-15T00:26:10.959736Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:25:45Z`
- `2026-09-15T00:25:22.912599Z` — **FUELINST**: 80 rows; marker `2026-09-15T00:25:00Z`
- `2026-09-15T00:24:19.103473Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:23:45Z`
- `2026-09-15T00:22:27.539624Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:21:45Z`
- `2026-09-15T00:21:24.227589Z` — **IMBALNGC**: 990 rows; marker `2026-09-15T00:17:00Z`
