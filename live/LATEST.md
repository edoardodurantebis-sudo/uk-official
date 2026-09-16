# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T10:29:49.155601Z`  
Current process started UTC: `2026-09-16T10:25:48.477170Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.83 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=450, 2026-09-16T10:25:48.477179Z)
- `FUELINST|fuelType=NPSHYD|generation` = **354** (n=450, 2026-09-16T10:25:48.477179Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=450, 2026-09-16T10:25:48.477179Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=450, 2026-09-16T10:25:48.477179Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=450, 2026-09-16T10:25:48.477179Z)
- `FUELINST|fuelType=OTHER|generation` = **1134** (n=450, 2026-09-16T10:25:48.477179Z)
- `FUELINST|fuelType=PS|generation` = **-5** (n=450, 2026-09-16T10:25:48.477179Z)
- `FUELINST|fuelType=WIND|generation` = **5190** (n=450, 2026-09-16T10:25:48.477179Z)
- `IMBALNGC|TOTAL|imbalance` = **5373** (n=74, 2026-09-16T10:19:08.498393Z)
- `INDDEM|TOTAL|demand` = **-15111** (n=74, 2026-09-16T10:19:08.498393Z)
- `INDGEN|TOTAL|generation` = **26011** (n=74, 2026-09-16T10:19:08.498393Z)
- `MELNGC|TOTAL|margin` = **34224** (n=74, 2026-09-16T10:18:52.641613Z)
- `NDF|TOTAL|demand` = **18514** (n=76, 2026-09-16T10:16:58.653151Z)
- `TSDF|TOTAL|demand` = **20638** (n=76, 2026-09-16T10:16:58.653151Z)
- `WINDFOR|TOTAL|generation` = **19327** (n=12, 2026-09-16T08:30:33.621364Z)

## Latest publication events

- `2026-09-16T10:28:27.895420Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:27:45Z`
- `2026-09-16T10:26:19.907711Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:25:45Z`
- `2026-09-16T10:25:48.477179Z` — **FUELINST**: 80 rows; marker `2026-09-16T10:25:00Z`
- `2026-09-16T10:24:18.361421Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:23:45Z`
- `2026-09-16T10:22:26.155374Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:21:45Z`
- `2026-09-16T10:20:28.425821Z` — **FUELINST**: 80 rows; marker `2026-09-16T10:20:00Z`
- `2026-09-16T10:20:28.425821Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:19:45Z`
- `2026-09-16T10:19:08.498393Z` — **INDGEN**: 630 rows; marker `2026-09-16T10:16:00Z`
- `2026-09-16T10:19:08.498393Z` — **INDDEM**: 630 rows; marker `2026-09-16T10:16:00Z`
- `2026-09-16T10:19:08.498393Z` — **IMBALNGC**: 630 rows; marker `2026-09-16T10:16:00Z`
- `2026-09-16T10:18:52.641613Z` — **MELNGC**: 630 rows; marker `2026-09-16T10:16:00Z`
- `2026-09-16T10:18:20.737306Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:17:45Z`
- `2026-09-16T10:16:58.653151Z` — **TSDF**: 630 rows; marker `2026-09-16T10:16:00Z`
- `2026-09-16T10:16:58.653151Z` — **NDF**: 35 rows; marker `2026-09-16T10:16:00Z`
- `2026-09-16T10:16:27.157578Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:15:45Z`
