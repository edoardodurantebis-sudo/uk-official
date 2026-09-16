# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T07:19:10.766723Z`  
Current process started UTC: `2026-09-16T07:15:11.079212Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **1371** (n=412, 2026-09-16T07:15:27.081230Z)
- `FUELINST|fuelType=NPSHYD|generation` = **482** (n=412, 2026-09-16T07:15:27.081230Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=412, 2026-09-16T07:15:27.081230Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=412, 2026-09-16T07:15:27.081230Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=412, 2026-09-16T07:15:27.081230Z)
- `FUELINST|fuelType=OTHER|generation` = **365** (n=412, 2026-09-16T07:15:27.081230Z)
- `FUELINST|fuelType=PS|generation` = **222** (n=412, 2026-09-16T07:15:27.081230Z)
- `FUELINST|fuelType=WIND|generation` = **8121** (n=412, 2026-09-16T07:15:27.081230Z)
- `IMBALNGC|TOTAL|imbalance` = **7314** (n=68, 2026-09-16T06:50:07.907292Z)
- `INDDEM|TOTAL|demand` = **-12469** (n=68, 2026-09-16T06:50:07.907292Z)
- `INDGEN|TOTAL|generation` = **26435** (n=68, 2026-09-16T06:50:07.907292Z)
- `MELNGC|TOTAL|margin` = **36325** (n=69, 2026-09-16T07:18:39.087802Z)
- `NDF|TOTAL|demand` = **18621** (n=70, 2026-09-16T07:17:19.600220Z)
- `TSDF|TOTAL|demand` = **19565** (n=70, 2026-09-16T07:17:19.600220Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T07:18:39.087802Z` — **MELNGC**: 738 rows; marker `2026-09-16T07:16:00Z`
- `2026-09-16T07:18:23.328572Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:17:45Z`
- `2026-09-16T07:17:19.600220Z` — **TSDF**: 738 rows; marker `2026-09-16T07:16:00Z`
- `2026-09-16T07:17:19.600220Z` — **NDF**: 41 rows; marker `2026-09-16T07:16:00Z`
- `2026-09-16T07:16:32.072579Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:15:45Z`
- `2026-09-16T07:15:27.081230Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:15:00Z`
- `2026-09-16T07:14:15.143194Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:13:45Z`
- `2026-09-16T07:12:21.223252Z` — **MID**: 0 rows; marker `2026-09-16T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T07:12:21.223252Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:11:45Z`
- `2026-09-16T07:10:32.774725Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:10:00Z`
- `2026-09-16T07:10:32.774725Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:09:45Z`
- `2026-09-16T07:08:24.960768Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:07:45Z`
- `2026-09-16T07:06:27.289503Z` — **MID**: 0 rows; marker `2026-09-16T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T07:06:27.289503Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:05:45Z`
- `2026-09-16T07:05:23.063380Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:05:00Z`
