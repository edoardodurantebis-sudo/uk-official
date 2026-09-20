# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T22:18:18.921505Z`  
Current process started UTC: `2026-09-20T22:14:17.738121Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1669, 2026-09-20T22:15:37.369331Z)
- `FUELINST|fuelType=OTHER|generation` = **223** (n=1669, 2026-09-20T22:15:37.369331Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1669, 2026-09-20T22:15:37.369331Z)
- `FUELINST|fuelType=WIND|generation` = **6347** (n=1669, 2026-09-20T22:15:37.369331Z)
- `IMBALNGC|TOTAL|imbalance` = **-5174** (n=274, 2026-09-20T21:51:36.257198Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=274, 2026-09-20T21:51:36.257198Z)
- `INDGEN|TOTAL|generation` = **15436** (n=274, 2026-09-20T21:51:36.257198Z)
- `MELNGC|TOTAL|margin` = **35706** (n=274, 2026-09-20T21:50:00.301077Z)
- `MID|dataProvider=APXMIDP|price` = **162.19** (n=14, 2026-09-20T22:12:19.543031Z)
- `MID|dataProvider=APXMIDP|volume` = **1643.2** (n=14, 2026-09-20T22:12:19.543031Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=28, 2026-09-20T22:12:19.543031Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=28, 2026-09-20T22:12:19.543031Z)
- `NDF|TOTAL|demand` = **20110** (n=281, 2026-09-20T22:17:29.159008Z)
- `TSDF|TOTAL|demand` = **20610** (n=281, 2026-09-20T22:17:29.159008Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T22:18:17.038682Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:17:45Z`
- `2026-09-20T22:17:29.159008Z` — **TSDF**: 1062 rows; marker `2026-09-20T22:17:00Z`
- `2026-09-20T22:17:29.159008Z` — **NDF**: 59 rows; marker `2026-09-20T22:17:00Z`
- `2026-09-20T22:16:25.422653Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:15:45Z`
- `2026-09-20T22:15:37.369331Z` — **FUELINST**: 80 rows; marker `2026-09-20T22:15:00Z`
- `2026-09-20T22:14:17.738128Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:13:45Z`
- `2026-09-20T22:12:19.543031Z` — **MID**: 2 rows; marker `2026-09-20T22:12:04Z`
- `2026-09-20T22:12:19.543031Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:11:45Z`
- `2026-09-20T22:10:27.490233Z` — **FUELINST**: 80 rows; marker `2026-09-20T22:10:00Z`
- `2026-09-20T22:10:12.086690Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:09:45Z`
- `2026-09-20T22:08:20.423214Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:07:45Z`
- `2026-09-20T22:06:28.409238Z` — **MID**: 1 rows; marker `2026-09-20T22:05:00Z`
- `2026-09-20T22:06:12.652366Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:05:45Z`
- `2026-09-20T22:05:33.091555Z` — **FUELINST**: 80 rows; marker `2026-09-20T22:05:00Z`
- `2026-09-20T22:04:12.325358Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:03:45Z`
