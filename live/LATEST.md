# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T06:52:20.865110Z`  
Current process started UTC: `2026-09-15T06:48:20.608081Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2574, delta=290, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=1992, delta=-144, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2136, delta=411, z=4.17 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **238** (n=119, 2026-09-15T06:50:43.139416Z)
- `FUELINST|fuelType=NPSHYD|generation` = **434** (n=119, 2026-09-15T06:50:43.139416Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=119, 2026-09-15T06:50:43.139416Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=119, 2026-09-15T06:50:43.139416Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=119, 2026-09-15T06:50:43.139416Z)
- `FUELINST|fuelType=OTHER|generation` = **2733** (n=119, 2026-09-15T06:50:43.139416Z)
- `FUELINST|fuelType=PS|generation` = **-259** (n=119, 2026-09-15T06:50:43.139416Z)
- `FUELINST|fuelType=WIND|generation` = **13597** (n=119, 2026-09-15T06:50:43.139416Z)
- `IMBALNGC|TOTAL|imbalance` = **-703** (n=21, 2026-09-15T06:50:27.324561Z)
- `INDDEM|TOTAL|demand` = **-12429** (n=21, 2026-09-15T06:50:11.912776Z)
- `INDGEN|TOTAL|generation` = **19781** (n=21, 2026-09-15T06:50:11.912776Z)
- `MELNGC|TOTAL|margin` = **33975** (n=21, 2026-09-15T06:49:56.392396Z)
- `NDF|TOTAL|demand` = **19934** (n=21, 2026-09-15T06:47:23.898461Z)
- `TSDF|TOTAL|demand` = **20484** (n=21, 2026-09-15T06:47:23.898461Z)
- `WINDFOR|TOTAL|generation` = **17059** (n=3, 2026-09-15T05:30:39.125309Z)

## Latest publication events

- `2026-09-15T06:52:18.543415Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:51:45Z`
- `2026-09-15T06:50:43.139416Z` — **FUELINST**: 80 rows; marker `2026-09-15T06:50:00Z`
- `2026-09-15T06:50:27.324561Z` — **IMBALNGC**: 756 rows; marker `2026-09-15T06:46:00Z`
- `2026-09-15T06:50:27.324561Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:49:45Z`
- `2026-09-15T06:50:11.912776Z` — **INDGEN**: 756 rows; marker `2026-09-15T06:46:00Z`
- `2026-09-15T06:50:11.912776Z` — **INDDEM**: 756 rows; marker `2026-09-15T06:46:00Z`
- `2026-09-15T06:49:56.392396Z` — **MELNGC**: 756 rows; marker `2026-09-15T06:46:00Z`
- `2026-09-15T06:48:20.608090Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:47:45Z`
- `2026-09-15T06:47:23.898461Z` — **TSDF**: 756 rows; marker `2026-09-15T06:46:00Z`
- `2026-09-15T06:47:23.898461Z` — **NDF**: 42 rows; marker `2026-09-15T06:46:00Z`
- `2026-09-15T06:46:19.090626Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:45:45Z`
- `2026-09-15T06:45:30.494839Z` — **FUELINST**: 80 rows; marker `2026-09-15T06:45:00Z`
- `2026-09-15T06:44:25.833824Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:43:45Z`
- `2026-09-15T06:42:12.242229Z` — **MID**: 0 rows; marker `2026-09-15T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T06:42:12.242229Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:41:45Z`
