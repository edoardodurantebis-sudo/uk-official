# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T03:49:19.035479Z`  
Current process started UTC: `2026-09-23T03:45:19.188603Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2308, 2026-09-23T03:45:35.343283Z)
- `FUELINST|fuelType=OTHER|generation` = **171** (n=2308, 2026-09-23T03:45:35.343283Z)
- `FUELINST|fuelType=PS|generation` = **144** (n=2308, 2026-09-23T03:45:35.343283Z)
- `FUELINST|fuelType=WIND|generation` = **6966** (n=2308, 2026-09-23T03:45:35.343283Z)
- `IMBALNGC|TOTAL|imbalance` = **-7992** (n=379, 2026-09-23T03:20:24.538683Z)
- `INDDEM|TOTAL|demand` = **-12415** (n=379, 2026-09-23T03:20:24.538683Z)
- `INDGEN|TOTAL|generation` = **13181** (n=379, 2026-09-23T03:20:24.538683Z)
- `MELNGC|TOTAL|margin` = **38571** (n=379, 2026-09-23T03:19:09.641247Z)
- `MID|dataProvider=APXMIDP|price` = **142.05** (n=121, 2026-09-23T03:42:14.086126Z)
- `MID|dataProvider=APXMIDP|volume` = **2444.8** (n=121, 2026-09-23T03:42:14.086126Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=238, 2026-09-23T03:42:14.086126Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=238, 2026-09-23T03:42:14.086126Z)
- `NDF|TOTAL|demand` = **20673** (n=388, 2026-09-23T03:47:43.996474Z)
- `TSDF|TOTAL|demand` = **21173** (n=388, 2026-09-23T03:47:43.996474Z)
- `WINDFOR|TOTAL|generation` = **7477** (n=65, 2026-09-23T03:30:40.879035Z)

## Latest publication events

- `2026-09-23T03:48:16.485785Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:47:45Z`
- `2026-09-23T03:47:43.996474Z` — **TSDF**: 864 rows; marker `2026-09-23T03:47:00Z`
- `2026-09-23T03:47:43.996474Z` — **NDF**: 48 rows; marker `2026-09-23T03:47:00Z`
- `2026-09-23T03:46:07.990683Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:45:45Z`
- `2026-09-23T03:45:35.343283Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:45:00Z`
- `2026-09-23T03:44:21.953693Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:43:45Z`
- `2026-09-23T03:42:14.086126Z` — **MID**: 2 rows; marker `2026-09-23T03:42:02Z`
- `2026-09-23T03:42:14.086126Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:41:45Z`
- `2026-09-23T03:40:21.446726Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:40:00Z`
- `2026-09-23T03:40:05.737598Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:39:45Z`
- `2026-09-23T03:38:30.161064Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:37:45Z`
- `2026-09-23T03:36:31.951809Z` — **MID**: 1 rows; marker `2026-09-23T03:35:00Z`
- `2026-09-23T03:36:15.773536Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:35:45Z`
- `2026-09-23T03:35:27.732043Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:35:00Z`
- `2026-09-23T03:34:08.148311Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:33:45Z`
