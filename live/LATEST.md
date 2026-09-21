# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T03:51:43.131201Z`  
Current process started UTC: `2026-09-21T03:47:42.721414Z`  
1-second metadata polls in this process: **231**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1736, 2026-09-21T03:50:40.036261Z)
- `FUELINST|fuelType=OTHER|generation` = **163** (n=1736, 2026-09-21T03:50:40.036261Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1736, 2026-09-21T03:50:40.036261Z)
- `FUELINST|fuelType=WIND|generation` = **3810** (n=1736, 2026-09-21T03:50:40.036261Z)
- `IMBALNGC|TOTAL|imbalance` = **-4043** (n=286, 2026-09-21T03:50:23.681881Z)
- `INDDEM|TOTAL|demand` = **-11760** (n=286, 2026-09-21T03:50:07.852391Z)
- `INDGEN|TOTAL|generation` = **16567** (n=286, 2026-09-21T03:50:07.852391Z)
- `MELNGC|TOTAL|margin` = **37551** (n=286, 2026-09-21T03:48:47.430896Z)
- `MID|dataProvider=APXMIDP|price` = **134.98** (n=25, 2026-09-21T03:42:20.628577Z)
- `MID|dataProvider=APXMIDP|volume` = **2427.8** (n=25, 2026-09-21T03:42:20.628577Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=50, 2026-09-21T03:42:20.628577Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=50, 2026-09-21T03:42:20.628577Z)
- `NDF|TOTAL|demand` = **20110** (n=292, 2026-09-21T03:47:42.721422Z)
- `TSDF|TOTAL|demand` = **20610** (n=292, 2026-09-21T03:47:42.721422Z)
- `WINDFOR|TOTAL|generation` = **8021** (n=49, 2026-09-21T03:30:39.847119Z)

## Latest publication events

- `2026-09-21T03:50:40.036261Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:50:00Z`
- `2026-09-21T03:50:23.681881Z` — **IMBALNGC**: 864 rows; marker `2026-09-21T03:46:00Z`
- `2026-09-21T03:50:23.681881Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:49:45Z`
- `2026-09-21T03:50:07.852391Z` — **INDGEN**: 864 rows; marker `2026-09-21T03:46:00Z`
- `2026-09-21T03:50:07.852391Z` — **INDDEM**: 864 rows; marker `2026-09-21T03:46:00Z`
- `2026-09-21T03:48:47.430896Z` — **MELNGC**: 864 rows; marker `2026-09-21T03:46:00Z`
- `2026-09-21T03:48:15.197892Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:47:45Z`
- `2026-09-21T03:47:42.721422Z` — **TSDF**: 864 rows; marker `2026-09-21T03:46:00Z`
- `2026-09-21T03:47:42.721422Z` — **NDF**: 48 rows; marker `2026-09-21T03:46:00Z`
- `2026-09-21T03:46:12.659694Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:45:45Z`
- `2026-09-21T03:45:41.259611Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:45:00Z`
- `2026-09-21T03:44:21.450258Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:43:45Z`
- `2026-09-21T03:42:20.628577Z` — **MID**: 2 rows; marker `2026-09-21T03:42:02Z`
- `2026-09-21T03:42:20.628577Z` — **FREQ**: 5761 rows; marker `2026-09-21T03:41:45Z`
- `2026-09-21T03:40:28.602883Z` — **FUELINST**: 80 rows; marker `2026-09-21T03:40:00Z`
