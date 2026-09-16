# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T04:23:14.639940Z`  
Current process started UTC: `2026-09-16T04:19:14.089155Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1349** (n=377, 2026-09-16T04:20:18.148372Z)
- `FUELINST|fuelType=NPSHYD|generation` = **397** (n=377, 2026-09-16T04:20:18.148372Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=377, 2026-09-16T04:20:18.148372Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=377, 2026-09-16T04:20:18.148372Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=377, 2026-09-16T04:20:18.148372Z)
- `FUELINST|fuelType=OTHER|generation` = **164** (n=377, 2026-09-16T04:20:18.148372Z)
- `FUELINST|fuelType=PS|generation` = **224** (n=377, 2026-09-16T04:20:18.148372Z)
- `FUELINST|fuelType=WIND|generation` = **9540** (n=377, 2026-09-16T04:20:18.148372Z)
- `IMBALNGC|TOTAL|imbalance` = **7147** (n=63, 2026-09-16T04:20:49.625238Z)
- `INDDEM|TOTAL|demand` = **-12199** (n=63, 2026-09-16T04:20:34.376971Z)
- `INDGEN|TOTAL|generation` = **26268** (n=63, 2026-09-16T04:20:34.376971Z)
- `MELNGC|TOTAL|margin` = **37542** (n=63, 2026-09-16T04:19:14.089164Z)
- `NDF|TOTAL|demand` = **18621** (n=64, 2026-09-16T04:17:25.701329Z)
- `TSDF|TOTAL|demand` = **19121** (n=64, 2026-09-16T04:17:25.701329Z)
- `WINDFOR|TOTAL|generation` = **18849** (n=10, 2026-09-16T03:30:50.299289Z)

## Latest publication events

- `2026-09-16T04:22:09.454145Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:21:45Z`
- `2026-09-16T04:20:49.625238Z` — **IMBALNGC**: 846 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:20:34.376971Z` — **INDGEN**: 846 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:20:34.376971Z` — **INDDEM**: 846 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:20:18.148372Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:20:00Z`
- `2026-09-16T04:20:02.168231Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:19:45Z`
- `2026-09-16T04:19:14.089164Z` — **MELNGC**: 846 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:18:13.443814Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:17:45Z`
- `2026-09-16T04:17:25.701329Z` — **TSDF**: 846 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:17:25.701329Z` — **NDF**: 47 rows; marker `2026-09-16T04:17:00Z`
- `2026-09-16T04:16:05.372798Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:15:45Z`
- `2026-09-16T04:15:49.118827Z` — **FUELINST**: 80 rows; marker `2026-09-16T04:15:00Z`
- `2026-09-16T04:14:09.636180Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:13:45Z`
- `2026-09-16T04:12:15.464348Z` — **MID**: 0 rows; marker `2026-09-16T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T04:12:15.464348Z` — **FREQ**: 5761 rows; marker `2026-09-16T04:11:45Z`
