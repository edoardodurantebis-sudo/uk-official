# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T23:50:50.494324Z`  
Current process started UTC: `2026-09-20T23:46:50.272452Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1688, 2026-09-20T23:50:36.707306Z)
- `FUELINST|fuelType=OTHER|generation` = **220** (n=1688, 2026-09-20T23:50:36.707306Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1688, 2026-09-20T23:50:36.707306Z)
- `FUELINST|fuelType=WIND|generation` = **5306** (n=1688, 2026-09-20T23:50:36.707306Z)
- `IMBALNGC|TOTAL|imbalance` = **-5221** (n=277, 2026-09-20T23:21:41.704783Z)
- `INDDEM|TOTAL|demand` = **-11829** (n=277, 2026-09-20T23:21:26.169619Z)
- `INDGEN|TOTAL|generation` = **15389** (n=277, 2026-09-20T23:21:26.169619Z)
- `MELNGC|TOTAL|margin` = **35822** (n=278, 2026-09-20T23:49:33.095120Z)
- `MID|dataProvider=APXMIDP|price` = **145.96** (n=17, 2026-09-20T23:42:12.025930Z)
- `MID|dataProvider=APXMIDP|volume` = **2079.9** (n=17, 2026-09-20T23:42:12.025930Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=34, 2026-09-20T23:42:12.025930Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=34, 2026-09-20T23:42:12.025930Z)
- `NDF|TOTAL|demand` = **20110** (n=284, 2026-09-20T23:47:25.276035Z)
- `TSDF|TOTAL|demand` = **20610** (n=284, 2026-09-20T23:47:25.276035Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-20T23:50:36.707306Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:50:00Z`
- `2026-09-20T23:50:20.811673Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:49:45Z`
- `2026-09-20T23:49:33.095120Z` — **MELNGC**: 1008 rows; marker `2026-09-20T23:47:00Z`
- `2026-09-20T23:48:13.217169Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:47:45Z`
- `2026-09-20T23:47:25.276035Z` — **TSDF**: 1008 rows; marker `2026-09-20T23:47:00Z`
- `2026-09-20T23:47:25.276035Z` — **NDF**: 56 rows; marker `2026-09-20T23:47:00Z`
- `2026-09-20T23:46:06.009985Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:45:45Z`
- `2026-09-20T23:45:34.427916Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:45:00Z`
- `2026-09-20T23:44:15.041757Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:43:45Z`
- `2026-09-20T23:42:12.025930Z` — **MID**: 2 rows; marker `2026-09-20T23:42:03Z`
- `2026-09-20T23:42:12.025930Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:41:45Z`
- `2026-09-20T23:40:35.784587Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:40:00Z`
- `2026-09-20T23:40:19.834925Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:39:45Z`
- `2026-09-20T23:38:12.406243Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:37:45Z`
- `2026-09-20T23:36:36.216175Z` — **MID**: 1 rows; marker `2026-09-20T23:35:00Z`
