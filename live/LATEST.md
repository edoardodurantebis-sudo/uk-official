# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T16:18:48.497028Z`  
Current process started UTC: `2026-09-20T16:14:48.854041Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=878, delta=-1, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=879, delta=80, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-986, delta=2, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-983, delta=3, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.72 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-988, delta=26, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.79 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=2, z=-3.83 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1597, 2026-09-20T16:15:40.859749Z)
- `FUELINST|fuelType=OTHER|generation` = **691** (n=1597, 2026-09-20T16:15:40.859749Z)
- `FUELINST|fuelType=PS|generation` = **-13** (n=1597, 2026-09-20T16:15:40.859749Z)
- `FUELINST|fuelType=WIND|generation` = **8096** (n=1597, 2026-09-20T16:15:40.859749Z)
- `IMBALNGC|TOTAL|imbalance` = **-5166** (n=262, 2026-09-20T15:53:48.373221Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=262, 2026-09-20T15:53:48.373221Z)
- `INDGEN|TOTAL|generation` = **15444** (n=262, 2026-09-20T15:53:48.373221Z)
- `MELNGC|TOTAL|margin` = **35924** (n=262, 2026-09-20T15:50:41.761166Z)
- `MID|dataProvider=APXMIDP|price` = **103.7** (n=2, 2026-09-20T16:12:12.901791Z)
- `MID|dataProvider=APXMIDP|volume` = **3820.3** (n=2, 2026-09-20T16:12:12.901791Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=4, 2026-09-20T16:12:12.901791Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=4, 2026-09-20T16:12:12.901791Z)
- `NDF|TOTAL|demand` = **20110** (n=269, 2026-09-20T16:17:48.642120Z)
- `TSDF|TOTAL|demand` = **20610** (n=269, 2026-09-20T16:17:48.642120Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T16:18:20.877546Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:17:45Z`
- `2026-09-20T16:17:48.642120Z` — **TSDF**: 1278 rows; marker `2026-09-20T16:17:00Z`
- `2026-09-20T16:17:48.642120Z` — **NDF**: 71 rows; marker `2026-09-20T16:17:00Z`
- `2026-09-20T16:16:12.592462Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:15:45Z`
- `2026-09-20T16:15:40.859749Z` — **FUELINST**: 80 rows; marker `2026-09-20T16:15:00Z`
- `2026-09-20T16:14:20.843065Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:13:45Z`
- `2026-09-20T16:12:28.997324Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:11:45Z`
- `2026-09-20T16:12:12.901791Z` — **MID**: 2 rows; marker `2026-09-20T16:12:04Z`
- `2026-09-20T16:10:36.932020Z` — **FUELINST**: 80 rows; marker `2026-09-20T16:10:00Z`
- `2026-09-20T16:10:36.932020Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:09:45Z`
- `2026-09-20T16:08:20.700005Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:07:45Z`
- `2026-09-20T16:06:29.397052Z` — **MID**: 1 rows; marker `2026-09-20T16:05:00Z`
- `2026-09-20T16:06:29.397052Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:05:45Z`
- `2026-09-20T16:05:41.389951Z` — **FUELINST**: 80 rows; marker `2026-09-20T16:05:00Z`
- `2026-09-20T16:04:21.704954Z` — **FREQ**: 5761 rows; marker `2026-09-20T16:03:45Z`
