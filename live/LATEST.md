# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T18:09:24.808670Z`  
Current process started UTC: `2026-09-20T18:05:24.959708Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1619, 2026-09-20T18:05:24.959719Z)
- `FUELINST|fuelType=OTHER|generation` = **2170** (n=1619, 2026-09-20T18:05:24.959719Z)
- `FUELINST|fuelType=PS|generation` = **530** (n=1619, 2026-09-20T18:05:24.959719Z)
- `FUELINST|fuelType=WIND|generation` = **6542** (n=1619, 2026-09-20T18:05:24.959719Z)
- `IMBALNGC|TOTAL|imbalance` = **-5165** (n=266, 2026-09-20T17:52:50.677463Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=266, 2026-09-20T17:52:18.650341Z)
- `INDGEN|TOTAL|generation` = **15445** (n=266, 2026-09-20T17:52:18.650341Z)
- `MELNGC|TOTAL|margin` = **35460** (n=266, 2026-09-20T17:49:55.213597Z)
- `MID|dataProvider=APXMIDP|price` = **179.7** (n=5, 2026-09-20T17:42:05.140675Z)
- `MID|dataProvider=APXMIDP|volume` = **2886.4** (n=5, 2026-09-20T17:42:05.140675Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=11, 2026-09-20T18:07:32.590804Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=11, 2026-09-20T18:07:32.590804Z)
- `NDF|TOTAL|demand` = **20110** (n=272, 2026-09-20T17:47:56.042158Z)
- `TSDF|TOTAL|demand` = **20610** (n=272, 2026-09-20T17:47:56.042158Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T18:08:20.597801Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:07:45Z`
- `2026-09-20T18:07:32.590804Z` — **MID**: 1 rows; marker `2026-09-20T18:05:00Z`
- `2026-09-20T18:06:13.060426Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:05:45Z`
- `2026-09-20T18:05:24.959719Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:05:00Z`
- `2026-09-20T18:04:11.353857Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:03:45Z`
- `2026-09-20T18:02:17.925110Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:01:45Z`
- `2026-09-20T18:00:42.299682Z` — **FUELHH**: 20 rows; marker `2026-09-20T18:00:00Z`
- `2026-09-20T18:00:42.299682Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:00:00Z`
- `2026-09-20T18:00:10.000716Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:59:45Z`
- `2026-09-20T17:58:02.295012Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:57:45Z`
- `2026-09-20T17:56:20.439741Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:55:45Z`
- `2026-09-20T17:55:15.276619Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:55:00Z`
- `2026-09-20T17:54:27.215176Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:53:45Z`
- `2026-09-20T17:52:50.677463Z` — **IMBALNGC**: 1224 rows; marker `2026-09-20T17:47:00Z`
- `2026-09-20T17:52:18.650341Z` — **INDGEN**: 1224 rows; marker `2026-09-20T17:47:00Z`
