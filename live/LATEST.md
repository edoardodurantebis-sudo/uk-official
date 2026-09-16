# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T03:37:08.881419Z`  
Current process started UTC: `2026-09-16T03:33:08.839904Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-714** (n=368, 2026-09-16T03:35:54.877424Z)
- `FUELINST|fuelType=NPSHYD|generation` = **398** (n=368, 2026-09-16T03:35:54.877424Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=368, 2026-09-16T03:35:54.877424Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=368, 2026-09-16T03:35:54.877424Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=368, 2026-09-16T03:35:54.877424Z)
- `FUELINST|fuelType=OTHER|generation` = **133** (n=368, 2026-09-16T03:35:54.877424Z)
- `FUELINST|fuelType=PS|generation` = **213** (n=368, 2026-09-16T03:35:54.877424Z)
- `FUELINST|fuelType=WIND|generation` = **9648** (n=368, 2026-09-16T03:35:54.877424Z)
- `IMBALNGC|TOTAL|imbalance` = **6025** (n=61, 2026-09-16T03:20:52.622308Z)
- `INDDEM|TOTAL|demand` = **-12207** (n=61, 2026-09-16T03:20:52.622308Z)
- `INDGEN|TOTAL|generation` = **25146** (n=61, 2026-09-16T03:20:52.622308Z)
- `MELNGC|TOTAL|margin` = **37540** (n=61, 2026-09-16T03:19:06.803098Z)
- `NDF|TOTAL|demand` = **18621** (n=62, 2026-09-16T03:17:30.975101Z)
- `TSDF|TOTAL|demand` = **19121** (n=62, 2026-09-16T03:17:30.975101Z)
- `WINDFOR|TOTAL|generation` = **18849** (n=10, 2026-09-16T03:30:50.299289Z)

## Latest publication events

- `2026-09-16T03:36:26.742777Z` — **MID**: 0 rows; marker `2026-09-16T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T03:36:11.027276Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:35:45Z`
- `2026-09-16T03:35:54.877424Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:35:00Z`
- `2026-09-16T03:34:17.847432Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:33:45Z`
- `2026-09-16T03:32:41.952080Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:31:45Z`
- `2026-09-16T03:30:50.299289Z` — **WINDFOR**: 73 rows; marker `2026-09-16T03:30:00Z`
- `2026-09-16T03:30:50.299289Z` — **FUELHH**: 20 rows; marker `2026-09-16T03:30:00Z`
- `2026-09-16T03:30:19.001467Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:30:00Z`
- `2026-09-16T03:30:03.048058Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:29:45Z`
- `2026-09-16T03:28:03.634717Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:27:45Z`
- `2026-09-16T03:26:11.223710Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:25:45Z`
- `2026-09-16T03:25:39.208053Z` — **FUELINST**: 80 rows; marker `2026-09-16T03:25:00Z`
- `2026-09-16T03:24:04.191033Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:23:45Z`
- `2026-09-16T03:22:28.685225Z` — **FREQ**: 5761 rows; marker `2026-09-16T03:21:45Z`
- `2026-09-16T03:20:52.622308Z` — **INDGEN**: 882 rows; marker `2026-09-16T03:17:00Z`
