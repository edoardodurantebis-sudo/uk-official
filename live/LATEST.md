# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T08:49:22.459416Z`  
Current process started UTC: `2026-09-23T08:45:22.353993Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2368, 2026-09-23T08:45:38.355996Z)
- `FUELINST|fuelType=OTHER|generation` = **467** (n=2368, 2026-09-23T08:45:38.355996Z)
- `FUELINST|fuelType=PS|generation` = **-17** (n=2368, 2026-09-23T08:45:38.355996Z)
- `FUELINST|fuelType=WIND|generation` = **10482** (n=2368, 2026-09-23T08:45:38.355996Z)
- `IMBALNGC|TOTAL|imbalance` = **-7271** (n=388, 2026-09-23T08:20:10.596300Z)
- `INDDEM|TOTAL|demand` = **-12654** (n=388, 2026-09-23T08:20:10.596300Z)
- `INDGEN|TOTAL|generation` = **13757** (n=388, 2026-09-23T08:20:10.596300Z)
- `MELNGC|TOTAL|margin` = **39298** (n=388, 2026-09-23T08:19:28.840514Z)
- `MID|dataProvider=APXMIDP|price` = **129.01** (n=131, 2026-09-23T08:42:13.686540Z)
- `MID|dataProvider=APXMIDP|volume` = **3712** (n=131, 2026-09-23T08:42:13.686540Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=258, 2026-09-23T08:42:13.686540Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=258, 2026-09-23T08:42:13.686540Z)
- `NDF|TOTAL|demand` = **20282** (n=398, 2026-09-23T08:47:29.493299Z)
- `TSDF|TOTAL|demand` = **21028** (n=398, 2026-09-23T08:47:29.493299Z)
- `WINDFOR|TOTAL|generation` = **6996** (n=67, 2026-09-23T08:30:29.420655Z)

## Latest publication events

- `2026-09-23T08:48:17.314162Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:47:45Z`
- `2026-09-23T08:47:29.493299Z` — **TSDF**: 684 rows; marker `2026-09-23T08:46:00Z`
- `2026-09-23T08:47:29.493299Z` — **NDF**: 38 rows; marker `2026-09-23T08:46:00Z`
- `2026-09-23T08:46:25.870077Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:45:45Z`
- `2026-09-23T08:45:38.355996Z` — **FUELINST**: 80 rows; marker `2026-09-23T08:45:00Z`
- `2026-09-23T08:44:21.666771Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:43:45Z`
- `2026-09-23T08:42:13.686540Z` — **MID**: 2 rows; marker `2026-09-23T08:42:03Z`
- `2026-09-23T08:42:13.686540Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:41:45Z`
- `2026-09-23T08:40:37.172170Z` — **FUELINST**: 80 rows; marker `2026-09-23T08:40:00Z`
- `2026-09-23T08:40:20.810176Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:39:45Z`
- `2026-09-23T08:38:12.570453Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:37:45Z`
- `2026-09-23T08:36:35.406831Z` — **MID**: 1 rows; marker `2026-09-23T08:35:00Z`
- `2026-09-23T08:36:19.940137Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:35:45Z`
- `2026-09-23T08:35:32.081292Z` — **FUELINST**: 80 rows; marker `2026-09-23T08:35:00Z`
- `2026-09-23T08:34:12.349835Z` — **FREQ**: 5761 rows; marker `2026-09-23T08:33:45Z`
