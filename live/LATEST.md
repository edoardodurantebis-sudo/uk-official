# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T05:42:58.698636Z`  
Current process started UTC: `2026-09-16T05:38:58.181625Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1411** (n=393, 2026-09-16T05:40:33.810223Z)
- `FUELINST|fuelType=NPSHYD|generation` = **552** (n=393, 2026-09-16T05:40:33.810223Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=393, 2026-09-16T05:40:33.810223Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=393, 2026-09-16T05:40:33.810223Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=393, 2026-09-16T05:40:33.810223Z)
- `FUELINST|fuelType=OTHER|generation` = **1244** (n=393, 2026-09-16T05:40:33.810223Z)
- `FUELINST|fuelType=PS|generation` = **223** (n=393, 2026-09-16T05:40:33.810223Z)
- `FUELINST|fuelType=WIND|generation` = **8503** (n=393, 2026-09-16T05:40:33.810223Z)
- `IMBALNGC|TOTAL|imbalance` = **7173** (n=65, 2026-09-16T05:20:17.305963Z)
- `INDDEM|TOTAL|demand` = **-12220** (n=65, 2026-09-16T05:20:17.305963Z)
- `INDGEN|TOTAL|generation` = **26294** (n=65, 2026-09-16T05:20:00.963476Z)
- `MELNGC|TOTAL|margin` = **37547** (n=65, 2026-09-16T05:18:56.750725Z)
- `NDF|TOTAL|demand` = **18621** (n=66, 2026-09-16T05:17:05.545597Z)
- `TSDF|TOTAL|demand` = **19121** (n=66, 2026-09-16T05:17:05.545597Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T05:42:09.892229Z` — **MID**: 0 rows; marker `2026-09-16T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T05:42:09.892229Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:41:45Z`
- `2026-09-16T05:40:33.810223Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:40:00Z`
- `2026-09-16T05:40:18.329170Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:39:45Z`
- `2026-09-16T05:38:18.531132Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:37:45Z`
- `2026-09-16T05:36:26.795641Z` — **MID**: 0 rows; marker `2026-09-16T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T05:36:11.086614Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:35:45Z`
- `2026-09-16T05:35:38.813623Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:35:00Z`
- `2026-09-16T05:34:19.405052Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:33:45Z`
- `2026-09-16T05:32:12.772966Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:31:45Z`
- `2026-09-16T05:30:53.425120Z` — **WINDFOR**: 73 rows; marker `2026-09-16T05:30:00Z`
- `2026-09-16T05:30:53.425120Z` — **FUELHH**: 20 rows; marker `2026-09-16T05:30:00Z`
- `2026-09-16T05:30:37.364241Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:30:00Z`
- `2026-09-16T05:30:09.853412Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:29:45Z`
- `2026-09-16T05:28:18.472972Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:27:45Z`
