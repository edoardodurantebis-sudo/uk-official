# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T08:44:00.474190Z`  
Current process started UTC: `2026-09-16T08:40:00.188555Z`  
1-second metadata polls in this process: **234**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=429, 2026-09-16T08:40:32.835984Z)
- `FUELINST|fuelType=NPSHYD|generation` = **391** (n=429, 2026-09-16T08:40:32.835984Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=429, 2026-09-16T08:40:32.835984Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=429, 2026-09-16T08:40:32.835984Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=429, 2026-09-16T08:40:32.835984Z)
- `FUELINST|fuelType=OTHER|generation` = **483** (n=429, 2026-09-16T08:40:32.835984Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=429, 2026-09-16T08:40:32.835984Z)
- `FUELINST|fuelType=WIND|generation` = **6576** (n=429, 2026-09-16T08:40:32.835984Z)
- `IMBALNGC|TOTAL|imbalance` = **7107** (n=70, 2026-09-16T08:20:33.253805Z)
- `INDDEM|TOTAL|demand` = **-12666** (n=70, 2026-09-16T08:20:17.283178Z)
- `INDGEN|TOTAL|generation` = **26560** (n=70, 2026-09-16T08:20:17.283178Z)
- `MELNGC|TOTAL|margin` = **36560** (n=70, 2026-09-16T08:19:13.388012Z)
- `NDF|TOTAL|demand` = **18514** (n=72, 2026-09-16T08:16:58.262307Z)
- `TSDF|TOTAL|demand` = **19458** (n=72, 2026-09-16T08:16:58.262307Z)
- `WINDFOR|TOTAL|generation` = **19327** (n=12, 2026-09-16T08:30:33.621364Z)

## Latest publication events

- `2026-09-16T08:42:25.484637Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:41:45Z`
- `2026-09-16T08:42:09.410343Z` — **MID**: 0 rows; marker `2026-09-16T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T08:40:32.835984Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:40:00Z`
- `2026-09-16T08:40:16.422036Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:39:45Z`
- `2026-09-16T08:38:28.222138Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:37:45Z`
- `2026-09-16T08:36:19.976455Z` — **MID**: 0 rows; marker `2026-09-16T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T08:36:19.976455Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:35:45Z`
- `2026-09-16T08:35:48.397795Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:35:00Z`
- `2026-09-16T08:34:17.835818Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:33:45Z`
- `2026-09-16T08:32:24.986527Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:31:45Z`
- `2026-09-16T08:30:33.621364Z` — **WINDFOR**: 73 rows; marker `2026-09-16T08:30:00Z`
- `2026-09-16T08:30:33.621364Z` — **FUELHH**: 20 rows; marker `2026-09-16T08:30:00Z`
- `2026-09-16T08:30:33.621364Z` — **FUELINST**: 80 rows; marker `2026-09-16T08:30:00Z`
- `2026-09-16T08:30:33.621364Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:29:45Z`
- `2026-09-16T08:28:25.594925Z` — **FREQ**: 5761 rows; marker `2026-09-16T08:27:45Z`
