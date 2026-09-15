# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T06:39:49.034857Z`  
Current process started UTC: `2026-09-15T06:35:48.574750Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=INTVKL|generation` = **238** (n=116, 2026-09-15T06:35:26.913075Z)
- `FUELINST|fuelType=NPSHYD|generation` = **433** (n=116, 2026-09-15T06:35:26.913075Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=116, 2026-09-15T06:35:26.913075Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=116, 2026-09-15T06:35:26.913075Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=116, 2026-09-15T06:35:26.913075Z)
- `FUELINST|fuelType=OTHER|generation` = **2574** (n=116, 2026-09-15T06:35:26.913075Z)
- `FUELINST|fuelType=PS|generation` = **-260** (n=116, 2026-09-15T06:35:26.913075Z)
- `FUELINST|fuelType=WIND|generation` = **13558** (n=116, 2026-09-15T06:35:26.913075Z)
- `IMBALNGC|TOTAL|imbalance` = **-590** (n=20, 2026-09-15T06:20:56.224391Z)
- `INDDEM|TOTAL|demand` = **-12440** (n=20, 2026-09-15T06:20:56.224391Z)
- `INDGEN|TOTAL|generation` = **19894** (n=20, 2026-09-15T06:20:56.224391Z)
- `MELNGC|TOTAL|margin` = **33902** (n=20, 2026-09-15T06:19:35.700118Z)
- `NDF|TOTAL|demand` = **19934** (n=20, 2026-09-15T06:17:34.110396Z)
- `TSDF|TOTAL|demand` = **20484** (n=20, 2026-09-15T06:17:34.110396Z)
- `WINDFOR|TOTAL|generation` = **17059** (n=3, 2026-09-15T05:30:39.125309Z)

## Latest publication events

- `2026-09-15T06:38:12.044620Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:37:45Z`
- `2026-09-15T06:37:24.516476Z` — **MID**: 0 rows; marker `2026-09-15T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T06:36:20.579271Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:35:45Z`
- `2026-09-15T06:35:26.913075Z` — **FUELINST**: 80 rows; marker `2026-09-15T06:35:00Z`
- `2026-09-15T06:34:22.737005Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:33:45Z`
- `2026-09-15T06:32:14.503973Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:31:45Z`
- `2026-09-15T06:30:22.297115Z` — **FUELHH**: 20 rows; marker `2026-09-15T06:30:00Z`
- `2026-09-15T06:30:22.297115Z` — **FUELINST**: 80 rows; marker `2026-09-15T06:30:00Z`
- `2026-09-15T06:30:06.901919Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:29:45Z`
- `2026-09-15T06:28:14.928369Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:27:45Z`
- `2026-09-15T06:26:13.082055Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:25:45Z`
- `2026-09-15T06:25:24.675892Z` — **FUELINST**: 80 rows; marker `2026-09-15T06:25:00Z`
- `2026-09-15T06:24:04.933135Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:23:45Z`
- `2026-09-15T06:22:15.797679Z` — **FREQ**: 5761 rows; marker `2026-09-15T06:21:45Z`
- `2026-09-15T06:20:56.224391Z` — **INDGEN**: 774 rows; marker `2026-09-15T06:17:00Z`
