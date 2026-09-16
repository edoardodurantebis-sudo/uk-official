# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T09:14:03.441290Z`  
Current process started UTC: `2026-09-16T09:10:03.006076Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.27 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1404** (n=435, 2026-09-16T09:10:36.723337Z)
- `FUELINST|fuelType=NPSHYD|generation` = **357** (n=435, 2026-09-16T09:10:36.723337Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=435, 2026-09-16T09:10:36.723337Z)
- `FUELINST|fuelType=OCGT|generation` = **1** (n=435, 2026-09-16T09:10:36.723337Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=435, 2026-09-16T09:10:36.723337Z)
- `FUELINST|fuelType=OTHER|generation` = **500** (n=435, 2026-09-16T09:10:36.723337Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=435, 2026-09-16T09:10:36.723337Z)
- `FUELINST|fuelType=WIND|generation` = **6265** (n=435, 2026-09-16T09:10:36.723337Z)
- `IMBALNGC|TOTAL|imbalance` = **6705** (n=71, 2026-09-16T08:49:32.469051Z)
- `INDDEM|TOTAL|demand` = **-12681** (n=71, 2026-09-16T08:49:32.469051Z)
- `INDGEN|TOTAL|generation` = **26163** (n=71, 2026-09-16T08:49:32.469051Z)
- `MELNGC|TOTAL|margin` = **35745** (n=71, 2026-09-16T08:49:00.683932Z)
- `NDF|TOTAL|demand` = **18514** (n=73, 2026-09-16T08:47:08.665911Z)
- `TSDF|TOTAL|demand` = **19458** (n=73, 2026-09-16T08:47:08.665911Z)
- `WINDFOR|TOTAL|generation` = **19327** (n=12, 2026-09-16T08:30:33.621364Z)

## Latest publication events

- `2026-09-16T09:12:14.287594Z` — **MID**: 0 rows; marker `2026-09-16T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T09:12:14.287594Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:11:45Z`
- `2026-09-16T09:10:36.723337Z` — **FUELINST**: 80 rows; marker `2026-09-16T09:10:00Z`
- `2026-09-16T09:10:21.007964Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:09:45Z`
- `2026-09-16T09:08:30.143053Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:07:45Z`
- `2026-09-16T09:07:25.808629Z` — **MID**: 0 rows; marker `2026-09-16T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T09:06:06.298997Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:05:45Z`
- `2026-09-16T09:05:50.127528Z` — **FUELINST**: 80 rows; marker `2026-09-16T09:05:00Z`
- `2026-09-16T09:04:14.557533Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:03:45Z`
- `2026-09-16T09:02:22.322782Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:01:45Z`
- `2026-09-16T09:00:36.686885Z` — **FUELHH**: 20 rows; marker `2026-09-16T09:00:00Z`
- `2026-09-16T09:00:20.541587Z` — **FUELINST**: 80 rows; marker `2026-09-16T09:00:00Z`
- `2026-09-16T09:00:20.541587Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:59:45Z`
- `2026-09-16T08:58:10.656159Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:57:45Z`
- `2026-09-16T08:56:06.698327Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:55:45Z`
