# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T06:08:05.861539Z`  
Current process started UTC: `2026-09-16T06:04:04.591288Z`  
1-second metadata polls in this process: **236**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-382** (n=398, 2026-09-16T06:05:39.835345Z)
- `FUELINST|fuelType=NPSHYD|generation` = **527** (n=398, 2026-09-16T06:05:39.835345Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=398, 2026-09-16T06:05:39.835345Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=398, 2026-09-16T06:05:39.835345Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=398, 2026-09-16T06:05:39.835345Z)
- `FUELINST|fuelType=OTHER|generation` = **1489** (n=398, 2026-09-16T06:05:39.835345Z)
- `FUELINST|fuelType=PS|generation` = **215** (n=398, 2026-09-16T06:05:39.835345Z)
- `FUELINST|fuelType=WIND|generation` = **7826** (n=398, 2026-09-16T06:05:39.835345Z)
- `IMBALNGC|TOTAL|imbalance` = **7214** (n=66, 2026-09-16T05:49:58.262916Z)
- `INDDEM|TOTAL|demand` = **-12220** (n=66, 2026-09-16T05:49:58.262916Z)
- `INDGEN|TOTAL|generation` = **26335** (n=66, 2026-09-16T05:49:58.262916Z)
- `MELNGC|TOTAL|margin` = **37526** (n=66, 2026-09-16T05:48:54.238626Z)
- `NDF|TOTAL|demand` = **18621** (n=67, 2026-09-16T05:46:57.992598Z)
- `TSDF|TOTAL|demand` = **19121** (n=67, 2026-09-16T05:46:57.992598Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T06:08:03.421430Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:07:45Z`
- `2026-09-16T06:06:27.556779Z` — **MID**: 0 rows; marker `2026-09-16T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T06:06:11.340250Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:05:45Z`
- `2026-09-16T06:05:39.835345Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:05:00Z`
- `2026-09-16T06:04:20.640803Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:03:45Z`
- `2026-09-16T06:02:19.350923Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:01:45Z`
- `2026-09-16T06:00:43.027624Z` — **FUELHH**: 20 rows; marker `2026-09-16T06:00:00Z`
- `2026-09-16T06:00:43.027624Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:00:00Z`
- `2026-09-16T06:00:27.265492Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:59:45Z`
- `2026-09-16T05:58:19.923262Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:57:45Z`
- `2026-09-16T05:56:28.112616Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:55:45Z`
- `2026-09-16T05:55:40.724179Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:55:00Z`
- `2026-09-16T05:54:14.634508Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:53:45Z`
- `2026-09-16T05:52:22.989231Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:51:45Z`
- `2026-09-16T05:50:30.944136Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:50:00Z`
