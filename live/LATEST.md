# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T04:42:14.342205Z`  
Current process started UTC: `2026-09-15T04:38:14.025485Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=93, 2026-09-15T04:40:41.689431Z)
- `FUELINST|fuelType=NPSHYD|generation` = **371** (n=93, 2026-09-15T04:40:41.689431Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=93, 2026-09-15T04:40:41.689431Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=93, 2026-09-15T04:40:41.689431Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=93, 2026-09-15T04:40:41.689431Z)
- `FUELINST|fuelType=OTHER|generation` = **202** (n=93, 2026-09-15T04:40:41.689431Z)
- `FUELINST|fuelType=PS|generation` = **-699** (n=93, 2026-09-15T04:40:41.689431Z)
- `FUELINST|fuelType=WIND|generation` = **13334** (n=93, 2026-09-15T04:40:41.689431Z)
- `IMBALNGC|TOTAL|imbalance` = **-469** (n=16, 2026-09-15T04:20:32.622977Z)
- `INDDEM|TOTAL|demand` = **-12442** (n=16, 2026-09-15T04:20:32.622977Z)
- `INDGEN|TOTAL|generation` = **20016** (n=16, 2026-09-15T04:20:32.622977Z)
- `MELNGC|TOTAL|margin` = **34070** (n=16, 2026-09-15T04:19:13.427589Z)
- `NDF|TOTAL|demand` = **19934** (n=16, 2026-09-15T04:17:21.694852Z)
- `TSDF|TOTAL|demand` = **20485** (n=16, 2026-09-15T04:17:21.694852Z)
- `WINDFOR|TOTAL|generation` = **16388** (n=2, 2026-09-15T03:30:48.465743Z)

## Latest publication events

- `2026-09-15T04:40:41.689431Z` — **FUELINST**: 80 rows; marker `2026-09-15T04:40:00Z`
- `2026-09-15T04:40:25.901173Z` — **FREQ**: 5761 rows; marker `2026-09-15T04:39:45Z`
- `2026-09-15T04:38:18.026104Z` — **FREQ**: 5761 rows; marker `2026-09-15T04:37:45Z`
- `2026-09-15T04:37:31.138099Z` — **MID**: 0 rows; marker `2026-09-15T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T04:36:27.547148Z` — **FREQ**: 5761 rows; marker `2026-09-15T04:35:45Z`
- `2026-09-15T04:35:40.032063Z` — **FUELINST**: 80 rows; marker `2026-09-15T04:35:00Z`
- `2026-09-15T04:34:20.262476Z` — **FREQ**: 5761 rows; marker `2026-09-15T04:33:45Z`
- `2026-09-15T04:32:40.245247Z` — **FREQ**: 5761 rows; marker `2026-09-15T04:31:45Z`
- `2026-09-15T04:30:30.919718Z` — **FUELHH**: 20 rows; marker `2026-09-15T04:30:00Z`
- `2026-09-15T04:30:30.919718Z` — **FUELINST**: 80 rows; marker `2026-09-15T04:30:00Z`
- `2026-09-15T04:30:14.833458Z` — **FREQ**: 5761 rows; marker `2026-09-15T04:29:45Z`
- `2026-09-15T04:28:22.052140Z` — **FREQ**: 5761 rows; marker `2026-09-15T04:27:45Z`
- `2026-09-15T04:26:14.639482Z` — **FREQ**: 5761 rows; marker `2026-09-15T04:25:45Z`
- `2026-09-15T04:25:42.720529Z` — **FUELINST**: 80 rows; marker `2026-09-15T04:25:00Z`
- `2026-09-15T04:24:15.927765Z` — **FREQ**: 5761 rows; marker `2026-09-15T04:23:45Z`
