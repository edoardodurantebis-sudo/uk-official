# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T03:43:03.853583Z`  
Current process started UTC: `2026-09-21T03:39:04.164508Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1734, 2026-09-21T03:40:28.602883Z)
- `FUELINST|fuelType=OTHER|generation` = **196** (n=1734, 2026-09-21T03:40:28.602883Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1734, 2026-09-21T03:40:28.602883Z)
- `FUELINST|fuelType=WIND|generation` = **3716** (n=1734, 2026-09-21T03:40:28.602883Z)
- `IMBALNGC|TOTAL|imbalance` = **-4820** (n=285, 2026-09-21T03:20:59.430477Z)
- `INDDEM|TOTAL|demand` = **-11798** (n=285, 2026-09-21T03:20:59.430477Z)
- `INDGEN|TOTAL|generation` = **15790** (n=285, 2026-09-21T03:20:59.430477Z)
- `MELNGC|TOTAL|margin` = **37568** (n=285, 2026-09-21T03:19:55.823626Z)
- `MID|dataProvider=APXMIDP|price` = **134.98** (n=25, 2026-09-21T03:42:20.628577Z)
- `MID|dataProvider=APXMIDP|volume` = **2427.8** (n=25, 2026-09-21T03:42:20.628577Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=50, 2026-09-21T03:42:20.628577Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=50, 2026-09-21T03:42:20.628577Z)
- `NDF|TOTAL|demand` = **20110** (n=291, 2026-09-21T03:17:46.317131Z)
- `TSDF|TOTAL|demand` = **20610** (n=291, 2026-09-21T03:17:46.317131Z)
- `WINDFOR|TOTAL|generation` = **8021** (n=49, 2026-09-21T03:30:39.847119Z)

## Latest publication events

- `2026-09-21T03:42:20.628577Z` — **MID**: 2 rows; marker `2026-09-21T03:42:02Z`
- `2026-09-21T03:42:20.628577Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:41:45Z`
- `2026-09-21T03:40:28.602883Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:40:00Z`
- `2026-09-21T03:40:13.149859Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:39:45Z`
- `2026-09-21T03:38:20.170189Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:37:45Z`
- `2026-09-21T03:36:44.673393Z` — **MID**: 1 rows; marker `2026-09-21T03:35:00Z`
- `2026-09-21T03:36:12.708492Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:35:45Z`
- `2026-09-21T03:35:23.738969Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:35:00Z`
- `2026-09-21T03:34:07.555208Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:33:45Z`
- `2026-09-21T03:32:15.799122Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:31:45Z`
- `2026-09-21T03:30:39.847119Z` — **WINDFOR**: 73 rows; marker `2026-09-21T03:30:00Z`
- `2026-09-21T03:30:39.847119Z` — **FUELHH**: 20 rows; marker `2026-09-21T03:30:00Z`
- `2026-09-21T03:30:39.847119Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:30:00Z`
- `2026-09-21T03:30:12.718007Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:29:45Z`
- `2026-09-21T03:28:03.430609Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:27:45Z`
