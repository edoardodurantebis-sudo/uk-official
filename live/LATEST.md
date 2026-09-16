# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T08:56:37.277116Z`  
Current process started UTC: `2026-09-16T08:52:37.527252Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=432, 2026-09-16T08:55:34.656191Z)
- `FUELINST|fuelType=NPSHYD|generation` = **382** (n=432, 2026-09-16T08:55:34.656191Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=432, 2026-09-16T08:55:34.656191Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=432, 2026-09-16T08:55:34.656191Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=432, 2026-09-16T08:55:34.656191Z)
- `FUELINST|fuelType=OTHER|generation` = **536** (n=432, 2026-09-16T08:55:34.656191Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=432, 2026-09-16T08:55:34.656191Z)
- `FUELINST|fuelType=WIND|generation` = **6393** (n=432, 2026-09-16T08:55:34.656191Z)
- `IMBALNGC|TOTAL|imbalance` = **6705** (n=71, 2026-09-16T08:49:32.469051Z)
- `INDDEM|TOTAL|demand` = **-12681** (n=71, 2026-09-16T08:49:32.469051Z)
- `INDGEN|TOTAL|generation` = **26163** (n=71, 2026-09-16T08:49:32.469051Z)
- `MELNGC|TOTAL|margin` = **35745** (n=71, 2026-09-16T08:49:00.683932Z)
- `NDF|TOTAL|demand` = **18514** (n=73, 2026-09-16T08:47:08.665911Z)
- `TSDF|TOTAL|demand` = **19458** (n=73, 2026-09-16T08:47:08.665911Z)
- `WINDFOR|TOTAL|generation` = **19327** (n=12, 2026-09-16T08:30:33.621364Z)

## Latest publication events

- `2026-09-16T08:56:06.698327Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:55:45Z`
- `2026-09-16T08:55:34.656191Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:55:00Z`
- `2026-09-16T08:54:31.249109Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:53:45Z`
- `2026-09-16T08:52:37.527259Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:51:45Z`
- `2026-09-16T08:50:36.295577Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:50:00Z`
- `2026-09-16T08:50:20.239450Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:49:45Z`
- `2026-09-16T08:49:32.469051Z` — **INDGEN**: 684 rows; marker `2026-09-16T08:46:00Z`
- `2026-09-16T08:49:32.469051Z` — **INDDEM**: 684 rows; marker `2026-09-16T08:46:00Z`
- `2026-09-16T08:49:32.469051Z` — **IMBALNGC**: 684 rows; marker `2026-09-16T08:46:00Z`
- `2026-09-16T08:49:00.683932Z` — **MELNGC**: 684 rows; marker `2026-09-16T08:46:00Z`
- `2026-09-16T08:48:28.521575Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:47:45Z`
- `2026-09-16T08:47:08.665911Z` — **TSDF**: 684 rows; marker `2026-09-16T08:46:00Z`
- `2026-09-16T08:47:08.665911Z` — **NDF**: 38 rows; marker `2026-09-16T08:46:00Z`
- `2026-09-16T08:46:20.451206Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:45:45Z`
- `2026-09-16T08:45:33.119230Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:45:00Z`
