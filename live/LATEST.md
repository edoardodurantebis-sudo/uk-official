# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T22:06:53.545142Z`  
Current process started UTC: `2026-09-22T22:02:53.547845Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2240, 2026-09-22T22:05:34.509671Z)
- `FUELINST|fuelType=OTHER|generation` = **290** (n=2240, 2026-09-22T22:05:34.509671Z)
- `FUELINST|fuelType=PS|generation` = **143** (n=2240, 2026-09-22T22:05:34.509671Z)
- `FUELINST|fuelType=WIND|generation` = **2500** (n=2240, 2026-09-22T22:05:34.509671Z)
- `IMBALNGC|TOTAL|imbalance` = **-8054** (n=368, 2026-09-22T21:51:18.504304Z)
- `INDDEM|TOTAL|demand` = **-12478** (n=368, 2026-09-22T21:51:02.571012Z)
- `INDGEN|TOTAL|generation` = **13119** (n=368, 2026-09-22T21:51:02.571012Z)
- `MELNGC|TOTAL|margin` = **37209** (n=368, 2026-09-22T21:49:10.751401Z)
- `MID|dataProvider=APXMIDP|price` = **156.24** (n=109, 2026-09-22T21:42:17.013922Z)
- `MID|dataProvider=APXMIDP|volume` = **3594.5** (n=109, 2026-09-22T21:42:17.013922Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=217, 2026-09-22T22:06:38.221673Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=217, 2026-09-22T22:06:38.221673Z)
- `NDF|TOTAL|demand` = **20673** (n=376, 2026-09-22T21:47:51.071149Z)
- `TSDF|TOTAL|demand` = **21173** (n=376, 2026-09-22T21:47:51.071149Z)
- `WINDFOR|TOTAL|generation` = **13612** (n=63, 2026-09-22T19:30:53.095849Z)

## Latest publication events

- `2026-09-22T22:06:38.221673Z` — **MID**: 1 rows; marker `2026-09-22T22:05:00Z`
- `2026-09-22T22:06:22.696839Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:05:45Z`
- `2026-09-22T22:05:34.509671Z` — **FUELINST**: 80 rows; marker `2026-09-22T22:05:00Z`
- `2026-09-22T22:04:13.868953Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:03:45Z`
- `2026-09-22T22:02:12.271833Z` — **FREQ**: 5761 rows; marker `2026-09-22T22:01:45Z`
- `2026-09-22T22:00:35.182532Z` — **FUELHH**: 20 rows; marker `2026-09-22T22:00:00Z`
- `2026-09-22T22:00:35.182532Z` — **FUELINST**: 80 rows; marker `2026-09-22T22:00:00Z`
- `2026-09-22T22:00:18.360532Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:59:45Z`
- `2026-09-22T21:58:13.107558Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:57:45Z`
- `2026-09-22T21:56:20.922354Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:55:45Z`
- `2026-09-22T21:55:33.248655Z` — **FUELINST**: 80 rows; marker `2026-09-22T21:55:00Z`
- `2026-09-22T21:54:28.431220Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:53:45Z`
- `2026-09-22T21:52:06.700071Z` — **FREQ**: 5761 rows; marker `2026-09-22T21:51:45Z`
- `2026-09-22T21:51:18.504304Z` — **IMBALNGC**: 1080 rows; marker `2026-09-22T21:47:00Z`
- `2026-09-22T21:51:02.571012Z` — **INDGEN**: 1080 rows; marker `2026-09-22T21:47:00Z`
