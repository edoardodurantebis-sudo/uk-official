# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T17:23:00.690204Z`  
Current process started UTC: `2026-09-20T17:19:01.222001Z`  
1-second metadata polls in this process: **233**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=2, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=944, delta=2, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=942, delta=62, z=3.67 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=878, delta=14, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=878, delta=1, z=3.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=877, delta=0, z=3.51 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=864, delta=502, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=877, delta=-1, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=878, delta=1, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=877, delta=-1, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=878, delta=-1, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=879, delta=80, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-986, delta=2, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-983, delta=3, z=-3.62 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1610, 2026-09-20T17:20:21.229759Z)
- `FUELINST|fuelType=OTHER|generation` = **1358** (n=1610, 2026-09-20T17:20:21.229759Z)
- `FUELINST|fuelType=PS|generation` = **213** (n=1610, 2026-09-20T17:20:21.229759Z)
- `FUELINST|fuelType=WIND|generation` = **7302** (n=1610, 2026-09-20T17:20:21.229759Z)
- `IMBALNGC|TOTAL|imbalance` = **-5172** (n=265, 2026-09-20T17:22:30.619450Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=265, 2026-09-20T17:22:15.156949Z)
- `INDGEN|TOTAL|generation` = **15438** (n=265, 2026-09-20T17:22:15.156949Z)
- `MELNGC|TOTAL|margin` = **35785** (n=265, 2026-09-20T17:20:21.229759Z)
- `MID|dataProvider=APXMIDP|price` = **175.57** (n=4, 2026-09-20T17:12:15.723267Z)
- `MID|dataProvider=APXMIDP|volume` = **3681.2** (n=4, 2026-09-20T17:12:15.723267Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=8, 2026-09-20T17:12:15.723267Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=8, 2026-09-20T17:12:15.723267Z)
- `NDF|TOTAL|demand` = **20110** (n=271, 2026-09-20T17:18:04.107232Z)
- `TSDF|TOTAL|demand` = **20610** (n=271, 2026-09-20T17:18:19.603936Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T17:22:30.619450Z` — **IMBALNGC**: 1242 rows; marker `2026-09-20T17:17:00Z`
- `2026-09-20T17:22:15.156949Z` — **INDGEN**: 1242 rows; marker `2026-09-20T17:17:00Z`
- `2026-09-20T17:22:15.156949Z` — **INDDEM**: 1242 rows; marker `2026-09-20T17:17:00Z`
- `2026-09-20T17:22:15.156949Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:21:45Z`
- `2026-09-20T17:20:37.482687Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:19:45Z`
- `2026-09-20T17:20:21.229759Z` — **MELNGC**: 1242 rows; marker `2026-09-20T17:17:00Z`
- `2026-09-20T17:20:21.229759Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:20:00Z`
- `2026-09-20T17:18:19.603936Z` — **TSDF**: 1242 rows; marker `2026-09-20T17:17:00Z`
- `2026-09-20T17:18:04.107232Z` — **NDF**: 69 rows; marker `2026-09-20T17:17:00Z`
- `2026-09-20T17:18:04.107232Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:17:45Z`
- `2026-09-20T17:16:07.154128Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:15:45Z`
- `2026-09-20T17:15:20.528110Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:15:00Z`
- `2026-09-20T17:14:07.506770Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:13:45Z`
- `2026-09-20T17:12:15.723267Z` — **MID**: 2 rows; marker `2026-09-20T17:12:03Z`
- `2026-09-20T17:12:15.723267Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:11:45Z`
