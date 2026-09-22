# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T20:00:13.893568Z`  
Current process started UTC: `2026-09-22T19:56:12.792022Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2214, 2026-09-22T19:55:25.656785Z)
- `FUELINST|fuelType=OTHER|generation` = **1284** (n=2214, 2026-09-22T19:55:25.656785Z)
- `FUELINST|fuelType=PS|generation` = **1128** (n=2214, 2026-09-22T19:55:25.656785Z)
- `FUELINST|fuelType=WIND|generation` = **1909** (n=2214, 2026-09-22T19:55:25.656785Z)
- `IMBALNGC|TOTAL|imbalance` = **-8036** (n=364, 2026-09-22T19:51:57.816636Z)
- `INDDEM|TOTAL|demand` = **-12477** (n=364, 2026-09-22T19:51:26.846334Z)
- `INDGEN|TOTAL|generation` = **13137** (n=364, 2026-09-22T19:51:26.846334Z)
- `MELNGC|TOTAL|margin` = **37124** (n=364, 2026-09-22T19:49:19.880289Z)
- `MID|dataProvider=APXMIDP|price` = **200.57** (n=105, 2026-09-22T19:42:17.631824Z)
- `MID|dataProvider=APXMIDP|volume` = **4422.9** (n=105, 2026-09-22T19:42:17.631824Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=208, 2026-09-22T19:42:17.631824Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=208, 2026-09-22T19:42:17.631824Z)
- `NDF|TOTAL|demand` = **20673** (n=372, 2026-09-22T19:47:28.882193Z)
- `TSDF|TOTAL|demand` = **21173** (n=372, 2026-09-22T19:47:44.782521Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T20:00:12.131661Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:59:45Z`
- `2026-09-22T19:58:20.525719Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:57:45Z`
- `2026-09-22T19:56:12.792032Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:55:45Z`
- `2026-09-22T19:55:25.656785Z` — **FUELINST**: 80 rows; marker `2026-09-22T19:55:00Z`
- `2026-09-22T19:54:05.594558Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:53:45Z`
- `2026-09-22T19:52:13.711640Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:51:45Z`
- `2026-09-22T19:51:57.816636Z` — **IMBALNGC**: 1152 rows; marker `2026-09-22T19:47:00Z`
- `2026-09-22T19:51:26.846334Z` — **INDGEN**: 1152 rows; marker `2026-09-22T19:47:00Z`
- `2026-09-22T19:51:26.846334Z` — **INDDEM**: 1152 rows; marker `2026-09-22T19:47:00Z`
- `2026-09-22T19:50:38.794266Z` — **FUELINST**: 80 rows; marker `2026-09-22T19:50:00Z`
- `2026-09-22T19:50:23.292122Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:49:45Z`
- `2026-09-22T19:49:19.880289Z` — **MELNGC**: 1152 rows; marker `2026-09-22T19:47:00Z`
- `2026-09-22T19:48:16.147275Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:47:45Z`
- `2026-09-22T19:47:44.782521Z` — **TSDF**: 1152 rows; marker `2026-09-22T19:47:00Z`
- `2026-09-22T19:47:28.882193Z` — **NDF**: 64 rows; marker `2026-09-22T19:47:00Z`
