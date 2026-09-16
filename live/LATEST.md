# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T04:31:39.648777Z`  
Current process started UTC: `2026-09-16T04:27:39.517697Z`  
1-second metadata polls in this process: **230**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1349** (n=379, 2026-09-16T04:30:22.948595Z)
- `FUELINST|fuelType=NPSHYD|generation` = **401** (n=379, 2026-09-16T04:30:22.948595Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=379, 2026-09-16T04:30:22.948595Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=379, 2026-09-16T04:30:22.948595Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=379, 2026-09-16T04:30:22.948595Z)
- `FUELINST|fuelType=OTHER|generation` = **302** (n=379, 2026-09-16T04:30:22.948595Z)
- `FUELINST|fuelType=PS|generation` = **219** (n=379, 2026-09-16T04:30:22.948595Z)
- `FUELINST|fuelType=WIND|generation` = **9610** (n=379, 2026-09-16T04:30:22.948595Z)
- `IMBALNGC|TOTAL|imbalance` = **7147** (n=63, 2026-09-16T04:20:49.625238Z)
- `INDDEM|TOTAL|demand` = **-12199** (n=63, 2026-09-16T04:20:34.376971Z)
- `INDGEN|TOTAL|generation` = **26268** (n=63, 2026-09-16T04:20:34.376971Z)
- `MELNGC|TOTAL|margin` = **37542** (n=63, 2026-09-16T04:19:14.089164Z)
- `NDF|TOTAL|demand` = **18621** (n=64, 2026-09-16T04:17:25.701329Z)
- `TSDF|TOTAL|demand` = **19121** (n=64, 2026-09-16T04:17:25.701329Z)
- `WINDFOR|TOTAL|generation` = **18849** (n=10, 2026-09-16T03:30:50.299289Z)

## Latest publication events

- `2026-09-16T04:30:39.096882Z` — **FUELHH**: 20 rows; marker `2026-09-16T04:30:00Z`
- `2026-09-16T04:30:22.948595Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:30:00Z`
- `2026-09-16T04:30:06.741819Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:29:45Z`
- `2026-09-16T04:28:11.896282Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:27:45Z`
- `2026-09-16T04:26:09.318942Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:25:45Z`
- `2026-09-16T04:25:21.894895Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:25:00Z`
- `2026-09-16T04:24:17.425251Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:23:45Z`
- `2026-09-16T04:22:09.454145Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:21:45Z`
- `2026-09-16T04:20:49.625238Z` — **IMBALNGC**: 846 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:20:34.376971Z` — **INDGEN**: 846 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:20:34.376971Z` — **INDDEM**: 846 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:20:18.148372Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:20:00Z`
- `2026-09-16T04:20:02.168231Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:19:45Z`
- `2026-09-16T04:19:14.089164Z` — **MELNGC**: 846 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:18:13.443814Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:17:45Z`
