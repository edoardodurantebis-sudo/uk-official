# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T04:43:57.789073Z`  
Current process started UTC: `2026-09-23T04:39:56.388196Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2319, 2026-09-23T04:40:28.609023Z)
- `FUELINST|fuelType=OTHER|generation` = **191** (n=2319, 2026-09-23T04:40:28.609023Z)
- `FUELINST|fuelType=PS|generation` = **144** (n=2319, 2026-09-23T04:40:28.609023Z)
- `FUELINST|fuelType=WIND|generation` = **9163** (n=2319, 2026-09-23T04:40:28.609023Z)
- `IMBALNGC|TOTAL|imbalance` = **-8037** (n=381, 2026-09-23T04:20:50.438169Z)
- `INDDEM|TOTAL|demand` = **-12419** (n=381, 2026-09-23T04:20:34.483089Z)
- `INDGEN|TOTAL|generation` = **13136** (n=381, 2026-09-23T04:20:34.483089Z)
- `MELNGC|TOTAL|margin` = **38527** (n=381, 2026-09-23T04:19:30.872775Z)
- `MID|dataProvider=APXMIDP|price` = **144.51** (n=123, 2026-09-23T04:42:20.177941Z)
- `MID|dataProvider=APXMIDP|volume` = **2320.7** (n=123, 2026-09-23T04:42:20.177941Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=242, 2026-09-23T04:42:20.177941Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=242, 2026-09-23T04:42:20.177941Z)
- `NDF|TOTAL|demand` = **20673** (n=389, 2026-09-23T04:17:39.019325Z)
- `TSDF|TOTAL|demand` = **21173** (n=389, 2026-09-23T04:17:39.019325Z)
- `WINDFOR|TOTAL|generation` = **7477** (n=65, 2026-09-23T03:30:40.879035Z)

## Latest publication events

- `2026-09-23T04:42:20.177941Z` — **MID**: 2 rows; marker `2026-09-23T04:42:04Z`
- `2026-09-23T04:42:20.177941Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:41:45Z`
- `2026-09-23T04:40:28.609023Z` — **FUELINST**: 80 rows; marker `2026-09-23T04:40:00Z`
- `2026-09-23T04:40:12.415164Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:39:45Z`
- `2026-09-23T04:38:23.496787Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:37:45Z`
- `2026-09-23T04:37:35.831256Z` — **MID**: 1 rows; marker `2026-09-23T04:35:00Z`
- `2026-09-23T04:36:14.547161Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:35:45Z`
- `2026-09-23T04:35:42.856993Z` — **FUELINST**: 80 rows; marker `2026-09-23T04:35:00Z`
- `2026-09-23T04:34:11.028793Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:33:45Z`
- `2026-09-23T04:32:18.756733Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:31:45Z`
- `2026-09-23T04:30:46.715629Z` — **FUELHH**: 20 rows; marker `2026-09-23T04:30:00Z`
- `2026-09-23T04:30:30.203331Z` — **FUELINST**: 80 rows; marker `2026-09-23T04:30:00Z`
- `2026-09-23T04:30:14.218977Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:29:45Z`
- `2026-09-23T04:28:05.603568Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:27:45Z`
- `2026-09-23T04:26:03.544709Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:25:45Z`
