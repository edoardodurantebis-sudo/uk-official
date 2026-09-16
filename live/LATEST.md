# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T01:43:22.046624Z`  
Current process started UTC: `2026-09-16T01:39:22.545572Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.86 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.90 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.94 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.97 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.01 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.05 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.10 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.14 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.19 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.23 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.28 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.33 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.38 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.44 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-4.49 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=345, 2026-09-16T01:40:30.059893Z)
- `FUELINST|fuelType=NPSHYD|generation` = **390** (n=345, 2026-09-16T01:40:30.059893Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=345, 2026-09-16T01:40:30.059893Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=345, 2026-09-16T01:40:30.059893Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=345, 2026-09-16T01:40:30.059893Z)
- `FUELINST|fuelType=OTHER|generation` = **134** (n=345, 2026-09-16T01:40:30.059893Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=345, 2026-09-16T01:40:30.059893Z)
- `FUELINST|fuelType=WIND|generation` = **10316** (n=345, 2026-09-16T01:40:30.059893Z)
- `IMBALNGC|TOTAL|imbalance` = **5960** (n=57, 2026-09-16T01:20:52.553654Z)
- `INDDEM|TOTAL|demand` = **-12159** (n=57, 2026-09-16T01:20:36.827610Z)
- `INDGEN|TOTAL|generation` = **25081** (n=57, 2026-09-16T01:20:52.553654Z)
- `MELNGC|TOTAL|margin` = **36035** (n=57, 2026-09-16T01:19:00.164721Z)
- `NDF|TOTAL|demand` = **18621** (n=58, 2026-09-16T01:17:30.926411Z)
- `TSDF|TOTAL|demand` = **19121** (n=58, 2026-09-16T01:17:46.933048Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T01:42:21.590746Z` — **MID**: 0 rows; marker `2026-09-16T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T01:42:21.590746Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:41:45Z`
- `2026-09-16T01:40:30.059893Z` — **FUELINST**: 80 rows; marker `2026-09-16T01:40:00Z`
- `2026-09-16T01:40:14.552036Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:39:45Z`
- `2026-09-16T01:38:22.562348Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:37:45Z`
- `2026-09-16T01:37:18.897141Z` — **MID**: 0 rows; marker `2026-09-16T01:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T01:36:14.937910Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:35:45Z`
- `2026-09-16T01:35:27.618676Z` — **FUELINST**: 80 rows; marker `2026-09-16T01:35:00Z`
- `2026-09-16T01:34:13.666470Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:33:45Z`
- `2026-09-16T01:32:21.459676Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:31:45Z`
- `2026-09-16T01:30:38.305885Z` — **FUELHH**: 20 rows; marker `2026-09-16T01:30:00Z`
- `2026-09-16T01:30:38.305885Z` — **FUELINST**: 80 rows; marker `2026-09-16T01:30:00Z`
- `2026-09-16T01:30:22.774567Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:29:45Z`
- `2026-09-16T01:28:14.983711Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:27:45Z`
- `2026-09-16T01:26:22.944531Z` — **FREQ**: 5761 rows; marker `2026-09-16T01:25:45Z`
