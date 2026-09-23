# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T04:56:38.223019Z`  
Current process started UTC: `2026-09-23T04:52:38.743476Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2322, 2026-09-23T04:55:37.265317Z)
- `FUELINST|fuelType=OTHER|generation` = **269** (n=2322, 2026-09-23T04:55:37.265317Z)
- `FUELINST|fuelType=PS|generation` = **144** (n=2322, 2026-09-23T04:55:37.265317Z)
- `FUELINST|fuelType=WIND|generation` = **9184** (n=2322, 2026-09-23T04:55:37.265317Z)
- `IMBALNGC|TOTAL|imbalance` = **-8014** (n=382, 2026-09-23T04:50:18.620136Z)
- `INDDEM|TOTAL|demand` = **-12419** (n=382, 2026-09-23T04:50:02.832880Z)
- `INDGEN|TOTAL|generation` = **13159** (n=382, 2026-09-23T04:50:02.832880Z)
- `MELNGC|TOTAL|margin` = **38542** (n=382, 2026-09-23T04:48:58.867240Z)
- `MID|dataProvider=APXMIDP|price` = **144.51** (n=123, 2026-09-23T04:42:20.177941Z)
- `MID|dataProvider=APXMIDP|volume` = **2320.7** (n=123, 2026-09-23T04:42:20.177941Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=242, 2026-09-23T04:42:20.177941Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=242, 2026-09-23T04:42:20.177941Z)
- `NDF|TOTAL|demand` = **20673** (n=390, 2026-09-23T04:47:11.681831Z)
- `TSDF|TOTAL|demand` = **21173** (n=390, 2026-09-23T04:47:11.681831Z)
- `WINDFOR|TOTAL|generation` = **7477** (n=65, 2026-09-23T03:30:40.879035Z)

## Latest publication events

- `2026-09-23T04:56:09.421345Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:55:45Z`
- `2026-09-23T04:55:37.265317Z` — **FUELINST**: 80 rows; marker `2026-09-23T04:55:00Z`
- `2026-09-23T04:54:17.755877Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:53:45Z`
- `2026-09-23T04:52:09.536667Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:51:45Z`
- `2026-09-23T04:50:33.894323Z` — **FUELINST**: 80 rows; marker `2026-09-23T04:50:00Z`
- `2026-09-23T04:50:18.620136Z` — **IMBALNGC**: 828 rows; marker `2026-09-23T04:46:00Z`
- `2026-09-23T04:50:18.620136Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:49:45Z`
- `2026-09-23T04:50:02.832880Z` — **INDGEN**: 828 rows; marker `2026-09-23T04:46:00Z`
- `2026-09-23T04:50:02.832880Z` — **INDDEM**: 828 rows; marker `2026-09-23T04:46:00Z`
- `2026-09-23T04:48:58.867240Z` — **MELNGC**: 828 rows; marker `2026-09-23T04:46:00Z`
- `2026-09-23T04:48:26.429043Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:47:45Z`
- `2026-09-23T04:47:11.681831Z` — **TSDF**: 828 rows; marker `2026-09-23T04:46:00Z`
- `2026-09-23T04:47:11.681831Z` — **NDF**: 46 rows; marker `2026-09-23T04:46:00Z`
- `2026-09-23T04:46:06.153399Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:45:45Z`
- `2026-09-23T04:45:34.539610Z` — **FUELINST**: 80 rows; marker `2026-09-23T04:45:00Z`
