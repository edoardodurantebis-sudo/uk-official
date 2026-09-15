# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T02:44:53.485667Z`  
Current process started UTC: `2026-09-15T02:40:53.514987Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2560, delta=-26, z=-2.39 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-367** (n=69, 2026-09-15T02:40:25.323685Z)
- `FUELINST|fuelType=NPSHYD|generation` = **337** (n=69, 2026-09-15T02:40:25.323685Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=69, 2026-09-15T02:40:25.323685Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=69, 2026-09-15T02:40:25.323685Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=69, 2026-09-15T02:40:25.323685Z)
- `FUELINST|fuelType=OTHER|generation` = **462** (n=69, 2026-09-15T02:40:25.323685Z)
- `FUELINST|fuelType=PS|generation` = **-417** (n=69, 2026-09-15T02:40:25.323685Z)
- `FUELINST|fuelType=WIND|generation` = **12483** (n=69, 2026-09-15T02:40:25.323685Z)
- `IMBALNGC|TOTAL|imbalance` = **247** (n=12, 2026-09-15T02:20:48.688934Z)
- `INDDEM|TOTAL|demand` = **-12319** (n=12, 2026-09-15T02:20:32.984280Z)
- `INDGEN|TOTAL|generation` = **20732** (n=12, 2026-09-15T02:20:32.984280Z)
- `MELNGC|TOTAL|margin` = **34104** (n=12, 2026-09-15T02:19:28.123721Z)
- `NDF|TOTAL|demand` = **19934** (n=12, 2026-09-15T02:17:36.288258Z)
- `TSDF|TOTAL|demand` = **20485** (n=12, 2026-09-15T02:17:36.288258Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-15T02:44:09.790541Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:43:45Z`
- `2026-09-15T02:42:17.522229Z` — **MID**: 0 rows; marker `2026-09-15T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T02:42:17.522229Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:41:45Z`
- `2026-09-15T02:40:25.323685Z` — **FUELINST**: 80 rows; marker `2026-09-15T02:40:00Z`
- `2026-09-15T02:40:25.323685Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:39:45Z`
- `2026-09-15T02:38:18.067969Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:37:45Z`
- `2026-09-15T02:36:41.518016Z` — **MID**: 0 rows; marker `2026-09-15T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T02:36:17.519928Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:35:45Z`
- `2026-09-15T02:35:29.397843Z` — **FUELINST**: 80 rows; marker `2026-09-15T02:35:00Z`
- `2026-09-15T02:34:09.771458Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:33:45Z`
- `2026-09-15T02:32:18.014523Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:31:45Z`
- `2026-09-15T02:30:42.002804Z` — **FUELHH**: 20 rows; marker `2026-09-15T02:30:00Z`
- `2026-09-15T02:30:42.002804Z` — **FUELINST**: 80 rows; marker `2026-09-15T02:30:00Z`
- `2026-09-15T02:30:26.523266Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:29:45Z`
- `2026-09-15T02:28:18.661026Z` — **FREQ**: 5761 rows; marker `2026-09-15T02:27:45Z`
