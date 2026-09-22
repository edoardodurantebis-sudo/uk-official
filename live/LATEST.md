# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T22:53:13.780582Z`  
Current process started UTC: `2026-09-22T22:49:14.019886Z`  
1-second metadata polls in this process: **233**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2249, 2026-09-22T22:50:34.832167Z)
- `FUELINST|fuelType=OTHER|generation` = **164** (n=2249, 2026-09-22T22:50:34.832167Z)
- `FUELINST|fuelType=PS|generation` = **148** (n=2249, 2026-09-22T22:50:34.832167Z)
- `FUELINST|fuelType=WIND|generation` = **2877** (n=2249, 2026-09-22T22:50:34.832167Z)
- `IMBALNGC|TOTAL|imbalance` = **-8056** (n=370, 2026-09-22T22:51:06.313942Z)
- `INDDEM|TOTAL|demand` = **-12493** (n=370, 2026-09-22T22:51:06.313942Z)
- `INDGEN|TOTAL|generation` = **13117** (n=370, 2026-09-22T22:51:06.313942Z)
- `MELNGC|TOTAL|margin` = **37229** (n=370, 2026-09-22T22:49:14.019892Z)
- `MID|dataProvider=APXMIDP|price` = **149.06** (n=111, 2026-09-22T22:42:09.286704Z)
- `MID|dataProvider=APXMIDP|volume` = **2075.2** (n=111, 2026-09-22T22:42:09.286704Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=218, 2026-09-22T22:12:20.902810Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=218, 2026-09-22T22:12:20.902810Z)
- `NDF|TOTAL|demand` = **20673** (n=378, 2026-09-22T22:47:24.442258Z)
- `TSDF|TOTAL|demand` = **21173** (n=378, 2026-09-22T22:47:24.442258Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T22:52:10.148126Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:51:45Z`
- `2026-09-22T22:51:06.313942Z` — **INDGEN**: 1044 rows; marker `2026-09-22T22:47:00Z`
- `2026-09-22T22:51:06.313942Z` — **INDDEM**: 1044 rows; marker `2026-09-22T22:47:00Z`
- `2026-09-22T22:51:06.313942Z` — **IMBALNGC**: 1044 rows; marker `2026-09-22T22:47:00Z`
- `2026-09-22T22:50:34.832167Z` — **FUELINST**: 80 rows; marker `2026-09-22T22:50:00Z`
- `2026-09-22T22:50:18.381754Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:49:45Z`
- `2026-09-22T22:49:14.019892Z` — **MELNGC**: 1044 rows; marker `2026-09-22T22:47:00Z`
- `2026-09-22T22:48:12.483336Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:47:45Z`
- `2026-09-22T22:47:24.442258Z` — **TSDF**: 1044 rows; marker `2026-09-22T22:47:00Z`
- `2026-09-22T22:47:24.442258Z` — **NDF**: 58 rows; marker `2026-09-22T22:47:00Z`
- `2026-09-22T22:46:04.725925Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:45:45Z`
- `2026-09-22T22:45:32.147568Z` — **FUELINST**: 80 rows; marker `2026-09-22T22:45:00Z`
- `2026-09-22T22:44:32.652014Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:43:45Z`
- `2026-09-22T22:42:09.286704Z` — **MID**: 1 rows; marker `2026-09-22T22:42:03Z`
- `2026-09-22T22:42:09.286704Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:41:45Z`
