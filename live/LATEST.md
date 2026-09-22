# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T15:57:41.572314Z`  
Current process started UTC: `2026-09-22T15:53:41.752265Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2166, 2026-09-22T15:55:34.494670Z)
- `FUELINST|fuelType=OTHER|generation` = **707** (n=2166, 2026-09-22T15:55:34.494670Z)
- `FUELINST|fuelType=PS|generation` = **285** (n=2166, 2026-09-22T15:55:34.494670Z)
- `FUELINST|fuelType=WIND|generation` = **1371** (n=2166, 2026-09-22T15:55:34.494670Z)
- `IMBALNGC|TOTAL|imbalance` = **-7942** (n=356, 2026-09-22T15:52:27.014740Z)
- `INDDEM|TOTAL|demand` = **-12476** (n=356, 2026-09-22T15:52:10.596481Z)
- `INDGEN|TOTAL|generation` = **13231** (n=356, 2026-09-22T15:52:10.596481Z)
- `MELNGC|TOTAL|margin` = **37185** (n=356, 2026-09-22T15:49:44.825117Z)
- `MID|dataProvider=APXMIDP|price` = **186.81** (n=97, 2026-09-22T15:42:20.713409Z)
- `MID|dataProvider=APXMIDP|volume` = **3626.6** (n=97, 2026-09-22T15:42:20.713409Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=192, 2026-09-22T15:42:20.713409Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=192, 2026-09-22T15:42:20.713409Z)
- `NDF|TOTAL|demand` = **20673** (n=364, 2026-09-22T15:47:37.690938Z)
- `TSDF|TOTAL|demand` = **21173** (n=364, 2026-09-22T15:47:53.867112Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T15:56:22.627017Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:55:45Z`
- `2026-09-22T15:55:34.494670Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:55:00Z`
- `2026-09-22T15:54:13.756225Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:53:45Z`
- `2026-09-22T15:52:27.014740Z` — **IMBALNGC**: 1296 rows; marker `2026-09-22T15:47:00Z`
- `2026-09-22T15:52:10.596481Z` — **INDGEN**: 1296 rows; marker `2026-09-22T15:47:00Z`
- `2026-09-22T15:52:10.596481Z` — **INDDEM**: 1296 rows; marker `2026-09-22T15:47:00Z`
- `2026-09-22T15:52:10.596481Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:51:45Z`
- `2026-09-22T15:50:33.830664Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:50:00Z`
- `2026-09-22T15:50:16.894110Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:49:45Z`
- `2026-09-22T15:49:44.825117Z` — **MELNGC**: 1296 rows; marker `2026-09-22T15:47:00Z`
- `2026-09-22T15:48:09.982166Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:47:45Z`
- `2026-09-22T15:47:53.867112Z` — **TSDF**: 1296 rows; marker `2026-09-22T15:47:00Z`
- `2026-09-22T15:47:37.690938Z` — **NDF**: 72 rows; marker `2026-09-22T15:47:00Z`
- `2026-09-22T15:46:17.006448Z` — **FREQ**: 5761 rows; marker `2026-09-22T15:45:45Z`
- `2026-09-22T15:45:29.144261Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:45:00Z`
