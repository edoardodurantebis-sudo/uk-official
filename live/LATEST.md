# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T19:43:18.004872Z`  
Current process started UTC: `2026-09-22T19:39:18.178982Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2211, 2026-09-22T19:40:41.551689Z)
- `FUELINST|fuelType=OTHER|generation` = **1752** (n=2211, 2026-09-22T19:40:41.551689Z)
- `FUELINST|fuelType=PS|generation` = **1151** (n=2211, 2026-09-22T19:40:41.551689Z)
- `FUELINST|fuelType=WIND|generation` = **1811** (n=2211, 2026-09-22T19:40:41.551689Z)
- `IMBALNGC|TOTAL|imbalance` = **-8035** (n=363, 2026-09-22T19:21:54.940895Z)
- `INDDEM|TOTAL|demand` = **-12477** (n=363, 2026-09-22T19:21:54.940895Z)
- `INDGEN|TOTAL|generation` = **13138** (n=363, 2026-09-22T19:21:54.940895Z)
- `MELNGC|TOTAL|margin` = **37122** (n=363, 2026-09-22T19:19:32.717871Z)
- `MID|dataProvider=APXMIDP|price` = **200.57** (n=105, 2026-09-22T19:42:17.631824Z)
- `MID|dataProvider=APXMIDP|volume` = **4422.9** (n=105, 2026-09-22T19:42:17.631824Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=208, 2026-09-22T19:42:17.631824Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=208, 2026-09-22T19:42:17.631824Z)
- `NDF|TOTAL|demand` = **20673** (n=371, 2026-09-22T19:17:35.772457Z)
- `TSDF|TOTAL|demand` = **21173** (n=371, 2026-09-22T19:17:35.772457Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T19:42:17.631824Z` — **MID**: 2 rows; marker `2026-09-22T19:42:03Z`
- `2026-09-22T19:42:17.631824Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:41:45Z`
- `2026-09-22T19:40:41.551689Z` — **FUELINST**: 80 rows; marker `2026-09-22T19:40:00Z`
- `2026-09-22T19:40:26.188940Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:39:45Z`
- `2026-09-22T19:38:17.031408Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:37:45Z`
- `2026-09-22T19:37:29.543952Z` — **MID**: 1 rows; marker `2026-09-22T19:35:00Z`
- `2026-09-22T19:36:08.913406Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:35:45Z`
- `2026-09-22T19:35:37.397854Z` — **FUELINST**: 80 rows; marker `2026-09-22T19:35:00Z`
- `2026-09-22T19:34:21.031866Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:33:45Z`
- `2026-09-22T19:32:12.783806Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:31:45Z`
- `2026-09-22T19:30:53.095849Z` — **WINDFOR**: 73 rows; marker `2026-09-22T19:30:00Z`
- `2026-09-22T19:30:53.095849Z` — **FUELHH**: 20 rows; marker `2026-09-22T19:30:00Z`
- `2026-09-22T19:30:53.095849Z` — **FUELINST**: 80 rows; marker `2026-09-22T19:30:00Z`
- `2026-09-22T19:30:26.122301Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:29:45Z`
- `2026-09-22T19:28:17.965680Z` — **FREQ**: 5761 rows; marker `2026-09-22T19:27:45Z`
