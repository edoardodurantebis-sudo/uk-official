# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T12:15:21.323663Z`  
Current process started UTC: `2026-09-16T12:11:21.878287Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3297, delta=3, z=-3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3294, delta=-4, z=-4.20 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3298, delta=-3, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=-7, z=-5.03 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3297, delta=-24, z=-4.07 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=471, 2026-09-16T12:10:39.009291Z)
- `FUELINST|fuelType=NPSHYD|generation` = **351** (n=471, 2026-09-16T12:10:39.009291Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3302** (n=471, 2026-09-16T12:10:39.009291Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=471, 2026-09-16T12:10:39.009291Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=471, 2026-09-16T12:10:39.009291Z)
- `FUELINST|fuelType=OTHER|generation` = **590** (n=471, 2026-09-16T12:10:39.009291Z)
- `FUELINST|fuelType=PS|generation` = **-5** (n=471, 2026-09-16T12:10:39.009291Z)
- `FUELINST|fuelType=WIND|generation` = **4127** (n=471, 2026-09-16T12:10:39.009291Z)
- `IMBALNGC|TOTAL|imbalance` = **6041** (n=77, 2026-09-16T11:53:47.798041Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=77, 2026-09-16T11:53:31.476082Z)
- `INDGEN|TOTAL|generation` = **24821** (n=77, 2026-09-16T11:53:31.476082Z)
- `MELNGC|TOTAL|margin` = **35471** (n=77, 2026-09-16T11:50:20.527601Z)
- `NDF|TOTAL|demand` = **18280** (n=79, 2026-09-16T11:48:20.444984Z)
- `TSDF|TOTAL|demand` = **18780** (n=79, 2026-09-16T11:48:20.444984Z)
- `WINDFOR|TOTAL|generation` = **19760** (n=13, 2026-09-16T10:30:36.030367Z)

## Latest publication events

- `2026-09-16T12:14:05.736038Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:13:45Z`
- `2026-09-16T12:12:29.811510Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:11:45Z`
- `2026-09-16T12:12:14.270229Z` — **MID**: 0 rows; marker `2026-09-16T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T12:10:39.009291Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:10:00Z`
- `2026-09-16T12:10:23.122942Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:09:45Z`
- `2026-09-16T12:08:30.389677Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:07:45Z`
- `2026-09-16T12:06:29.580958Z` — **MID**: 0 rows; marker `2026-09-16T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T12:06:29.580958Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:05:45Z`
- `2026-09-16T12:05:41.810956Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:05:00Z`
- `2026-09-16T12:04:21.497689Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:03:45Z`
- `2026-09-16T12:02:29.607648Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:01:45Z`
- `2026-09-16T12:00:36.813089Z` — **FUELHH**: 20 rows; marker `2026-09-16T12:00:00Z`
- `2026-09-16T12:00:36.813089Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:00:00Z`
- `2026-09-16T12:00:21.363778Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:59:45Z`
- `2026-09-16T11:58:46.129556Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:57:45Z`
