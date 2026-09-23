# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T05:21:50.519613Z`  
Current process started UTC: `2026-09-23T05:17:50.630776Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2327, 2026-09-23T05:20:30.118588Z)
- `FUELINST|fuelType=OTHER|generation` = **763** (n=2327, 2026-09-23T05:20:30.118588Z)
- `FUELINST|fuelType=PS|generation` = **145** (n=2327, 2026-09-23T05:20:30.118588Z)
- `FUELINST|fuelType=WIND|generation` = **8703** (n=2327, 2026-09-23T05:20:30.118588Z)
- `IMBALNGC|TOTAL|imbalance` = **-7937** (n=383, 2026-09-23T05:20:45.831650Z)
- `INDDEM|TOTAL|demand` = **-12417** (n=383, 2026-09-23T05:20:30.118588Z)
- `INDGEN|TOTAL|generation` = **13236** (n=383, 2026-09-23T05:20:13.965205Z)
- `MELNGC|TOTAL|margin` = **38584** (n=383, 2026-09-23T05:18:38.543677Z)
- `MID|dataProvider=APXMIDP|price` = **149.12** (n=124, 2026-09-23T05:12:06.594276Z)
- `MID|dataProvider=APXMIDP|volume` = **3029** (n=124, 2026-09-23T05:12:06.594276Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=244, 2026-09-23T05:12:06.594276Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=244, 2026-09-23T05:12:06.594276Z)
- `NDF|TOTAL|demand` = **20673** (n=391, 2026-09-23T05:17:07.311486Z)
- `TSDF|TOTAL|demand` = **21173** (n=391, 2026-09-23T05:17:07.311486Z)
- `WINDFOR|TOTAL|generation` = **7477** (n=65, 2026-09-23T03:30:40.879035Z)

## Latest publication events

- `2026-09-23T05:20:45.831650Z` — **IMBALNGC**: 810 rows; marker `2026-09-23T05:16:00Z`
- `2026-09-23T05:20:30.118588Z` — **INDDEM**: 810 rows; marker `2026-09-23T05:16:00Z`
- `2026-09-23T05:20:30.118588Z` — **FUELINST**: 80 rows; marker `2026-09-23T05:20:00Z`
- `2026-09-23T05:20:13.965205Z` — **INDGEN**: 810 rows; marker `2026-09-23T05:16:00Z`
- `2026-09-23T05:20:13.965205Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:19:45Z`
- `2026-09-23T05:18:38.543677Z` — **MELNGC**: 810 rows; marker `2026-09-23T05:16:00Z`
- `2026-09-23T05:18:06.632806Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:17:45Z`
- `2026-09-23T05:17:07.311486Z` — **TSDF**: 810 rows; marker `2026-09-23T05:16:00Z`
- `2026-09-23T05:17:07.311486Z` — **NDF**: 45 rows; marker `2026-09-23T05:16:00Z`
- `2026-09-23T05:16:19.736191Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:15:45Z`
- `2026-09-23T05:15:31.389636Z` — **FUELINST**: 80 rows; marker `2026-09-23T05:15:00Z`
- `2026-09-23T05:14:11.285640Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:13:45Z`
- `2026-09-23T05:12:06.594276Z` — **MID**: 2 rows; marker `2026-09-23T05:12:03Z`
- `2026-09-23T05:12:06.594276Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:11:45Z`
- `2026-09-23T05:10:46.911575Z` — **FUELINST**: 80 rows; marker `2026-09-23T05:10:00Z`
