# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T03:22:39.941739Z`  
Current process started UTC: `2026-09-15T03:18:39.983265Z`  
1-second metadata polls in this process: **233**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2672, delta=95, z=11.64 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1354** (n=77, 2026-09-15T03:20:31.870826Z)
- `FUELINST|fuelType=NPSHYD|generation` = **348** (n=77, 2026-09-15T03:20:31.870826Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=77, 2026-09-15T03:20:31.870826Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=77, 2026-09-15T03:20:31.870826Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=77, 2026-09-15T03:20:31.870826Z)
- `FUELINST|fuelType=OTHER|generation` = **351** (n=77, 2026-09-15T03:20:31.870826Z)
- `FUELINST|fuelType=PS|generation` = **-775** (n=77, 2026-09-15T03:20:31.870826Z)
- `FUELINST|fuelType=WIND|generation` = **13728** (n=77, 2026-09-15T03:20:31.870826Z)
- `IMBALNGC|TOTAL|imbalance` = **229** (n=14, 2026-09-15T03:21:03.261997Z)
- `INDDEM|TOTAL|demand` = **-12413** (n=14, 2026-09-15T03:21:03.261997Z)
- `INDGEN|TOTAL|generation` = **20713** (n=14, 2026-09-15T03:21:03.261997Z)
- `MELNGC|TOTAL|margin` = **34110** (n=14, 2026-09-15T03:20:15.578674Z)
- `NDF|TOTAL|demand` = **19934** (n=14, 2026-09-15T03:18:02.752215Z)
- `TSDF|TOTAL|demand` = **20485** (n=14, 2026-09-15T03:17:46.512016Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-15T03:22:06.931617Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:21:45Z`
- `2026-09-15T03:21:03.261997Z` — **INDGEN**: 882 rows; marker `2026-09-15T03:17:00Z`
- `2026-09-15T03:21:03.261997Z` — **INDDEM**: 882 rows; marker `2026-09-15T03:17:00Z`
- `2026-09-15T03:21:03.261997Z` — **IMBALNGC**: 882 rows; marker `2026-09-15T03:17:00Z`
- `2026-09-15T03:20:31.870826Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:20:00Z`
- `2026-09-15T03:20:15.578674Z` — **MELNGC**: 882 rows; marker `2026-09-15T03:17:00Z`
- `2026-09-15T03:20:15.578674Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:19:45Z`
- `2026-09-15T03:18:19.114335Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:17:45Z`
- `2026-09-15T03:18:02.752215Z` — **NDF**: 49 rows; marker `2026-09-15T03:17:00Z`
- `2026-09-15T03:17:46.512016Z` — **TSDF**: 882 rows; marker `2026-09-15T03:17:00Z`
- `2026-09-15T03:16:25.268400Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:15:45Z`
- `2026-09-15T03:15:53.033565Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:15:00Z`
- `2026-09-15T03:14:16.930122Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:13:45Z`
- `2026-09-15T03:12:08.767741Z` — **MID**: 0 rows; marker `2026-09-15T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T03:12:08.767741Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:11:45Z`
