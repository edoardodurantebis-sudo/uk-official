# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T04:16:58.336361Z`  
Current process started UTC: `2026-09-21T04:12:58.147416Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1741, 2026-09-21T04:15:24.739505Z)
- `FUELINST|fuelType=OTHER|generation` = **325** (n=1741, 2026-09-21T04:15:24.739505Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1741, 2026-09-21T04:15:24.739505Z)
- `FUELINST|fuelType=WIND|generation` = **4055** (n=1741, 2026-09-21T04:15:24.739505Z)
- `IMBALNGC|TOTAL|imbalance` = **-4043** (n=286, 2026-09-21T03:50:23.681881Z)
- `INDDEM|TOTAL|demand` = **-11760** (n=286, 2026-09-21T03:50:07.852391Z)
- `INDGEN|TOTAL|generation` = **16567** (n=286, 2026-09-21T03:50:07.852391Z)
- `MELNGC|TOTAL|margin` = **37551** (n=286, 2026-09-21T03:48:47.430896Z)
- `MID|dataProvider=APXMIDP|price` = **151.5** (n=26, 2026-09-21T04:12:12.897424Z)
- `MID|dataProvider=APXMIDP|volume` = **2228** (n=26, 2026-09-21T04:12:12.897424Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=52, 2026-09-21T04:12:12.897424Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=52, 2026-09-21T04:12:12.897424Z)
- `NDF|TOTAL|demand` = **20110** (n=292, 2026-09-21T03:47:42.721422Z)
- `TSDF|TOTAL|demand` = **20610** (n=292, 2026-09-21T03:47:42.721422Z)
- `WINDFOR|TOTAL|generation` = **8021** (n=49, 2026-09-21T03:30:39.847119Z)

## Latest publication events

- `2026-09-21T04:16:12.458267Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:15:45Z`
- `2026-09-21T04:15:24.739505Z` — **FUELINST**: 80 rows; marker `2026-09-21T04:15:00Z`
- `2026-09-21T04:14:20.220052Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:13:45Z`
- `2026-09-21T04:12:12.897424Z` — **MID**: 2 rows; marker `2026-09-21T04:12:03Z`
- `2026-09-21T04:12:12.897424Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:11:45Z`
- `2026-09-21T04:10:20.572442Z` — **FUELINST**: 80 rows; marker `2026-09-21T04:10:00Z`
- `2026-09-21T04:10:04.679254Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:09:45Z`
- `2026-09-21T04:08:03.079390Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:07:45Z`
- `2026-09-21T04:07:45.900003Z` — **MID**: 1 rows; marker `2026-09-21T04:05:00Z`
- `2026-09-21T04:06:09.891698Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:05:45Z`
- `2026-09-21T04:05:21.670868Z` — **FUELINST**: 80 rows; marker `2026-09-21T04:05:00Z`
- `2026-09-21T04:04:09.411013Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:03:45Z`
- `2026-09-21T04:02:01.983579Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:01:45Z`
- `2026-09-21T04:00:41.233979Z` — **FUELHH**: 20 rows; marker `2026-09-21T04:00:00Z`
- `2026-09-21T04:00:41.233979Z` — **FUELINST**: 80 rows; marker `2026-09-21T04:00:00Z`
