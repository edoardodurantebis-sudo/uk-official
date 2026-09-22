# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T17:48:28.159631Z`  
Current process started UTC: `2026-09-22T17:44:27.366936Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=635, delta=0, z=10.18 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=831, delta=0, z=3.52 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2188, 2026-09-22T17:45:31.573353Z)
- `FUELINST|fuelType=OTHER|generation` = **2638** (n=2188, 2026-09-22T17:45:31.573353Z)
- `FUELINST|fuelType=PS|generation` = **1508** (n=2188, 2026-09-22T17:45:31.573353Z)
- `FUELINST|fuelType=WIND|generation` = **1386** (n=2188, 2026-09-22T17:45:31.573353Z)
- `IMBALNGC|TOTAL|imbalance` = **-7938** (n=359, 2026-09-22T17:22:24.916749Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=359, 2026-09-22T17:22:24.916749Z)
- `INDGEN|TOTAL|generation` = **13236** (n=359, 2026-09-22T17:22:24.916749Z)
- `MELNGC|TOTAL|margin` = **37176** (n=359, 2026-09-22T17:20:15.251844Z)
- `MID|dataProvider=APXMIDP|price` = **227.31** (n=101, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=APXMIDP|volume` = **3881.3** (n=101, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=200, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=200, 2026-09-22T17:42:07.200932Z)
- `NDF|TOTAL|demand` = **20673** (n=368, 2026-09-22T17:47:39.575069Z)
- `TSDF|TOTAL|demand` = **21173** (n=368, 2026-09-22T17:47:55.003325Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T17:48:10.867799Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:47:45Z`
- `2026-09-22T17:47:55.003325Z` — **TSDF**: 1224 rows; marker `2026-09-22T17:47:00Z`
- `2026-09-22T17:47:39.575069Z` — **NDF**: 68 rows; marker `2026-09-22T17:47:00Z`
- `2026-09-22T17:46:19.342895Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:45:45Z`
- `2026-09-22T17:45:31.573353Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:45:00Z`
- `2026-09-22T17:44:27.366944Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:43:45Z`
- `2026-09-22T17:42:22.561264Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:41:45Z`
- `2026-09-22T17:42:07.200932Z` — **MID**: 2 rows; marker `2026-09-22T17:42:03Z`
- `2026-09-22T17:40:31.338629Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:40:00Z`
- `2026-09-22T17:40:14.922977Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:39:45Z`
- `2026-09-22T17:38:23.507853Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:37:45Z`
- `2026-09-22T17:37:35.863529Z` — **MID**: 1 rows; marker `2026-09-22T17:35:00Z`
- `2026-09-22T17:36:15.778159Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:35:45Z`
- `2026-09-22T17:35:27.403714Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:35:00Z`
- `2026-09-22T17:34:08.003333Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:33:45Z`
