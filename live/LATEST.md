# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T05:32:31.102228Z`  
Current process started UTC: `2026-09-15T05:28:30.657473Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNEM` `generation` — half-hour generation mix [fuelType=INTNEM] generation: value=-748, delta=-264, z=-3.70 -> generation-mix component moved
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-12413, delta=-86, z=-3.82 -> demand pressure easing
- **MELNGC** `TOTAL` `margin` — indicated margin [TOTAL] margin: value=34104, delta=1370, z=NA -> margin/tightness state changed
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=0, z=3.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=1, z=4.75 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=3.56 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=3.86 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=-299, delta=8, z=3.95 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=4.25 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=4.80 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=5.62 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=-307, delta=170, z=4.89 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=7.11 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0.004, z=11.23 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2683, delta=11, z=5.04 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-453** (n=103, 2026-09-15T05:30:22.772794Z)
- `FUELINST|fuelType=NPSHYD|generation` = **448** (n=103, 2026-09-15T05:30:22.772794Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=103, 2026-09-15T05:30:22.772794Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=103, 2026-09-15T05:30:22.772794Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=103, 2026-09-15T05:30:22.772794Z)
- `FUELINST|fuelType=OTHER|generation` = **464** (n=103, 2026-09-15T05:30:22.772794Z)
- `FUELINST|fuelType=PS|generation` = **-258** (n=103, 2026-09-15T05:30:22.772794Z)
- `FUELINST|fuelType=WIND|generation` = **13492** (n=103, 2026-09-15T05:30:22.772794Z)
- `IMBALNGC|TOTAL|imbalance` = **-524** (n=18, 2026-09-15T05:20:42.604404Z)
- `INDDEM|TOTAL|demand` = **-12440** (n=18, 2026-09-15T05:20:26.933942Z)
- `INDGEN|TOTAL|generation` = **19960** (n=18, 2026-09-15T05:20:42.604404Z)
- `MELNGC|TOTAL|margin` = **33992** (n=18, 2026-09-15T05:19:31.055349Z)
- `NDF|TOTAL|demand` = **19934** (n=18, 2026-09-15T05:17:22.119466Z)
- `TSDF|TOTAL|demand` = **20484** (n=18, 2026-09-15T05:17:22.119466Z)
- `WINDFOR|TOTAL|generation` = **17059** (n=3, 2026-09-15T05:30:39.125309Z)

## Latest publication events

- `2026-09-15T05:32:14.704011Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:31:45Z`
- `2026-09-15T05:30:54.541259Z` — **FUELHH**: 20 rows; marker `2026-09-15T05:30:00Z`
- `2026-09-15T05:30:39.125309Z` — **WINDFOR**: 73 rows; marker `2026-09-15T05:30:00Z`
- `2026-09-15T05:30:22.772794Z` — **FUELINST**: 80 rows; marker `2026-09-15T05:30:00Z`
- `2026-09-15T05:30:22.772794Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:29:45Z`
- `2026-09-15T05:28:10.562034Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:27:45Z`
- `2026-09-15T05:26:02.673607Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:25:45Z`
- `2026-09-15T05:25:46.569024Z` — **FUELINST**: 80 rows; marker `2026-09-15T05:25:00Z`
- `2026-09-15T05:24:26.899656Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:23:45Z`
- `2026-09-15T05:22:34.930305Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:21:45Z`
- `2026-09-15T05:20:42.604404Z` — **INDGEN**: 810 rows; marker `2026-09-15T05:17:00Z`
- `2026-09-15T05:20:42.604404Z` — **IMBALNGC**: 810 rows; marker `2026-09-15T05:17:00Z`
- `2026-09-15T05:20:26.933942Z` — **INDDEM**: 810 rows; marker `2026-09-15T05:16:00Z`
- `2026-09-15T05:20:26.933942Z` — **FUELINST**: 80 rows; marker `2026-09-15T05:20:00Z`
- `2026-09-15T05:20:26.933942Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:19:45Z`
