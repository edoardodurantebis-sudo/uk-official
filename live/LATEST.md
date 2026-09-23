# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T05:17:39.048424Z`  
Current process started UTC: `2026-09-23T05:13:39.271135Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2326, 2026-09-23T05:15:31.389636Z)
- `FUELINST|fuelType=OTHER|generation` = **716** (n=2326, 2026-09-23T05:15:31.389636Z)
- `FUELINST|fuelType=PS|generation` = **38** (n=2326, 2026-09-23T05:15:31.389636Z)
- `FUELINST|fuelType=WIND|generation` = **8912** (n=2326, 2026-09-23T05:15:31.389636Z)
- `IMBALNGC|TOTAL|imbalance` = **-8014** (n=382, 2026-09-23T04:50:18.620136Z)
- `INDDEM|TOTAL|demand` = **-12419** (n=382, 2026-09-23T04:50:02.832880Z)
- `INDGEN|TOTAL|generation` = **13159** (n=382, 2026-09-23T04:50:02.832880Z)
- `MELNGC|TOTAL|margin` = **38542** (n=382, 2026-09-23T04:48:58.867240Z)
- `MID|dataProvider=APXMIDP|price` = **149.12** (n=124, 2026-09-23T05:12:06.594276Z)
- `MID|dataProvider=APXMIDP|volume` = **3029** (n=124, 2026-09-23T05:12:06.594276Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=244, 2026-09-23T05:12:06.594276Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=244, 2026-09-23T05:12:06.594276Z)
- `NDF|TOTAL|demand` = **20673** (n=391, 2026-09-23T05:17:07.311486Z)
- `TSDF|TOTAL|demand` = **21173** (n=391, 2026-09-23T05:17:07.311486Z)
- `WINDFOR|TOTAL|generation` = **7477** (n=65, 2026-09-23T03:30:40.879035Z)

## Latest publication events

- `2026-09-23T05:17:07.311486Z` — **TSDF**: 810 rows; marker `2026-09-23T05:16:00Z`
- `2026-09-23T05:17:07.311486Z` — **NDF**: 45 rows; marker `2026-09-23T05:16:00Z`
- `2026-09-23T05:16:19.736191Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:15:45Z`
- `2026-09-23T05:15:31.389636Z` — **FUELINST**: 80 rows; marker `2026-09-23T05:15:00Z`
- `2026-09-23T05:14:11.285640Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:13:45Z`
- `2026-09-23T05:12:06.594276Z` — **MID**: 2 rows; marker `2026-09-23T05:12:03Z`
- `2026-09-23T05:12:06.594276Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:11:45Z`
- `2026-09-23T05:10:46.911575Z` — **FUELINST**: 80 rows; marker `2026-09-23T05:10:00Z`
- `2026-09-23T05:10:14.914229Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:09:45Z`
- `2026-09-23T05:08:16.604598Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:07:45Z`
- `2026-09-23T05:06:22.847368Z` — **MID**: 1 rows; marker `2026-09-23T05:05:00Z`
- `2026-09-23T05:06:22.847368Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:05:45Z`
- `2026-09-23T05:05:35.344349Z` — **FUELINST**: 80 rows; marker `2026-09-23T05:05:00Z`
- `2026-09-23T05:04:14.840765Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:03:45Z`
- `2026-09-23T05:02:23.399089Z` — **FREQ**: 5761 rows; marker `2026-09-23T05:01:45Z`
