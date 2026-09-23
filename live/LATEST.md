# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T05:38:40.846582Z`  
Current process started UTC: `2026-09-23T05:34:40.993618Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2330, 2026-09-23T05:35:30.999352Z)
- `FUELINST|fuelType=OTHER|generation` = **1114** (n=2330, 2026-09-23T05:35:30.999352Z)
- `FUELINST|fuelType=PS|generation` = **144** (n=2330, 2026-09-23T05:35:30.999352Z)
- `FUELINST|fuelType=WIND|generation` = **8286** (n=2330, 2026-09-23T05:35:30.999352Z)
- `IMBALNGC|TOTAL|imbalance` = **-7937** (n=383, 2026-09-23T05:20:45.831650Z)
- `INDDEM|TOTAL|demand` = **-12417** (n=383, 2026-09-23T05:20:30.118588Z)
- `INDGEN|TOTAL|generation` = **13236** (n=383, 2026-09-23T05:20:13.965205Z)
- `MELNGC|TOTAL|margin` = **38584** (n=383, 2026-09-23T05:18:38.543677Z)
- `MID|dataProvider=APXMIDP|price` = **149.12** (n=124, 2026-09-23T05:12:06.594276Z)
- `MID|dataProvider=APXMIDP|volume` = **3029** (n=124, 2026-09-23T05:12:06.594276Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=245, 2026-09-23T05:36:35.502686Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=245, 2026-09-23T05:36:35.502686Z)
- `NDF|TOTAL|demand` = **20673** (n=391, 2026-09-23T05:17:07.311486Z)
- `TSDF|TOTAL|demand` = **21173** (n=391, 2026-09-23T05:17:07.311486Z)
- `WINDFOR|TOTAL|generation` = **7305** (n=66, 2026-09-23T05:30:43.471788Z)

## Latest publication events

- `2026-09-23T05:38:11.110204Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:37:45Z`
- `2026-09-23T05:36:35.502686Z` — **MID**: 1 rows; marker `2026-09-23T05:35:00Z`
- `2026-09-23T05:36:19.215187Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:35:45Z`
- `2026-09-23T05:35:30.999352Z` — **FUELINST**: 80 rows; marker `2026-09-23T05:35:00Z`
- `2026-09-23T05:34:11.502895Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:33:45Z`
- `2026-09-23T05:32:19.585672Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:31:45Z`
- `2026-09-23T05:30:43.471788Z` — **WINDFOR**: 73 rows; marker `2026-09-23T05:30:00Z`
- `2026-09-23T05:30:43.471788Z` — **FUELHH**: 20 rows; marker `2026-09-23T05:30:00Z`
- `2026-09-23T05:30:27.307036Z` — **FUELINST**: 80 rows; marker `2026-09-23T05:30:00Z`
- `2026-09-23T05:30:27.307036Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:29:45Z`
- `2026-09-23T05:28:10.860097Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:27:45Z`
- `2026-09-23T05:26:19.009680Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:25:45Z`
- `2026-09-23T05:25:30.752986Z` — **FUELINST**: 80 rows; marker `2026-09-23T05:25:00Z`
- `2026-09-23T05:24:11.004335Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:23:45Z`
- `2026-09-23T05:22:19.317749Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:21:45Z`
