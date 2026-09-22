# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T21:49:59.635332Z`  
Current process started UTC: `2026-09-22T21:45:59.503090Z`  
1-second metadata polls in this process: **234**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2236, 2026-09-22T21:45:29.668798Z)
- `FUELINST|fuelType=OTHER|generation` = **184** (n=2236, 2026-09-22T21:45:29.668798Z)
- `FUELINST|fuelType=PS|generation` = **143** (n=2236, 2026-09-22T21:45:29.668798Z)
- `FUELINST|fuelType=WIND|generation` = **2465** (n=2236, 2026-09-22T21:45:29.668798Z)
- `IMBALNGC|TOTAL|imbalance` = **-8019** (n=367, 2026-09-22T21:21:02.373107Z)
- `INDDEM|TOTAL|demand` = **-12477** (n=367, 2026-09-22T21:20:46.150531Z)
- `INDGEN|TOTAL|generation` = **13154** (n=367, 2026-09-22T21:21:02.373107Z)
- `MELNGC|TOTAL|margin` = **37209** (n=368, 2026-09-22T21:49:10.751401Z)
- `MID|dataProvider=APXMIDP|price` = **156.24** (n=109, 2026-09-22T21:42:17.013922Z)
- `MID|dataProvider=APXMIDP|volume` = **3594.5** (n=109, 2026-09-22T21:42:17.013922Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=216, 2026-09-22T21:42:17.013922Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=216, 2026-09-22T21:42:17.013922Z)
- `NDF|TOTAL|demand` = **20673** (n=376, 2026-09-22T21:47:51.071149Z)
- `TSDF|TOTAL|demand` = **21173** (n=376, 2026-09-22T21:47:51.071149Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T21:49:10.751401Z` — **MELNGC**: 1080 rows; marker `2026-09-22T21:47:00Z`
- `2026-09-22T21:48:07.144207Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:47:45Z`
- `2026-09-22T21:47:51.071149Z` — **TSDF**: 1080 rows; marker `2026-09-22T21:47:00Z`
- `2026-09-22T21:47:51.071149Z` — **NDF**: 60 rows; marker `2026-09-22T21:47:00Z`
- `2026-09-22T21:46:15.505229Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:45:45Z`
- `2026-09-22T21:45:29.668798Z` — **FUELINST**: 80 rows; marker `2026-09-22T21:45:00Z`
- `2026-09-22T21:44:09.631582Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:43:45Z`
- `2026-09-22T21:42:17.013922Z` — **MID**: 2 rows; marker `2026-09-22T21:42:03Z`
- `2026-09-22T21:42:17.013922Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:41:45Z`
- `2026-09-22T21:40:33.393910Z` — **FUELINST**: 80 rows; marker `2026-09-22T21:40:00Z`
- `2026-09-22T21:40:16.820611Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:39:45Z`
- `2026-09-22T21:38:08.993796Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:37:45Z`
- `2026-09-22T21:36:33.356104Z` — **MID**: 1 rows; marker `2026-09-22T21:35:00Z`
- `2026-09-22T21:36:01.791907Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:35:45Z`
- `2026-09-22T21:35:29.692363Z` — **FUELINST**: 80 rows; marker `2026-09-22T21:35:00Z`
