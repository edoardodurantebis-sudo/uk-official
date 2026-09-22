# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T23:39:29.909077Z`  
Current process started UTC: `2026-09-22T23:35:29.973294Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2258, 2026-09-22T23:35:31.973529Z)
- `FUELINST|fuelType=OTHER|generation` = **307** (n=2258, 2026-09-22T23:35:31.973529Z)
- `FUELINST|fuelType=PS|generation` = **147** (n=2258, 2026-09-22T23:35:31.973529Z)
- `FUELINST|fuelType=WIND|generation` = **3182** (n=2258, 2026-09-22T23:35:31.973529Z)
- `IMBALNGC|TOTAL|imbalance` = **-8049** (n=371, 2026-09-22T23:20:54.957362Z)
- `INDDEM|TOTAL|demand` = **-12484** (n=371, 2026-09-22T23:20:38.644672Z)
- `INDGEN|TOTAL|generation` = **13124** (n=371, 2026-09-22T23:20:38.644672Z)
- `MELNGC|TOTAL|margin` = **37229** (n=371, 2026-09-22T23:19:02.295219Z)
- `MID|dataProvider=APXMIDP|price` = **152.39** (n=112, 2026-09-22T23:12:13.961447Z)
- `MID|dataProvider=APXMIDP|volume` = **2011.5** (n=112, 2026-09-22T23:12:13.961447Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=221, 2026-09-22T23:37:23.596123Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=221, 2026-09-22T23:37:23.596123Z)
- `NDF|TOTAL|demand` = **20673** (n=379, 2026-09-22T23:17:27.155171Z)
- `TSDF|TOTAL|demand` = **21173** (n=379, 2026-09-22T23:17:27.155171Z)
- `WINDFOR|TOTAL|generation` = **13770** (n=64, 2026-09-22T23:30:32.481751Z)

## Latest publication events

- `2026-09-22T23:38:11.011367Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:37:45Z`
- `2026-09-22T23:37:23.596123Z` — **MID**: 1 rows; marker `2026-09-22T23:35:00Z`
- `2026-09-22T23:36:03.439966Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:35:45Z`
- `2026-09-22T23:35:31.973529Z` — **FUELINST**: 80 rows; marker `2026-09-22T23:35:00Z`
- `2026-09-22T23:34:12.323097Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:33:45Z`
- `2026-09-22T23:32:04.240173Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:31:45Z`
- `2026-09-22T23:30:48.567107Z` — **FUELHH**: 20 rows; marker `2026-09-22T23:30:00Z`
- `2026-09-22T23:30:32.481751Z` — **WINDFOR**: 73 rows; marker `2026-09-22T23:30:00Z`
- `2026-09-22T23:30:32.481751Z` — **FUELINST**: 80 rows; marker `2026-09-22T23:30:00Z`
- `2026-09-22T23:29:59.966620Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:29:45Z`
- `2026-09-22T23:28:24.444733Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:27:45Z`
- `2026-09-22T23:26:21.926919Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:25:45Z`
- `2026-09-22T23:25:33.607775Z` — **FUELINST**: 80 rows; marker `2026-09-22T23:25:00Z`
- `2026-09-22T23:24:13.693826Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:23:45Z`
- `2026-09-22T23:22:14.352661Z` — **FREQ**: 5761 rows; marker `2026-09-22T23:21:45Z`
