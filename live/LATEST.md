# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T00:53:59.883557Z`  
Current process started UTC: `2026-09-21T00:50:00.066617Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1700, 2026-09-21T00:50:34.008572Z)
- `FUELINST|fuelType=OTHER|generation` = **94** (n=1700, 2026-09-21T00:50:34.008572Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1700, 2026-09-21T00:50:34.008572Z)
- `FUELINST|fuelType=WIND|generation` = **4975** (n=1700, 2026-09-21T00:50:34.008572Z)
- `IMBALNGC|TOTAL|imbalance` = **-4908** (n=280, 2026-09-21T00:50:34.008572Z)
- `INDDEM|TOTAL|demand` = **-11839** (n=280, 2026-09-21T00:50:34.008572Z)
- `INDGEN|TOTAL|generation` = **15702** (n=280, 2026-09-21T00:50:34.008572Z)
- `MELNGC|TOTAL|margin` = **35809** (n=280, 2026-09-21T00:49:13.970934Z)
- `MID|dataProvider=APXMIDP|price` = **143.68** (n=19, 2026-09-21T00:42:09.562065Z)
- `MID|dataProvider=APXMIDP|volume` = **1882.9** (n=19, 2026-09-21T00:42:09.562065Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=38, 2026-09-21T00:42:09.562065Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=38, 2026-09-21T00:42:09.562065Z)
- `NDF|TOTAL|demand` = **20110** (n=286, 2026-09-21T00:47:22.847115Z)
- `TSDF|TOTAL|demand` = **20610** (n=286, 2026-09-21T00:47:22.847115Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T00:52:09.896632Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:51:45Z`
- `2026-09-21T00:50:34.008572Z` — **INDGEN**: 972 rows; marker `2026-09-21T00:47:00Z`
- `2026-09-21T00:50:34.008572Z` — **INDDEM**: 972 rows; marker `2026-09-21T00:47:00Z`
- `2026-09-21T00:50:34.008572Z` — **IMBALNGC**: 972 rows; marker `2026-09-21T00:47:00Z`
- `2026-09-21T00:50:34.008572Z` — **FUELINST**: 80 rows; marker `2026-09-21T00:50:00Z`
- `2026-09-21T00:50:02.066857Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:49:45Z`
- `2026-09-21T00:49:13.970934Z` — **MELNGC**: 972 rows; marker `2026-09-21T00:47:00Z`
- `2026-09-21T00:48:26.702327Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:47:45Z`
- `2026-09-21T00:47:22.847115Z` — **TSDF**: 972 rows; marker `2026-09-21T00:47:00Z`
- `2026-09-21T00:47:22.847115Z` — **NDF**: 54 rows; marker `2026-09-21T00:47:00Z`
- `2026-09-21T00:46:03.941602Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:45:45Z`
- `2026-09-21T00:45:48.467963Z` — **FUELINST**: 80 rows; marker `2026-09-21T00:45:00Z`
- `2026-09-21T00:44:19.253353Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:43:45Z`
- `2026-09-21T00:42:25.564041Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:41:45Z`
- `2026-09-21T00:42:09.562065Z` — **MID**: 2 rows; marker `2026-09-21T00:42:04Z`
