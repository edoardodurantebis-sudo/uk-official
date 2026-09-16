# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T04:19:00.576020Z`  
Current process started UTC: `2026-09-16T04:15:01.113860Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1349** (n=376, 2026-09-16T04:15:49.118827Z)
- `FUELINST|fuelType=NPSHYD|generation` = **396** (n=376, 2026-09-16T04:15:49.118827Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=376, 2026-09-16T04:15:49.118827Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=376, 2026-09-16T04:15:49.118827Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=376, 2026-09-16T04:15:49.118827Z)
- `FUELINST|fuelType=OTHER|generation` = **251** (n=376, 2026-09-16T04:15:49.118827Z)
- `FUELINST|fuelType=PS|generation` = **223** (n=376, 2026-09-16T04:15:49.118827Z)
- `FUELINST|fuelType=WIND|generation` = **9486** (n=376, 2026-09-16T04:15:49.118827Z)
- `IMBALNGC|TOTAL|imbalance` = **7021** (n=62, 2026-09-16T03:50:43.848366Z)
- `INDDEM|TOTAL|demand` = **-12202** (n=62, 2026-09-16T03:50:43.848366Z)
- `INDGEN|TOTAL|generation` = **26142** (n=62, 2026-09-16T03:50:43.848366Z)
- `MELNGC|TOTAL|margin` = **37540** (n=62, 2026-09-16T03:49:25.287483Z)
- `NDF|TOTAL|demand` = **18621** (n=64, 2026-09-16T04:17:25.701329Z)
- `TSDF|TOTAL|demand` = **19121** (n=64, 2026-09-16T04:17:25.701329Z)
- `WINDFOR|TOTAL|generation` = **18849** (n=10, 2026-09-16T03:30:50.299289Z)

## Latest publication events

- `2026-09-16T04:18:13.443814Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:17:45Z`
- `2026-09-16T04:17:25.701329Z` — **TSDF**: 846 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:17:25.701329Z` — **NDF**: 47 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:16:05.372798Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:15:45Z`
- `2026-09-16T04:15:49.118827Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:15:00Z`
- `2026-09-16T04:14:09.636180Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:13:45Z`
- `2026-09-16T04:12:15.464348Z` — **MID**: 0 rows; marker `2026-09-16T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T04:12:15.464348Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:11:45Z`
- `2026-09-16T04:10:39.289480Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:10:00Z`
- `2026-09-16T04:10:23.658745Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:09:45Z`
- `2026-09-16T04:08:16.182792Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:07:45Z`
- `2026-09-16T04:06:39.924530Z` — **MID**: 0 rows; marker `2026-09-16T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T04:06:39.924530Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:05:45Z`
- `2026-09-16T04:05:39.469733Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:05:00Z`
- `2026-09-16T04:04:19.257852Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:03:45Z`
