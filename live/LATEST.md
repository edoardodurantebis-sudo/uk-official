# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T22:40:35.448622Z`  
Current process started UTC: `2026-09-22T22:36:35.759933Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2247, 2026-09-22T22:40:21.265879Z)
- `FUELINST|fuelType=OTHER|generation` = **221** (n=2247, 2026-09-22T22:40:21.265879Z)
- `FUELINST|fuelType=PS|generation` = **146** (n=2247, 2026-09-22T22:40:21.265879Z)
- `FUELINST|fuelType=WIND|generation` = **2727** (n=2247, 2026-09-22T22:40:21.265879Z)
- `IMBALNGC|TOTAL|imbalance` = **-8047** (n=369, 2026-09-22T22:21:05.780894Z)
- `INDDEM|TOTAL|demand` = **-12478** (n=369, 2026-09-22T22:21:05.780894Z)
- `INDGEN|TOTAL|generation` = **13126** (n=369, 2026-09-22T22:21:05.780894Z)
- `MELNGC|TOTAL|margin` = **37229** (n=369, 2026-09-22T22:19:28.499770Z)
- `MID|dataProvider=APXMIDP|price` = **142.47** (n=110, 2026-09-22T22:12:20.902810Z)
- `MID|dataProvider=APXMIDP|volume` = **2339.7** (n=110, 2026-09-22T22:12:20.902810Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=218, 2026-09-22T22:12:20.902810Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=218, 2026-09-22T22:12:20.902810Z)
- `NDF|TOTAL|demand` = **20673** (n=377, 2026-09-22T22:17:37.582289Z)
- `TSDF|TOTAL|demand` = **21173** (n=377, 2026-09-22T22:17:37.582289Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T22:40:21.265879Z` — **FUELINST**: 80 rows; marker `2026-09-22T22:40:00Z`
- `2026-09-22T22:40:04.261799Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:39:45Z`
- `2026-09-22T22:38:11.855800Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:37:45Z`
- `2026-09-22T22:36:07.627573Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:35:45Z`
- `2026-09-22T22:35:35.505350Z` — **FUELINST**: 80 rows; marker `2026-09-22T22:35:00Z`
- `2026-09-22T22:34:15.137125Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:33:45Z`
- `2026-09-22T22:32:23.060483Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:31:45Z`
- `2026-09-22T22:30:35.603780Z` — **FUELHH**: 20 rows; marker `2026-09-22T22:30:00Z`
- `2026-09-22T22:30:35.603780Z` — **FUELINST**: 80 rows; marker `2026-09-22T22:30:00Z`
- `2026-09-22T22:30:19.603584Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:29:45Z`
- `2026-09-22T22:28:27.330834Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:27:45Z`
- `2026-09-22T22:26:22.669896Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:25:45Z`
- `2026-09-22T22:25:34.709871Z` — **FUELINST**: 80 rows; marker `2026-09-22T22:25:00Z`
- `2026-09-22T22:24:14.543693Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:23:45Z`
- `2026-09-22T22:22:25.793152Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:21:45Z`
