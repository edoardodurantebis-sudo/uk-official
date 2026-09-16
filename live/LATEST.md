# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T05:17:54.210957Z`  
Current process started UTC: `2026-09-16T05:13:54.399106Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1410** (n=388, 2026-09-16T05:15:45.926400Z)
- `FUELINST|fuelType=NPSHYD|generation` = **514** (n=388, 2026-09-16T05:15:45.926400Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=388, 2026-09-16T05:15:45.926400Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=388, 2026-09-16T05:15:45.926400Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=388, 2026-09-16T05:15:45.926400Z)
- `FUELINST|fuelType=OTHER|generation` = **803** (n=388, 2026-09-16T05:15:45.926400Z)
- `FUELINST|fuelType=PS|generation` = **223** (n=388, 2026-09-16T05:15:45.926400Z)
- `FUELINST|fuelType=WIND|generation` = **9149** (n=388, 2026-09-16T05:15:45.926400Z)
- `IMBALNGC|TOTAL|imbalance` = **7203** (n=64, 2026-09-16T04:50:19.267417Z)
- `INDDEM|TOTAL|demand` = **-12179** (n=64, 2026-09-16T04:50:03.921403Z)
- `INDGEN|TOTAL|generation` = **26324** (n=64, 2026-09-16T04:50:03.921403Z)
- `MELNGC|TOTAL|margin` = **37521** (n=64, 2026-09-16T04:49:14.608454Z)
- `NDF|TOTAL|demand` = **18621** (n=66, 2026-09-16T05:17:05.545597Z)
- `TSDF|TOTAL|demand` = **19121** (n=66, 2026-09-16T05:17:05.545597Z)
- `WINDFOR|TOTAL|generation` = **18849** (n=10, 2026-09-16T03:30:50.299289Z)

## Latest publication events

- `2026-09-16T05:17:05.545597Z` — **TSDF**: 810 rows; marker `2026-09-16T05:16:00Z`
- `2026-09-16T05:17:05.545597Z` — **NDF**: 45 rows; marker `2026-09-16T05:16:00Z`
- `2026-09-16T05:16:18.011153Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:15:45Z`
- `2026-09-16T05:15:45.926400Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:15:00Z`
- `2026-09-16T05:14:10.401063Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:13:45Z`
- `2026-09-16T05:12:08.428953Z` — **MID**: 0 rows; marker `2026-09-16T05:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T05:12:08.428953Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:11:45Z`
- `2026-09-16T05:10:48.334146Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:10:00Z`
- `2026-09-16T05:10:16.228378Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:09:45Z`
- `2026-09-16T05:08:26.690909Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:07:45Z`
- `2026-09-16T05:06:18.302867Z` — **MID**: 0 rows; marker `2026-09-16T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T05:06:18.302867Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:05:45Z`
- `2026-09-16T05:05:29.963115Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:05:00Z`
- `2026-09-16T05:04:26.514317Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:03:45Z`
- `2026-09-16T05:02:17.795695Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:01:45Z`
