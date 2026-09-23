# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T07:53:44.345819Z`  
Current process started UTC: `2026-09-23T07:49:44.675522Z`  
1-second metadata polls in this process: **236**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2357, 2026-09-23T07:50:33.858849Z)
- `FUELINST|fuelType=OTHER|generation` = **971** (n=2357, 2026-09-23T07:50:33.858849Z)
- `FUELINST|fuelType=PS|generation` = **-20** (n=2357, 2026-09-23T07:50:33.858849Z)
- `FUELINST|fuelType=WIND|generation` = **10262** (n=2357, 2026-09-23T07:50:33.858849Z)
- `IMBALNGC|TOTAL|imbalance` = **-7454** (n=387, 2026-09-23T07:20:50.693900Z)
- `INDDEM|TOTAL|demand` = **-12650** (n=387, 2026-09-23T07:20:50.693900Z)
- `INDGEN|TOTAL|generation` = **13965** (n=387, 2026-09-23T07:20:50.693900Z)
- `MELNGC|TOTAL|margin` = **38775** (n=387, 2026-09-23T07:19:31.866782Z)
- `MID|dataProvider=APXMIDP|price` = **144.65** (n=129, 2026-09-23T07:42:13.099699Z)
- `MID|dataProvider=APXMIDP|volume` = **3836.7** (n=129, 2026-09-23T07:42:13.099699Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=254, 2026-09-23T07:42:13.099699Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=254, 2026-09-23T07:42:13.099699Z)
- `NDF|TOTAL|demand` = **19504** (n=396, 2026-09-23T07:45:44.740867Z)
- `TSDF|TOTAL|demand` = **20004** (n=396, 2026-09-23T07:45:44.740867Z)
- `WINDFOR|TOTAL|generation` = **7305** (n=66, 2026-09-23T05:30:43.471788Z)

## Latest publication events

- `2026-09-23T07:52:25.892827Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:51:45Z`
- `2026-09-23T07:50:33.858849Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:50:00Z`
- `2026-09-23T07:50:17.612773Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:49:45Z`
- `2026-09-23T07:48:28.832855Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:47:45Z`
- `2026-09-23T07:46:18.681863Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:45:45Z`
- `2026-09-23T07:45:44.740867Z` — **TSDF**: 864 rows; marker `2026-09-23T07:45:00Z`
- `2026-09-23T07:45:44.740867Z` — **NDF**: 48 rows; marker `2026-09-23T07:45:00Z`
- `2026-09-23T07:45:28.744529Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:45:00Z`
- `2026-09-23T07:44:20.568868Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:43:45Z`
- `2026-09-23T07:42:13.099699Z` — **MID**: 2 rows; marker `2026-09-23T07:42:03Z`
- `2026-09-23T07:42:13.099699Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:41:45Z`
- `2026-09-23T07:40:26.222350Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:40:00Z`
- `2026-09-23T07:40:26.222350Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:39:45Z`
- `2026-09-23T07:38:16.730861Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:37:45Z`
- `2026-09-23T07:36:28.257530Z` — **MID**: 1 rows; marker `2026-09-23T07:35:00Z`
