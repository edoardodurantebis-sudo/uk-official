# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T02:42:43.323633Z`  
Current process started UTC: `2026-09-16T02:38:42.713879Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-681** (n=357, 2026-09-16T02:40:34.738661Z)
- `FUELINST|fuelType=NPSHYD|generation` = **397** (n=357, 2026-09-16T02:40:34.738661Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=357, 2026-09-16T02:40:34.738661Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=357, 2026-09-16T02:40:34.738661Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=357, 2026-09-16T02:40:34.738661Z)
- `FUELINST|fuelType=OTHER|generation` = **83** (n=357, 2026-09-16T02:40:34.738661Z)
- `FUELINST|fuelType=PS|generation` = **107** (n=357, 2026-09-16T02:40:34.738661Z)
- `FUELINST|fuelType=WIND|generation` = **10149** (n=357, 2026-09-16T02:40:34.738661Z)
- `IMBALNGC|TOTAL|imbalance` = **6007** (n=59, 2026-09-16T02:20:26.284629Z)
- `INDDEM|TOTAL|demand` = **-12203** (n=59, 2026-09-16T02:20:26.284629Z)
- `INDGEN|TOTAL|generation` = **25128** (n=59, 2026-09-16T02:20:26.284629Z)
- `MELNGC|TOTAL|margin` = **37539** (n=59, 2026-09-16T02:19:06.362522Z)
- `NDF|TOTAL|demand` = **18621** (n=60, 2026-09-16T02:17:14.647012Z)
- `TSDF|TOTAL|demand` = **19121** (n=60, 2026-09-16T02:17:14.647012Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-16T02:42:10.510131Z` — **MID**: 0 rows; marker `2026-09-16T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T02:42:10.510131Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:41:45Z`
- `2026-09-16T02:40:34.738661Z` — **FUELINST**: 80 rows; marker `2026-09-16T02:40:00Z`
- `2026-09-16T02:40:18.725258Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:39:45Z`
- `2026-09-16T02:38:14.330797Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:37:45Z`
- `2026-09-16T02:36:22.316056Z` — **MID**: 0 rows; marker `2026-09-16T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T02:36:22.316056Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:35:45Z`
- `2026-09-16T02:35:34.916516Z` — **FUELINST**: 80 rows; marker `2026-09-16T02:35:00Z`
- `2026-09-16T02:34:15.411707Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:33:45Z`
- `2026-09-16T02:32:23.934658Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:31:45Z`
- `2026-09-16T02:30:33.597983Z` — **FUELHH**: 20 rows; marker `2026-09-16T02:30:00Z`
- `2026-09-16T02:30:33.597983Z` — **FUELINST**: 80 rows; marker `2026-09-16T02:30:00Z`
- `2026-09-16T02:30:18.134780Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:29:45Z`
- `2026-09-16T02:28:18.623219Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:27:45Z`
- `2026-09-16T02:26:10.299898Z` — **FREQ**: 5761 rows; marker `2026-09-16T02:25:45Z`
