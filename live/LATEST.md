# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T17:31:30.038203Z`  
Current process started UTC: `2026-09-22T17:27:29.926879Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=823, delta=10, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=597, delta=1, z=11.96 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=587, delta=286, z=15.29 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=596, delta=1, z=12.35 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2185, 2026-09-22T17:30:26.121213Z)
- `FUELINST|fuelType=OTHER|generation` = **2386** (n=2185, 2026-09-22T17:30:26.121213Z)
- `FUELINST|fuelType=PS|generation` = **1509** (n=2185, 2026-09-22T17:30:26.121213Z)
- `FUELINST|fuelType=WIND|generation` = **1351** (n=2185, 2026-09-22T17:30:26.121213Z)
- `IMBALNGC|TOTAL|imbalance` = **-7938** (n=359, 2026-09-22T17:22:24.916749Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=359, 2026-09-22T17:22:24.916749Z)
- `INDGEN|TOTAL|generation` = **13236** (n=359, 2026-09-22T17:22:24.916749Z)
- `MELNGC|TOTAL|margin` = **37176** (n=359, 2026-09-22T17:20:15.251844Z)
- `MID|dataProvider=APXMIDP|price` = **236.8** (n=100, 2026-09-22T17:12:05.245859Z)
- `MID|dataProvider=APXMIDP|volume` = **4231.1** (n=100, 2026-09-22T17:12:05.245859Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=198, 2026-09-22T17:12:05.245859Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=198, 2026-09-22T17:12:05.245859Z)
- `NDF|TOTAL|demand` = **20673** (n=367, 2026-09-22T17:18:14.274069Z)
- `TSDF|TOTAL|demand` = **21173** (n=367, 2026-09-22T17:18:14.274069Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T17:30:41.695424Z` — **FUELHH**: 20 rows; marker `2026-09-22T17:30:00Z`
- `2026-09-22T17:30:26.121213Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:30:00Z`
- `2026-09-22T17:30:10.020779Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:29:45Z`
- `2026-09-22T17:28:17.932081Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:27:45Z`
- `2026-09-22T17:26:06.221845Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:25:45Z`
- `2026-09-22T17:25:34.535658Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:25:00Z`
- `2026-09-22T17:24:13.615861Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:23:45Z`
- `2026-09-22T17:22:24.916749Z` — **INDGEN**: 1242 rows; marker `2026-09-22T17:17:00Z`
- `2026-09-22T17:22:24.916749Z` — **INDDEM**: 1242 rows; marker `2026-09-22T17:17:00Z`
- `2026-09-22T17:22:24.916749Z` — **IMBALNGC**: 1242 rows; marker `2026-09-22T17:17:00Z`
- `2026-09-22T17:22:09.150226Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:21:45Z`
- `2026-09-22T17:20:31.046731Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:20:00Z`
- `2026-09-22T17:20:15.251844Z` — **MELNGC**: 1242 rows; marker `2026-09-22T17:17:00Z`
- `2026-09-22T17:20:15.251844Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:19:45Z`
- `2026-09-22T17:18:14.274069Z` — **TSDF**: 1242 rows; marker `2026-09-22T17:17:00Z`
