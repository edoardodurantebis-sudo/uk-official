# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T07:52:42.627437Z`  
Current process started UTC: `2026-09-16T07:48:42.730582Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1374** (n=419, 2026-09-16T07:50:34.744304Z)
- `FUELINST|fuelType=NPSHYD|generation` = **428** (n=419, 2026-09-16T07:50:34.744304Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=419, 2026-09-16T07:50:34.744304Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=419, 2026-09-16T07:50:34.744304Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=419, 2026-09-16T07:50:34.744304Z)
- `FUELINST|fuelType=OTHER|generation` = **357** (n=419, 2026-09-16T07:50:34.744304Z)
- `FUELINST|fuelType=PS|generation` = **229** (n=419, 2026-09-16T07:50:34.744304Z)
- `FUELINST|fuelType=WIND|generation` = **7449** (n=419, 2026-09-16T07:50:34.744304Z)
- `IMBALNGC|TOTAL|imbalance` = **6872** (n=69, 2026-09-16T07:20:10.341890Z)
- `INDDEM|TOTAL|demand` = **-12664** (n=69, 2026-09-16T07:19:53.371027Z)
- `INDGEN|TOTAL|generation` = **26437** (n=69, 2026-09-16T07:19:53.371027Z)
- `MELNGC|TOTAL|margin` = **36325** (n=69, 2026-09-16T07:18:39.087802Z)
- `NDF|TOTAL|demand` = **19870** (n=71, 2026-09-16T07:45:55.070573Z)
- `TSDF|TOTAL|demand` = **20370** (n=71, 2026-09-16T07:45:55.070573Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T07:52:27.413590Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:51:45Z`
- `2026-09-16T07:50:34.744304Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:50:00Z`
- `2026-09-16T07:50:34.744304Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:49:45Z`
- `2026-09-16T07:48:20.166081Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:47:45Z`
- `2026-09-16T07:46:27.188779Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:45:45Z`
- `2026-09-16T07:45:55.070573Z` — **TSDF**: 864 rows; marker `2026-09-16T07:45:00Z`
- `2026-09-16T07:45:55.070573Z` — **NDF**: 48 rows; marker `2026-09-16T07:45:00Z`
- `2026-09-16T07:45:39.729502Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:45:00Z`
- `2026-09-16T07:44:35.774459Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:43:45Z`
- `2026-09-16T07:42:27.802190Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:41:45Z`
- `2026-09-16T07:42:11.846517Z` — **MID**: 0 rows; marker `2026-09-16T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T07:40:36.344510Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:40:00Z`
- `2026-09-16T07:40:20.275632Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:39:45Z`
- `2026-09-16T07:38:16.503413Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:37:45Z`
- `2026-09-16T07:36:24.344669Z` — **MID**: 0 rows; marker `2026-09-16T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
