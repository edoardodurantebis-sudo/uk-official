# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T00:45:37.238018Z`  
Current process started UTC: `2026-09-21T00:41:37.558158Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=994, delta=146, z=3.51 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1698, 2026-09-21T00:40:39.994265Z)
- `FUELINST|fuelType=OTHER|generation` = **99** (n=1698, 2026-09-21T00:40:39.994265Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1698, 2026-09-21T00:40:39.994265Z)
- `FUELINST|fuelType=WIND|generation` = **4987** (n=1698, 2026-09-21T00:40:39.994265Z)
- `IMBALNGC|TOTAL|imbalance` = **-4890** (n=279, 2026-09-21T00:20:52.151209Z)
- `INDDEM|TOTAL|demand` = **-11840** (n=279, 2026-09-21T00:20:52.151209Z)
- `INDGEN|TOTAL|generation` = **15720** (n=279, 2026-09-21T00:20:52.151209Z)
- `MELNGC|TOTAL|margin` = **35784** (n=279, 2026-09-21T00:19:06.302567Z)
- `MID|dataProvider=APXMIDP|price` = **143.68** (n=19, 2026-09-21T00:42:09.562065Z)
- `MID|dataProvider=APXMIDP|volume` = **1882.9** (n=19, 2026-09-21T00:42:09.562065Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=38, 2026-09-21T00:42:09.562065Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=38, 2026-09-21T00:42:09.562065Z)
- `NDF|TOTAL|demand` = **20110** (n=285, 2026-09-21T00:17:29.179731Z)
- `TSDF|TOTAL|demand` = **20610** (n=285, 2026-09-21T00:17:29.179731Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T00:44:19.253353Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:43:45Z`
- `2026-09-21T00:42:25.564041Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:41:45Z`
- `2026-09-21T00:42:09.562065Z` — **MID**: 2 rows; marker `2026-09-21T00:42:04Z`
- `2026-09-21T00:40:39.994265Z` — **FUELINST**: 80 rows; marker `2026-09-21T00:40:00Z`
- `2026-09-21T00:40:23.966549Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:39:45Z`
- `2026-09-21T00:38:15.506548Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:37:45Z`
- `2026-09-21T00:36:24.590081Z` — **MID**: 1 rows; marker `2026-09-21T00:35:00Z`
- `2026-09-21T00:36:24.590081Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:35:45Z`
- `2026-09-21T00:35:36.563917Z` — **FUELINST**: 80 rows; marker `2026-09-21T00:35:00Z`
- `2026-09-21T00:34:17.065168Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:33:45Z`
- `2026-09-21T00:32:15.746502Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:31:45Z`
- `2026-09-21T00:30:52.373505Z` — **FUELHH**: 20 rows; marker `2026-09-21T00:30:00Z`
- `2026-09-21T00:30:36.087406Z` — **FUELINST**: 80 rows; marker `2026-09-21T00:30:00Z`
- `2026-09-21T00:30:20.320084Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:29:45Z`
- `2026-09-21T00:28:15.913142Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:27:45Z`
