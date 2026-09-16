# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T11:33:04.125483Z`  
Current process started UTC: `2026-09-16T11:29:04.325768Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11768, delta=3343, z=1.00 -> demand pressure up
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-15111, delta=-1226, z=-8.15 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=0, z=-5.69 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=-1204, z=-7.82 -> demand pressure easing
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=463, 2026-09-16T11:30:29.856805Z)
- `FUELINST|fuelType=NPSHYD|generation` = **353** (n=463, 2026-09-16T11:30:29.856805Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=463, 2026-09-16T11:30:29.856805Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=463, 2026-09-16T11:30:29.856805Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=463, 2026-09-16T11:30:29.856805Z)
- `FUELINST|fuelType=OTHER|generation` = **1032** (n=463, 2026-09-16T11:30:29.856805Z)
- `FUELINST|fuelType=PS|generation` = **-5** (n=463, 2026-09-16T11:30:29.856805Z)
- `FUELINST|fuelType=WIND|generation` = **4182** (n=463, 2026-09-16T11:30:29.856805Z)
- `IMBALNGC|TOTAL|imbalance` = **6020** (n=76, 2026-09-16T11:24:11.584614Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=76, 2026-09-16T11:23:55.594657Z)
- `INDGEN|TOTAL|generation` = **24800** (n=76, 2026-09-16T11:24:11.584614Z)
- `MELNGC|TOTAL|margin` = **35435** (n=76, 2026-09-16T11:20:44.487650Z)
- `NDF|TOTAL|demand` = **18280** (n=78, 2026-09-16T11:18:21.826484Z)
- `TSDF|TOTAL|demand` = **18780** (n=78, 2026-09-16T11:18:37.882202Z)
- `WINDFOR|TOTAL|generation` = **19760** (n=13, 2026-09-16T10:30:36.030367Z)

## Latest publication events

- `2026-09-16T11:32:05.834621Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:31:45Z`
- `2026-09-16T11:30:29.856805Z` — **FUELHH**: 20 rows; marker `2026-09-16T11:30:00Z`
- `2026-09-16T11:30:29.856805Z` — **FUELINST**: 80 rows; marker `2026-09-16T11:30:00Z`
- `2026-09-16T11:30:29.856805Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:29:45Z`
- `2026-09-16T11:28:05.702590Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:27:45Z`
- `2026-09-16T11:26:13.818299Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:25:45Z`
- `2026-09-16T11:25:25.806542Z` — **FUELINST**: 80 rows; marker `2026-09-16T11:25:00Z`
- `2026-09-16T11:24:11.584614Z` — **INDGEN**: 1458 rows; marker `2026-09-16T11:18:00Z`
- `2026-09-16T11:24:11.584614Z` — **IMBALNGC**: 1458 rows; marker `2026-09-16T11:18:00Z`
- `2026-09-16T11:24:11.584614Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:23:45Z`
- `2026-09-16T11:23:55.594657Z` — **INDDEM**: 1458 rows; marker `2026-09-16T11:18:00Z`
- `2026-09-16T11:22:03.160804Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:21:45Z`
- `2026-09-16T11:20:44.487650Z` — **MELNGC**: 1458 rows; marker `2026-09-16T11:18:00Z`
- `2026-09-16T11:20:44.487650Z` — **FUELINST**: 80 rows; marker `2026-09-16T11:20:00Z`
- `2026-09-16T11:20:28.561637Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:19:45Z`
