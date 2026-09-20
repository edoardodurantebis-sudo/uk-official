# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T22:47:41.351855Z`  
Current process started UTC: `2026-09-20T22:43:41.075845Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1675, 2026-09-20T22:45:33.209334Z)
- `FUELINST|fuelType=OTHER|generation` = **146** (n=1675, 2026-09-20T22:45:33.209334Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1675, 2026-09-20T22:45:33.209334Z)
- `FUELINST|fuelType=WIND|generation` = **6177** (n=1675, 2026-09-20T22:45:33.209334Z)
- `IMBALNGC|TOTAL|imbalance` = **-5194** (n=275, 2026-09-20T22:21:29.287977Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=275, 2026-09-20T22:21:13.652319Z)
- `INDGEN|TOTAL|generation` = **15416** (n=275, 2026-09-20T22:21:13.652319Z)
- `MELNGC|TOTAL|margin` = **35776** (n=275, 2026-09-20T22:19:37.453400Z)
- `MID|dataProvider=APXMIDP|price` = **151.09** (n=15, 2026-09-20T22:42:14.615124Z)
- `MID|dataProvider=APXMIDP|volume` = **1740.6** (n=15, 2026-09-20T22:42:14.615124Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=30, 2026-09-20T22:42:14.615124Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=30, 2026-09-20T22:42:14.615124Z)
- `NDF|TOTAL|demand` = **20110** (n=282, 2026-09-20T22:47:25.895666Z)
- `TSDF|TOTAL|demand` = **20610** (n=282, 2026-09-20T22:47:25.895666Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T22:47:25.895666Z` — **TSDF**: 1044 rows; marker `2026-09-20T22:47:00Z`
- `2026-09-20T22:47:25.895666Z` — **NDF**: 58 rows; marker `2026-09-20T22:47:00Z`
- `2026-09-20T22:46:05.443573Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:45:45Z`
- `2026-09-20T22:45:33.209334Z` — **FUELINST**: 80 rows; marker `2026-09-20T22:45:00Z`
- `2026-09-20T22:44:13.079361Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:43:45Z`
- `2026-09-20T22:42:14.615124Z` — **MID**: 2 rows; marker `2026-09-20T22:42:03Z`
- `2026-09-20T22:42:14.615124Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:41:45Z`
- `2026-09-20T22:40:22.460946Z` — **FUELINST**: 80 rows; marker `2026-09-20T22:40:00Z`
- `2026-09-20T22:40:06.610365Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:39:45Z`
- `2026-09-20T22:38:15.865622Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:37:45Z`
- `2026-09-20T22:36:39.128498Z` — **MID**: 1 rows; marker `2026-09-20T22:35:00Z`
- `2026-09-20T22:36:23.634172Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:35:45Z`
- `2026-09-20T22:35:35.554888Z` — **FUELINST**: 80 rows; marker `2026-09-20T22:35:00Z`
- `2026-09-20T22:34:22.511406Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:33:45Z`
- `2026-09-20T22:32:30.499214Z` — **FREQ**: 5761 rows; marker `2026-09-20T22:31:45Z`
