# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T13:49:39.022694Z`  
Current process started UTC: `2026-09-22T13:45:38.864808Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2140, 2026-09-22T13:45:25.375286Z)
- `FUELINST|fuelType=OTHER|generation` = **505** (n=2140, 2026-09-22T13:45:25.375286Z)
- `FUELINST|fuelType=PS|generation` = **-23** (n=2140, 2026-09-22T13:45:25.375286Z)
- `FUELINST|fuelType=WIND|generation` = **2256** (n=2140, 2026-09-22T13:45:25.375286Z)
- `IMBALNGC|TOTAL|imbalance` = **-7101** (n=351, 2026-09-22T13:23:27.914109Z)
- `INDDEM|TOTAL|demand` = **-12489** (n=351, 2026-09-22T13:23:11.544375Z)
- `INDGEN|TOTAL|generation` = **14057** (n=351, 2026-09-22T13:23:11.544375Z)
- `MELNGC|TOTAL|margin` = **37210** (n=351, 2026-09-22T13:20:32.064206Z)
- `MID|dataProvider=APXMIDP|price` = **127.71** (n=93, 2026-09-22T13:42:13.694515Z)
- `MID|dataProvider=APXMIDP|volume` = **4616.4** (n=93, 2026-09-22T13:42:13.694515Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=184, 2026-09-22T13:42:13.694515Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=184, 2026-09-22T13:42:13.694515Z)
- `NDF|TOTAL|demand` = **20658** (n=360, 2026-09-22T13:48:21.765518Z)
- `TSDF|TOTAL|demand` = **21158** (n=360, 2026-09-22T13:48:21.765518Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T13:48:21.765518Z` — **TSDF**: 1368 rows; marker `2026-09-22T13:47:00Z`
- `2026-09-22T13:48:21.765518Z` — **NDF**: 76 rows; marker `2026-09-22T13:47:00Z`
- `2026-09-22T13:48:21.765518Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:47:45Z`
- `2026-09-22T13:46:13.869928Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:45:45Z`
- `2026-09-22T13:45:25.375286Z` — **FUELINST**: 80 rows; marker `2026-09-22T13:45:00Z`
- `2026-09-22T13:44:21.767464Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:43:45Z`
- `2026-09-22T13:42:13.694515Z` — **MID**: 2 rows; marker `2026-09-22T13:42:03Z`
- `2026-09-22T13:42:13.694515Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:41:45Z`
- `2026-09-22T13:40:26.646329Z` — **FUELINST**: 80 rows; marker `2026-09-22T13:40:00Z`
- `2026-09-22T13:40:10.510724Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:39:45Z`
- `2026-09-22T13:38:18.291074Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:37:45Z`
- `2026-09-22T13:37:30.659187Z` — **MID**: 1 rows; marker `2026-09-22T13:35:00Z`
- `2026-09-22T13:36:13.167558Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:35:45Z`
- `2026-09-22T13:35:24.146171Z` — **FUELINST**: 80 rows; marker `2026-09-22T13:35:00Z`
- `2026-09-22T13:34:04.377025Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:33:45Z`
