# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T07:40:56.432985Z`  
Current process started UTC: `2026-09-23T07:36:56.601678Z`  
1-second metadata polls in this process: **236**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2355, 2026-09-23T07:40:26.222350Z)
- `FUELINST|fuelType=OTHER|generation` = **762** (n=2355, 2026-09-23T07:40:26.222350Z)
- `FUELINST|fuelType=PS|generation` = **-18** (n=2355, 2026-09-23T07:40:26.222350Z)
- `FUELINST|fuelType=WIND|generation` = **10247** (n=2355, 2026-09-23T07:40:26.222350Z)
- `IMBALNGC|TOTAL|imbalance` = **-7454** (n=387, 2026-09-23T07:20:50.693900Z)
- `INDDEM|TOTAL|demand` = **-12650** (n=387, 2026-09-23T07:20:50.693900Z)
- `INDGEN|TOTAL|generation` = **13965** (n=387, 2026-09-23T07:20:50.693900Z)
- `MELNGC|TOTAL|margin` = **38775** (n=387, 2026-09-23T07:19:31.866782Z)
- `MID|dataProvider=APXMIDP|price` = **146.49** (n=128, 2026-09-23T07:12:21.657766Z)
- `MID|dataProvider=APXMIDP|volume` = **3534.8** (n=128, 2026-09-23T07:12:21.657766Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=253, 2026-09-23T07:36:28.257530Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=253, 2026-09-23T07:36:28.257530Z)
- `NDF|TOTAL|demand` = **20673** (n=395, 2026-09-23T07:17:39.850538Z)
- `TSDF|TOTAL|demand` = **21419** (n=395, 2026-09-23T07:17:39.850538Z)
- `WINDFOR|TOTAL|generation` = **7305** (n=66, 2026-09-23T05:30:43.471788Z)

## Latest publication events

- `2026-09-23T07:40:26.222350Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:40:00Z`
- `2026-09-23T07:40:26.222350Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:39:45Z`
- `2026-09-23T07:38:16.730861Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:37:45Z`
- `2026-09-23T07:36:28.257530Z` — **MID**: 1 rows; marker `2026-09-23T07:35:00Z`
- `2026-09-23T07:36:12.246081Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:35:45Z`
- `2026-09-23T07:35:39.890402Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:35:00Z`
- `2026-09-23T07:34:19.828512Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:33:45Z`
- `2026-09-23T07:32:16.552849Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:31:45Z`
- `2026-09-23T07:30:40.292287Z` — **FUELHH**: 20 rows; marker `2026-09-23T07:30:00Z`
- `2026-09-23T07:30:40.292287Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:30:00Z`
- `2026-09-23T07:30:23.559979Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:29:45Z`
- `2026-09-23T07:28:14.735503Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:27:45Z`
- `2026-09-23T07:26:07.140711Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:25:45Z`
- `2026-09-23T07:25:35.114661Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:25:00Z`
- `2026-09-23T07:24:15.439395Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:23:45Z`
