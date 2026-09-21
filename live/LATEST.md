# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T19:42:26.246646Z`  
Current process started UTC: `2026-09-21T19:38:26.296331Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=149, delta=-12, z=3.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=161, delta=-8, z=4.02 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=185, delta=-45, z=4.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=169, delta=-2, z=4.27 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=171, delta=-17, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=188, delta=-2, z=4.87 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=190, delta=0, z=4.96 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=190, delta=-12, z=5.00 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=202, delta=-28, z=5.39 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=3738, delta=237, z=4.84 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=230, delta=-14, z=6.75 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3544, delta=-139, z=4.31 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.29 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3683, delta=-137, z=4.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=230, delta=0, z=6.36 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1923, 2026-09-21T19:40:34.758663Z)
- `FUELINST|fuelType=OTHER|generation` = **1877** (n=1923, 2026-09-21T19:40:34.758663Z)
- `FUELINST|fuelType=PS|generation` = **526** (n=1923, 2026-09-21T19:40:34.758663Z)
- `FUELINST|fuelType=WIND|generation` = **3647** (n=1923, 2026-09-21T19:40:34.758663Z)
- `IMBALNGC|TOTAL|imbalance` = **-2794** (n=316, 2026-09-21T19:22:19.743624Z)
- `INDDEM|TOTAL|demand` = **-12262** (n=316, 2026-09-21T19:22:03.647375Z)
- `INDGEN|TOTAL|generation` = **18665** (n=316, 2026-09-21T19:22:03.647375Z)
- `MELNGC|TOTAL|margin` = **36087** (n=316, 2026-09-21T19:19:39.632500Z)
- `MID|dataProvider=APXMIDP|price` = **193.44** (n=57, 2026-09-21T19:42:10.036286Z)
- `MID|dataProvider=APXMIDP|volume` = **3317.9** (n=57, 2026-09-21T19:42:10.036286Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=112, 2026-09-21T19:42:10.036286Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=112, 2026-09-21T19:42:10.036286Z)
- `NDF|TOTAL|demand` = **20959** (n=323, 2026-09-21T19:17:47.883666Z)
- `TSDF|TOTAL|demand` = **21459** (n=323, 2026-09-21T19:17:47.883666Z)
- `WINDFOR|TOTAL|generation` = **8621** (n=55, 2026-09-21T19:31:01.402061Z)

## Latest publication events

- `2026-09-21T19:42:10.036286Z` — **MID**: 2 rows; marker `2026-09-21T19:42:03Z`
- `2026-09-21T19:42:10.036286Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:41:45Z`
- `2026-09-21T19:40:34.758663Z` — **FUELINST**: 80 rows; marker `2026-09-21T19:40:00Z`
- `2026-09-21T19:40:18.275080Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:39:45Z`
- `2026-09-21T19:38:26.296343Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:37:45Z`
- `2026-09-21T19:37:22.649184Z` — **MID**: 1 rows; marker `2026-09-21T19:35:00Z`
- `2026-09-21T19:36:18.538497Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:35:45Z`
- `2026-09-21T19:35:30.954426Z` — **FUELINST**: 80 rows; marker `2026-09-21T19:35:00Z`
- `2026-09-21T19:34:26.145697Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:33:45Z`
- `2026-09-21T19:32:21.414992Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:31:45Z`
- `2026-09-21T19:31:01.402061Z` — **WINDFOR**: 73 rows; marker `2026-09-21T19:30:00Z`
- `2026-09-21T19:30:45.399650Z` — **FUELHH**: 20 rows; marker `2026-09-21T19:30:00Z`
- `2026-09-21T19:30:29.293629Z` — **FUELINST**: 80 rows; marker `2026-09-21T19:30:00Z`
- `2026-09-21T19:30:13.585831Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:29:45Z`
- `2026-09-21T19:28:06.145601Z` — **FREQ**: 5761 rows; marker `2026-09-21T19:27:45Z`
