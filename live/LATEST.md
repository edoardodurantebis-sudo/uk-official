# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T17:18:48.795592Z`  
Current process started UTC: `2026-09-20T17:14:48.523185Z`  
1-second metadata polls in this process: **220**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.65 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1609, 2026-09-20T17:15:20.528110Z)
- `FUELINST|fuelType=OTHER|generation` = **1340** (n=1609, 2026-09-20T17:15:20.528110Z)
- `FUELINST|fuelType=PS|generation` = **167** (n=1609, 2026-09-20T17:15:20.528110Z)
- `FUELINST|fuelType=WIND|generation` = **7417** (n=1609, 2026-09-20T17:15:20.528110Z)
- `IMBALNGC|TOTAL|imbalance` = **-5190** (n=264, 2026-09-20T16:52:33.552792Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=264, 2026-09-20T16:52:33.552792Z)
- `INDGEN|TOTAL|generation` = **15420** (n=264, 2026-09-20T16:52:33.552792Z)
- `MELNGC|TOTAL|margin` = **35884** (n=264, 2026-09-20T16:50:09.583962Z)
- `MID|dataProvider=APXMIDP|price` = **175.57** (n=4, 2026-09-20T17:12:15.723267Z)
- `MID|dataProvider=APXMIDP|volume` = **3681.2** (n=4, 2026-09-20T17:12:15.723267Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=8, 2026-09-20T17:12:15.723267Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=8, 2026-09-20T17:12:15.723267Z)
- `NDF|TOTAL|demand` = **20110** (n=271, 2026-09-20T17:18:04.107232Z)
- `TSDF|TOTAL|demand` = **20610** (n=271, 2026-09-20T17:18:19.603936Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T17:18:19.603936Z` — **TSDF**: 1242 rows; marker `2026-09-20T17:17:00Z`
- `2026-09-20T17:18:04.107232Z` — **NDF**: 69 rows; marker `2026-09-20T17:17:00Z`
- `2026-09-20T17:18:04.107232Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:17:45Z`
- `2026-09-20T17:16:07.154128Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:15:45Z`
- `2026-09-20T17:15:20.528110Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:15:00Z`
- `2026-09-20T17:14:07.506770Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:13:45Z`
- `2026-09-20T17:12:15.723267Z` — **MID**: 2 rows; marker `2026-09-20T17:12:03Z`
- `2026-09-20T17:12:15.723267Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:11:45Z`
- `2026-09-20T17:10:22.638392Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:10:00Z`
- `2026-09-20T17:10:06.815289Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:09:45Z`
- `2026-09-20T17:07:59.306764Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:07:45Z`
- `2026-09-20T17:06:23.542943Z` — **MID**: 1 rows; marker `2026-09-20T17:05:00Z`
- `2026-09-20T17:06:23.542943Z` — **FUELINST**: 80 rows; marker `2026-09-20T17:05:00Z`
- `2026-09-20T17:06:23.542943Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:05:45Z`
- `2026-09-20T17:04:23.117430Z` — **FREQ**: 5761 rows; marker `2026-09-20T17:03:45Z`
