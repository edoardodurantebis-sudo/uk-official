# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T19:51:24.369720Z`  
Current process started UTC: `2026-09-20T19:47:24.559213Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2793, delta=365, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2736, delta=-158, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2894, delta=-83, z=3.94 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2977, delta=12, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2965, delta=268, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2697, delta=209, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2791, delta=35, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2756, delta=187, z=3.80 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=938, delta=-6, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=-1, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=947, delta=3, z=3.59 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=944, delta=66, z=3.69 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1640, 2026-09-20T19:50:38.996711Z)
- `FUELINST|fuelType=OTHER|generation` = **1526** (n=1640, 2026-09-20T19:50:38.996711Z)
- `FUELINST|fuelType=PS|generation` = **227** (n=1640, 2026-09-20T19:50:38.996711Z)
- `FUELINST|fuelType=WIND|generation` = **5732** (n=1640, 2026-09-20T19:50:38.996711Z)
- `IMBALNGC|TOTAL|imbalance` = **-5338** (n=269, 2026-09-20T19:22:11.796988Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=269, 2026-09-20T19:21:56.156895Z)
- `INDGEN|TOTAL|generation` = **15272** (n=269, 2026-09-20T19:21:40.377483Z)
- `MELNGC|TOTAL|margin` = **35546** (n=270, 2026-09-20T19:49:32.910930Z)
- `MID|dataProvider=APXMIDP|price` = **195.13** (n=9, 2026-09-20T19:42:10.464432Z)
- `MID|dataProvider=APXMIDP|volume` = **2761.6** (n=9, 2026-09-20T19:42:10.464432Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=18, 2026-09-20T19:42:10.464432Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=18, 2026-09-20T19:42:10.464432Z)
- `NDF|TOTAL|demand` = **20110** (n=276, 2026-09-20T19:47:40.694785Z)
- `TSDF|TOTAL|demand` = **20610** (n=276, 2026-09-20T19:47:40.694785Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T19:50:38.996711Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:50:00Z`
- `2026-09-20T19:50:22.760933Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:49:45Z`
- `2026-09-20T19:49:32.910930Z` — **MELNGC**: 1152 rows; marker `2026-09-20T19:47:00Z`
- `2026-09-20T19:48:12.838505Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:47:45Z`
- `2026-09-20T19:47:40.694785Z` — **TSDF**: 1152 rows; marker `2026-09-20T19:47:00Z`
- `2026-09-20T19:47:40.694785Z` — **NDF**: 64 rows; marker `2026-09-20T19:47:00Z`
- `2026-09-20T19:46:08.352336Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:45:45Z`
- `2026-09-20T19:45:36.700661Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:45:00Z`
- `2026-09-20T19:44:16.949948Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:43:45Z`
- `2026-09-20T19:42:26.501663Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:41:45Z`
- `2026-09-20T19:42:10.464432Z` — **MID**: 2 rows; marker `2026-09-20T19:42:02Z`
- `2026-09-20T19:40:34.348737Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:40:00Z`
- `2026-09-20T19:40:18.892393Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:39:45Z`
- `2026-09-20T19:38:59.254203Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:37:45Z`
- `2026-09-20T19:36:22.759785Z` — **MID**: 1 rows; marker `2026-09-20T19:35:00Z`
