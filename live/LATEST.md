# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T07:31:44.992964Z`  
Current process started UTC: `2026-09-16T07:27:45.113105Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **1371** (n=415, 2026-09-16T07:30:40.638320Z)
- `FUELINST|fuelType=NPSHYD|generation` = **468** (n=415, 2026-09-16T07:30:40.638320Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=415, 2026-09-16T07:30:40.638320Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=415, 2026-09-16T07:30:40.638320Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=415, 2026-09-16T07:30:40.638320Z)
- `FUELINST|fuelType=OTHER|generation` = **415** (n=415, 2026-09-16T07:30:40.638320Z)
- `FUELINST|fuelType=PS|generation` = **222** (n=415, 2026-09-16T07:30:40.638320Z)
- `FUELINST|fuelType=WIND|generation` = **7899** (n=415, 2026-09-16T07:30:40.638320Z)
- `IMBALNGC|TOTAL|imbalance` = **6872** (n=69, 2026-09-16T07:20:10.341890Z)
- `INDDEM|TOTAL|demand` = **-12664** (n=69, 2026-09-16T07:19:53.371027Z)
- `INDGEN|TOTAL|generation` = **26437** (n=69, 2026-09-16T07:19:53.371027Z)
- `MELNGC|TOTAL|margin` = **36325** (n=69, 2026-09-16T07:18:39.087802Z)
- `NDF|TOTAL|demand` = **18621** (n=70, 2026-09-16T07:17:19.600220Z)
- `TSDF|TOTAL|demand` = **19565** (n=70, 2026-09-16T07:17:19.600220Z)
- `WINDFOR|TOTAL|generation` = **19006** (n=11, 2026-09-16T05:30:53.425120Z)

## Latest publication events

- `2026-09-16T07:30:40.638320Z` — **FUELHH**: 20 rows; marker `2026-09-16T07:30:00Z`
- `2026-09-16T07:30:40.638320Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:30:00Z`
- `2026-09-16T07:30:08.963054Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:29:45Z`
- `2026-09-16T07:28:17.116912Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:27:45Z`
- `2026-09-16T07:26:14.002625Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:25:45Z`
- `2026-09-16T07:25:26.143555Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:25:00Z`
- `2026-09-16T07:24:21.374087Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:23:45Z`
- `2026-09-16T07:22:18.632037Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:21:45Z`
- `2026-09-16T07:20:26.377296Z` — **FUELINST**: 80 rows; marker `2026-09-16T07:20:00Z`
- `2026-09-16T07:20:26.377296Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:19:45Z`
- `2026-09-16T07:20:10.341890Z` — **IMBALNGC**: 738 rows; marker `2026-09-16T07:16:00Z`
- `2026-09-16T07:19:53.371027Z` — **INDGEN**: 738 rows; marker `2026-09-16T07:16:00Z`
- `2026-09-16T07:19:53.371027Z` — **INDDEM**: 738 rows; marker `2026-09-16T07:16:00Z`
- `2026-09-16T07:18:39.087802Z` — **MELNGC**: 738 rows; marker `2026-09-16T07:16:00Z`
- `2026-09-16T07:18:23.328572Z` — **FREQ**: 5761 rows; marker `2026-09-16T07:17:45Z`
