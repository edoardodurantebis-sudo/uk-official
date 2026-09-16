# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T05:09:27.240919Z`  
Current process started UTC: `2026-09-16T05:05:26.962816Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1394** (n=386, 2026-09-16T05:05:29.963115Z)
- `FUELINST|fuelType=NPSHYD|generation` = **505** (n=386, 2026-09-16T05:05:29.963115Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=386, 2026-09-16T05:05:29.963115Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=386, 2026-09-16T05:05:29.963115Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=386, 2026-09-16T05:05:29.963115Z)
- `FUELINST|fuelType=OTHER|generation` = **473** (n=386, 2026-09-16T05:05:29.963115Z)
- `FUELINST|fuelType=PS|generation` = **-37** (n=386, 2026-09-16T05:05:29.963115Z)
- `FUELINST|fuelType=WIND|generation` = **9324** (n=386, 2026-09-16T05:05:29.963115Z)
- `IMBALNGC|TOTAL|imbalance` = **7203** (n=64, 2026-09-16T04:50:19.267417Z)
- `INDDEM|TOTAL|demand` = **-12179** (n=64, 2026-09-16T04:50:03.921403Z)
- `INDGEN|TOTAL|generation` = **26324** (n=64, 2026-09-16T04:50:03.921403Z)
- `MELNGC|TOTAL|margin` = **37521** (n=64, 2026-09-16T04:49:14.608454Z)
- `NDF|TOTAL|demand` = **18621** (n=65, 2026-09-16T04:47:23.268822Z)
- `TSDF|TOTAL|demand` = **19121** (n=65, 2026-09-16T04:47:23.268822Z)
- `WINDFOR|TOTAL|generation` = **18849** (n=10, 2026-09-16T03:30:50.299289Z)

## Latest publication events

- `2026-09-16T05:08:26.690909Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:07:45Z`
- `2026-09-16T05:06:18.302867Z` — **MID**: 0 rows; marker `2026-09-16T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T05:06:18.302867Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:05:45Z`
- `2026-09-16T05:05:29.963115Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:05:00Z`
- `2026-09-16T05:04:26.514317Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:03:45Z`
- `2026-09-16T05:02:17.795695Z` — **FREQ**: 5761 rows; marker `2026-09-16T05:01:45Z`
- `2026-09-16T05:00:32.280949Z` — **FUELHH**: 20 rows; marker `2026-09-16T05:00:00Z`
- `2026-09-16T05:00:32.280949Z` — **FUELINST**: 80 rows; marker `2026-09-16T05:00:00Z`
- `2026-09-16T05:00:16.742518Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:59:45Z`
- `2026-09-16T04:58:25.791144Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:57:45Z`
- `2026-09-16T04:56:18.023272Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:55:45Z`
- `2026-09-16T04:55:30.054339Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:55:00Z`
- `2026-09-16T04:54:25.735534Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:53:45Z`
- `2026-09-16T04:52:11.077805Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:51:45Z`
- `2026-09-16T04:50:34.838750Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:50:00Z`
