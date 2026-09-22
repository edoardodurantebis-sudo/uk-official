# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T20:12:55.855046Z`  
Current process started UTC: `2026-09-22T20:08:55.731237Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2217, 2026-09-22T20:10:35.806840Z)
- `FUELINST|fuelType=OTHER|generation` = **841** (n=2217, 2026-09-22T20:10:35.806840Z)
- `FUELINST|fuelType=PS|generation` = **883** (n=2217, 2026-09-22T20:10:35.806840Z)
- `FUELINST|fuelType=WIND|generation` = **1977** (n=2217, 2026-09-22T20:10:35.806840Z)
- `IMBALNGC|TOTAL|imbalance` = **-8036** (n=364, 2026-09-22T19:51:57.816636Z)
- `INDDEM|TOTAL|demand` = **-12477** (n=364, 2026-09-22T19:51:26.846334Z)
- `INDGEN|TOTAL|generation` = **13137** (n=364, 2026-09-22T19:51:26.846334Z)
- `MELNGC|TOTAL|margin` = **37124** (n=364, 2026-09-22T19:49:19.880289Z)
- `MID|dataProvider=APXMIDP|price` = **190.89** (n=106, 2026-09-22T20:12:12.354760Z)
- `MID|dataProvider=APXMIDP|volume` = **4249.8** (n=106, 2026-09-22T20:12:12.354760Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=210, 2026-09-22T20:12:12.354760Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=210, 2026-09-22T20:12:12.354760Z)
- `NDF|TOTAL|demand` = **20673** (n=372, 2026-09-22T19:47:28.882193Z)
- `TSDF|TOTAL|demand` = **21173** (n=372, 2026-09-22T19:47:44.782521Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T20:12:28.486945Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:11:45Z`
- `2026-09-22T20:12:12.354760Z` — **MID**: 2 rows; marker `2026-09-22T20:12:04Z`
- `2026-09-22T20:10:35.806840Z` — **FUELINST**: 80 rows; marker `2026-09-22T20:10:00Z`
- `2026-09-22T20:10:19.741642Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:09:45Z`
- `2026-09-22T20:08:27.586200Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:07:45Z`
- `2026-09-22T20:06:19.330857Z` — **MID**: 1 rows; marker `2026-09-22T20:05:00Z`
- `2026-09-22T20:06:19.330857Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:05:45Z`
- `2026-09-22T20:05:31.890626Z` — **FUELINST**: 80 rows; marker `2026-09-22T20:05:00Z`
- `2026-09-22T20:04:13.645840Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:03:45Z`
- `2026-09-22T20:02:20.894890Z` — **FREQ**: 5761 rows; marker `2026-09-22T20:01:45Z`
- `2026-09-22T20:00:28.221658Z` — **FUELHH**: 20 rows; marker `2026-09-22T20:00:00Z`
- `2026-09-22T20:00:28.221658Z` — **FUELINST**: 80 rows; marker `2026-09-22T20:00:00Z`
- `2026-09-22T20:00:12.131661Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:59:45Z`
- `2026-09-22T19:58:20.525719Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:57:45Z`
- `2026-09-22T19:56:12.792032Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:55:45Z`
