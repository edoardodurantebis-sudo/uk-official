# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T23:17:15.305615Z`  
Current process started UTC: `2026-09-20T23:13:14.989830Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1681, 2026-09-20T23:15:43.150045Z)
- `FUELINST|fuelType=OTHER|generation` = **393** (n=1681, 2026-09-20T23:15:43.150045Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1681, 2026-09-20T23:15:43.150045Z)
- `FUELINST|fuelType=WIND|generation` = **5796** (n=1681, 2026-09-20T23:15:43.150045Z)
- `IMBALNGC|TOTAL|imbalance` = **-5220** (n=276, 2026-09-20T22:51:06.081867Z)
- `INDDEM|TOTAL|demand` = **-11829** (n=276, 2026-09-20T22:51:06.081867Z)
- `INDGEN|TOTAL|generation` = **15390** (n=276, 2026-09-20T22:51:06.081867Z)
- `MELNGC|TOTAL|margin` = **35759** (n=276, 2026-09-20T22:49:14.589741Z)
- `MID|dataProvider=APXMIDP|price` = **157.3** (n=16, 2026-09-20T23:12:15.981992Z)
- `MID|dataProvider=APXMIDP|volume` = **2248.8** (n=16, 2026-09-20T23:12:15.981992Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=32, 2026-09-20T23:12:15.981992Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=32, 2026-09-20T23:12:15.981992Z)
- `NDF|TOTAL|demand` = **20110** (n=282, 2026-09-20T22:47:25.895666Z)
- `TSDF|TOTAL|demand` = **20610** (n=282, 2026-09-20T22:47:25.895666Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T23:16:13.295650Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:15:45Z`
- `2026-09-20T23:15:43.150045Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:15:00Z`
- `2026-09-20T23:14:22.998394Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:13:45Z`
- `2026-09-20T23:12:15.981992Z` — **MID**: 2 rows; marker `2026-09-20T23:12:03Z`
- `2026-09-20T23:12:15.981992Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:11:45Z`
- `2026-09-20T23:10:55.743334Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:10:00Z`
- `2026-09-20T23:10:23.898465Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:09:45Z`
- `2026-09-20T23:08:16.227391Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:07:45Z`
- `2026-09-20T23:06:40.186510Z` — **MID**: 1 rows; marker `2026-09-20T23:05:00Z`
- `2026-09-20T23:06:24.318087Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:05:45Z`
- `2026-09-20T23:05:36.249404Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:05:00Z`
- `2026-09-20T23:04:21.843577Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:03:45Z`
- `2026-09-20T23:02:12.754814Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:01:45Z`
- `2026-09-20T23:00:37.067914Z` — **FUELHH**: 20 rows; marker `2026-09-20T23:00:00Z`
- `2026-09-20T23:00:37.067914Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:00:00Z`
