# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T03:19:54.385220Z`  
Current process started UTC: `2026-09-23T03:15:54.373811Z`  
1-second metadata polls in this process: **230**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2302, 2026-09-23T03:15:39.743496Z)
- `FUELINST|fuelType=OTHER|generation` = **388** (n=2302, 2026-09-23T03:15:39.743496Z)
- `FUELINST|fuelType=PS|generation` = **-11** (n=2302, 2026-09-23T03:15:39.743496Z)
- `FUELINST|fuelType=WIND|generation` = **5840** (n=2302, 2026-09-23T03:15:39.743496Z)
- `IMBALNGC|TOTAL|imbalance` = **-7980** (n=378, 2026-09-23T02:50:54.801224Z)
- `INDDEM|TOTAL|demand` = **-12419** (n=378, 2026-09-23T02:50:38.459440Z)
- `INDGEN|TOTAL|generation` = **13193** (n=378, 2026-09-23T02:50:38.459440Z)
- `MELNGC|TOTAL|margin` = **38571** (n=379, 2026-09-23T03:19:09.641247Z)
- `MID|dataProvider=APXMIDP|price` = **144.45** (n=120, 2026-09-23T03:12:11.959147Z)
- `MID|dataProvider=APXMIDP|volume` = **2189.7** (n=120, 2026-09-23T03:12:11.959147Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=236, 2026-09-23T03:12:11.959147Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=236, 2026-09-23T03:12:11.959147Z)
- `NDF|TOTAL|demand` = **20673** (n=387, 2026-09-23T03:17:16.723089Z)
- `TSDF|TOTAL|demand` = **21173** (n=387, 2026-09-23T03:17:16.723089Z)
- `WINDFOR|TOTAL|generation` = **13770** (n=64, 2026-09-22T23:30:32.481751Z)

## Latest publication events

- `2026-09-23T03:19:09.641247Z` — **MELNGC**: 882 rows; marker `2026-09-23T03:16:00Z`
- `2026-09-23T03:18:21.309236Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:17:45Z`
- `2026-09-23T03:17:16.723089Z` — **TSDF**: 882 rows; marker `2026-09-23T03:16:00Z`
- `2026-09-23T03:17:16.723089Z` — **NDF**: 49 rows; marker `2026-09-23T03:16:00Z`
- `2026-09-23T03:16:11.393954Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:15:45Z`
- `2026-09-23T03:15:39.743496Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:15:00Z`
- `2026-09-23T03:14:20.116280Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:13:45Z`
- `2026-09-23T03:12:11.959147Z` — **MID**: 2 rows; marker `2026-09-23T03:12:03Z`
- `2026-09-23T03:12:11.959147Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:11:45Z`
- `2026-09-23T03:10:35.385230Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:10:00Z`
- `2026-09-23T03:10:19.142144Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:09:45Z`
- `2026-09-23T03:08:11.589289Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:07:45Z`
- `2026-09-23T03:07:23.829139Z` — **MID**: 1 rows; marker `2026-09-23T03:05:00Z`
- `2026-09-23T03:06:08.358982Z` — **FREQ**: 5761 rows; marker `2026-09-23T03:05:45Z`
- `2026-09-23T03:05:36.140844Z` — **FUELINST**: 80 rows; marker `2026-09-23T03:05:00Z`
