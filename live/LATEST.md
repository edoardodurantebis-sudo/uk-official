# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T18:26:11.515218Z`  
Current process started UTC: `2026-09-20T18:22:11.511120Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2756, delta=187, z=3.80 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1623, 2026-09-20T18:25:38.701470Z)
- `FUELINST|fuelType=OTHER|generation` = **2756** (n=1623, 2026-09-20T18:25:38.701470Z)
- `FUELINST|fuelType=PS|generation` = **222** (n=1623, 2026-09-20T18:25:38.701470Z)
- `FUELINST|fuelType=WIND|generation` = **6303** (n=1623, 2026-09-20T18:25:38.701470Z)
- `IMBALNGC|TOTAL|imbalance` = **-5158** (n=267, 2026-09-20T18:22:27.571295Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=267, 2026-09-20T18:22:11.511126Z)
- `INDGEN|TOTAL|generation` = **15452** (n=267, 2026-09-20T18:22:11.511126Z)
- `MELNGC|TOTAL|margin` = **35430** (n=267, 2026-09-20T18:19:50.921827Z)
- `MID|dataProvider=APXMIDP|price` = **187.71** (n=6, 2026-09-20T18:12:19.744840Z)
- `MID|dataProvider=APXMIDP|volume` = **2330.9** (n=6, 2026-09-20T18:12:19.744840Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=12, 2026-09-20T18:12:19.744840Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=12, 2026-09-20T18:12:19.744840Z)
- `NDF|TOTAL|demand` = **20110** (n=273, 2026-09-20T18:17:59.222740Z)
- `TSDF|TOTAL|demand` = **20610** (n=273, 2026-09-20T18:17:59.222740Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T18:25:38.701470Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:25:00Z`
- `2026-09-20T18:24:19.036558Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:23:45Z`
- `2026-09-20T18:22:27.571295Z` — **IMBALNGC**: 1206 rows; marker `2026-09-20T18:17:00Z`
- `2026-09-20T18:22:11.511126Z` — **INDGEN**: 1206 rows; marker `2026-09-20T18:17:00Z`
- `2026-09-20T18:22:11.511126Z` — **INDDEM**: 1206 rows; marker `2026-09-20T18:17:00Z`
- `2026-09-20T18:22:11.511126Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:21:45Z`
- `2026-09-20T18:20:23.606513Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:20:00Z`
- `2026-09-20T18:20:23.606513Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:19:45Z`
- `2026-09-20T18:19:50.921827Z` — **MELNGC**: 1206 rows; marker `2026-09-20T18:17:00Z`
- `2026-09-20T18:18:15.254570Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:17:45Z`
- `2026-09-20T18:17:59.222740Z` — **TSDF**: 1206 rows; marker `2026-09-20T18:17:00Z`
- `2026-09-20T18:17:59.222740Z` — **NDF**: 67 rows; marker `2026-09-20T18:17:00Z`
- `2026-09-20T18:16:09.874209Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:15:45Z`
- `2026-09-20T18:15:21.582751Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:15:00Z`
- `2026-09-20T18:14:33.834087Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:13:45Z`
