# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T06:49:55.431946Z`  
Current process started UTC: `2026-09-16T06:45:55.618557Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=INTVKL|generation` = **156** (n=406, 2026-09-16T06:45:33.332082Z)
- `FUELINST|fuelType=NPSHYD|generation` = **544** (n=406, 2026-09-16T06:45:33.332082Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=406, 2026-09-16T06:45:33.332082Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=406, 2026-09-16T06:45:33.332082Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=406, 2026-09-16T06:45:33.332082Z)
- `FUELINST|fuelType=OTHER|generation` = **1802** (n=406, 2026-09-16T06:45:33.332082Z)
- `FUELINST|fuelType=PS|generation` = **222** (n=406, 2026-09-16T06:45:33.332082Z)
- `FUELINST|fuelType=WIND|generation` = **7549** (n=406, 2026-09-16T06:45:33.332082Z)
- `IMBALNGC|TOTAL|imbalance` = **7190** (n=67, 2026-09-16T06:19:50.911181Z)
- `INDDEM|TOTAL|demand` = **-12220** (n=67, 2026-09-16T06:19:50.911181Z)
- `INDGEN|TOTAL|generation` = **26311** (n=67, 2026-09-16T06:19:50.911181Z)
- `MELNGC|TOTAL|margin` = **37402** (n=68, 2026-09-16T06:48:52.438403Z)
- `NDF|TOTAL|demand` = **18621** (n=69, 2026-09-16T06:46:59.687571Z)
- `TSDF|TOTAL|demand` = **19121** (n=69, 2026-09-16T06:46:59.687571Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T06:48:52.438403Z` — **MELNGC**: 756 rows; marker `2026-09-16T06:46:00Z`
- `2026-09-16T06:48:20.947158Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:47:45Z`
- `2026-09-16T06:46:59.687571Z` — **TSDF**: 756 rows; marker `2026-09-16T06:46:00Z`
- `2026-09-16T06:46:59.687571Z` — **NDF**: 42 rows; marker `2026-09-16T06:46:00Z`
- `2026-09-16T06:46:28.293378Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:45:45Z`
- `2026-09-16T06:45:33.332082Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:45:00Z`
- `2026-09-16T06:44:28.626893Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:43:45Z`
- `2026-09-16T06:42:20.995791Z` — **MID**: 0 rows; marker `2026-09-16T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T06:42:20.995791Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:41:45Z`
- `2026-09-16T06:40:28.429970Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:40:00Z`
- `2026-09-16T06:40:12.805776Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:39:45Z`
- `2026-09-16T06:38:21.222789Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:37:45Z`
- `2026-09-16T06:36:33.153586Z` — **MID**: 0 rows; marker `2026-09-16T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T06:36:17.584131Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:35:45Z`
- `2026-09-16T06:35:29.943839Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:35:00Z`
