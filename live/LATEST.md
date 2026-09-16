# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T09:51:49.099348Z`  
Current process started UTC: `2026-09-16T09:47:48.999816Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=0, z=-5.69 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-13885, delta=-1204, z=-7.82 -> demand pressure easing
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.27 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.52 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.55 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.57 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.60 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.63 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.66 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.69 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.73 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.76 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.79 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.83 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=49.972, delta=0, z=-3.86 -> frequency excursion; balancing stress check

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1404** (n=443, 2026-09-16T09:50:32.416153Z)
- `FUELINST|fuelType=NPSHYD|generation` = **354** (n=443, 2026-09-16T09:50:32.416153Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=443, 2026-09-16T09:50:32.416153Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=443, 2026-09-16T09:50:32.416153Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=443, 2026-09-16T09:50:32.416153Z)
- `FUELINST|fuelType=OTHER|generation` = **691** (n=443, 2026-09-16T09:50:32.416153Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=443, 2026-09-16T09:50:32.416153Z)
- `FUELINST|fuelType=WIND|generation` = **5617** (n=443, 2026-09-16T09:50:32.416153Z)
- `IMBALNGC|TOTAL|imbalance` = **5367** (n=73, 2026-09-16T09:49:11.404298Z)
- `INDDEM|TOTAL|demand` = **-13885** (n=73, 2026-09-16T09:49:11.404298Z)
- `INDGEN|TOTAL|generation` = **26005** (n=73, 2026-09-16T09:49:27.608942Z)
- `MELNGC|TOTAL|margin` = **34159** (n=73, 2026-09-16T09:48:39.518853Z)
- `NDF|TOTAL|demand` = **18514** (n=75, 2026-09-16T09:46:48.581530Z)
- `TSDF|TOTAL|demand` = **20638** (n=75, 2026-09-16T09:46:48.581530Z)
- `WINDFOR|TOTAL|generation` = **19327** (n=12, 2026-09-16T08:30:33.621364Z)

## Latest publication events

- `2026-09-16T09:50:32.416153Z` — **FUELINST**: 80 rows; marker `2026-09-16T09:50:00Z`
- `2026-09-16T09:50:32.416153Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:49:45Z`
- `2026-09-16T09:49:27.608942Z` — **INDGEN**: 648 rows; marker `2026-09-16T09:46:00Z`
- `2026-09-16T09:49:11.404298Z` — **INDDEM**: 648 rows; marker `2026-09-16T09:46:00Z`
- `2026-09-16T09:49:11.404298Z` — **IMBALNGC**: 648 rows; marker `2026-09-16T09:46:00Z`
- `2026-09-16T09:48:39.518853Z` — **MELNGC**: 648 rows; marker `2026-09-16T09:46:00Z`
- `2026-09-16T09:48:08.002709Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:47:45Z`
- `2026-09-16T09:46:48.581530Z` — **TSDF**: 648 rows; marker `2026-09-16T09:46:00Z`
- `2026-09-16T09:46:48.581530Z` — **NDF**: 36 rows; marker `2026-09-16T09:46:00Z`
- `2026-09-16T09:46:17.052872Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:45:45Z`
- `2026-09-16T09:45:29.042425Z` — **FUELINST**: 80 rows; marker `2026-09-16T09:45:00Z`
- `2026-09-16T09:44:09.677946Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:43:45Z`
- `2026-09-16T09:42:09.662751Z` — **MID**: 0 rows; marker `2026-09-16T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-16T09:42:09.662751Z` — **FREQ**: 5761 rows; marker `2026-09-16T09:41:45Z`
- `2026-09-16T09:40:32.829141Z` — **FUELINST**: 80 rows; marker `2026-09-16T09:40:00Z`
