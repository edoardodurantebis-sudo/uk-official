# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T17:48:24.187440Z`  
Current process started UTC: `2026-09-20T17:44:24.803381Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=877, delta=0, z=3.51 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=864, delta=502, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=877, delta=-1, z=3.53 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1615, 2026-09-20T17:45:43.101401Z)
- `FUELINST|fuelType=OTHER|generation` = **1738** (n=1615, 2026-09-20T17:45:43.101401Z)
- `FUELINST|fuelType=PS|generation` = **-14** (n=1615, 2026-09-20T17:45:43.101401Z)
- `FUELINST|fuelType=WIND|generation` = **6971** (n=1615, 2026-09-20T17:45:43.101401Z)
- `IMBALNGC|TOTAL|imbalance` = **-5172** (n=265, 2026-09-20T17:22:30.619450Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=265, 2026-09-20T17:22:15.156949Z)
- `INDGEN|TOTAL|generation` = **15438** (n=265, 2026-09-20T17:22:15.156949Z)
- `MELNGC|TOTAL|margin` = **35785** (n=265, 2026-09-20T17:20:21.229759Z)
- `MID|dataProvider=APXMIDP|price` = **179.7** (n=5, 2026-09-20T17:42:05.140675Z)
- `MID|dataProvider=APXMIDP|volume` = **2886.4** (n=5, 2026-09-20T17:42:05.140675Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=10, 2026-09-20T17:42:05.140675Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=10, 2026-09-20T17:42:05.140675Z)
- `NDF|TOTAL|demand` = **20110** (n=272, 2026-09-20T17:47:56.042158Z)
- `TSDF|TOTAL|demand` = **20610** (n=272, 2026-09-20T17:47:56.042158Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T17:47:56.042158Z` — **TSDF**: 1224 rows; marker `2026-09-20T17:47:00Z`
- `2026-09-20T17:47:56.042158Z` — **NDF**: 68 rows; marker `2026-09-20T17:47:00Z`
- `2026-09-20T17:46:20.157347Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:45:45Z`
- `2026-09-20T17:45:43.101401Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:45:00Z`
- `2026-09-20T17:44:24.803388Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:43:45Z`
- `2026-09-20T17:42:21.009828Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:41:45Z`
- `2026-09-20T17:42:05.140675Z` — **MID**: 2 rows; marker `2026-09-20T17:42:03Z`
- `2026-09-20T17:40:29.242278Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:40:00Z`
- `2026-09-20T17:40:13.260269Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:39:45Z`
- `2026-09-20T17:38:21.671408Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:37:45Z`
- `2026-09-20T17:36:30.173200Z` — **MID**: 1 rows; marker `2026-09-20T17:35:00Z`
- `2026-09-20T17:36:14.781906Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:35:45Z`
- `2026-09-20T17:35:27.911886Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:35:00Z`
- `2026-09-20T17:34:23.822120Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:33:45Z`
- `2026-09-20T17:32:15.694966Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:31:45Z`
