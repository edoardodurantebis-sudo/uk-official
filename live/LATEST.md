# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T00:16:11.517560Z`  
Current process started UTC: `2026-09-21T00:12:09.501492Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1693, 2026-09-21T00:15:21.515246Z)
- `FUELINST|fuelType=OTHER|generation` = **87** (n=1693, 2026-09-21T00:15:21.515246Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1693, 2026-09-21T00:15:21.515246Z)
- `FUELINST|fuelType=WIND|generation` = **5089** (n=1693, 2026-09-21T00:15:21.515246Z)
- `IMBALNGC|TOTAL|imbalance` = **-5229** (n=278, 2026-09-20T23:51:16.921635Z)
- `INDDEM|TOTAL|demand` = **-11840** (n=278, 2026-09-20T23:51:01.647164Z)
- `INDGEN|TOTAL|generation` = **15381** (n=278, 2026-09-20T23:51:01.647164Z)
- `MELNGC|TOTAL|margin` = **35822** (n=278, 2026-09-20T23:49:33.095120Z)
- `MID|dataProvider=APXMIDP|price` = **138.2** (n=18, 2026-09-21T00:12:09.501502Z)
- `MID|dataProvider=APXMIDP|volume` = **1990.5** (n=18, 2026-09-21T00:12:09.501502Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=36, 2026-09-21T00:12:09.501502Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=36, 2026-09-21T00:12:09.501502Z)
- `NDF|TOTAL|demand` = **20110** (n=284, 2026-09-20T23:47:25.276035Z)
- `TSDF|TOTAL|demand` = **20610** (n=284, 2026-09-20T23:47:25.276035Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T00:16:08.964776Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:15:45Z`
- `2026-09-21T00:15:21.515246Z` — **FUELINST**: 80 rows; marker `2026-09-21T00:15:00Z`
- `2026-09-21T00:14:17.269799Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:13:45Z`
- `2026-09-21T00:12:09.501502Z` — **MID**: 2 rows; marker `2026-09-21T00:12:03Z`
- `2026-09-21T00:12:09.501502Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:11:45Z`
- `2026-09-21T00:10:33.389464Z` — **FUELINST**: 80 rows; marker `2026-09-21T00:10:00Z`
- `2026-09-21T00:10:17.613134Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:09:45Z`
- `2026-09-21T00:08:57.401657Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:07:45Z`
- `2026-09-21T00:06:38.109137Z` — **MID**: 1 rows; marker `2026-09-21T00:05:00Z`
- `2026-09-21T00:06:21.971558Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:05:45Z`
- `2026-09-21T00:05:34.442114Z` — **FUELINST**: 80 rows; marker `2026-09-21T00:05:00Z`
- `2026-09-21T00:04:13.835327Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:03:45Z`
- `2026-09-21T00:02:22.220287Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:01:45Z`
- `2026-09-21T00:00:30.281144Z` — **FUELHH**: 20 rows; marker `2026-09-21T00:00:00Z`
- `2026-09-21T00:00:30.281144Z` — **FUELINST**: 80 rows; marker `2026-09-21T00:00:00Z`
