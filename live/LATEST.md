# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T04:06:07.390376Z`  
Current process started UTC: `2026-09-23T04:02:07.934113Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2312, 2026-09-23T04:05:36.313853Z)
- `FUELINST|fuelType=OTHER|generation` = **216** (n=2312, 2026-09-23T04:05:36.313853Z)
- `FUELINST|fuelType=PS|generation` = **144** (n=2312, 2026-09-23T04:05:36.313853Z)
- `FUELINST|fuelType=WIND|generation` = **7639** (n=2312, 2026-09-23T04:05:36.313853Z)
- `IMBALNGC|TOTAL|imbalance` = **-8081** (n=380, 2026-09-23T03:51:07.776008Z)
- `INDDEM|TOTAL|demand` = **-12404** (n=380, 2026-09-23T03:50:50.995108Z)
- `INDGEN|TOTAL|generation` = **13092** (n=380, 2026-09-23T03:50:50.995108Z)
- `MELNGC|TOTAL|margin` = **38548** (n=380, 2026-09-23T03:49:47.123502Z)
- `MID|dataProvider=APXMIDP|price` = **142.05** (n=121, 2026-09-23T03:42:14.086126Z)
- `MID|dataProvider=APXMIDP|volume` = **2444.8** (n=121, 2026-09-23T03:42:14.086126Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=238, 2026-09-23T03:42:14.086126Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=238, 2026-09-23T03:42:14.086126Z)
- `NDF|TOTAL|demand` = **20673** (n=388, 2026-09-23T03:47:43.996474Z)
- `TSDF|TOTAL|demand` = **21173** (n=388, 2026-09-23T03:47:43.996474Z)
- `WINDFOR|TOTAL|generation` = **7477** (n=65, 2026-09-23T03:30:40.879035Z)

## Latest publication events

- `2026-09-23T04:05:36.313853Z` — **FUELINST**: 80 rows; marker `2026-09-23T04:05:00Z`
- `2026-09-23T04:04:16.557329Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:03:45Z`
- `2026-09-23T04:02:24.159778Z` — **FREQ**: 5761 rows; marker `2026-09-23T04:01:45Z`
- `2026-09-23T04:00:39.032184Z` — **FUELHH**: 20 rows; marker `2026-09-23T04:00:00Z`
- `2026-09-23T04:00:39.032184Z` — **FUELINST**: 80 rows; marker `2026-09-23T04:00:00Z`
- `2026-09-23T04:00:22.574242Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:59:45Z`
- `2026-09-23T03:58:30.706704Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:57:45Z`
- `2026-09-23T03:56:23.464597Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:55:45Z`
- `2026-09-23T03:55:35.864099Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:55:00Z`
- `2026-09-23T03:54:16.092652Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:53:45Z`
- `2026-09-23T03:52:11.315235Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:51:45Z`
- `2026-09-23T03:51:07.776008Z` — **IMBALNGC**: 864 rows; marker `2026-09-23T03:47:00Z`
- `2026-09-23T03:50:50.995108Z` — **INDGEN**: 864 rows; marker `2026-09-23T03:47:00Z`
- `2026-09-23T03:50:50.995108Z` — **INDDEM**: 864 rows; marker `2026-09-23T03:47:00Z`
- `2026-09-23T03:50:34.756965Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:50:00Z`
