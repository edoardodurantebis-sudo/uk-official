# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T08:31:21.233502Z`  
Current process started UTC: `2026-09-16T08:27:21.587608Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.94 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=427, 2026-09-16T08:30:33.621364Z)
- `FUELINST|fuelType=NPSHYD|generation` = **422** (n=427, 2026-09-16T08:30:33.621364Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=427, 2026-09-16T08:30:33.621364Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=427, 2026-09-16T08:30:33.621364Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=427, 2026-09-16T08:30:33.621364Z)
- `FUELINST|fuelType=OTHER|generation` = **388** (n=427, 2026-09-16T08:30:33.621364Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=427, 2026-09-16T08:30:33.621364Z)
- `FUELINST|fuelType=WIND|generation` = **6719** (n=427, 2026-09-16T08:30:33.621364Z)
- `IMBALNGC|TOTAL|imbalance` = **7107** (n=70, 2026-09-16T08:20:33.253805Z)
- `INDDEM|TOTAL|demand` = **-12666** (n=70, 2026-09-16T08:20:17.283178Z)
- `INDGEN|TOTAL|generation` = **26560** (n=70, 2026-09-16T08:20:17.283178Z)
- `MELNGC|TOTAL|margin` = **36560** (n=70, 2026-09-16T08:19:13.388012Z)
- `NDF|TOTAL|demand` = **18514** (n=72, 2026-09-16T08:16:58.262307Z)
- `TSDF|TOTAL|demand` = **19458** (n=72, 2026-09-16T08:16:58.262307Z)
- `WINDFOR|TOTAL|generation` = **19327** (n=12, 2026-09-16T08:30:33.621364Z)

## Latest publication events

- `2026-09-16T08:30:33.621364Z` — **WINDFOR**: 73 rows; marker `2026-09-16T08:30:00Z`
- `2026-09-16T08:30:33.621364Z` — **FUELHH**: 20 rows; marker `2026-09-16T08:30:00Z`
- `2026-09-16T08:30:33.621364Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:30:00Z`
- `2026-09-16T08:30:33.621364Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:29:45Z`
- `2026-09-16T08:28:25.594925Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:27:45Z`
- `2026-09-16T08:26:10.750487Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:25:45Z`
- `2026-09-16T08:25:39.229353Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:25:00Z`
- `2026-09-16T08:24:19.949523Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:23:45Z`
- `2026-09-16T08:22:09.657677Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:21:45Z`
- `2026-09-16T08:20:33.253805Z` — **IMBALNGC**: 702 rows; marker `2026-09-16T08:16:00Z`
- `2026-09-16T08:20:33.253805Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:20:00Z`
- `2026-09-16T08:20:33.253805Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:19:45Z`
- `2026-09-16T08:20:17.283178Z` — **INDGEN**: 702 rows; marker `2026-09-16T08:16:00Z`
- `2026-09-16T08:20:17.283178Z` — **INDDEM**: 702 rows; marker `2026-09-16T08:16:00Z`
- `2026-09-16T08:19:13.388012Z` — **MELNGC**: 702 rows; marker `2026-09-16T08:16:00Z`
