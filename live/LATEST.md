# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T18:21:59.564487Z`  
Current process started UTC: `2026-09-20T18:17:59.222731Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=938, delta=-6, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=-1, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=947, delta=3, z=3.59 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=944, delta=66, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=944, delta=-1, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=945, delta=-1, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=2, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=944, delta=2, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=942, delta=62, z=3.67 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=878, delta=14, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=878, delta=1, z=3.50 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1622, 2026-09-20T18:20:23.606513Z)
- `FUELINST|fuelType=OTHER|generation` = **2569** (n=1622, 2026-09-20T18:20:23.606513Z)
- `FUELINST|fuelType=PS|generation` = **225** (n=1622, 2026-09-20T18:20:23.606513Z)
- `FUELINST|fuelType=WIND|generation` = **6440** (n=1622, 2026-09-20T18:20:23.606513Z)
- `IMBALNGC|TOTAL|imbalance` = **-5165** (n=266, 2026-09-20T17:52:50.677463Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=266, 2026-09-20T17:52:18.650341Z)
- `INDGEN|TOTAL|generation` = **15445** (n=266, 2026-09-20T17:52:18.650341Z)
- `MELNGC|TOTAL|margin` = **35430** (n=267, 2026-09-20T18:19:50.921827Z)
- `MID|dataProvider=APXMIDP|price` = **187.71** (n=6, 2026-09-20T18:12:19.744840Z)
- `MID|dataProvider=APXMIDP|volume` = **2330.9** (n=6, 2026-09-20T18:12:19.744840Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=12, 2026-09-20T18:12:19.744840Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=12, 2026-09-20T18:12:19.744840Z)
- `NDF|TOTAL|demand` = **20110** (n=273, 2026-09-20T18:17:59.222740Z)
- `TSDF|TOTAL|demand` = **20610** (n=273, 2026-09-20T18:17:59.222740Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T18:20:23.606513Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:20:00Z`
- `2026-09-20T18:20:23.606513Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:19:45Z`
- `2026-09-20T18:19:50.921827Z` — **MELNGC**: 1206 rows; marker `2026-09-20T18:17:00Z`
- `2026-09-20T18:18:15.254570Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:17:45Z`
- `2026-09-20T18:17:59.222740Z` — **TSDF**: 1206 rows; marker `2026-09-20T18:17:00Z`
- `2026-09-20T18:17:59.222740Z` — **NDF**: 67 rows; marker `2026-09-20T18:17:00Z`
- `2026-09-20T18:16:09.874209Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:15:45Z`
- `2026-09-20T18:15:21.582751Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:15:00Z`
- `2026-09-20T18:14:33.834087Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:13:45Z`
- `2026-09-20T18:12:19.744840Z` — **MID**: 2 rows; marker `2026-09-20T18:12:03Z`
- `2026-09-20T18:12:04.167014Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:11:45Z`
- `2026-09-20T18:10:27.589966Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:10:00Z`
- `2026-09-20T18:10:27.589966Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:09:45Z`
- `2026-09-20T18:08:20.597801Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:07:45Z`
- `2026-09-20T18:07:32.590804Z` — **MID**: 1 rows; marker `2026-09-20T18:05:00Z`
