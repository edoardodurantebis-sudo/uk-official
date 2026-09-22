# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T14:27:59.399755Z`  
Current process started UTC: `2026-09-22T14:23:59.148216Z`  
1-second metadata polls in this process: **236**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2148, 2026-09-22T14:25:18.664552Z)
- `FUELINST|fuelType=OTHER|generation` = **488** (n=2148, 2026-09-22T14:25:18.664552Z)
- `FUELINST|fuelType=PS|generation` = **-18** (n=2148, 2026-09-22T14:25:18.664552Z)
- `FUELINST|fuelType=WIND|generation` = **1834** (n=2148, 2026-09-22T14:25:18.664552Z)
- `IMBALNGC|TOTAL|imbalance` = **-7950** (n=353, 2026-09-22T14:22:48.105595Z)
- `INDDEM|TOTAL|demand` = **-12481** (n=353, 2026-09-22T14:22:48.105595Z)
- `INDGEN|TOTAL|generation` = **13208** (n=353, 2026-09-22T14:22:48.105595Z)
- `MELNGC|TOTAL|margin` = **37134** (n=353, 2026-09-22T14:19:53.107273Z)
- `MID|dataProvider=APXMIDP|price` = **132.53** (n=94, 2026-09-22T14:12:07.191375Z)
- `MID|dataProvider=APXMIDP|volume` = **3780.7** (n=94, 2026-09-22T14:12:07.191375Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=186, 2026-09-22T14:12:07.191375Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=186, 2026-09-22T14:12:07.191375Z)
- `NDF|TOTAL|demand` = **20658** (n=361, 2026-09-22T14:18:02.576360Z)
- `TSDF|TOTAL|demand` = **21158** (n=361, 2026-09-22T14:18:02.576360Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T14:26:06.797130Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:25:45Z`
- `2026-09-22T14:25:18.664552Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:25:00Z`
- `2026-09-22T14:24:15.196487Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:23:45Z`
- `2026-09-22T14:22:48.105595Z` — **INDGEN**: 1350 rows; marker `2026-09-22T14:17:00Z`
- `2026-09-22T14:22:48.105595Z` — **INDDEM**: 1350 rows; marker `2026-09-22T14:17:00Z`
- `2026-09-22T14:22:48.105595Z` — **IMBALNGC**: 1350 rows; marker `2026-09-22T14:17:00Z`
- `2026-09-22T14:22:00.718681Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:21:45Z`
- `2026-09-22T14:20:24.641048Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:20:00Z`
- `2026-09-22T14:20:09.176462Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:19:45Z`
- `2026-09-22T14:19:53.107273Z` — **MELNGC**: 1350 rows; marker `2026-09-22T14:17:00Z`
- `2026-09-22T14:18:02.576360Z` — **TSDF**: 1350 rows; marker `2026-09-22T14:17:00Z`
- `2026-09-22T14:18:02.576360Z` — **NDF**: 75 rows; marker `2026-09-22T14:17:00Z`
- `2026-09-22T14:18:02.576360Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:17:45Z`
- `2026-09-22T14:16:10.748927Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:15:45Z`
- `2026-09-22T14:15:38.557273Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:15:00Z`
