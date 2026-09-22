# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T15:48:57.164270Z`  
Current process started UTC: `2026-09-22T15:44:57.140190Z`  
1-second metadata polls in this process: **234**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2164, 2026-09-22T15:45:29.144261Z)
- `FUELINST|fuelType=OTHER|generation` = **811** (n=2164, 2026-09-22T15:45:29.144261Z)
- `FUELINST|fuelType=PS|generation` = **285** (n=2164, 2026-09-22T15:45:29.144261Z)
- `FUELINST|fuelType=WIND|generation` = **1401** (n=2164, 2026-09-22T15:45:29.144261Z)
- `IMBALNGC|TOTAL|imbalance` = **-7955** (n=355, 2026-09-22T15:22:47.715019Z)
- `INDDEM|TOTAL|demand` = **-12481** (n=355, 2026-09-22T15:22:31.530428Z)
- `INDGEN|TOTAL|generation` = **13218** (n=355, 2026-09-22T15:22:47.715019Z)
- `MELNGC|TOTAL|margin` = **37207** (n=355, 2026-09-22T15:20:24.168308Z)
- `MID|dataProvider=APXMIDP|price` = **186.81** (n=97, 2026-09-22T15:42:20.713409Z)
- `MID|dataProvider=APXMIDP|volume` = **3626.6** (n=97, 2026-09-22T15:42:20.713409Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=192, 2026-09-22T15:42:20.713409Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=192, 2026-09-22T15:42:20.713409Z)
- `NDF|TOTAL|demand` = **20673** (n=364, 2026-09-22T15:47:37.690938Z)
- `TSDF|TOTAL|demand` = **21173** (n=364, 2026-09-22T15:47:53.867112Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T15:48:09.982166Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:47:45Z`
- `2026-09-22T15:47:53.867112Z` — **TSDF**: 1296 rows; marker `2026-09-22T15:47:00Z`
- `2026-09-22T15:47:37.690938Z` — **NDF**: 72 rows; marker `2026-09-22T15:47:00Z`
- `2026-09-22T15:46:17.006448Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:45:45Z`
- `2026-09-22T15:45:29.144261Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:45:00Z`
- `2026-09-22T15:44:12.497770Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:43:45Z`
- `2026-09-22T15:42:20.713409Z` — **MID**: 2 rows; marker `2026-09-22T15:42:04Z`
- `2026-09-22T15:42:20.713409Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:41:45Z`
- `2026-09-22T15:40:28.459080Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:40:00Z`
- `2026-09-22T15:40:12.966551Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:39:45Z`
- `2026-09-22T15:38:21.513895Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:37:45Z`
- `2026-09-22T15:37:33.465868Z` — **MID**: 1 rows; marker `2026-09-22T15:35:00Z`
- `2026-09-22T15:36:29.304036Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:35:00Z`
- `2026-09-22T15:36:29.304036Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:35:45Z`
- `2026-09-22T15:34:10.102585Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:33:45Z`
