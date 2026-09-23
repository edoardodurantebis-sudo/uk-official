# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-23T07:32:30.265591Z`  
Current process started UTC: `2026-09-23T07:28:29.929173Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2353, 2026-09-23T07:30:40.292287Z)
- `FUELINST|fuelType=OTHER|generation` = **685** (n=2353, 2026-09-23T07:30:40.292287Z)
- `FUELINST|fuelType=PS|generation` = **-17** (n=2353, 2026-09-23T07:30:40.292287Z)
- `FUELINST|fuelType=WIND|generation` = **10411** (n=2353, 2026-09-23T07:30:40.292287Z)
- `IMBALNGC|TOTAL|imbalance` = **-7454** (n=387, 2026-09-23T07:20:50.693900Z)
- `INDDEM|TOTAL|demand` = **-12650** (n=387, 2026-09-23T07:20:50.693900Z)
- `INDGEN|TOTAL|generation` = **13965** (n=387, 2026-09-23T07:20:50.693900Z)
- `MELNGC|TOTAL|margin` = **38775** (n=387, 2026-09-23T07:19:31.866782Z)
- `MID|dataProvider=APXMIDP|price` = **146.49** (n=128, 2026-09-23T07:12:21.657766Z)
- `MID|dataProvider=APXMIDP|volume` = **3534.8** (n=128, 2026-09-23T07:12:21.657766Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=252, 2026-09-23T07:12:21.657766Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=252, 2026-09-23T07:12:21.657766Z)
- `NDF|TOTAL|demand` = **20673** (n=395, 2026-09-23T07:17:39.850538Z)
- `TSDF|TOTAL|demand` = **21419** (n=395, 2026-09-23T07:17:39.850538Z)
- `WINDFOR|TOTAL|generation` = **7305** (n=66, 2026-09-23T05:30:43.471788Z)

## Latest publication events

- `2026-09-23T07:32:16.552849Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:31:45Z`
- `2026-09-23T07:30:40.292287Z` — **FUELHH**: 20 rows; marker `2026-09-23T07:30:00Z`
- `2026-09-23T07:30:40.292287Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:30:00Z`
- `2026-09-23T07:30:23.559979Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:29:45Z`
- `2026-09-23T07:28:14.735503Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:27:45Z`
- `2026-09-23T07:26:07.140711Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:25:45Z`
- `2026-09-23T07:25:35.114661Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:25:00Z`
- `2026-09-23T07:24:15.439395Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:23:45Z`
- `2026-09-23T07:22:10.437491Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:21:45Z`
- `2026-09-23T07:20:50.693900Z` — **INDGEN**: 738 rows; marker `2026-09-23T07:17:00Z`
- `2026-09-23T07:20:50.693900Z` — **INDDEM**: 738 rows; marker `2026-09-23T07:17:00Z`
- `2026-09-23T07:20:50.693900Z` — **IMBALNGC**: 738 rows; marker `2026-09-23T07:17:00Z`
- `2026-09-23T07:20:35.163440Z` — **FUELINST**: 80 rows; marker `2026-09-23T07:20:00Z`
- `2026-09-23T07:20:18.864344Z` — **FREQ**: 5761 rows; marker `2026-09-23T07:19:45Z`
- `2026-09-23T07:19:31.866782Z` — **MELNGC**: 738 rows; marker `2026-09-23T07:17:00Z`
