# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T08:57:47.577156Z`  
Current process started UTC: `2026-09-23T08:53:47.941302Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2370, 2026-09-23T08:55:41.262544Z)
- `FUELINST|fuelType=OTHER|generation` = **542** (n=2370, 2026-09-23T08:55:41.262544Z)
- `FUELINST|fuelType=PS|generation` = **-17** (n=2370, 2026-09-23T08:55:41.262544Z)
- `FUELINST|fuelType=WIND|generation` = **10571** (n=2370, 2026-09-23T08:55:41.262544Z)
- `IMBALNGC|TOTAL|imbalance` = **-7365** (n=389, 2026-09-23T08:50:58.548221Z)
- `INDDEM|TOTAL|demand` = **-12660** (n=389, 2026-09-23T08:50:58.548221Z)
- `INDGEN|TOTAL|generation` = **13663** (n=389, 2026-09-23T08:50:58.548221Z)
- `MELNGC|TOTAL|margin` = **39658** (n=389, 2026-09-23T08:49:36.929955Z)
- `MID|dataProvider=APXMIDP|price` = **129.01** (n=131, 2026-09-23T08:42:13.686540Z)
- `MID|dataProvider=APXMIDP|volume` = **3712** (n=131, 2026-09-23T08:42:13.686540Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=258, 2026-09-23T08:42:13.686540Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=258, 2026-09-23T08:42:13.686540Z)
- `NDF|TOTAL|demand` = **20282** (n=398, 2026-09-23T08:47:29.493299Z)
- `TSDF|TOTAL|demand` = **21028** (n=398, 2026-09-23T08:47:29.493299Z)
- `WINDFOR|TOTAL|generation` = **6996** (n=67, 2026-09-23T08:30:29.420655Z)

## Latest publication events

- `2026-09-23T08:56:29.617663Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:55:45Z`
- `2026-09-23T08:55:41.262544Z` — **FUELINST**: 80 rows; marker `2026-09-23T08:55:00Z`
- `2026-09-23T08:54:20.445062Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:53:45Z`
- `2026-09-23T08:52:19.227031Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:51:45Z`
- `2026-09-23T08:50:58.548221Z` — **INDGEN**: 684 rows; marker `2026-09-23T08:46:00Z`
- `2026-09-23T08:50:58.548221Z` — **INDDEM**: 684 rows; marker `2026-09-23T08:46:00Z`
- `2026-09-23T08:50:58.548221Z` — **IMBALNGC**: 684 rows; marker `2026-09-23T08:46:00Z`
- `2026-09-23T08:50:42.030907Z` — **FUELINST**: 80 rows; marker `2026-09-23T08:50:00Z`
- `2026-09-23T08:50:25.889775Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:49:45Z`
- `2026-09-23T08:49:36.929955Z` — **MELNGC**: 684 rows; marker `2026-09-23T08:46:00Z`
- `2026-09-23T08:48:17.314162Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:47:45Z`
- `2026-09-23T08:47:29.493299Z` — **TSDF**: 684 rows; marker `2026-09-23T08:46:00Z`
- `2026-09-23T08:47:29.493299Z` — **NDF**: 38 rows; marker `2026-09-23T08:46:00Z`
- `2026-09-23T08:46:25.870077Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:45:45Z`
- `2026-09-23T08:45:38.355996Z` — **FUELINST**: 80 rows; marker `2026-09-23T08:45:00Z`
