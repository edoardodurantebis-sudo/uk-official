# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T19:30:40.027970Z`  
Current process started UTC: `2026-09-22T19:26:39.953797Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=635, delta=0, z=9.42 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2208, 2026-09-22T19:25:22.925372Z)
- `FUELINST|fuelType=OTHER|generation` = **1970** (n=2208, 2026-09-22T19:25:22.925372Z)
- `FUELINST|fuelType=PS|generation` = **1365** (n=2208, 2026-09-22T19:25:22.925372Z)
- `FUELINST|fuelType=WIND|generation` = **1731** (n=2208, 2026-09-22T19:25:22.925372Z)
- `IMBALNGC|TOTAL|imbalance` = **-8035** (n=363, 2026-09-22T19:21:54.940895Z)
- `INDDEM|TOTAL|demand` = **-12477** (n=363, 2026-09-22T19:21:54.940895Z)
- `INDGEN|TOTAL|generation` = **13138** (n=363, 2026-09-22T19:21:54.940895Z)
- `MELNGC|TOTAL|margin` = **37122** (n=363, 2026-09-22T19:19:32.717871Z)
- `MID|dataProvider=APXMIDP|price` = **213.71** (n=104, 2026-09-22T19:12:11.784214Z)
- `MID|dataProvider=APXMIDP|volume` = **4290.7** (n=104, 2026-09-22T19:12:11.784214Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=206, 2026-09-22T19:12:11.784214Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=206, 2026-09-22T19:12:11.784214Z)
- `NDF|TOTAL|demand` = **20673** (n=371, 2026-09-22T19:17:35.772457Z)
- `TSDF|TOTAL|demand` = **21173** (n=371, 2026-09-22T19:17:35.772457Z)
- `WINDFOR|TOTAL|generation` = **13535** (n=62, 2026-09-22T16:30:39.657630Z)

## Latest publication events

- `2026-09-22T19:30:26.122301Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:29:45Z`
- `2026-09-22T19:28:17.965680Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:27:45Z`
- `2026-09-22T19:26:10.485989Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:25:45Z`
- `2026-09-22T19:25:22.925372Z` — **FUELINST**: 80 rows; marker `2026-09-22T19:25:00Z`
- `2026-09-22T19:24:18.770939Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:23:45Z`
- `2026-09-22T19:22:26.579656Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:21:45Z`
- `2026-09-22T19:21:54.940895Z` — **INDGEN**: 1170 rows; marker `2026-09-22T19:17:00Z`
- `2026-09-22T19:21:54.940895Z` — **INDDEM**: 1170 rows; marker `2026-09-22T19:17:00Z`
- `2026-09-22T19:21:54.940895Z` — **IMBALNGC**: 1170 rows; marker `2026-09-22T19:17:00Z`
- `2026-09-22T19:20:34.877161Z` — **FUELINST**: 80 rows; marker `2026-09-22T19:20:00Z`
- `2026-09-22T19:20:19.408377Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:19:45Z`
- `2026-09-22T19:19:32.717871Z` — **MELNGC**: 1170 rows; marker `2026-09-22T19:17:00Z`
- `2026-09-22T19:18:13.158686Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:17:45Z`
- `2026-09-22T19:17:35.772457Z` — **TSDF**: 1170 rows; marker `2026-09-22T19:17:00Z`
- `2026-09-22T19:17:35.772457Z` — **NDF**: 65 rows; marker `2026-09-22T19:17:00Z`
