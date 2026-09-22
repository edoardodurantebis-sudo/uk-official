# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T23:26:53.203483Z`  
Current process started UTC: `2026-09-22T23:22:52.860691Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2256, 2026-09-22T23:25:33.607775Z)
- `FUELINST|fuelType=OTHER|generation` = **246** (n=2256, 2026-09-22T23:25:33.607775Z)
- `FUELINST|fuelType=PS|generation` = **147** (n=2256, 2026-09-22T23:25:33.607775Z)
- `FUELINST|fuelType=WIND|generation` = **3167** (n=2256, 2026-09-22T23:25:33.607775Z)
- `IMBALNGC|TOTAL|imbalance` = **-8049** (n=371, 2026-09-22T23:20:54.957362Z)
- `INDDEM|TOTAL|demand` = **-12484** (n=371, 2026-09-22T23:20:38.644672Z)
- `INDGEN|TOTAL|generation` = **13124** (n=371, 2026-09-22T23:20:38.644672Z)
- `MELNGC|TOTAL|margin` = **37229** (n=371, 2026-09-22T23:19:02.295219Z)
- `MID|dataProvider=APXMIDP|price` = **152.39** (n=112, 2026-09-22T23:12:13.961447Z)
- `MID|dataProvider=APXMIDP|volume` = **2011.5** (n=112, 2026-09-22T23:12:13.961447Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=220, 2026-09-22T23:12:13.961447Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=220, 2026-09-22T23:12:13.961447Z)
- `NDF|TOTAL|demand` = **20673** (n=379, 2026-09-22T23:17:27.155171Z)
- `TSDF|TOTAL|demand` = **21173** (n=379, 2026-09-22T23:17:27.155171Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T23:26:21.926919Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:25:45Z`
- `2026-09-22T23:25:33.607775Z` — **FUELINST**: 80 rows; marker `2026-09-22T23:25:00Z`
- `2026-09-22T23:24:13.693826Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:23:45Z`
- `2026-09-22T23:22:14.352661Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:21:45Z`
- `2026-09-22T23:20:54.957362Z` — **IMBALNGC**: 1026 rows; marker `2026-09-22T23:17:00Z`
- `2026-09-22T23:20:38.644672Z` — **INDGEN**: 1026 rows; marker `2026-09-22T23:16:00Z`
- `2026-09-22T23:20:38.644672Z` — **INDDEM**: 1026 rows; marker `2026-09-22T23:16:00Z`
- `2026-09-22T23:20:38.644672Z` — **FUELINST**: 80 rows; marker `2026-09-22T23:20:00Z`
- `2026-09-22T23:20:23.121390Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:19:45Z`
- `2026-09-22T23:19:02.295219Z` — **MELNGC**: 1026 rows; marker `2026-09-22T23:17:00Z`
- `2026-09-22T23:18:14.474523Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:17:45Z`
- `2026-09-22T23:17:27.155171Z` — **TSDF**: 1026 rows; marker `2026-09-22T23:17:00Z`
- `2026-09-22T23:17:27.155171Z` — **NDF**: 57 rows; marker `2026-09-22T23:17:00Z`
- `2026-09-22T23:16:22.968372Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:15:45Z`
- `2026-09-22T23:15:34.919147Z` — **FUELINST**: 80 rows; marker `2026-09-22T23:15:00Z`
