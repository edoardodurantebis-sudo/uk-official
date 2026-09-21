# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T07:31:55.861477Z`  
Current process started UTC: `2026-09-21T07:27:56.193025Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3499, delta=5, z=8.02 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=805, delta=-32, z=3.79 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3498, delta=4, z=7.26 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=804, delta=-2, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3494, delta=-6, z=7.20 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=806, delta=2, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=-1, z=7.58 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=804, delta=0, z=3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3501, delta=1, z=7.75 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=804, delta=0, z=3.72 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3500, delta=1, z=7.84 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=804, delta=-5, z=3.74 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3499, delta=3, z=7.94 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=809, delta=-23, z=3.80 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2993, delta=730, z=4.09 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1780, 2026-09-21T07:30:36.300397Z)
- `FUELINST|fuelType=OTHER|generation` = **2350** (n=1780, 2026-09-21T07:30:36.300397Z)
- `FUELINST|fuelType=PS|generation` = **382** (n=1780, 2026-09-21T07:30:36.300397Z)
- `FUELINST|fuelType=WIND|generation` = **4286** (n=1780, 2026-09-21T07:30:36.300397Z)
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

- `2026-09-21T07:30:36.300397Z` — **FUELHH**: 20 rows; marker `2026-09-21T07:30:00Z`
- `2026-09-21T07:30:36.300397Z` — **FUELINST**: 80 rows; marker `2026-09-21T07:30:00Z`
- `2026-09-21T07:30:20.159348Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:29:45Z`
- `2026-09-21T07:28:12.200568Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:27:45Z`
- `2026-09-21T07:26:07.653951Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:25:45Z`
- `2026-09-21T07:25:36.141689Z` — **FUELINST**: 80 rows; marker `2026-09-21T07:25:00Z`
- `2026-09-21T07:24:15.912187Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:23:45Z`
- `2026-09-21T07:22:08.227657Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:21:45Z`
- `2026-09-21T07:20:32.699166Z` — **FUELINST**: 80 rows; marker `2026-09-21T07:20:00Z`
- `2026-09-21T07:20:17.144355Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:19:45Z`
- `2026-09-21T07:20:01.335621Z` — **IMBALNGC**: 738 rows; marker `2026-09-21T07:16:00Z`
- `2026-09-21T07:19:45.573026Z` — **INDGEN**: 738 rows; marker `2026-09-21T07:16:00Z`
- `2026-09-21T07:19:45.573026Z` — **INDDEM**: 738 rows; marker `2026-09-21T07:16:00Z`
- `2026-09-21T07:18:45.711844Z` — **MELNGC**: 738 rows; marker `2026-09-21T07:16:00Z`
- `2026-09-21T07:18:13.451525Z` — **FREQ**: 5761 rows; marker `2026-09-21T07:17:45Z`
