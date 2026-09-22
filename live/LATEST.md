# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T17:18:42.078154Z`  
Current process started UTC: `2026-09-22T17:14:42.110762Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=598, delta=2, z=11.26 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=833, delta=10, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=596, delta=-1, z=11.56 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=823, delta=10, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=597, delta=1, z=11.96 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=587, delta=286, z=15.29 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=596, delta=1, z=12.35 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=595, delta=1, z=12.79 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=594, delta=1, z=13.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=593, delta=0, z=13.83 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=593, delta=45, z=14.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=548, delta=67, z=13.93 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=301, delta=202, z=8.27 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=481, delta=100, z=12.60 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=381, delta=82, z=10.10 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2182, 2026-09-22T17:15:34.588501Z)
- `FUELINST|fuelType=OTHER|generation` = **2293** (n=2182, 2026-09-22T17:15:34.588501Z)
- `FUELINST|fuelType=PS|generation` = **1508** (n=2182, 2026-09-22T17:15:34.588501Z)
- `FUELINST|fuelType=WIND|generation` = **1345** (n=2182, 2026-09-22T17:15:34.588501Z)
- `IMBALNGC|TOTAL|imbalance` = **-7954** (n=358, 2026-09-22T16:53:45.809507Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=358, 2026-09-22T16:53:29.392532Z)
- `INDGEN|TOTAL|generation` = **13219** (n=358, 2026-09-22T16:53:45.809507Z)
- `MELNGC|TOTAL|margin` = **37151** (n=358, 2026-09-22T16:50:03.584874Z)
- `MID|dataProvider=APXMIDP|price` = **236.8** (n=100, 2026-09-22T17:12:05.245859Z)
- `MID|dataProvider=APXMIDP|volume` = **4231.1** (n=100, 2026-09-22T17:12:05.245859Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=198, 2026-09-22T17:12:05.245859Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=198, 2026-09-22T17:12:05.245859Z)
- `NDF|TOTAL|demand` = **20673** (n=367, 2026-09-22T17:18:14.274069Z)
- `TSDF|TOTAL|demand` = **21173** (n=367, 2026-09-22T17:18:14.274069Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T17:18:14.274069Z` — **TSDF**: 1242 rows; marker `2026-09-22T17:17:00Z`
- `2026-09-22T17:18:14.274069Z` — **NDF**: 69 rows; marker `2026-09-22T17:17:00Z`
- `2026-09-22T17:18:14.274069Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:17:45Z`
- `2026-09-22T17:16:21.868430Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:15:45Z`
- `2026-09-22T17:15:34.588501Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:15:00Z`
- `2026-09-22T17:14:29.059045Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:13:45Z`
- `2026-09-22T17:12:21.390849Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:11:45Z`
- `2026-09-22T17:12:05.245859Z` — **MID**: 2 rows; marker `2026-09-22T17:12:02Z`
- `2026-09-22T17:10:45.213316Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:10:00Z`
- `2026-09-22T17:10:29.499452Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:09:45Z`
- `2026-09-22T17:08:24.066132Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:07:45Z`
- `2026-09-22T17:06:14.637297Z` — **MID**: 1 rows; marker `2026-09-22T17:05:00Z`
- `2026-09-22T17:06:14.637297Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:05:45Z`
- `2026-09-22T17:05:42.480228Z` — **FUELINST**: 80 rows; marker `2026-09-22T17:05:00Z`
- `2026-09-22T17:04:23.004474Z` — **FREQ**: 5761 rows; marker `2026-09-22T17:03:45Z`
