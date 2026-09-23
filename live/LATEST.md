# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T03:40:54.260583Z`  
Current process started UTC: `2026-09-23T03:36:54.149324Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2307, 2026-09-23T03:40:21.446726Z)
- `FUELINST|fuelType=OTHER|generation` = **247** (n=2307, 2026-09-23T03:40:21.446726Z)
- `FUELINST|fuelType=PS|generation` = **144** (n=2307, 2026-09-23T03:40:21.446726Z)
- `FUELINST|fuelType=WIND|generation` = **6695** (n=2307, 2026-09-23T03:40:21.446726Z)
- `IMBALNGC|TOTAL|imbalance` = **-7992** (n=379, 2026-09-23T03:20:24.538683Z)
- `INDDEM|TOTAL|demand` = **-12415** (n=379, 2026-09-23T03:20:24.538683Z)
- `INDGEN|TOTAL|generation` = **13181** (n=379, 2026-09-23T03:20:24.538683Z)
- `MELNGC|TOTAL|margin` = **38571** (n=379, 2026-09-23T03:19:09.641247Z)
- `MID|dataProvider=APXMIDP|price` = **144.45** (n=120, 2026-09-23T03:12:11.959147Z)
- `MID|dataProvider=APXMIDP|volume` = **2189.7** (n=120, 2026-09-23T03:12:11.959147Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=237, 2026-09-23T03:36:31.951809Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=237, 2026-09-23T03:36:31.951809Z)
- `NDF|TOTAL|demand` = **20673** (n=387, 2026-09-23T03:17:16.723089Z)
- `TSDF|TOTAL|demand` = **21173** (n=387, 2026-09-23T03:17:16.723089Z)
- `WINDFOR|TOTAL|generation` = **7477** (n=65, 2026-09-23T03:30:40.879035Z)

## Latest publication events

- `2026-09-23T03:40:21.446726Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:40:00Z`
- `2026-09-23T03:40:05.737598Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:39:45Z`
- `2026-09-23T03:38:30.161064Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:37:45Z`
- `2026-09-23T03:36:31.951809Z` — **MID**: 1 rows; marker `2026-09-23T03:35:00Z`
- `2026-09-23T03:36:15.773536Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:35:45Z`
- `2026-09-23T03:35:27.732043Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:35:00Z`
- `2026-09-23T03:34:08.148311Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:33:45Z`
- `2026-09-23T03:32:17.044931Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:31:45Z`
- `2026-09-23T03:30:40.879035Z` — **WINDFOR**: 73 rows; marker `2026-09-23T03:30:00Z`
- `2026-09-23T03:30:40.879035Z` — **FUELHH**: 20 rows; marker `2026-09-23T03:30:00Z`
- `2026-09-23T03:30:40.879035Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:30:00Z`
- `2026-09-23T03:30:09.421957Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:29:45Z`
- `2026-09-23T03:28:08.319577Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:27:45Z`
- `2026-09-23T03:26:16.554249Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:25:45Z`
- `2026-09-23T03:25:44.120420Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:25:00Z`
