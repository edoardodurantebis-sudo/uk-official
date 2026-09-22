# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T07:44:14.924428Z`  
Current process started UTC: `2026-09-22T07:40:13.517562Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3136, delta=-128, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3264, delta=142, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3122, delta=169, z=3.61 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3657, delta=-2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=-1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3662, delta=5, z=3.53 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3659, delta=11, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3656, delta=2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3659, delta=-2, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3661, delta=1, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3660, delta=-3, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3663, delta=14, z=3.65 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-2, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=1, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3648, delta=-5, z=3.50 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=2067, 2026-09-22T07:40:45.277138Z)
- `FUELINST|fuelType=OTHER|generation` = **781** (n=2067, 2026-09-22T07:40:45.277138Z)
- `FUELINST|fuelType=PS|generation` = **-172** (n=2067, 2026-09-22T07:40:45.277138Z)
- `FUELINST|fuelType=WIND|generation` = **3472** (n=2067, 2026-09-22T07:40:45.277138Z)
- `IMBALNGC|TOTAL|imbalance` = **-3831** (n=340, 2026-09-22T07:19:53.015943Z)
- `INDDEM|TOTAL|demand` = **-12688** (n=340, 2026-09-22T07:19:53.015943Z)
- `INDGEN|TOTAL|generation` = **17876** (n=340, 2026-09-22T07:19:53.015943Z)
- `MELNGC|TOTAL|margin` = **37783** (n=340, 2026-09-22T07:19:04.110635Z)
- `MID|dataProvider=APXMIDP|price` = **150.12** (n=81, 2026-09-22T07:42:21.458933Z)
- `MID|dataProvider=APXMIDP|volume` = **2917.3** (n=81, 2026-09-22T07:42:21.458933Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=160, 2026-09-22T07:42:21.458933Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=160, 2026-09-22T07:42:21.458933Z)
- `NDF|TOTAL|demand` = **20959** (n=347, 2026-09-22T07:17:12.886968Z)
- `TSDF|TOTAL|demand` = **21707** (n=347, 2026-09-22T07:17:12.886968Z)
- `WINDFOR|TOTAL|generation` = **12340** (n=58, 2026-09-22T05:30:40.954997Z)

## Latest publication events

- `2026-09-22T07:44:13.326961Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:43:45Z`
- `2026-09-22T07:42:21.458933Z` — **MID**: 2 rows; marker `2026-09-22T07:42:04Z`
- `2026-09-22T07:42:21.458933Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:41:45Z`
- `2026-09-22T07:40:45.277138Z` — **FUELINST**: 80 rows; marker `2026-09-22T07:40:00Z`
- `2026-09-22T07:40:13.517573Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:39:45Z`
- `2026-09-22T07:38:24.358775Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:37:45Z`
- `2026-09-22T07:36:16.580519Z` — **MID**: 1 rows; marker `2026-09-22T07:35:00Z`
- `2026-09-22T07:36:16.580519Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:35:45Z`
- `2026-09-22T07:36:00.435579Z` — **FUELINST**: 80 rows; marker `2026-09-22T07:35:00Z`
- `2026-09-22T07:34:19.354883Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:33:45Z`
- `2026-09-22T07:32:26.607808Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:31:45Z`
- `2026-09-22T07:30:40.384837Z` — **FUELHH**: 20 rows; marker `2026-09-22T07:30:00Z`
- `2026-09-22T07:30:40.384837Z` — **FUELINST**: 80 rows; marker `2026-09-22T07:30:00Z`
- `2026-09-22T07:30:25.029262Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:29:45Z`
- `2026-09-22T07:28:15.638761Z` — **FREQ**: 5761 rows; marker `2026-09-22T07:27:45Z`
