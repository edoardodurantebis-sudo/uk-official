# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T01:25:19.554990Z`  
Current process started UTC: `2026-09-15T01:21:19.808959Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-359** (n=53, 2026-09-15T01:20:23.822367Z)
- `FUELINST|fuelType=NPSHYD|generation` = **331** (n=53, 2026-09-15T01:20:23.822367Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3319** (n=53, 2026-09-15T01:20:23.822367Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=53, 2026-09-15T01:20:23.822367Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=53, 2026-09-15T01:20:23.822367Z)
- `FUELINST|fuelType=OTHER|generation` = **110** (n=53, 2026-09-15T01:20:23.822367Z)
- `FUELINST|fuelType=PS|generation` = **-7** (n=53, 2026-09-15T01:20:23.822367Z)
- `FUELINST|fuelType=WIND|generation` = **12278** (n=53, 2026-09-15T01:20:23.822367Z)
- `IMBALNGC|TOTAL|imbalance` = **246** (n=10, 2026-09-15T01:21:35.962228Z)
- `INDDEM|TOTAL|demand` = **-12315** (n=10, 2026-09-15T01:21:19.808966Z)
- `INDGEN|TOTAL|generation` = **20731** (n=10, 2026-09-15T01:21:19.808966Z)
- `MELNGC|TOTAL|margin` = **32694** (n=10, 2026-09-15T01:19:52.385560Z)
- `NDF|TOTAL|demand` = **19934** (n=10, 2026-09-15T01:17:59.634588Z)
- `TSDF|TOTAL|demand` = **20485** (n=10, 2026-09-15T01:17:59.634588Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-15T01:24:15.511189Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:23:45Z`
- `2026-09-15T01:22:23.297742Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:21:45Z`
- `2026-09-15T01:21:35.962228Z` — **IMBALNGC**: 954 rows; marker `2026-09-15T01:17:00Z`
- `2026-09-15T01:21:19.808966Z` — **INDGEN**: 954 rows; marker `2026-09-15T01:17:00Z`
- `2026-09-15T01:21:19.808966Z` — **INDDEM**: 954 rows; marker `2026-09-15T01:17:00Z`
- `2026-09-15T01:20:23.822367Z` — **FUELINST**: 80 rows; marker `2026-09-15T01:20:00Z`
- `2026-09-15T01:20:23.822367Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:19:45Z`
- `2026-09-15T01:19:52.385560Z` — **MELNGC**: 954 rows; marker `2026-09-15T01:17:00Z`
- `2026-09-15T01:18:15.690448Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:17:45Z`
- `2026-09-15T01:17:59.634588Z` — **TSDF**: 954 rows; marker `2026-09-15T01:17:00Z`
- `2026-09-15T01:17:59.634588Z` — **NDF**: 53 rows; marker `2026-09-15T01:17:00Z`
- `2026-09-15T01:16:23.839973Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:15:45Z`
- `2026-09-15T01:15:52.238933Z` — **FUELINST**: 80 rows; marker `2026-09-15T01:15:00Z`
- `2026-09-15T01:14:16.336655Z` — **FREQ**: 5761 rows; marker `2026-09-15T01:13:45Z`
- `2026-09-15T01:12:12.294479Z` — **MID**: 0 rows; marker `2026-09-15T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
