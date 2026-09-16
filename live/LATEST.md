# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T12:02:46.562738Z`  
Current process started UTC: `2026-09-16T11:58:46.129548Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.66 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=469, 2026-09-16T12:00:36.813089Z)
- `FUELINST|fuelType=NPSHYD|generation` = **353** (n=469, 2026-09-16T12:00:36.813089Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3294** (n=469, 2026-09-16T12:00:36.813089Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=469, 2026-09-16T12:00:36.813089Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=469, 2026-09-16T12:00:36.813089Z)
- `FUELINST|fuelType=OTHER|generation` = **840** (n=469, 2026-09-16T12:00:36.813089Z)
- `FUELINST|fuelType=PS|generation` = **-5** (n=469, 2026-09-16T12:00:36.813089Z)
- `FUELINST|fuelType=WIND|generation` = **4262** (n=469, 2026-09-16T12:00:36.813089Z)
- `IMBALNGC|TOTAL|imbalance` = **6041** (n=77, 2026-09-16T11:53:47.798041Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=77, 2026-09-16T11:53:31.476082Z)
- `INDGEN|TOTAL|generation` = **24821** (n=77, 2026-09-16T11:53:31.476082Z)
- `MELNGC|TOTAL|margin` = **35471** (n=77, 2026-09-16T11:50:20.527601Z)
- `NDF|TOTAL|demand` = **18280** (n=79, 2026-09-16T11:48:20.444984Z)
- `TSDF|TOTAL|demand` = **18780** (n=79, 2026-09-16T11:48:20.444984Z)
- `WINDFOR|TOTAL|generation` = **19760** (n=13, 2026-09-16T10:30:36.030367Z)

## Latest publication events

- `2026-09-16T12:02:29.607648Z` — **FREQ**: 5761 rows; marker `2026-09-16T12:01:45Z`
- `2026-09-16T12:00:36.813089Z` — **FUELHH**: 20 rows; marker `2026-09-16T12:00:00Z`
- `2026-09-16T12:00:36.813089Z` — **FUELINST**: 80 rows; marker `2026-09-16T12:00:00Z`
- `2026-09-16T12:00:21.363778Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:59:45Z`
- `2026-09-16T11:58:46.129556Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:57:45Z`
- `2026-09-16T11:56:10.953924Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:55:45Z`
- `2026-09-16T11:55:38.926241Z` — **FUELINST**: 80 rows; marker `2026-09-16T11:55:00Z`
- `2026-09-16T11:54:19.410617Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:53:45Z`
- `2026-09-16T11:53:47.798041Z` — **IMBALNGC**: 1440 rows; marker `2026-09-16T11:47:00Z`
- `2026-09-16T11:53:31.476082Z` — **INDGEN**: 1440 rows; marker `2026-09-16T11:47:00Z`
- `2026-09-16T11:53:31.476082Z` — **INDDEM**: 1440 rows; marker `2026-09-16T11:47:00Z`
- `2026-09-16T11:52:12.065749Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:51:45Z`
- `2026-09-16T11:50:35.949948Z` — **FUELINST**: 80 rows; marker `2026-09-16T11:50:00Z`
- `2026-09-16T11:50:20.527601Z` — **MELNGC**: 1440 rows; marker `2026-09-16T11:47:00Z`
- `2026-09-16T11:50:20.527601Z` — **FREQ**: 5761 rows; marker `2026-09-16T11:49:45Z`
