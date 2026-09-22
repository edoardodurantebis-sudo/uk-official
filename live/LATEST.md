# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T14:45:04.006670Z`  
Current process started UTC: `2026-09-22T14:41:03.618683Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3729, delta=7, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3732, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3731, delta=9, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3737, delta=0, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3722, delta=43, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3737, delta=4, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3733, delta=3, z=3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3730, delta=10, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3136, delta=-128, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3264, delta=142, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3122, delta=169, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=-1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3662, delta=5, z=3.53 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2151, 2026-09-22T14:40:31.219114Z)
- `FUELINST|fuelType=OTHER|generation` = **517** (n=2151, 2026-09-22T14:40:31.219114Z)
- `FUELINST|fuelType=PS|generation` = **-18** (n=2151, 2026-09-22T14:40:31.219114Z)
- `FUELINST|fuelType=WIND|generation` = **1711** (n=2151, 2026-09-22T14:40:31.219114Z)
- `IMBALNGC|TOTAL|imbalance` = **-7950** (n=353, 2026-09-22T14:22:48.105595Z)
- `INDDEM|TOTAL|demand` = **-12481** (n=353, 2026-09-22T14:22:48.105595Z)
- `INDGEN|TOTAL|generation` = **13208** (n=353, 2026-09-22T14:22:48.105595Z)
- `MELNGC|TOTAL|margin` = **37134** (n=353, 2026-09-22T14:19:53.107273Z)
- `MID|dataProvider=APXMIDP|price` = **135.36** (n=95, 2026-09-22T14:42:07.626642Z)
- `MID|dataProvider=APXMIDP|volume` = **2983.6** (n=95, 2026-09-22T14:42:07.626642Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=188, 2026-09-22T14:42:07.626642Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=188, 2026-09-22T14:42:07.626642Z)
- `NDF|TOTAL|demand` = **20658** (n=361, 2026-09-22T14:18:02.576360Z)
- `TSDF|TOTAL|demand` = **21158** (n=361, 2026-09-22T14:18:02.576360Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T14:44:15.725906Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:43:45Z`
- `2026-09-22T14:42:07.626642Z` — **MID**: 2 rows; marker `2026-09-22T14:42:03Z`
- `2026-09-22T14:42:07.626642Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:41:45Z`
- `2026-09-22T14:40:31.219114Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:40:00Z`
- `2026-09-22T14:40:14.764918Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:39:45Z`
- `2026-09-22T14:38:05.650333Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:37:45Z`
- `2026-09-22T14:37:33.912799Z` — **MID**: 1 rows; marker `2026-09-22T14:35:00Z`
- `2026-09-22T14:36:15.386299Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:35:45Z`
- `2026-09-22T14:35:26.987472Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:35:00Z`
- `2026-09-22T14:34:07.226677Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:33:45Z`
- `2026-09-22T14:32:28.050416Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:31:45Z`
- `2026-09-22T14:30:38.121890Z` — **FUELHH**: 20 rows; marker `2026-09-22T14:30:00Z`
- `2026-09-22T14:30:22.324682Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:30:00Z`
- `2026-09-22T14:30:22.324682Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:29:45Z`
- `2026-09-22T14:28:13.989714Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:27:45Z`
