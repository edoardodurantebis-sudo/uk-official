# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T00:13:08.252626Z`  
Current process started UTC: `2026-09-23T00:09:06.698093Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2265, 2026-09-23T00:10:26.708728Z)
- `FUELINST|fuelType=OTHER|generation` = **206** (n=2265, 2026-09-23T00:10:26.708728Z)
- `FUELINST|fuelType=PS|generation` = **147** (n=2265, 2026-09-23T00:10:26.708728Z)
- `FUELINST|fuelType=WIND|generation` = **3910** (n=2265, 2026-09-23T00:10:26.708728Z)
- `IMBALNGC|TOTAL|imbalance` = **-7998** (n=372, 2026-09-22T23:50:47.210542Z)
- `INDDEM|TOTAL|demand` = **-12486** (n=372, 2026-09-22T23:50:47.210542Z)
- `INDGEN|TOTAL|generation` = **13175** (n=372, 2026-09-22T23:50:47.210542Z)
- `MELNGC|TOTAL|margin` = **37219** (n=372, 2026-09-22T23:48:55.280062Z)
- `MID|dataProvider=APXMIDP|price` = **149.47** (n=114, 2026-09-23T00:12:18.807483Z)
- `MID|dataProvider=APXMIDP|volume` = **2227.9** (n=114, 2026-09-23T00:12:18.807483Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=224, 2026-09-23T00:12:18.807483Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=224, 2026-09-23T00:12:18.807483Z)
- `NDF|TOTAL|demand` = **20673** (n=380, 2026-09-22T23:47:09.882400Z)
- `TSDF|TOTAL|demand` = **21173** (n=380, 2026-09-22T23:47:25.302034Z)
- `WINDFOR|TOTAL|generation` = **13770** (n=64, 2026-09-22T23:30:32.481751Z)

## Latest publication events

- `2026-09-23T00:12:18.807483Z` — **MID**: 2 rows; marker `2026-09-23T00:12:03Z`
- `2026-09-23T00:12:18.807483Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:11:45Z`
- `2026-09-23T00:10:26.708728Z` — **FUELINST**: 80 rows; marker `2026-09-23T00:10:00Z`
- `2026-09-23T00:10:26.708728Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:09:45Z`
- `2026-09-23T00:08:08.338230Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:07:45Z`
- `2026-09-23T00:06:31.832268Z` — **MID**: 1 rows; marker `2026-09-23T00:05:00Z`
- `2026-09-23T00:06:14.653062Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:05:45Z`
- `2026-09-23T00:05:26.756522Z` — **FUELINST**: 80 rows; marker `2026-09-23T00:05:00Z`
- `2026-09-23T00:04:12.064411Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:03:45Z`
- `2026-09-23T00:02:20.256014Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:01:45Z`
- `2026-09-23T00:00:43.912481Z` — **FUELHH**: 20 rows; marker `2026-09-23T00:00:00Z`
- `2026-09-23T00:00:27.754997Z` — **FUELINST**: 80 rows; marker `2026-09-23T00:00:00Z`
- `2026-09-23T00:00:11.973275Z` — **FREQ**: 5760 rows; marker `2026-09-22T23:59:45Z`
- `2026-09-22T23:58:20.416329Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:57:45Z`
- `2026-09-22T23:56:28.844039Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:55:45Z`
