# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T19:21:25.040539Z`  
Current process started UTC: `2026-09-20T19:17:24.647556Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1634, 2026-09-20T19:20:35.493142Z)
- `FUELINST|fuelType=OTHER|generation` = **1843** (n=1634, 2026-09-20T19:20:35.493142Z)
- `FUELINST|fuelType=PS|generation` = **228** (n=1634, 2026-09-20T19:20:35.493142Z)
- `FUELINST|fuelType=WIND|generation` = **5668** (n=1634, 2026-09-20T19:20:35.493142Z)
- `IMBALNGC|TOTAL|imbalance` = **-5141** (n=268, 2026-09-20T18:52:58.646959Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=268, 2026-09-20T18:52:58.646959Z)
- `INDGEN|TOTAL|generation` = **15469** (n=268, 2026-09-20T18:52:58.646959Z)
- `MELNGC|TOTAL|margin` = **35583** (n=269, 2026-09-20T19:20:03.973467Z)
- `MID|dataProvider=APXMIDP|price` = **196.91** (n=8, 2026-09-20T19:12:09.434470Z)
- `MID|dataProvider=APXMIDP|volume` = **2752.7** (n=8, 2026-09-20T19:12:09.434470Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=16, 2026-09-20T19:12:09.434470Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=16, 2026-09-20T19:12:09.434470Z)
- `NDF|TOTAL|demand` = **20110** (n=275, 2026-09-20T19:17:56.651564Z)
- `TSDF|TOTAL|demand` = **20610** (n=275, 2026-09-20T19:17:56.651564Z)
- `WINDFOR|TOTAL|generation` = **2115** (n=46, 2026-09-20T16:30:40.211698Z)

## Latest publication events

- `2026-09-20T19:20:35.493142Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:20:00Z`
- `2026-09-20T19:20:20.157578Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:19:45Z`
- `2026-09-20T19:20:03.973467Z` — **MELNGC**: 1170 rows; marker `2026-09-20T19:17:00Z`
- `2026-09-20T19:18:12.374890Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:17:45Z`
- `2026-09-20T19:17:56.651564Z` — **TSDF**: 1170 rows; marker `2026-09-20T19:17:00Z`
- `2026-09-20T19:17:56.651564Z` — **NDF**: 65 rows; marker `2026-09-20T19:17:00Z`
- `2026-09-20T19:16:24.687600Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:15:45Z`
- `2026-09-20T19:15:36.602462Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:15:00Z`
- `2026-09-20T19:14:16.727091Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:13:45Z`
- `2026-09-20T19:12:25.032309Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:11:45Z`
- `2026-09-20T19:12:09.434470Z` — **MID**: 2 rows; marker `2026-09-20T19:12:03Z`
- `2026-09-20T19:10:33.157995Z` — **FUELINST**: 80 rows; marker `2026-09-20T19:10:00Z`
- `2026-09-20T19:10:17.309131Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:09:45Z`
- `2026-09-20T19:08:25.303571Z` — **FREQ**: 5761 rows; marker `2026-09-20T19:07:45Z`
- `2026-09-20T19:06:21.458461Z` — **MID**: 1 rows; marker `2026-09-20T19:05:00Z`
