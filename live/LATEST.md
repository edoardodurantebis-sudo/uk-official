# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T09:22:28.851865Z`  
Current process started UTC: `2026-09-16T09:18:28.841645Z`  
1-second metadata polls in this process: **229**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=-1204, z=-7.82 -> demand pressure easing
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.27 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.52 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.55 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.57 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.60 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.63 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.66 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.69 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.73 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.76 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.79 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.83 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.86 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.90 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1404** (n=437, 2026-09-16T09:20:39.701665Z)
- `FUELINST|fuelType=NPSHYD|generation` = **358** (n=437, 2026-09-16T09:20:39.701665Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=437, 2026-09-16T09:20:39.701665Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=437, 2026-09-16T09:20:39.701665Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=437, 2026-09-16T09:20:39.701665Z)
- `FUELINST|fuelType=OTHER|generation` = **418** (n=437, 2026-09-16T09:20:39.701665Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=437, 2026-09-16T09:20:39.701665Z)
- `FUELINST|fuelType=WIND|generation` = **5833** (n=437, 2026-09-16T09:20:39.701665Z)
- `IMBALNGC|TOTAL|imbalance` = **5364** (n=72, 2026-09-16T09:20:07.059543Z)
- `INDDEM|TOTAL|demand` = **-13885** (n=72, 2026-09-16T09:20:07.059543Z)
- `INDGEN|TOTAL|generation` = **26002** (n=72, 2026-09-16T09:20:07.059543Z)
- `MELNGC|TOTAL|margin` = **34508** (n=72, 2026-09-16T09:19:16.848245Z)
- `NDF|TOTAL|demand` = **18514** (n=74, 2026-09-16T09:17:11.864576Z)
- `TSDF|TOTAL|demand` = **20638** (n=74, 2026-09-16T09:17:11.864576Z)
- `WINDFOR|TOTAL|generation` = **19327** (n=12, 2026-09-16T08:30:33.621364Z)

## Latest publication events

- `2026-09-16T09:22:15.192381Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:21:45Z`
- `2026-09-16T09:20:39.701665Z` — **FUELINST**: 80 rows; marker `2026-09-16T09:20:00Z`
- `2026-09-16T09:20:23.551339Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:19:45Z`
- `2026-09-16T09:20:07.059543Z` — **INDGEN**: 666 rows; marker `2026-09-16T09:16:00Z`
- `2026-09-16T09:20:07.059543Z` — **INDDEM**: 666 rows; marker `2026-09-16T09:16:00Z`
- `2026-09-16T09:20:07.059543Z` — **IMBALNGC**: 666 rows; marker `2026-09-16T09:16:00Z`
- `2026-09-16T09:19:16.848245Z` — **MELNGC**: 666 rows; marker `2026-09-16T09:16:00Z`
- `2026-09-16T09:18:28.841654Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:17:45Z`
- `2026-09-16T09:17:11.864576Z` — **TSDF**: 666 rows; marker `2026-09-16T09:16:00Z`
- `2026-09-16T09:17:11.864576Z` — **NDF**: 37 rows; marker `2026-09-16T09:16:00Z`
- `2026-09-16T09:16:23.513496Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:15:45Z`
- `2026-09-16T09:15:35.299603Z` — **FUELINST**: 80 rows; marker `2026-09-16T09:15:00Z`
- `2026-09-16T09:14:14.682318Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:13:45Z`
- `2026-09-16T09:12:14.287594Z` — **MID**: 0 rows; marker `2026-09-16T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T09:12:14.287594Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:11:45Z`
