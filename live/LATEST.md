# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T18:38:52.724939Z`  
Current process started UTC: `2026-09-20T18:34:52.790611Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2791, delta=35, z=3.85 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1625, 2026-09-20T18:35:40.953739Z)
- `FUELINST|fuelType=OTHER|generation` = **2488** (n=1625, 2026-09-20T18:35:40.953739Z)
- `FUELINST|fuelType=PS|generation` = **222** (n=1625, 2026-09-20T18:35:40.953739Z)
- `FUELINST|fuelType=WIND|generation` = **6053** (n=1625, 2026-09-20T18:35:40.953739Z)
- `IMBALNGC|TOTAL|imbalance` = **-5158** (n=267, 2026-09-20T18:22:27.571295Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=267, 2026-09-20T18:22:11.511126Z)
- `INDGEN|TOTAL|generation` = **15452** (n=267, 2026-09-20T18:22:11.511126Z)
- `MELNGC|TOTAL|margin` = **35430** (n=267, 2026-09-20T18:19:50.921827Z)
- `MID|dataProvider=APXMIDP|price` = **187.71** (n=6, 2026-09-20T18:12:19.744840Z)
- `MID|dataProvider=APXMIDP|volume` = **2330.9** (n=6, 2026-09-20T18:12:19.744840Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=13, 2026-09-20T18:36:28.337347Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=13, 2026-09-20T18:36:28.337347Z)
- `NDF|TOTAL|demand` = **20110** (n=273, 2026-09-20T18:17:59.222740Z)
- `TSDF|TOTAL|demand` = **20610** (n=273, 2026-09-20T18:17:59.222740Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T18:38:20.007302Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:37:45Z`
- `2026-09-20T18:36:28.337347Z` — **MID**: 1 rows; marker `2026-09-20T18:35:00Z`
- `2026-09-20T18:36:28.337347Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:35:45Z`
- `2026-09-20T18:35:40.953739Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:35:00Z`
- `2026-09-20T18:34:20.661220Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:33:45Z`
- `2026-09-20T18:32:28.482470Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:31:45Z`
- `2026-09-20T18:30:35.886091Z` — **FUELHH**: 20 rows; marker `2026-09-20T18:30:00Z`
- `2026-09-20T18:30:35.886091Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:30:00Z`
- `2026-09-20T18:30:35.886091Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:29:45Z`
- `2026-09-20T18:28:15.880774Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:27:45Z`
- `2026-09-20T18:26:23.600221Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:25:45Z`
- `2026-09-20T18:25:38.701470Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:25:00Z`
- `2026-09-20T18:24:19.036558Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:23:45Z`
- `2026-09-20T18:22:27.571295Z` — **IMBALNGC**: 1206 rows; marker `2026-09-20T18:17:00Z`
- `2026-09-20T18:22:11.511126Z` — **INDGEN**: 1206 rows; marker `2026-09-20T18:17:00Z`
