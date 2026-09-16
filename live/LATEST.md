# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T00:48:45.620668Z`  
Current process started UTC: `2026-09-16T00:44:45.694524Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.47 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.58 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.69 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.81 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-5.94 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.07 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.22 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.37 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.54 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.72 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-6.92 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-7.14 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-7.37 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-7.64 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-7.93 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **65** (n=334, 2026-09-16T00:45:49.916752Z)
- `FUELINST|fuelType=NPSHYD|generation` = **394** (n=334, 2026-09-16T00:45:49.916752Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=334, 2026-09-16T00:45:49.916752Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=334, 2026-09-16T00:45:49.916752Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=334, 2026-09-16T00:45:49.916752Z)
- `FUELINST|fuelType=OTHER|generation` = **170** (n=334, 2026-09-16T00:45:49.916752Z)
- `FUELINST|fuelType=PS|generation` = **392** (n=334, 2026-09-16T00:45:49.916752Z)
- `FUELINST|fuelType=WIND|generation` = **10967** (n=334, 2026-09-16T00:45:49.916752Z)
- `IMBALNGC|TOTAL|imbalance` = **6035** (n=55, 2026-09-16T00:20:47.111437Z)
- `INDDEM|TOTAL|demand` = **-12095** (n=55, 2026-09-16T00:20:30.888031Z)
- `INDGEN|TOTAL|generation` = **25156** (n=55, 2026-09-16T00:20:30.888031Z)
- `MELNGC|TOTAL|margin` = **35662** (n=55, 2026-09-16T00:19:43.131683Z)
- `NDF|TOTAL|demand` = **18621** (n=57, 2026-09-16T00:47:26.234067Z)
- `TSDF|TOTAL|demand` = **19121** (n=57, 2026-09-16T00:47:26.234067Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T00:48:13.882929Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:47:45Z`
- `2026-09-16T00:47:26.234067Z` — **TSDF**: 972 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:47:26.234067Z` — **NDF**: 54 rows; marker `2026-09-16T00:47:00Z`
- `2026-09-16T00:46:22.004745Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:45:45Z`
- `2026-09-16T00:45:49.916752Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:45:00Z`
- `2026-09-16T00:44:06.649565Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:43:45Z`
- `2026-09-16T00:42:15.008440Z` — **MID**: 0 rows; marker `2026-09-16T00:42:05Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T00:42:15.008440Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:41:45Z`
- `2026-09-16T00:40:23.613072Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:40:00Z`
- `2026-09-16T00:40:08.170756Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:39:45Z`
- `2026-09-16T00:38:16.161996Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:37:45Z`
- `2026-09-16T00:36:24.923901Z` — **MID**: 0 rows; marker `2026-09-16T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T00:36:04.852429Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:35:45Z`
- `2026-09-16T00:35:48.567057Z` — **FUELINST**: 80 rows; marker `2026-09-16T00:35:00Z`
- `2026-09-16T00:34:13.002185Z` — **FREQ**: 5761 rows; marker `2026-09-16T00:33:45Z`
