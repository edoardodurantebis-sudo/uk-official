# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T18:22:20.671789Z`  
Current process started UTC: `2026-09-22T18:18:21.050470Z`  
1-second metadata polls in this process: **230**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3672, delta=-32, z=4.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=632, delta=-5, z=8.76 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3704, delta=270, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=637, delta=0, z=9.00 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3434, delta=339, z=4.03 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=637, delta=0, z=9.17 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3095, delta=239, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=637, delta=1, z=9.35 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=635, delta=22, z=10.83 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=832, delta=5, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=636, delta=1, z=9.53 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=832, delta=-1, z=3.50 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=635, delta=0, z=9.72 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=833, delta=1, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=635, delta=0, z=9.94 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2195, 2026-09-22T18:20:28.049472Z)
- `FUELINST|fuelType=OTHER|generation` = **3672** (n=2195, 2026-09-22T18:20:28.049472Z)
- `FUELINST|fuelType=PS|generation` = **1360** (n=2195, 2026-09-22T18:20:28.049472Z)
- `FUELINST|fuelType=WIND|generation` = **1638** (n=2195, 2026-09-22T18:20:28.049472Z)
- `IMBALNGC|TOTAL|imbalance` = **-7940** (n=360, 2026-09-22T17:52:55.340139Z)
- `INDDEM|TOTAL|demand` = **-12478** (n=361, 2026-09-22T18:22:05.951674Z)
- `INDGEN|TOTAL|generation` = **13165** (n=361, 2026-09-22T18:22:05.951674Z)
- `MELNGC|TOTAL|margin` = **37157** (n=361, 2026-09-22T18:19:41.061285Z)
- `MID|dataProvider=APXMIDP|price` = **228.4** (n=102, 2026-09-22T18:12:16.637488Z)
- `MID|dataProvider=APXMIDP|volume` = **3689.8** (n=102, 2026-09-22T18:12:16.637488Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=202, 2026-09-22T18:12:16.637488Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=202, 2026-09-22T18:12:16.637488Z)
- `NDF|TOTAL|demand` = **20673** (n=369, 2026-09-22T18:17:46.123884Z)
- `TSDF|TOTAL|demand` = **21173** (n=369, 2026-09-22T18:17:46.123884Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T18:22:05.951674Z` — **INDGEN**: 1206 rows; marker `2026-09-22T18:17:00Z`
- `2026-09-22T18:22:05.951674Z` — **INDDEM**: 1206 rows; marker `2026-09-22T18:17:00Z`
- `2026-09-22T18:22:05.951674Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:21:45Z`
- `2026-09-22T18:20:28.049472Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:20:00Z`
- `2026-09-22T18:20:12.678446Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:19:45Z`
- `2026-09-22T18:19:41.061285Z` — **MELNGC**: 1206 rows; marker `2026-09-22T18:17:00Z`
- `2026-09-22T18:18:02.380295Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:17:45Z`
- `2026-09-22T18:17:46.123884Z` — **TSDF**: 1206 rows; marker `2026-09-22T18:17:00Z`
- `2026-09-22T18:17:46.123884Z` — **NDF**: 67 rows; marker `2026-09-22T18:17:00Z`
- `2026-09-22T18:16:10.081643Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:15:45Z`
- `2026-09-22T18:15:38.765531Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:15:00Z`
- `2026-09-22T18:14:02.774660Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:13:45Z`
- `2026-09-22T18:12:16.637488Z` — **MID**: 2 rows; marker `2026-09-22T18:12:03Z`
- `2026-09-22T18:12:01.067111Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:11:45Z`
- `2026-09-22T18:10:39.723691Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:10:00Z`
