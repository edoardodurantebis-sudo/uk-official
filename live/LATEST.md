# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T02:51:04.823371Z`  
Current process started UTC: `2026-09-16T02:47:04.086306Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-681** (n=359, 2026-09-16T02:50:30.651273Z)
- `FUELINST|fuelType=NPSHYD|generation` = **398** (n=359, 2026-09-16T02:50:30.651273Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=359, 2026-09-16T02:50:30.651273Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=359, 2026-09-16T02:50:30.651273Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=359, 2026-09-16T02:50:30.651273Z)
- `FUELINST|fuelType=OTHER|generation` = **83** (n=359, 2026-09-16T02:50:30.651273Z)
- `FUELINST|fuelType=PS|generation` = **106** (n=359, 2026-09-16T02:50:30.651273Z)
- `FUELINST|fuelType=WIND|generation` = **9897** (n=359, 2026-09-16T02:50:30.651273Z)
- `IMBALNGC|TOTAL|imbalance` = **6027** (n=60, 2026-09-16T02:51:02.679902Z)
- `INDDEM|TOTAL|demand` = **-12203** (n=59, 2026-09-16T02:20:26.284629Z)
- `INDGEN|TOTAL|generation` = **25148** (n=60, 2026-09-16T02:51:02.679902Z)
- `MELNGC|TOTAL|margin` = **37540** (n=60, 2026-09-16T02:48:55.534436Z)
- `NDF|TOTAL|demand` = **18621** (n=61, 2026-09-16T02:47:20.255278Z)
- `TSDF|TOTAL|demand` = **19121** (n=61, 2026-09-16T02:47:20.255278Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T02:51:02.679902Z` — **INDGEN**: 900 rows; marker `2026-09-16T02:46:00Z`
- `2026-09-16T02:51:02.679902Z` — **IMBALNGC**: 900 rows; marker `2026-09-16T02:47:00Z`
- `2026-09-16T02:50:30.651273Z` — **FUELINST**: 80 rows; marker `2026-09-16T02:50:00Z`
- `2026-09-16T02:50:15.093058Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:49:45Z`
- `2026-09-16T02:48:55.534436Z` — **MELNGC**: 900 rows; marker `2026-09-16T02:47:00Z`
- `2026-09-16T02:48:07.998099Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:47:45Z`
- `2026-09-16T02:47:20.255278Z` — **TSDF**: 900 rows; marker `2026-09-16T02:47:00Z`
- `2026-09-16T02:47:20.255278Z` — **NDF**: 50 rows; marker `2026-09-16T02:47:00Z`
- `2026-09-16T02:46:10.830175Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:45:45Z`
- `2026-09-16T02:45:38.551209Z` — **FUELINST**: 80 rows; marker `2026-09-16T02:45:00Z`
- `2026-09-16T02:44:02.801330Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:43:45Z`
- `2026-09-16T02:42:10.510131Z` — **MID**: 0 rows; marker `2026-09-16T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T02:42:10.510131Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:41:45Z`
- `2026-09-16T02:40:34.738661Z` — **FUELINST**: 80 rows; marker `2026-09-16T02:40:00Z`
- `2026-09-16T02:40:18.725258Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:39:45Z`
