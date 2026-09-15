# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T05:53:30.386760Z`  
Current process started UTC: `2026-09-15T05:49:30.212823Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=20484, delta=0, z=-4.01 -> demand pressure easing
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-453** (n=107, 2026-09-15T05:50:37.336728Z)
- `FUELINST|fuelType=NPSHYD|generation` = **453** (n=107, 2026-09-15T05:50:37.336728Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=107, 2026-09-15T05:50:37.336728Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=107, 2026-09-15T05:50:37.336728Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=107, 2026-09-15T05:50:37.336728Z)
- `FUELINST|fuelType=OTHER|generation` = **1725** (n=107, 2026-09-15T05:50:37.336728Z)
- `FUELINST|fuelType=PS|generation` = **-24** (n=107, 2026-09-15T05:50:37.336728Z)
- `FUELINST|fuelType=WIND|generation` = **13437** (n=107, 2026-09-15T05:50:37.336728Z)
- `IMBALNGC|TOTAL|imbalance` = **-587** (n=19, 2026-09-15T05:51:09.500647Z)
- `INDDEM|TOTAL|demand` = **-12440** (n=19, 2026-09-15T05:50:53.467496Z)
- `INDGEN|TOTAL|generation` = **19897** (n=19, 2026-09-15T05:50:53.467496Z)
- `MELNGC|TOTAL|margin` = **33927** (n=19, 2026-09-15T05:49:34.213489Z)
- `NDF|TOTAL|demand` = **19934** (n=19, 2026-09-15T05:47:11.171890Z)
- `TSDF|TOTAL|demand` = **20484** (n=19, 2026-09-15T05:47:11.171890Z)
- `WINDFOR|TOTAL|generation` = **17059** (n=3, 2026-09-15T05:30:39.125309Z)

## Latest publication events

- `2026-09-15T05:52:13.366772Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:51:45Z`
- `2026-09-15T05:51:09.500647Z` — **IMBALNGC**: 792 rows; marker `2026-09-15T05:47:00Z`
- `2026-09-15T05:50:53.467496Z` — **INDGEN**: 792 rows; marker `2026-09-15T05:46:00Z`
- `2026-09-15T05:50:53.467496Z` — **INDDEM**: 792 rows; marker `2026-09-15T05:46:00Z`
- `2026-09-15T05:50:37.336728Z` — **FUELINST**: 80 rows; marker `2026-09-15T05:50:00Z`
- `2026-09-15T05:50:21.527322Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:49:45Z`
- `2026-09-15T05:49:34.213489Z` — **MELNGC**: 792 rows; marker `2026-09-15T05:47:00Z`
- `2026-09-15T05:48:14.528862Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:47:45Z`
- `2026-09-15T05:47:11.171890Z` — **TSDF**: 792 rows; marker `2026-09-15T05:47:00Z`
- `2026-09-15T05:47:11.171890Z` — **NDF**: 44 rows; marker `2026-09-15T05:47:00Z`
- `2026-09-15T05:46:06.937334Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:45:45Z`
- `2026-09-15T05:45:51.370959Z` — **FUELINST**: 80 rows; marker `2026-09-15T05:45:00Z`
- `2026-09-15T05:44:19.914630Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:43:45Z`
- `2026-09-15T05:42:11.690706Z` — **MID**: 0 rows; marker `2026-09-15T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T05:42:11.690706Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:41:45Z`
