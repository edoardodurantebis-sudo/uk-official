# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T18:56:24.652059Z`  
Current process started UTC: `2026-09-22T18:52:24.632538Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=635, delta=0, z=9.42 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=832, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3685, delta=-56, z=4.34 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=633, delta=1, z=8.48 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3741, delta=69, z=4.44 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2202, 2026-09-22T18:55:38.490292Z)
- `FUELINST|fuelType=OTHER|generation` = **3152** (n=2202, 2026-09-22T18:55:38.490292Z)
- `FUELINST|fuelType=PS|generation` = **1509** (n=2202, 2026-09-22T18:55:38.490292Z)
- `FUELINST|fuelType=WIND|generation` = **1709** (n=2202, 2026-09-22T18:55:38.490292Z)
- `IMBALNGC|TOTAL|imbalance` = **-7982** (n=362, 2026-09-22T18:52:09.988158Z)
- `INDDEM|TOTAL|demand` = **-12477** (n=362, 2026-09-22T18:52:09.988158Z)
- `INDGEN|TOTAL|generation` = **13192** (n=362, 2026-09-22T18:52:09.988158Z)
- `MELNGC|TOTAL|margin` = **37168** (n=362, 2026-09-22T18:49:46.589650Z)
- `MID|dataProvider=APXMIDP|price` = **224.96** (n=103, 2026-09-22T18:42:13.356217Z)
- `MID|dataProvider=APXMIDP|volume` = **4114.8** (n=103, 2026-09-22T18:42:13.356217Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=204, 2026-09-22T18:42:13.356217Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=204, 2026-09-22T18:42:13.356217Z)
- `NDF|TOTAL|demand` = **20673** (n=370, 2026-09-22T18:48:10.178049Z)
- `TSDF|TOTAL|demand` = **21173** (n=370, 2026-09-22T18:48:10.178049Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T18:55:38.490292Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:55:00Z`
- `2026-09-22T18:54:18.207799Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:53:45Z`
- `2026-09-22T18:52:25.632681Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:51:45Z`
- `2026-09-22T18:52:09.988158Z` — **INDGEN**: 1188 rows; marker `2026-09-22T18:47:00Z`
- `2026-09-22T18:52:09.988158Z` — **INDDEM**: 1188 rows; marker `2026-09-22T18:47:00Z`
- `2026-09-22T18:52:09.988158Z` — **IMBALNGC**: 1188 rows; marker `2026-09-22T18:47:00Z`
- `2026-09-22T18:50:33.884958Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:50:00Z`
- `2026-09-22T18:50:17.915849Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:49:45Z`
- `2026-09-22T18:49:46.589650Z` — **MELNGC**: 1188 rows; marker `2026-09-22T18:47:00Z`
- `2026-09-22T18:48:10.178049Z` — **TSDF**: 1188 rows; marker `2026-09-22T18:47:00Z`
- `2026-09-22T18:48:10.178049Z` — **NDF**: 66 rows; marker `2026-09-22T18:47:00Z`
- `2026-09-22T18:48:10.178049Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:47:45Z`
- `2026-09-22T18:46:17.913064Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:45:45Z`
- `2026-09-22T18:45:30.143617Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:45:00Z`
- `2026-09-22T18:44:09.953782Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:43:45Z`
