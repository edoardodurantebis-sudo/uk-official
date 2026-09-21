# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T07:23:29.265291Z`  
Current process started UTC: `2026-09-21T07:19:29.453496Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=-1, z=7.58 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=804, delta=0, z=3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=1, z=7.75 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=804, delta=0, z=3.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=1, z=7.84 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=804, delta=-5, z=3.74 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=3, z=7.94 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=809, delta=-23, z=3.80 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2993, delta=730, z=4.09 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3494, delta=0, z=8.74 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=837, delta=4, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2981, delta=-159, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3496, delta=-1, z=7.94 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=832, delta=-5, z=4.04 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3140, delta=101, z=4.20 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1778, 2026-09-21T07:20:32.699166Z)
- `FUELINST|fuelType=OTHER|generation` = **2577** (n=1778, 2026-09-21T07:20:32.699166Z)
- `FUELINST|fuelType=PS|generation` = **224** (n=1778, 2026-09-21T07:20:32.699166Z)
- `FUELINST|fuelType=WIND|generation` = **4220** (n=1778, 2026-09-21T07:20:32.699166Z)
- `IMBALNGC|TOTAL|imbalance` = **-3297** (n=293, 2026-09-21T07:20:01.335621Z)
- `INDDEM|TOTAL|demand` = **-12833** (n=293, 2026-09-21T07:19:45.573026Z)
- `INDGEN|TOTAL|generation` = **17972** (n=293, 2026-09-21T07:19:45.573026Z)
- `MELNGC|TOTAL|margin` = **38254** (n=293, 2026-09-21T07:18:45.711844Z)
- `MID|dataProvider=APXMIDP|price` = **198.55** (n=32, 2026-09-21T07:12:12.315114Z)
- `MID|dataProvider=APXMIDP|volume` = **2402.1** (n=32, 2026-09-21T07:12:12.315114Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=64, 2026-09-21T07:12:12.315114Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=64, 2026-09-21T07:12:12.315114Z)
- `NDF|TOTAL|demand` = **20110** (n=299, 2026-09-21T07:17:09.233740Z)
- `TSDF|TOTAL|demand` = **21269** (n=299, 2026-09-21T07:17:09.233740Z)
- `WINDFOR|TOTAL|generation` = **8794** (n=50, 2026-09-21T05:30:44.368414Z)

## Latest publication events

- `2026-09-21T07:22:08.227657Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:21:45Z`
- `2026-09-21T07:20:32.699166Z` — **FUELINST**: 80 rows; marker `2026-09-21T07:20:00Z`
- `2026-09-21T07:20:17.144355Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:19:45Z`
- `2026-09-21T07:20:01.335621Z` — **IMBALNGC**: 738 rows; marker `2026-09-21T07:16:00Z`
- `2026-09-21T07:19:45.573026Z` — **INDGEN**: 738 rows; marker `2026-09-21T07:16:00Z`
- `2026-09-21T07:19:45.573026Z` — **INDDEM**: 738 rows; marker `2026-09-21T07:16:00Z`
- `2026-09-21T07:18:45.711844Z` — **MELNGC**: 738 rows; marker `2026-09-21T07:16:00Z`
- `2026-09-21T07:18:13.451525Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:17:45Z`
- `2026-09-21T07:17:09.233740Z` — **TSDF**: 738 rows; marker `2026-09-21T07:16:00Z`
- `2026-09-21T07:17:09.233740Z` — **NDF**: 41 rows; marker `2026-09-21T07:16:00Z`
- `2026-09-21T07:16:05.161775Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:15:45Z`
- `2026-09-21T07:15:32.861644Z` — **FUELINST**: 80 rows; marker `2026-09-21T07:15:00Z`
- `2026-09-21T07:14:05.059189Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:13:45Z`
- `2026-09-21T07:12:12.315114Z` — **MID**: 2 rows; marker `2026-09-21T07:12:03Z`
- `2026-09-21T07:12:12.315114Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:11:45Z`
