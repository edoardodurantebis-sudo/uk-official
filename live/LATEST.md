# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T05:20:00.211526Z`  
Current process started UTC: `2026-09-15T05:16:00.342792Z`  
1-second metadata polls in this process: **234**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-452** (n=100, 2026-09-15T05:15:35.034834Z)
- `FUELINST|fuelType=NPSHYD|generation` = **444** (n=100, 2026-09-15T05:15:35.034834Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=100, 2026-09-15T05:15:35.034834Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=100, 2026-09-15T05:15:35.034834Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=100, 2026-09-15T05:15:35.034834Z)
- `FUELINST|fuelType=OTHER|generation` = **349** (n=100, 2026-09-15T05:15:35.034834Z)
- `FUELINST|fuelType=PS|generation` = **-815** (n=100, 2026-09-15T05:15:35.034834Z)
- `FUELINST|fuelType=WIND|generation` = **13585** (n=100, 2026-09-15T05:15:35.034834Z)
- `IMBALNGC|TOTAL|imbalance` = **-473** (n=17, 2026-09-15T04:50:51.091053Z)
- `INDDEM|TOTAL|demand` = **-12442** (n=17, 2026-09-15T04:50:51.091053Z)
- `INDGEN|TOTAL|generation` = **20012** (n=17, 2026-09-15T04:50:51.091053Z)
- `MELNGC|TOTAL|margin` = **33992** (n=18, 2026-09-15T05:19:31.055349Z)
- `NDF|TOTAL|demand` = **19934** (n=18, 2026-09-15T05:17:22.119466Z)
- `TSDF|TOTAL|demand` = **20484** (n=18, 2026-09-15T05:17:22.119466Z)
- `WINDFOR|TOTAL|generation` = **16388** (n=2, 2026-09-15T03:30:48.465743Z)

## Latest publication events

- `2026-09-15T05:19:31.055349Z` — **MELNGC**: 810 rows; marker `2026-09-15T05:17:00Z`
- `2026-09-15T05:18:27.084980Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:17:45Z`
- `2026-09-15T05:17:22.119466Z` — **TSDF**: 810 rows; marker `2026-09-15T05:17:00Z`
- `2026-09-15T05:17:22.119466Z` — **NDF**: 45 rows; marker `2026-09-15T05:17:00Z`
- `2026-09-15T05:16:16.344734Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:15:45Z`
- `2026-09-15T05:15:35.034834Z` — **FUELINST**: 80 rows; marker `2026-09-15T05:15:00Z`
- `2026-09-15T05:14:14.749567Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:13:45Z`
- `2026-09-15T05:12:21.224078Z` — **MID**: 0 rows; marker `2026-09-15T05:12:06Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T05:12:21.224078Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:11:45Z`
- `2026-09-15T05:10:34.800299Z` — **FUELINST**: 80 rows; marker `2026-09-15T05:10:00Z`
- `2026-09-15T05:10:19.408372Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:09:45Z`
- `2026-09-15T05:08:25.947092Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:07:45Z`
- `2026-09-15T05:06:23.175277Z` — **MID**: 0 rows; marker `2026-09-15T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T05:06:23.175277Z` — **FREQ**: 5761 rows; marker `2026-09-15T05:05:45Z`
- `2026-09-15T05:05:35.832536Z` — **FUELINST**: 80 rows; marker `2026-09-15T05:05:00Z`
