# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T04:52:37.570611Z`  
Current process started UTC: `2026-09-16T04:48:37.604832Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.97 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1349** (n=383, 2026-09-16T04:50:34.838750Z)
- `FUELINST|fuelType=NPSHYD|generation` = **424** (n=383, 2026-09-16T04:50:34.838750Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=383, 2026-09-16T04:50:34.838750Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=383, 2026-09-16T04:50:34.838750Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=383, 2026-09-16T04:50:34.838750Z)
- `FUELINST|fuelType=OTHER|generation` = **738** (n=383, 2026-09-16T04:50:34.838750Z)
- `FUELINST|fuelType=PS|generation` = **228** (n=383, 2026-09-16T04:50:34.838750Z)
- `FUELINST|fuelType=WIND|generation` = **9147** (n=383, 2026-09-16T04:50:34.838750Z)
- `IMBALNGC|TOTAL|imbalance` = **7203** (n=64, 2026-09-16T04:50:19.267417Z)
- `INDDEM|TOTAL|demand` = **-12179** (n=64, 2026-09-16T04:50:03.921403Z)
- `INDGEN|TOTAL|generation` = **26324** (n=64, 2026-09-16T04:50:03.921403Z)
- `MELNGC|TOTAL|margin` = **37521** (n=64, 2026-09-16T04:49:14.608454Z)
- `NDF|TOTAL|demand` = **18621** (n=65, 2026-09-16T04:47:23.268822Z)
- `TSDF|TOTAL|demand` = **19121** (n=65, 2026-09-16T04:47:23.268822Z)
- `WINDFOR|TOTAL|generation` = **18849** (n=10, 2026-09-16T03:30:50.299289Z)

## Latest publication events

- `2026-09-16T04:52:11.077805Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:51:45Z`
- `2026-09-16T04:50:34.838750Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:50:00Z`
- `2026-09-16T04:50:19.267417Z` — **IMBALNGC**: 828 rows; marker `2026-09-16T04:46:00Z`
- `2026-09-16T04:50:19.267417Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:49:45Z`
- `2026-09-16T04:50:03.921403Z` — **INDGEN**: 828 rows; marker `2026-09-16T04:46:00Z`
- `2026-09-16T04:50:03.921403Z` — **INDDEM**: 828 rows; marker `2026-09-16T04:46:00Z`
- `2026-09-16T04:49:14.608454Z` — **MELNGC**: 828 rows; marker `2026-09-16T04:46:00Z`
- `2026-09-16T04:48:11.218146Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:47:45Z`
- `2026-09-16T04:47:23.268822Z` — **TSDF**: 828 rows; marker `2026-09-16T04:46:00Z`
- `2026-09-16T04:47:23.268822Z` — **NDF**: 46 rows; marker `2026-09-16T04:46:00Z`
- `2026-09-16T04:46:19.473274Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:45:45Z`
- `2026-09-16T04:45:31.205337Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:45:00Z`
- `2026-09-16T04:44:27.461656Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:43:45Z`
- `2026-09-16T04:42:08.945705Z` — **MID**: 0 rows; marker `2026-09-16T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T04:42:08.945705Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:41:45Z`
