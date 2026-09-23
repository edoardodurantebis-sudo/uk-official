# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T01:29:54.558548Z`  
Current process started UTC: `2026-09-23T01:25:54.398221Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=165, delta=-434, z=1.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=437, delta=-153, z=5.21 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3204, delta=-351, z=3.66 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=599, delta=-36, z=7.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.34 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3238, delta=-72, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=0, z=7.43 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3310, delta=62, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=-2, z=7.53 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3248, delta=-217, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=592, delta=-48, z=7.65 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3465, delta=-220, z=3.99 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=640, delta=7, z=8.44 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3555, delta=892, z=4.30 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2280, 2026-09-23T01:25:26.266305Z)
- `FUELINST|fuelType=OTHER|generation` = **198** (n=2280, 2026-09-23T01:25:26.266305Z)
- `FUELINST|fuelType=PS|generation` = **147** (n=2280, 2026-09-23T01:25:26.266305Z)
- `FUELINST|fuelType=WIND|generation` = **4865** (n=2280, 2026-09-23T01:25:26.266305Z)
- `IMBALNGC|TOTAL|imbalance` = **-7986** (n=375, 2026-09-23T01:21:41.714873Z)
- `INDDEM|TOTAL|demand` = **-12442** (n=375, 2026-09-23T01:21:41.714873Z)
- `INDGEN|TOTAL|generation` = **13187** (n=375, 2026-09-23T01:21:41.714873Z)
- `MELNGC|TOTAL|margin` = **37235** (n=375, 2026-09-23T01:19:17.798071Z)
- `MID|dataProvider=APXMIDP|price` = **142.86** (n=116, 2026-09-23T01:12:11.851877Z)
- `MID|dataProvider=APXMIDP|volume` = **2545.7** (n=116, 2026-09-23T01:12:11.851877Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=228, 2026-09-23T01:12:11.851877Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=228, 2026-09-23T01:12:11.851877Z)
- `NDF|TOTAL|demand` = **20673** (n=383, 2026-09-23T01:17:25.758780Z)
- `TSDF|TOTAL|demand` = **21173** (n=383, 2026-09-23T01:17:25.758780Z)
- `WINDFOR|TOTAL|generation` = **13770** (n=64, 2026-09-22T23:30:32.481751Z)

## Latest publication events

- `2026-09-23T01:28:17.961448Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:27:45Z`
- `2026-09-23T01:26:10.400195Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:25:45Z`
- `2026-09-23T01:25:26.266305Z` — **FUELINST**: 80 rows; marker `2026-09-23T01:25:00Z`
- `2026-09-23T01:24:06.621060Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:23:45Z`
- `2026-09-23T01:22:13.675269Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:21:45Z`
- `2026-09-23T01:21:41.714873Z` — **INDGEN**: 954 rows; marker `2026-09-23T01:17:00Z`
- `2026-09-23T01:21:41.714873Z` — **INDDEM**: 954 rows; marker `2026-09-23T01:17:00Z`
- `2026-09-23T01:21:41.714873Z` — **IMBALNGC**: 954 rows; marker `2026-09-23T01:17:00Z`
- `2026-09-23T01:20:22.225612Z` — **FUELINST**: 80 rows; marker `2026-09-23T01:20:00Z`
- `2026-09-23T01:20:05.857318Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:19:45Z`
- `2026-09-23T01:19:17.798071Z` — **MELNGC**: 954 rows; marker `2026-09-23T01:17:00Z`
- `2026-09-23T01:18:13.654986Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:17:45Z`
- `2026-09-23T01:17:25.758780Z` — **TSDF**: 954 rows; marker `2026-09-23T01:17:00Z`
- `2026-09-23T01:17:25.758780Z` — **NDF**: 53 rows; marker `2026-09-23T01:17:00Z`
- `2026-09-23T01:16:53.465515Z` — **FREQ**: 5761 rows; marker `2026-09-23T01:15:45Z`
