# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T00:55:39.097918Z`  
Current process started UTC: `2026-09-23T00:51:38.743901Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2274, 2026-09-23T00:55:38.056293Z)
- `FUELINST|fuelType=OTHER|generation` = **192** (n=2274, 2026-09-23T00:55:38.056293Z)
- `FUELINST|fuelType=PS|generation` = **147** (n=2274, 2026-09-23T00:55:38.056293Z)
- `FUELINST|fuelType=WIND|generation` = **4392** (n=2274, 2026-09-23T00:55:38.056293Z)
- `IMBALNGC|TOTAL|imbalance` = **-7998** (n=374, 2026-09-23T00:50:38.640494Z)
- `INDDEM|TOTAL|demand` = **-12436** (n=374, 2026-09-23T00:50:38.640494Z)
- `INDGEN|TOTAL|generation` = **13175** (n=374, 2026-09-23T00:50:38.640494Z)
- `MELNGC|TOTAL|margin` = **37235** (n=374, 2026-09-23T00:49:02.646873Z)
- `MID|dataProvider=APXMIDP|price` = **143.69** (n=115, 2026-09-23T00:42:12.527096Z)
- `MID|dataProvider=APXMIDP|volume` = **2280.8** (n=115, 2026-09-23T00:42:12.527096Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=226, 2026-09-23T00:42:12.527096Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=226, 2026-09-23T00:42:12.527096Z)
- `NDF|TOTAL|demand` = **20673** (n=382, 2026-09-23T00:47:27.122061Z)
- `TSDF|TOTAL|demand` = **21173** (n=382, 2026-09-23T00:47:27.122061Z)
- `WINDFOR|TOTAL|generation` = **13770** (n=64, 2026-09-22T23:30:32.481751Z)

## Latest publication events

- `2026-09-23T00:55:38.056293Z` — **FUELINST**: 80 rows; marker `2026-09-23T00:55:00Z`
- `2026-09-23T00:54:18.527199Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:53:45Z`
- `2026-09-23T00:52:10.748425Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:51:45Z`
- `2026-09-23T00:50:38.640494Z` — **INDGEN**: 972 rows; marker `2026-09-23T00:47:00Z`
- `2026-09-23T00:50:38.640494Z` — **INDDEM**: 972 rows; marker `2026-09-23T00:47:00Z`
- `2026-09-23T00:50:38.640494Z` — **IMBALNGC**: 972 rows; marker `2026-09-23T00:47:00Z`
- `2026-09-23T00:50:38.640494Z` — **FUELINST**: 80 rows; marker `2026-09-23T00:50:00Z`
- `2026-09-23T00:50:23.078652Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:49:45Z`
- `2026-09-23T00:49:02.646873Z` — **MELNGC**: 972 rows; marker `2026-09-23T00:47:00Z`
- `2026-09-23T00:48:14.761960Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:47:45Z`
- `2026-09-23T00:47:27.122061Z` — **TSDF**: 972 rows; marker `2026-09-23T00:47:00Z`
- `2026-09-23T00:47:27.122061Z` — **NDF**: 54 rows; marker `2026-09-23T00:47:00Z`
- `2026-09-23T00:46:07.201692Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:45:45Z`
- `2026-09-23T00:45:35.049167Z` — **FUELINST**: 80 rows; marker `2026-09-23T00:45:00Z`
- `2026-09-23T00:44:14.756571Z` — **FREQ**: 5761 rows; marker `2026-09-23T00:43:45Z`
