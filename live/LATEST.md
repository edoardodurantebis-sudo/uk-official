# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T18:47:53.787627Z`  
Current process started UTC: `2026-09-22T18:43:53.951888Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3310, delta=62, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=590, delta=-2, z=7.53 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3248, delta=-217, z=3.65 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=592, delta=-48, z=7.65 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3465, delta=-220, z=3.99 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=640, delta=7, z=8.44 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3555, delta=892, z=4.30 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=635, delta=0, z=9.42 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=832, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3685, delta=-56, z=4.34 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=633, delta=1, z=8.48 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3741, delta=69, z=4.44 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=632, delta=0, z=8.61 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3672, delta=-32, z=4.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=632, delta=-5, z=8.76 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2200, 2026-09-22T18:45:30.143617Z)
- `FUELINST|fuelType=OTHER|generation` = **3310** (n=2200, 2026-09-22T18:45:30.143617Z)
- `FUELINST|fuelType=PS|generation` = **1510** (n=2200, 2026-09-22T18:45:30.143617Z)
- `FUELINST|fuelType=WIND|generation` = **1711** (n=2200, 2026-09-22T18:45:30.143617Z)
- `IMBALNGC|TOTAL|imbalance` = **-8008** (n=361, 2026-09-22T18:22:34.684273Z)
- `INDDEM|TOTAL|demand` = **-12478** (n=361, 2026-09-22T18:22:05.951674Z)
- `INDGEN|TOTAL|generation` = **13165** (n=361, 2026-09-22T18:22:05.951674Z)
- `MELNGC|TOTAL|margin` = **37157** (n=361, 2026-09-22T18:19:41.061285Z)
- `MID|dataProvider=APXMIDP|price` = **224.96** (n=103, 2026-09-22T18:42:13.356217Z)
- `MID|dataProvider=APXMIDP|volume` = **4114.8** (n=103, 2026-09-22T18:42:13.356217Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=204, 2026-09-22T18:42:13.356217Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=204, 2026-09-22T18:42:13.356217Z)
- `NDF|TOTAL|demand` = **20673** (n=369, 2026-09-22T18:17:46.123884Z)
- `TSDF|TOTAL|demand` = **21173** (n=369, 2026-09-22T18:17:46.123884Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T18:46:17.913064Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:45:45Z`
- `2026-09-22T18:45:30.143617Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:45:00Z`
- `2026-09-22T18:44:09.953782Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:43:45Z`
- `2026-09-22T18:42:13.356217Z` — **MID**: 2 rows; marker `2026-09-22T18:42:04Z`
- `2026-09-22T18:42:13.356217Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:41:45Z`
- `2026-09-22T18:40:37.522258Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:40:00Z`
- `2026-09-22T18:40:21.087523Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:39:45Z`
- `2026-09-22T18:38:12.727178Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:37:45Z`
- `2026-09-22T18:36:35.900177Z` — **MID**: 1 rows; marker `2026-09-22T18:35:00Z`
- `2026-09-22T18:36:19.875646Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:35:45Z`
- `2026-09-22T18:35:32.642097Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:35:00Z`
- `2026-09-22T18:34:12.709506Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:33:45Z`
- `2026-09-22T18:32:19.943428Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:31:45Z`
- `2026-09-22T18:30:59.769122Z` — **FUELHH**: 20 rows; marker `2026-09-22T18:30:00Z`
- `2026-09-22T18:30:30.776436Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:30:00Z`
