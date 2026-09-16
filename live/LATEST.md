# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T07:06:38.420297Z`  
Current process started UTC: `2026-09-16T07:02:38.310205Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **976** (n=410, 2026-09-16T07:05:23.063380Z)
- `FUELINST|fuelType=NPSHYD|generation` = **484** (n=410, 2026-09-16T07:05:23.063380Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=410, 2026-09-16T07:05:23.063380Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=410, 2026-09-16T07:05:23.063380Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=410, 2026-09-16T07:05:23.063380Z)
- `FUELINST|fuelType=OTHER|generation` = **724** (n=410, 2026-09-16T07:05:23.063380Z)
- `FUELINST|fuelType=PS|generation` = **222** (n=410, 2026-09-16T07:05:23.063380Z)
- `FUELINST|fuelType=WIND|generation` = **8058** (n=410, 2026-09-16T07:05:23.063380Z)
- `IMBALNGC|TOTAL|imbalance` = **7314** (n=68, 2026-09-16T06:50:07.907292Z)
- `INDDEM|TOTAL|demand` = **-12469** (n=68, 2026-09-16T06:50:07.907292Z)
- `INDGEN|TOTAL|generation` = **26435** (n=68, 2026-09-16T06:50:07.907292Z)
- `MELNGC|TOTAL|margin` = **37402** (n=68, 2026-09-16T06:48:52.438403Z)
- `NDF|TOTAL|demand` = **18621** (n=69, 2026-09-16T06:46:59.687571Z)
- `TSDF|TOTAL|demand` = **19121** (n=69, 2026-09-16T06:46:59.687571Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T07:06:27.289503Z` — **MID**: 0 rows; marker `2026-09-16T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T07:06:27.289503Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:05:45Z`
- `2026-09-16T07:05:23.063380Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:05:00Z`
- `2026-09-16T07:04:19.594620Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:03:45Z`
- `2026-09-16T07:02:25.961264Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:01:45Z`
- `2026-09-16T07:00:35.540024Z` — **FUELHH**: 20 rows; marker `2026-09-16T07:00:00Z`
- `2026-09-16T07:00:35.540024Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:00:00Z`
- `2026-09-16T07:00:19.976972Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:59:45Z`
- `2026-09-16T06:58:28.316418Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:57:45Z`
- `2026-09-16T06:56:15.598407Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:55:45Z`
- `2026-09-16T06:55:43.575577Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:55:00Z`
- `2026-09-16T06:54:23.927879Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:53:45Z`
- `2026-09-16T06:52:15.637490Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:51:45Z`
- `2026-09-16T06:50:39.929765Z` — **FUELINST**: 80 rows; marker `2026-09-16T06:50:00Z`
- `2026-09-16T06:50:23.794156Z` — **FREQ**: 5761 rows; marker `2026-09-16T06:49:45Z`
