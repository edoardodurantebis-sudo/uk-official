# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T05:34:36.914929Z`  
Current process started UTC: `2026-09-16T05:30:37.364234Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1411** (n=391, 2026-09-16T05:30:37.364241Z)
- `FUELINST|fuelType=NPSHYD|generation` = **529** (n=391, 2026-09-16T05:30:37.364241Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=391, 2026-09-16T05:30:37.364241Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=391, 2026-09-16T05:30:37.364241Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=391, 2026-09-16T05:30:37.364241Z)
- `FUELINST|fuelType=OTHER|generation` = **1275** (n=391, 2026-09-16T05:30:37.364241Z)
- `FUELINST|fuelType=PS|generation` = **223** (n=391, 2026-09-16T05:30:37.364241Z)
- `FUELINST|fuelType=WIND|generation` = **8663** (n=391, 2026-09-16T05:30:37.364241Z)
- `IMBALNGC|TOTAL|imbalance` = **7173** (n=65, 2026-09-16T05:20:17.305963Z)
- `INDDEM|TOTAL|demand` = **-12220** (n=65, 2026-09-16T05:20:17.305963Z)
- `INDGEN|TOTAL|generation` = **26294** (n=65, 2026-09-16T05:20:00.963476Z)
- `MELNGC|TOTAL|margin` = **37547** (n=65, 2026-09-16T05:18:56.750725Z)
- `NDF|TOTAL|demand` = **18621** (n=66, 2026-09-16T05:17:05.545597Z)
- `TSDF|TOTAL|demand` = **19121** (n=66, 2026-09-16T05:17:05.545597Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T05:34:19.405052Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:33:45Z`
- `2026-09-16T05:32:12.772966Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:31:45Z`
- `2026-09-16T05:30:53.425120Z` — **WINDFOR**: 73 rows; marker `2026-09-16T05:30:00Z`
- `2026-09-16T05:30:53.425120Z` — **FUELHH**: 20 rows; marker `2026-09-16T05:30:00Z`
- `2026-09-16T05:30:37.364241Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:30:00Z`
- `2026-09-16T05:30:09.853412Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:29:45Z`
- `2026-09-16T05:28:18.472972Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:27:45Z`
- `2026-09-16T05:26:25.832104Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:25:45Z`
- `2026-09-16T05:25:57.781576Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:25:00Z`
- `2026-09-16T05:24:06.295646Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:23:45Z`
- `2026-09-16T05:22:14.606139Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:21:45Z`
- `2026-09-16T05:20:33.093664Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:20:00Z`
- `2026-09-16T05:20:17.305963Z` — **INDDEM**: 810 rows; marker `2026-09-16T05:16:00Z`
- `2026-09-16T05:20:17.305963Z` — **IMBALNGC**: 810 rows; marker `2026-09-16T05:16:00Z`
- `2026-09-16T05:20:17.305963Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:19:45Z`
