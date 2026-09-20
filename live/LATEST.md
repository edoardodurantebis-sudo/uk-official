# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T23:42:24.692480Z`  
Current process started UTC: `2026-09-20T23:38:24.818920Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1686, 2026-09-20T23:40:35.784587Z)
- `FUELINST|fuelType=OTHER|generation` = **135** (n=1686, 2026-09-20T23:40:35.784587Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1686, 2026-09-20T23:40:35.784587Z)
- `FUELINST|fuelType=WIND|generation` = **5531** (n=1686, 2026-09-20T23:40:35.784587Z)
- `IMBALNGC|TOTAL|imbalance` = **-5221** (n=277, 2026-09-20T23:21:41.704783Z)
- `INDDEM|TOTAL|demand` = **-11829** (n=277, 2026-09-20T23:21:26.169619Z)
- `INDGEN|TOTAL|generation` = **15389** (n=277, 2026-09-20T23:21:26.169619Z)
- `MELNGC|TOTAL|margin` = **35811** (n=277, 2026-09-20T23:19:18.463918Z)
- `MID|dataProvider=APXMIDP|price` = **145.96** (n=17, 2026-09-20T23:42:12.025930Z)
- `MID|dataProvider=APXMIDP|volume` = **2079.9** (n=17, 2026-09-20T23:42:12.025930Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=34, 2026-09-20T23:42:12.025930Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=34, 2026-09-20T23:42:12.025930Z)
- `NDF|TOTAL|demand` = **20110** (n=283, 2026-09-20T23:17:42.348630Z)
- `TSDF|TOTAL|demand` = **20610** (n=283, 2026-09-20T23:17:42.348630Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-20T23:42:12.025930Z` — **MID**: 2 rows; marker `2026-09-20T23:42:03Z`
- `2026-09-20T23:42:12.025930Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:41:45Z`
- `2026-09-20T23:40:35.784587Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:40:00Z`
- `2026-09-20T23:40:19.834925Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:39:45Z`
- `2026-09-20T23:38:12.406243Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:37:45Z`
- `2026-09-20T23:36:36.216175Z` — **MID**: 1 rows; marker `2026-09-20T23:35:00Z`
- `2026-09-20T23:36:04.443269Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:35:45Z`
- `2026-09-20T23:35:48.225512Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:35:00Z`
- `2026-09-20T23:34:12.528437Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:33:45Z`
- `2026-09-20T23:32:13.860948Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:31:45Z`
- `2026-09-20T23:30:37.519891Z` — **WINDFOR**: 73 rows; marker `2026-09-20T23:30:00Z`
- `2026-09-20T23:30:37.519891Z` — **FUELHH**: 20 rows; marker `2026-09-20T23:30:00Z`
- `2026-09-20T23:30:37.519891Z` — **FUELINST**: 80 rows; marker `2026-09-20T23:30:00Z`
- `2026-09-20T23:30:05.184927Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:29:45Z`
- `2026-09-20T23:28:13.422588Z` — **FREQ**: 5761 rows; marker `2026-09-20T23:27:45Z`
