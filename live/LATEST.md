# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T07:15:00.753565Z`  
Current process started UTC: `2026-09-16T07:11:00.629831Z`  
1-second metadata polls in this process: **230**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1331** (n=411, 2026-09-16T07:10:32.774725Z)
- `FUELINST|fuelType=NPSHYD|generation` = **482** (n=411, 2026-09-16T07:10:32.774725Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=411, 2026-09-16T07:10:32.774725Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=411, 2026-09-16T07:10:32.774725Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=411, 2026-09-16T07:10:32.774725Z)
- `FUELINST|fuelType=OTHER|generation` = **444** (n=411, 2026-09-16T07:10:32.774725Z)
- `FUELINST|fuelType=PS|generation` = **222** (n=411, 2026-09-16T07:10:32.774725Z)
- `FUELINST|fuelType=WIND|generation` = **8103** (n=411, 2026-09-16T07:10:32.774725Z)
- `IMBALNGC|TOTAL|imbalance` = **7314** (n=68, 2026-09-16T06:50:07.907292Z)
- `INDDEM|TOTAL|demand` = **-12469** (n=68, 2026-09-16T06:50:07.907292Z)
- `INDGEN|TOTAL|generation` = **26435** (n=68, 2026-09-16T06:50:07.907292Z)
- `MELNGC|TOTAL|margin` = **37402** (n=68, 2026-09-16T06:48:52.438403Z)
- `NDF|TOTAL|demand` = **18621** (n=69, 2026-09-16T06:46:59.687571Z)
- `TSDF|TOTAL|demand` = **19121** (n=69, 2026-09-16T06:46:59.687571Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T07:14:15.143194Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:13:45Z`
- `2026-09-16T07:12:21.223252Z` — **MID**: 0 rows; marker `2026-09-16T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T07:12:21.223252Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:11:45Z`
- `2026-09-16T07:10:32.774725Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:10:00Z`
- `2026-09-16T07:10:32.774725Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:09:45Z`
- `2026-09-16T07:08:24.960768Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:07:45Z`
- `2026-09-16T07:06:27.289503Z` — **MID**: 0 rows; marker `2026-09-16T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T07:06:27.289503Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:05:45Z`
- `2026-09-16T07:05:23.063380Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:05:00Z`
- `2026-09-16T07:04:19.594620Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:03:45Z`
- `2026-09-16T07:02:25.961264Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:01:45Z`
- `2026-09-16T07:00:35.540024Z` — **FUELHH**: 20 rows; marker `2026-09-16T07:00:00Z`
- `2026-09-16T07:00:35.540024Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:00:00Z`
- `2026-09-16T07:00:19.976972Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:59:45Z`
- `2026-09-16T06:58:28.316418Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:57:45Z`
