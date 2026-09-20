# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T15:40:27.512700Z`  
Current process started UTC: `2026-09-20T15:36:27.945048Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1589, 2026-09-20T15:35:46.247772Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1589, 2026-09-20T15:35:46.247772Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1589, 2026-09-20T15:35:46.247772Z)
- `FUELINST|fuelType=OTHER|generation` = **646** (n=1589, 2026-09-20T15:35:46.247772Z)
- `FUELINST|fuelType=PS|generation` = **-34** (n=1589, 2026-09-20T15:35:46.247772Z)
- `FUELINST|fuelType=WIND|generation` = **8675** (n=1589, 2026-09-20T15:35:46.247772Z)
- `IMBALNGC|TOTAL|imbalance` = **-5160** (n=261, 2026-09-20T15:23:28.329195Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=261, 2026-09-20T15:23:11.331116Z)
- `INDGEN|TOTAL|generation` = **15450** (n=261, 2026-09-20T15:23:11.331116Z)
- `MELNGC|TOTAL|margin` = **35924** (n=261, 2026-09-20T15:20:29.348401Z)
- `NDF|TOTAL|demand` = **20110** (n=267, 2026-09-20T15:17:54.992847Z)
- `TSDF|TOTAL|demand` = **20610** (n=267, 2026-09-20T15:17:54.992847Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=1, 2026-09-20T15:36:27.945056Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=1, 2026-09-20T15:36:27.945056Z)

## Latest publication events

- `2026-09-20T15:40:11.644341Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:39:45Z`
- `2026-09-20T15:38:19.995835Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:37:45Z`
- `2026-09-20T15:36:27.945056Z` — **MID**: 1 rows; marker `2026-09-20T15:35:00Z`
- `2026-09-20T15:36:27.945056Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:35:45Z`
- `2026-09-20T15:35:46.247772Z` — **FUELINST**: 80 rows; marker `2026-09-20T15:35:00Z`
- `2026-09-20T15:34:10.610073Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:33:45Z`
- `2026-09-20T15:32:33.894297Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:31:45Z`
- `2026-09-20T15:30:46.433472Z` — **FUELHH**: 20 rows; marker `2026-09-20T15:30:00Z`
- `2026-09-20T15:30:31.002493Z` — **FUELINST**: 80 rows; marker `2026-09-20T15:30:00Z`
- `2026-09-20T15:30:14.848736Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:29:45Z`
- `2026-09-20T15:28:06.391598Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:27:45Z`
- `2026-09-20T15:26:18.404693Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:25:45Z`
- `2026-09-20T15:25:46.137940Z` — **FUELINST**: 80 rows; marker `2026-09-20T15:25:00Z`
- `2026-09-20T15:24:10.147445Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:23:45Z`
- `2026-09-20T15:23:53.769893Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`
