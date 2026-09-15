# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T03:56:09.071916Z`  
Current process started UTC: `2026-09-15T03:52:09.022153Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1354** (n=84, 2026-09-15T03:55:41.216719Z)
- `FUELINST|fuelType=NPSHYD|generation` = **351** (n=84, 2026-09-15T03:55:41.216719Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=84, 2026-09-15T03:55:41.216719Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=84, 2026-09-15T03:55:41.216719Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=84, 2026-09-15T03:55:41.216719Z)
- `FUELINST|fuelType=OTHER|generation` = **299** (n=84, 2026-09-15T03:55:41.216719Z)
- `FUELINST|fuelType=PS|generation` = **-319** (n=84, 2026-09-15T03:55:41.216719Z)
- `FUELINST|fuelType=WIND|generation` = **13950** (n=84, 2026-09-15T03:55:41.216719Z)
- `IMBALNGC|TOTAL|imbalance` = **-315** (n=15, 2026-09-15T03:51:09.251010Z)
- `INDDEM|TOTAL|demand` = **-12414** (n=15, 2026-09-15T03:50:53.265546Z)
- `INDGEN|TOTAL|generation` = **20170** (n=15, 2026-09-15T03:50:53.265546Z)
- `MELNGC|TOTAL|margin` = **34094** (n=15, 2026-09-15T03:49:33.636617Z)
- `NDF|TOTAL|demand` = **19934** (n=15, 2026-09-15T03:47:22.559174Z)
- `TSDF|TOTAL|demand` = **20485** (n=15, 2026-09-15T03:47:22.559174Z)
- `WINDFOR|TOTAL|generation` = **16388** (n=2, 2026-09-15T03:30:48.465743Z)

## Latest publication events

- `2026-09-15T03:55:41.216719Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:55:00Z`
- `2026-09-15T03:54:05.194914Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:53:45Z`
- `2026-09-15T03:52:13.022657Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:51:45Z`
- `2026-09-15T03:51:09.251010Z` — **IMBALNGC**: 864 rows; marker `2026-09-15T03:47:00Z`
- `2026-09-15T03:50:53.265546Z` — **INDGEN**: 864 rows; marker `2026-09-15T03:46:00Z`
- `2026-09-15T03:50:53.265546Z` — **INDDEM**: 864 rows; marker `2026-09-15T03:46:00Z`
- `2026-09-15T03:50:37.263297Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:50:00Z`
- `2026-09-15T03:50:21.763388Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:49:45Z`
- `2026-09-15T03:49:33.636617Z` — **MELNGC**: 864 rows; marker `2026-09-15T03:47:00Z`
- `2026-09-15T03:48:30.254041Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:47:45Z`
- `2026-09-15T03:47:22.559174Z` — **TSDF**: 864 rows; marker `2026-09-15T03:47:00Z`
- `2026-09-15T03:47:22.559174Z` — **NDF**: 48 rows; marker `2026-09-15T03:47:00Z`
- `2026-09-15T03:46:18.985286Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:45:45Z`
- `2026-09-15T03:45:30.490123Z` — **FUELINST**: 80 rows; marker `2026-09-15T03:45:00Z`
- `2026-09-15T03:44:25.766617Z` — **FREQ**: 5761 rows; marker `2026-09-15T03:43:45Z`
