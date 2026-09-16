# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T01:22:27.621697Z`  
Current process started UTC: `2026-09-16T01:18:27.960505Z`  
1-second metadata polls in this process: **227**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.28 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.33 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.38 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.44 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.49 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.55 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.61 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.67 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.74 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.80 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.87 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.95 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.02 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.11 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.19 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=341, 2026-09-16T01:20:36.827610Z)
- `FUELINST|fuelType=NPSHYD|generation` = **390** (n=341, 2026-09-16T01:20:36.827610Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=341, 2026-09-16T01:20:36.827610Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=341, 2026-09-16T01:20:36.827610Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=341, 2026-09-16T01:20:36.827610Z)
- `FUELINST|fuelType=OTHER|generation` = **173** (n=341, 2026-09-16T01:20:36.827610Z)
- `FUELINST|fuelType=PS|generation` = **224** (n=341, 2026-09-16T01:20:36.827610Z)
- `FUELINST|fuelType=WIND|generation` = **10361** (n=341, 2026-09-16T01:20:36.827610Z)
- `IMBALNGC|TOTAL|imbalance` = **5960** (n=57, 2026-09-16T01:20:52.553654Z)
- `INDDEM|TOTAL|demand` = **-12159** (n=57, 2026-09-16T01:20:36.827610Z)
- `INDGEN|TOTAL|generation` = **25081** (n=57, 2026-09-16T01:20:52.553654Z)
- `MELNGC|TOTAL|margin` = **36035** (n=57, 2026-09-16T01:19:00.164721Z)
- `NDF|TOTAL|demand` = **18621** (n=58, 2026-09-16T01:17:30.926411Z)
- `TSDF|TOTAL|demand` = **19121** (n=58, 2026-09-16T01:17:46.933048Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T01:22:12.580881Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:21:45Z`
- `2026-09-16T01:20:52.553654Z` — **INDGEN**: 954 rows; marker `2026-09-16T01:17:00Z`
- `2026-09-16T01:20:52.553654Z` — **IMBALNGC**: 954 rows; marker `2026-09-16T01:17:00Z`
- `2026-09-16T01:20:36.827610Z` — **INDDEM**: 954 rows; marker `2026-09-16T01:17:00Z`
- `2026-09-16T01:20:36.827610Z` — **FUELINST**: 80 rows; marker `2026-09-16T01:20:00Z`
- `2026-09-16T01:20:04.982596Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:19:45Z`
- `2026-09-16T01:19:00.164721Z` — **MELNGC**: 954 rows; marker `2026-09-16T01:17:00Z`
- `2026-09-16T01:18:27.960514Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:17:45Z`
- `2026-09-16T01:17:46.933048Z` — **TSDF**: 954 rows; marker `2026-09-16T01:17:00Z`
- `2026-09-16T01:17:30.926411Z` — **NDF**: 53 rows; marker `2026-09-16T01:17:00Z`
- `2026-09-16T01:16:11.501269Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:15:45Z`
- `2026-09-16T01:15:39.497078Z` — **FUELINST**: 80 rows; marker `2026-09-16T01:15:00Z`
- `2026-09-16T01:14:03.778500Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:13:45Z`
- `2026-09-16T01:12:12.689506Z` — **MID**: 0 rows; marker `2026-09-16T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T01:12:12.689506Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:11:45Z`
