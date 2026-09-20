# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T17:39:59.116465Z`  
Current process started UTC: `2026-09-20T17:35:58.779617Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=877, delta=0, z=3.51 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=864, delta=502, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=877, delta=-1, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=878, delta=1, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=877, delta=-1, z=3.56 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1613, 2026-09-20T17:35:27.911886Z)
- `FUELINST|fuelType=OTHER|generation` = **1534** (n=1613, 2026-09-20T17:35:27.911886Z)
- `FUELINST|fuelType=PS|generation` = **208** (n=1613, 2026-09-20T17:35:27.911886Z)
- `FUELINST|fuelType=WIND|generation` = **7092** (n=1613, 2026-09-20T17:35:27.911886Z)
- `IMBALNGC|TOTAL|imbalance` = **-5172** (n=265, 2026-09-20T17:22:30.619450Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=265, 2026-09-20T17:22:15.156949Z)
- `INDGEN|TOTAL|generation` = **15438** (n=265, 2026-09-20T17:22:15.156949Z)
- `MELNGC|TOTAL|margin` = **35785** (n=265, 2026-09-20T17:20:21.229759Z)
- `MID|dataProvider=APXMIDP|price` = **175.57** (n=4, 2026-09-20T17:12:15.723267Z)
- `MID|dataProvider=APXMIDP|volume` = **3681.2** (n=4, 2026-09-20T17:12:15.723267Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=9, 2026-09-20T17:36:30.173200Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=9, 2026-09-20T17:36:30.173200Z)
- `NDF|TOTAL|demand` = **20110** (n=271, 2026-09-20T17:18:04.107232Z)
- `TSDF|TOTAL|demand` = **20610** (n=271, 2026-09-20T17:18:19.603936Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T17:38:21.671408Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:37:45Z`
- `2026-09-20T17:36:30.173200Z` — **MID**: 1 rows; marker `2026-09-20T17:35:00Z`
- `2026-09-20T17:36:14.781906Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:35:45Z`
- `2026-09-20T17:35:27.911886Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:35:00Z`
- `2026-09-20T17:34:23.822120Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:33:45Z`
- `2026-09-20T17:32:15.694966Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:31:45Z`
- `2026-09-20T17:30:37.607812Z` — **FUELHH**: 20 rows; marker `2026-09-20T17:30:00Z`
- `2026-09-20T17:30:37.607812Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:30:00Z`
- `2026-09-20T17:30:21.429184Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:29:45Z`
- `2026-09-20T17:28:12.184902Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:27:45Z`
- `2026-09-20T17:26:09.583823Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:25:45Z`
- `2026-09-20T17:25:20.387502Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:25:00Z`
- `2026-09-20T17:24:16.187404Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:23:45Z`
- `2026-09-20T17:22:30.619450Z` — **IMBALNGC**: 1242 rows; marker `2026-09-20T17:17:00Z`
- `2026-09-20T17:22:15.156949Z` — **INDGEN**: 1242 rows; marker `2026-09-20T17:17:00Z`
