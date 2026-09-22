# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T17:52:39.835767Z`  
Current process started UTC: `2026-09-22T17:48:39.706310Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=635, delta=0, z=9.94 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=832, delta=1, z=3.52 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2189, 2026-09-22T17:50:34.329913Z)
- `FUELINST|fuelType=OTHER|generation` = **2703** (n=2189, 2026-09-22T17:50:34.329913Z)
- `FUELINST|fuelType=PS|generation` = **1509** (n=2189, 2026-09-22T17:50:34.329913Z)
- `FUELINST|fuelType=WIND|generation` = **1382** (n=2189, 2026-09-22T17:50:34.329913Z)
- `IMBALNGC|TOTAL|imbalance` = **-7938** (n=359, 2026-09-22T17:22:24.916749Z)
- `INDDEM|TOTAL|demand` = **-12478** (n=360, 2026-09-22T17:52:10.596146Z)
- `INDGEN|TOTAL|generation` = **13233** (n=360, 2026-09-22T17:52:10.596146Z)
- `MELNGC|TOTAL|margin` = **37173** (n=360, 2026-09-22T17:49:30.712468Z)
- `MID|dataProvider=APXMIDP|price` = **227.31** (n=101, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=APXMIDP|volume` = **3881.3** (n=101, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=200, 2026-09-22T17:42:07.200932Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=200, 2026-09-22T17:42:07.200932Z)
- `NDF|TOTAL|demand` = **20673** (n=368, 2026-09-22T17:47:39.575069Z)
- `TSDF|TOTAL|demand` = **21173** (n=368, 2026-09-22T17:47:55.003325Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T17:52:10.596146Z` — **INDGEN**: 1224 rows; marker `2026-09-22T17:47:00Z`
- `2026-09-22T17:52:10.596146Z` — **INDDEM**: 1224 rows; marker `2026-09-22T17:47:00Z`
- `2026-09-22T17:52:10.596146Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:51:45Z`
- `2026-09-22T17:50:34.329913Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:50:00Z`
- `2026-09-22T17:50:34.329913Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:49:45Z`
- `2026-09-22T17:49:30.712468Z` — **MELNGC**: 1224 rows; marker `2026-09-22T17:47:00Z`
- `2026-09-22T17:48:10.867799Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:47:45Z`
- `2026-09-22T17:47:55.003325Z` — **TSDF**: 1224 rows; marker `2026-09-22T17:47:00Z`
- `2026-09-22T17:47:39.575069Z` — **NDF**: 68 rows; marker `2026-09-22T17:47:00Z`
- `2026-09-22T17:46:19.342895Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:45:45Z`
- `2026-09-22T17:45:31.573353Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:45:00Z`
- `2026-09-22T17:44:27.366944Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:43:45Z`
- `2026-09-22T17:42:22.561264Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:41:45Z`
- `2026-09-22T17:42:07.200932Z` — **MID**: 2 rows; marker `2026-09-22T17:42:03Z`
- `2026-09-22T17:40:31.338629Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:40:00Z`
