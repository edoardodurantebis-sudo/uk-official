# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T20:03:58.982372Z`  
Current process started UTC: `2026-09-20T19:59:59.086776Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1642, 2026-09-20T20:00:35.231371Z)
- `FUELINST|fuelType=OTHER|generation` = **1306** (n=1642, 2026-09-20T20:00:35.231371Z)
- `FUELINST|fuelType=PS|generation` = **227** (n=1642, 2026-09-20T20:00:35.231371Z)
- `FUELINST|fuelType=WIND|generation` = **5707** (n=1642, 2026-09-20T20:00:35.231371Z)
- `IMBALNGC|TOTAL|imbalance` = **-5337** (n=270, 2026-09-20T19:51:37.785496Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=270, 2026-09-20T19:51:37.785496Z)
- `INDGEN|TOTAL|generation` = **15273** (n=270, 2026-09-20T19:51:37.785496Z)
- `MELNGC|TOTAL|margin` = **35546** (n=270, 2026-09-20T19:49:32.910930Z)
- `MID|dataProvider=APXMIDP|price` = **195.13** (n=9, 2026-09-20T19:42:10.464432Z)
- `MID|dataProvider=APXMIDP|volume` = **2761.6** (n=9, 2026-09-20T19:42:10.464432Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=18, 2026-09-20T19:42:10.464432Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=18, 2026-09-20T19:42:10.464432Z)
- `NDF|TOTAL|demand` = **20110** (n=276, 2026-09-20T19:47:40.694785Z)
- `TSDF|TOTAL|demand` = **20610** (n=276, 2026-09-20T19:47:40.694785Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T20:02:26.869989Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:01:45Z`
- `2026-09-20T20:00:35.231371Z` — **FUELHH**: 20 rows; marker `2026-09-20T20:00:00Z`
- `2026-09-20T20:00:35.231371Z` — **FUELINST**: 80 rows; marker `2026-09-20T20:00:00Z`
- `2026-09-20T20:00:19.745651Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:59:45Z`
- `2026-09-20T19:58:12.253843Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:57:45Z`
- `2026-09-20T19:56:04.667193Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:55:45Z`
- `2026-09-20T19:55:48.588898Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:55:00Z`
- `2026-09-20T19:54:17.863123Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:53:45Z`
- `2026-09-20T19:52:25.439749Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:51:45Z`
- `2026-09-20T19:51:37.785496Z` — **INDGEN**: 1152 rows; marker `2026-09-20T19:47:00Z`
- `2026-09-20T19:51:37.785496Z` — **INDDEM**: 1152 rows; marker `2026-09-20T19:47:00Z`
- `2026-09-20T19:51:37.785496Z` — **IMBALNGC**: 1152 rows; marker `2026-09-20T19:47:00Z`
- `2026-09-20T19:50:38.996711Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:50:00Z`
- `2026-09-20T19:50:22.760933Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:49:45Z`
- `2026-09-20T19:49:32.910930Z` — **MELNGC**: 1152 rows; marker `2026-09-20T19:47:00Z`
