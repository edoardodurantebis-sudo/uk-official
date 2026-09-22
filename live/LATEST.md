# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T13:15:46.616785Z`  
Current process started UTC: `2026-09-22T13:11:47.085470Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2133, 2026-09-22T13:10:30.856626Z)
- `FUELINST|fuelType=OTHER|generation` = **625** (n=2133, 2026-09-22T13:10:30.856626Z)
- `FUELINST|fuelType=PS|generation` = **-6** (n=2133, 2026-09-22T13:10:30.856626Z)
- `FUELINST|fuelType=WIND|generation` = **2469** (n=2133, 2026-09-22T13:10:30.856626Z)
- `IMBALNGC|TOTAL|imbalance` = **-7090** (n=350, 2026-09-22T12:53:49.151614Z)
- `INDDEM|TOTAL|demand` = **-12490** (n=350, 2026-09-22T12:53:33.557974Z)
- `INDGEN|TOTAL|generation` = **14068** (n=350, 2026-09-22T12:53:49.151614Z)
- `MELNGC|TOTAL|margin` = **37206** (n=350, 2026-09-22T12:50:52.874396Z)
- `MID|dataProvider=APXMIDP|price` = **123.86** (n=92, 2026-09-22T13:12:19.089418Z)
- `MID|dataProvider=APXMIDP|volume` = **4159.4** (n=92, 2026-09-22T13:12:19.089418Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=182, 2026-09-22T13:12:19.089418Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=182, 2026-09-22T13:12:19.089418Z)
- `NDF|TOTAL|demand` = **20658** (n=358, 2026-09-22T12:48:17.842061Z)
- `TSDF|TOTAL|demand` = **21158** (n=358, 2026-09-22T12:48:17.842061Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T13:14:12.038734Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:13:45Z`
- `2026-09-22T13:12:19.089418Z` — **MID**: 2 rows; marker `2026-09-22T13:12:04Z`
- `2026-09-22T13:12:19.089418Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:11:45Z`
- `2026-09-22T13:10:30.856626Z` — **FUELINST**: 80 rows; marker `2026-09-22T13:10:00Z`
- `2026-09-22T13:10:30.856626Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:09:45Z`
- `2026-09-22T13:08:23.319938Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:07:45Z`
- `2026-09-22T13:07:34.406335Z` — **MID**: 1 rows; marker `2026-09-22T13:05:00Z`
- `2026-09-22T13:06:27.475218Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:05:45Z`
- `2026-09-22T13:05:39.425602Z` — **FUELINST**: 80 rows; marker `2026-09-22T13:05:00Z`
- `2026-09-22T13:04:19.883257Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:03:45Z`
- `2026-09-22T13:02:15.237417Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:01:45Z`
- `2026-09-22T13:00:39.623069Z` — **FUELHH**: 20 rows; marker `2026-09-22T13:00:00Z`
- `2026-09-22T13:00:39.623069Z` — **FUELINST**: 80 rows; marker `2026-09-22T13:00:00Z`
- `2026-09-22T13:00:23.379370Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:59:45Z`
- `2026-09-22T12:58:21.000165Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:57:45Z`
