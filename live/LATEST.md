# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T22:19:30.438810Z`  
Current process started UTC: `2026-09-22T22:15:29.372923Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2242, 2026-09-22T22:15:29.372931Z)
- `FUELINST|fuelType=OTHER|generation` = **300** (n=2242, 2026-09-22T22:15:29.372931Z)
- `FUELINST|fuelType=PS|generation` = **144** (n=2242, 2026-09-22T22:15:29.372931Z)
- `FUELINST|fuelType=WIND|generation` = **2564** (n=2242, 2026-09-22T22:15:29.372931Z)
- `IMBALNGC|TOTAL|imbalance` = **-8054** (n=368, 2026-09-22T21:51:18.504304Z)
- `INDDEM|TOTAL|demand` = **-12478** (n=368, 2026-09-22T21:51:02.571012Z)
- `INDGEN|TOTAL|generation` = **13119** (n=368, 2026-09-22T21:51:02.571012Z)
- `MELNGC|TOTAL|margin` = **37229** (n=369, 2026-09-22T22:19:28.499770Z)
- `MID|dataProvider=APXMIDP|price` = **142.47** (n=110, 2026-09-22T22:12:20.902810Z)
- `MID|dataProvider=APXMIDP|volume` = **2339.7** (n=110, 2026-09-22T22:12:20.902810Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=218, 2026-09-22T22:12:20.902810Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=218, 2026-09-22T22:12:20.902810Z)
- `NDF|TOTAL|demand` = **20673** (n=377, 2026-09-22T22:17:37.582289Z)
- `TSDF|TOTAL|demand` = **21173** (n=377, 2026-09-22T22:17:37.582289Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T22:19:28.499770Z` — **MELNGC**: 1062 rows; marker `2026-09-22T22:17:00Z`
- `2026-09-22T22:18:25.052026Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:17:45Z`
- `2026-09-22T22:17:37.582289Z` — **TSDF**: 1062 rows; marker `2026-09-22T22:17:00Z`
- `2026-09-22T22:17:37.582289Z` — **NDF**: 59 rows; marker `2026-09-22T22:17:00Z`
- `2026-09-22T22:16:17.376853Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:15:45Z`
- `2026-09-22T22:15:29.372931Z` — **FUELINST**: 80 rows; marker `2026-09-22T22:15:00Z`
- `2026-09-22T22:14:12.561729Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:13:45Z`
- `2026-09-22T22:12:20.902810Z` — **MID**: 2 rows; marker `2026-09-22T22:12:03Z`
- `2026-09-22T22:12:20.902810Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:11:45Z`
- `2026-09-22T22:10:33.283332Z` — **FUELINST**: 80 rows; marker `2026-09-22T22:10:00Z`
- `2026-09-22T22:10:17.081095Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:09:45Z`
- `2026-09-22T22:08:09.308062Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:07:45Z`
- `2026-09-22T22:06:38.221673Z` — **MID**: 1 rows; marker `2026-09-22T22:05:00Z`
- `2026-09-22T22:06:22.696839Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:05:45Z`
- `2026-09-22T22:05:34.509671Z` — **FUELINST**: 80 rows; marker `2026-09-22T22:05:00Z`
