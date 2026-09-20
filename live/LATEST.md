# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T19:04:00.851644Z`  
Current process started UTC: `2026-09-20T19:00:00.669016Z`  
1-second metadata polls in this process: **234**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1630, 2026-09-20T19:00:33.585618Z)
- `FUELINST|fuelType=OTHER|generation` = **2736** (n=1630, 2026-09-20T19:00:33.585618Z)
- `FUELINST|fuelType=PS|generation` = **223** (n=1630, 2026-09-20T19:00:33.585618Z)
- `FUELINST|fuelType=WIND|generation` = **5428** (n=1630, 2026-09-20T19:00:33.585618Z)
- `IMBALNGC|TOTAL|imbalance` = **-5141** (n=268, 2026-09-20T18:52:58.646959Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=268, 2026-09-20T18:52:58.646959Z)
- `INDGEN|TOTAL|generation` = **15469** (n=268, 2026-09-20T18:52:58.646959Z)
- `MELNGC|TOTAL|margin` = **35401** (n=268, 2026-09-20T18:50:08.994493Z)
- `MID|dataProvider=APXMIDP|price` = **195.65** (n=7, 2026-09-20T18:42:19.980396Z)
- `MID|dataProvider=APXMIDP|volume` = **2599.7** (n=7, 2026-09-20T18:42:19.980396Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=14, 2026-09-20T18:42:19.980396Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=14, 2026-09-20T18:42:19.980396Z)
- `NDF|TOTAL|demand` = **20110** (n=274, 2026-09-20T18:48:01.508794Z)
- `TSDF|TOTAL|demand` = **20610** (n=274, 2026-09-20T18:48:17.659387Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T19:02:13.952874Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:01:45Z`
- `2026-09-20T19:00:49.617468Z` — **FUELHH**: 20 rows; marker `2026-09-20T19:00:00Z`
- `2026-09-20T19:00:33.585618Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:00:00Z`
- `2026-09-20T19:00:17.956866Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:59:45Z`
- `2026-09-20T18:58:17.628433Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:57:45Z`
- `2026-09-20T18:56:09.572492Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:55:45Z`
- `2026-09-20T18:55:21.986431Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:55:00Z`
- `2026-09-20T18:54:02.407140Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:53:45Z`
- `2026-09-20T18:52:58.646959Z` — **INDGEN**: 1188 rows; marker `2026-09-20T18:47:00Z`
- `2026-09-20T18:52:58.646959Z` — **INDDEM**: 1188 rows; marker `2026-09-20T18:47:00Z`
- `2026-09-20T18:52:58.646959Z` — **IMBALNGC**: 1188 rows; marker `2026-09-20T18:47:00Z`
- `2026-09-20T18:52:11.091813Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:51:45Z`
- `2026-09-20T18:50:41.308026Z` — **FUELINST**: 80 rows; marker `2026-09-20T18:50:00Z`
- `2026-09-20T18:50:25.476734Z` — **FREQ**: 5761 rows; marker `2026-09-20T18:49:45Z`
- `2026-09-20T18:50:08.994493Z` — **MELNGC**: 1188 rows; marker `2026-09-20T18:47:00Z`
