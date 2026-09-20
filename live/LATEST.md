# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T17:10:24.157636Z`  
Current process started UTC: `2026-09-20T17:06:23.542933Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.67 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1608, 2026-09-20T17:10:22.638392Z)
- `FUELINST|fuelType=OTHER|generation` = **1107** (n=1608, 2026-09-20T17:10:22.638392Z)
- `FUELINST|fuelType=PS|generation` = **62** (n=1608, 2026-09-20T17:10:22.638392Z)
- `FUELINST|fuelType=WIND|generation` = **7740** (n=1608, 2026-09-20T17:10:22.638392Z)
- `IMBALNGC|TOTAL|imbalance` = **-5190** (n=264, 2026-09-20T16:52:33.552792Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=264, 2026-09-20T16:52:33.552792Z)
- `INDGEN|TOTAL|generation` = **15420** (n=264, 2026-09-20T16:52:33.552792Z)
- `MELNGC|TOTAL|margin` = **35884** (n=264, 2026-09-20T16:50:09.583962Z)
- `MID|dataProvider=APXMIDP|price` = **134.16** (n=3, 2026-09-20T16:42:18.136782Z)
- `MID|dataProvider=APXMIDP|volume` = **3510.2** (n=3, 2026-09-20T16:42:18.136782Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=7, 2026-09-20T17:06:23.542943Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=7, 2026-09-20T17:06:23.542943Z)
- `NDF|TOTAL|demand` = **20110** (n=270, 2026-09-20T16:47:45.958775Z)
- `TSDF|TOTAL|demand` = **20610** (n=270, 2026-09-20T16:47:45.958775Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T17:10:22.638392Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:10:00Z`
- `2026-09-20T17:10:06.815289Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:09:45Z`
- `2026-09-20T17:07:59.306764Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:07:45Z`
- `2026-09-20T17:06:23.542943Z` — **MID**: 1 rows; marker `2026-09-20T17:05:00Z`
- `2026-09-20T17:06:23.542943Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:05:00Z`
- `2026-09-20T17:06:23.542943Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:05:45Z`
- `2026-09-20T17:04:23.117430Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:03:45Z`
- `2026-09-20T17:02:15.366814Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:01:45Z`
- `2026-09-20T17:00:38.211022Z` — **FUELHH**: 20 rows; marker `2026-09-20T17:00:00Z`
- `2026-09-20T17:00:38.211022Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:00:00Z`
- `2026-09-20T17:00:22.823468Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:59:45Z`
- `2026-09-20T16:58:14.074717Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:57:45Z`
- `2026-09-20T16:56:27.100418Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:55:45Z`
- `2026-09-20T16:55:39.672188Z` — **FUELINST**: 80 rows; marker `2026-09-20T16:55:00Z`
- `2026-09-20T16:54:18.433013Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:53:45Z`
