# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T10:42:29.764696Z`  
Current process started UTC: `2026-09-16T10:38:29.692650Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=453, 2026-09-16T10:40:23.179066Z)
- `FUELINST|fuelType=NPSHYD|generation` = **363** (n=453, 2026-09-16T10:40:23.179066Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=453, 2026-09-16T10:40:23.179066Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=453, 2026-09-16T10:40:23.179066Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=453, 2026-09-16T10:40:23.179066Z)
- `FUELINST|fuelType=OTHER|generation` = **1004** (n=453, 2026-09-16T10:40:23.179066Z)
- `FUELINST|fuelType=PS|generation` = **-5** (n=453, 2026-09-16T10:40:23.179066Z)
- `FUELINST|fuelType=WIND|generation` = **4913** (n=453, 2026-09-16T10:40:23.179066Z)
- `IMBALNGC|TOTAL|imbalance` = **5373** (n=74, 2026-09-16T10:19:08.498393Z)
- `INDDEM|TOTAL|demand` = **-15111** (n=74, 2026-09-16T10:19:08.498393Z)
- `INDGEN|TOTAL|generation` = **26011** (n=74, 2026-09-16T10:19:08.498393Z)
- `MELNGC|TOTAL|margin` = **34224** (n=74, 2026-09-16T10:18:52.641613Z)
- `NDF|TOTAL|demand` = **18514** (n=76, 2026-09-16T10:16:58.653151Z)
- `TSDF|TOTAL|demand` = **20638** (n=76, 2026-09-16T10:16:58.653151Z)
- `WINDFOR|TOTAL|generation` = **19760** (n=13, 2026-09-16T10:30:36.030367Z)

## Latest publication events

- `2026-09-16T10:42:15.306172Z` — **MID**: 0 rows; marker `2026-09-16T10:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T10:42:15.306172Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:41:45Z`
- `2026-09-16T10:40:23.179066Z` — **FUELINST**: 80 rows; marker `2026-09-16T10:40:00Z`
- `2026-09-16T10:40:07.706198Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:39:45Z`
- `2026-09-16T10:38:15.904300Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:37:45Z`
- `2026-09-16T10:36:23.794973Z` — **MID**: 0 rows; marker `2026-09-16T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T10:36:07.617634Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:35:45Z`
- `2026-09-16T10:35:35.896320Z` — **FUELINST**: 80 rows; marker `2026-09-16T10:35:00Z`
- `2026-09-16T10:34:16.363756Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:33:45Z`
- `2026-09-16T10:32:12.365713Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:31:45Z`
- `2026-09-16T10:30:36.030367Z` — **WINDFOR**: 73 rows; marker `2026-09-16T10:30:00Z`
- `2026-09-16T10:30:36.030367Z` — **FUELHH**: 20 rows; marker `2026-09-16T10:30:00Z`
- `2026-09-16T10:30:36.030367Z` — **FUELINST**: 80 rows; marker `2026-09-16T10:30:00Z`
- `2026-09-16T10:30:03.948419Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:29:45Z`
- `2026-09-16T10:28:27.895420Z` — **FREQ**: 5761 rows; marker `2026-09-16T10:27:45Z`
