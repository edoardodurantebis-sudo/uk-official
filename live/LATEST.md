# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T17:44:13.566932Z`  
Current process started UTC: `2026-09-22T17:40:13.922862Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=635, delta=0, z=10.43 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=831, delta=0, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=635, delta=1, z=10.70 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=831, delta=0, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=613, delta=26, z=12.48 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=827, delta=54, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=634, delta=1, z=10.98 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=831, delta=0, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=633, delta=13, z=11.28 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=831, delta=0, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=620, delta=22, z=11.36 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=831, delta=-2, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=598, delta=2, z=11.26 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=833, delta=10, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=596, delta=-1, z=11.56 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2187, 2026-09-22T17:40:31.338629Z)
- `FUELINST|fuelType=OTHER|generation` = **2578** (n=2187, 2026-09-22T17:40:31.338629Z)
- `FUELINST|fuelType=PS|generation` = **1508** (n=2187, 2026-09-22T17:40:31.338629Z)
- `FUELINST|fuelType=WIND|generation` = **1377** (n=2187, 2026-09-22T17:40:31.338629Z)
- `IMBALNGC|TOTAL|imbalance` = **-7938** (n=359, 2026-09-22T17:22:24.916749Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=359, 2026-09-22T17:22:24.916749Z)
- `INDGEN|TOTAL|generation` = **13236** (n=359, 2026-09-22T17:22:24.916749Z)
- `MELNGC|TOTAL|margin` = **37176** (n=359, 2026-09-22T17:20:15.251844Z)
- `MID|dataProvider=APXMIDP|price` = **227.31** (n=101, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=APXMIDP|volume` = **3881.3** (n=101, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=200, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=200, 2026-09-22T17:42:07.200932Z)
- `NDF|TOTAL|demand` = **20673** (n=367, 2026-09-22T17:18:14.274069Z)
- `TSDF|TOTAL|demand` = **21173** (n=367, 2026-09-22T17:18:14.274069Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T17:42:22.561264Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:41:45Z`
- `2026-09-22T17:42:07.200932Z` — **MID**: 2 rows; marker `2026-09-22T17:42:03Z`
- `2026-09-22T17:40:31.338629Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:40:00Z`
- `2026-09-22T17:40:14.922977Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:39:45Z`
- `2026-09-22T17:38:23.507853Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:37:45Z`
- `2026-09-22T17:37:35.863529Z` — **MID**: 1 rows; marker `2026-09-22T17:35:00Z`
- `2026-09-22T17:36:15.778159Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:35:45Z`
- `2026-09-22T17:35:27.403714Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:35:00Z`
- `2026-09-22T17:34:08.003333Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:33:45Z`
- `2026-09-22T17:32:16.517551Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:31:45Z`
- `2026-09-22T17:30:41.695424Z` — **FUELHH**: 20 rows; marker `2026-09-22T17:30:00Z`
- `2026-09-22T17:30:26.121213Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:30:00Z`
- `2026-09-22T17:30:10.020779Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:29:45Z`
- `2026-09-22T17:28:17.932081Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:27:45Z`
- `2026-09-22T17:26:06.221845Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:25:45Z`
