# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T15:57:48.630380Z`  
Current process started UTC: `2026-09-20T15:53:48.373213Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-989, delta=24, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.13 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1593, 2026-09-20T15:55:41.232473Z)
- `FUELINST|fuelType=OTHER|generation` = **1138** (n=1593, 2026-09-20T15:55:41.232473Z)
- `FUELINST|fuelType=PS|generation` = **-16** (n=1593, 2026-09-20T15:55:41.232473Z)
- `FUELINST|fuelType=WIND|generation` = **8622** (n=1593, 2026-09-20T15:55:41.232473Z)
- `IMBALNGC|TOTAL|imbalance` = **-5166** (n=262, 2026-09-20T15:53:48.373221Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=262, 2026-09-20T15:53:48.373221Z)
- `INDGEN|TOTAL|generation` = **15444** (n=262, 2026-09-20T15:53:48.373221Z)
- `MELNGC|TOTAL|margin` = **35924** (n=262, 2026-09-20T15:50:41.761166Z)
- `MID|dataProvider=APXMIDP|price` = **38.19** (n=1, 2026-09-20T15:42:15.990925Z)
- `MID|dataProvider=APXMIDP|volume` = **3728.5** (n=1, 2026-09-20T15:42:15.990925Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=2, 2026-09-20T15:42:15.990925Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=2, 2026-09-20T15:42:15.990925Z)
- `NDF|TOTAL|demand` = **20110** (n=268, 2026-09-20T15:48:01.819270Z)
- `TSDF|TOTAL|demand` = **20610** (n=268, 2026-09-20T15:48:01.819270Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T15:56:12.778812Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:55:45Z`
- `2026-09-20T15:55:41.232473Z` — **FUELINST**: 80 rows; marker `2026-09-20T15:55:00Z`
- `2026-09-20T15:54:20.957811Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:53:45Z`
- `2026-09-20T15:53:48.373221Z` — **INDGEN**: 1296 rows; marker `2026-09-20T15:47:00Z`
- `2026-09-20T15:53:48.373221Z` — **INDDEM**: 1296 rows; marker `2026-09-20T15:47:00Z`
- `2026-09-20T15:53:48.373221Z` — **IMBALNGC**: 1296 rows; marker `2026-09-20T15:47:00Z`
- `2026-09-20T15:52:34.577895Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:51:45Z`
- `2026-09-20T15:50:41.761166Z` — **MELNGC**: 1296 rows; marker `2026-09-20T15:47:00Z`
- `2026-09-20T15:50:25.130116Z` — **FUELINST**: 80 rows; marker `2026-09-20T15:50:00Z`
- `2026-09-20T15:50:09.454789Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:49:45Z`
- `2026-09-20T15:48:17.817075Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:47:45Z`
- `2026-09-20T15:48:01.819270Z` — **TSDF**: 1296 rows; marker `2026-09-20T15:47:00Z`
- `2026-09-20T15:48:01.819270Z` — **NDF**: 72 rows; marker `2026-09-20T15:47:00Z`
- `2026-09-20T15:46:09.589596Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:45:45Z`
- `2026-09-20T15:45:37.531075Z` — **FUELINST**: 80 rows; marker `2026-09-20T15:45:00Z`
