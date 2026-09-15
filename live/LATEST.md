# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T03:35:14.776746Z`  
Current process started UTC: `2026-09-15T03:31:14.786768Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1354** (n=79, 2026-09-15T03:30:32.352514Z)
- `FUELINST|fuelType=NPSHYD|generation` = **342** (n=79, 2026-09-15T03:30:32.352514Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3322** (n=79, 2026-09-15T03:30:32.352514Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=79, 2026-09-15T03:30:32.352514Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=79, 2026-09-15T03:30:32.352514Z)
- `FUELINST|fuelType=OTHER|generation` = **304** (n=79, 2026-09-15T03:30:32.352514Z)
- `FUELINST|fuelType=PS|generation` = **-581** (n=79, 2026-09-15T03:30:32.352514Z)
- `FUELINST|fuelType=WIND|generation` = **13777** (n=79, 2026-09-15T03:30:32.352514Z)
- `IMBALNGC|TOTAL|imbalance` = **229** (n=14, 2026-09-15T03:21:03.261997Z)
- `INDDEM|TOTAL|demand` = **-12413** (n=14, 2026-09-15T03:21:03.261997Z)
- `INDGEN|TOTAL|generation` = **20713** (n=14, 2026-09-15T03:21:03.261997Z)
- `MELNGC|TOTAL|margin` = **34110** (n=14, 2026-09-15T03:20:15.578674Z)
- `NDF|TOTAL|demand` = **19934** (n=14, 2026-09-15T03:18:02.752215Z)
- `TSDF|TOTAL|demand` = **20485** (n=14, 2026-09-15T03:17:46.512016Z)
- `WINDFOR|TOTAL|generation` = **16388** (n=2, 2026-09-15T03:30:48.465743Z)

## Latest publication events

- `2026-09-15T03:34:11.190056Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:33:45Z`
- `2026-09-15T03:32:18.878509Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:31:45Z`
- `2026-09-15T03:30:48.465743Z` — **WINDFOR**: 73 rows; marker `2026-09-15T03:30:00Z`
- `2026-09-15T03:30:32.352514Z` — **FUELHH**: 20 rows; marker `2026-09-15T03:30:00Z`
- `2026-09-15T03:30:32.352514Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:30:00Z`
- `2026-09-15T03:30:16.308231Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:29:45Z`
- `2026-09-15T03:28:23.722009Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:27:45Z`
- `2026-09-15T03:26:22.749790Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:25:45Z`
- `2026-09-15T03:25:35.319926Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:25:00Z`
- `2026-09-15T03:24:47.387880Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:23:45Z`
- `2026-09-15T03:22:06.931617Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:21:45Z`
- `2026-09-15T03:21:03.261997Z` — **INDGEN**: 882 rows; marker `2026-09-15T03:17:00Z`
- `2026-09-15T03:21:03.261997Z` — **INDDEM**: 882 rows; marker `2026-09-15T03:17:00Z`
- `2026-09-15T03:21:03.261997Z` — **IMBALNGC**: 882 rows; marker `2026-09-15T03:17:00Z`
- `2026-09-15T03:20:31.870826Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:20:00Z`
