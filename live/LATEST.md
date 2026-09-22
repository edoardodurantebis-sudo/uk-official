# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T18:39:16.226659Z`  
Current process started UTC: `2026-09-22T18:35:16.613094Z`  
1-second metadata polls in this process: **233**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3704, delta=270, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=637, delta=0, z=9.00 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3434, delta=339, z=4.03 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=637, delta=0, z=9.17 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2198, 2026-09-22T18:35:32.642097Z)
- `FUELINST|fuelType=OTHER|generation` = **3465** (n=2198, 2026-09-22T18:35:32.642097Z)
- `FUELINST|fuelType=PS|generation` = **1459** (n=2198, 2026-09-22T18:35:32.642097Z)
- `FUELINST|fuelType=WIND|generation` = **1718** (n=2198, 2026-09-22T18:35:32.642097Z)
- `IMBALNGC|TOTAL|imbalance` = **-8008** (n=361, 2026-09-22T18:22:34.684273Z)
- `INDDEM|TOTAL|demand` = **-12478** (n=361, 2026-09-22T18:22:05.951674Z)
- `INDGEN|TOTAL|generation` = **13165** (n=361, 2026-09-22T18:22:05.951674Z)
- `MELNGC|TOTAL|margin` = **37157** (n=361, 2026-09-22T18:19:41.061285Z)
- `MID|dataProvider=APXMIDP|price` = **228.4** (n=102, 2026-09-22T18:12:16.637488Z)
- `MID|dataProvider=APXMIDP|volume` = **3689.8** (n=102, 2026-09-22T18:12:16.637488Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=203, 2026-09-22T18:36:35.900177Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=203, 2026-09-22T18:36:35.900177Z)
- `NDF|TOTAL|demand` = **20673** (n=369, 2026-09-22T18:17:46.123884Z)
- `TSDF|TOTAL|demand` = **21173** (n=369, 2026-09-22T18:17:46.123884Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T18:38:12.727178Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:37:45Z`
- `2026-09-22T18:36:35.900177Z` — **MID**: 1 rows; marker `2026-09-22T18:35:00Z`
- `2026-09-22T18:36:19.875646Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:35:45Z`
- `2026-09-22T18:35:32.642097Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:35:00Z`
- `2026-09-22T18:34:12.709506Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:33:45Z`
- `2026-09-22T18:32:19.943428Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:31:45Z`
- `2026-09-22T18:30:59.769122Z` — **FUELHH**: 20 rows; marker `2026-09-22T18:30:00Z`
- `2026-09-22T18:30:30.776436Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:30:00Z`
- `2026-09-22T18:30:14.526537Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:29:45Z`
- `2026-09-22T18:28:07.110937Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:27:45Z`
- `2026-09-22T18:26:04.087526Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:25:45Z`
- `2026-09-22T18:25:32.056604Z` — **FUELINST**: 80 rows; marker `2026-09-22T18:25:00Z`
- `2026-09-22T18:24:12.231114Z` — **FREQ**: 5761 rows; marker `2026-09-22T18:23:45Z`
- `2026-09-22T18:22:34.684273Z` — **IMBALNGC**: 1206 rows; marker `2026-09-22T18:17:00Z`
- `2026-09-22T18:22:05.951674Z` — **INDGEN**: 1206 rows; marker `2026-09-22T18:17:00Z`
