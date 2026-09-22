# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T23:52:08.321109Z`  
Current process started UTC: `2026-09-22T23:48:07.217185Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2261, 2026-09-22T23:50:30.883625Z)
- `FUELINST|fuelType=OTHER|generation` = **162** (n=2261, 2026-09-22T23:50:30.883625Z)
- `FUELINST|fuelType=PS|generation` = **147** (n=2261, 2026-09-22T23:50:30.883625Z)
- `FUELINST|fuelType=WIND|generation` = **3650** (n=2261, 2026-09-22T23:50:30.883625Z)
- `IMBALNGC|TOTAL|imbalance` = **-7998** (n=372, 2026-09-22T23:50:47.210542Z)
- `INDDEM|TOTAL|demand` = **-12486** (n=372, 2026-09-22T23:50:47.210542Z)
- `INDGEN|TOTAL|generation` = **13175** (n=372, 2026-09-22T23:50:47.210542Z)
- `MELNGC|TOTAL|margin` = **37219** (n=372, 2026-09-22T23:48:55.280062Z)
- `MID|dataProvider=APXMIDP|price` = **144.39** (n=113, 2026-09-22T23:42:06.586148Z)
- `MID|dataProvider=APXMIDP|volume` = **1964.5** (n=113, 2026-09-22T23:42:06.586148Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=222, 2026-09-22T23:42:06.586148Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=222, 2026-09-22T23:42:06.586148Z)
- `NDF|TOTAL|demand` = **20673** (n=380, 2026-09-22T23:47:09.882400Z)
- `TSDF|TOTAL|demand` = **21173** (n=380, 2026-09-22T23:47:25.302034Z)
- `WINDFOR|TOTAL|generation` = **13770** (n=64, 2026-09-22T23:30:32.481751Z)

## Latest publication events

- `2026-09-22T23:52:06.312543Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:51:45Z`
- `2026-09-22T23:50:47.210542Z` — **INDGEN**: 1008 rows; marker `2026-09-22T23:46:00Z`
- `2026-09-22T23:50:47.210542Z` — **INDDEM**: 1008 rows; marker `2026-09-22T23:46:00Z`
- `2026-09-22T23:50:47.210542Z` — **IMBALNGC**: 1008 rows; marker `2026-09-22T23:46:00Z`
- `2026-09-22T23:50:30.883625Z` — **FUELINST**: 80 rows; marker `2026-09-22T23:50:00Z`
- `2026-09-22T23:50:15.058140Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:49:45Z`
- `2026-09-22T23:48:55.280062Z` — **MELNGC**: 1008 rows; marker `2026-09-22T23:46:00Z`
- `2026-09-22T23:48:07.217194Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:47:45Z`
- `2026-09-22T23:47:25.302034Z` — **TSDF**: 1008 rows; marker `2026-09-22T23:47:00Z`
- `2026-09-22T23:47:09.882400Z` — **NDF**: 56 rows; marker `2026-09-22T23:46:00Z`
- `2026-09-22T23:46:21.502559Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:45:45Z`
- `2026-09-22T23:45:34.316187Z` — **FUELINST**: 80 rows; marker `2026-09-22T23:45:00Z`
- `2026-09-22T23:44:14.074313Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:43:45Z`
- `2026-09-22T23:42:06.586148Z` — **MID**: 2 rows; marker `2026-09-22T23:42:03Z`
- `2026-09-22T23:42:06.586148Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:41:45Z`
