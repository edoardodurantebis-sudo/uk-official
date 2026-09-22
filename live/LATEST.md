# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T00:17:55.701694Z`  
Current process started UTC: `2026-09-22T00:13:55.395112Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=2, z=4.49 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=-2, z=4.48 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=2, z=4.54 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3649, delta=2, z=4.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=4, z=4.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3646, delta=-1, z=4.49 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3647, delta=-3, z=4.53 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=-2, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3652, delta=3, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3649, delta=-4, z=4.64 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3647, delta=5, z=4.77 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3653, delta=3, z=4.73 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3650, delta=5, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3645, delta=2, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3643, delta=-2, z=4.66 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1978, 2026-09-22T00:15:31.487477Z)
- `FUELINST|fuelType=OTHER|generation` = **161** (n=1978, 2026-09-22T00:15:31.487477Z)
- `FUELINST|fuelType=PS|generation` = **-284** (n=1978, 2026-09-22T00:15:31.487477Z)
- `FUELINST|fuelType=WIND|generation` = **3778** (n=1978, 2026-09-22T00:15:31.487477Z)
- `IMBALNGC|TOTAL|imbalance` = **-2010** (n=325, 2026-09-21T23:51:16.103087Z)
- `INDDEM|TOTAL|demand` = **-12382** (n=325, 2026-09-21T23:51:16.103087Z)
- `INDGEN|TOTAL|generation` = **19449** (n=325, 2026-09-21T23:51:16.103087Z)
- `MELNGC|TOTAL|margin` = **36218** (n=325, 2026-09-21T23:49:39.843008Z)
- `MID|dataProvider=APXMIDP|price` = **143.47** (n=66, 2026-09-22T00:12:10.010962Z)
- `MID|dataProvider=APXMIDP|volume` = **2140.6** (n=66, 2026-09-22T00:12:10.010962Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=130, 2026-09-22T00:12:10.010962Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=130, 2026-09-22T00:12:10.010962Z)
- `NDF|TOTAL|demand` = **20959** (n=333, 2026-09-22T00:17:23.355768Z)
- `TSDF|TOTAL|demand` = **21459** (n=333, 2026-09-22T00:17:23.355768Z)
- `WINDFOR|TOTAL|generation` = **9503** (n=56, 2026-09-21T23:30:37.821418Z)

## Latest publication events

- `2026-09-22T00:17:23.355768Z` — **TSDF**: 990 rows; marker `2026-09-22T00:17:00Z`
- `2026-09-22T00:17:23.355768Z` — **NDF**: 55 rows; marker `2026-09-22T00:17:00Z`
- `2026-09-22T00:16:19.170589Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:15:45Z`
- `2026-09-22T00:15:31.487477Z` — **FUELINST**: 80 rows; marker `2026-09-22T00:15:00Z`
- `2026-09-22T00:14:11.396270Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:13:45Z`
- `2026-09-22T00:12:10.010962Z` — **MID**: 2 rows; marker `2026-09-22T00:12:03Z`
- `2026-09-22T00:12:10.010962Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:11:45Z`
- `2026-09-22T00:10:34.518023Z` — **FUELINST**: 80 rows; marker `2026-09-22T00:10:00Z`
- `2026-09-22T00:10:18.229513Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:09:45Z`
- `2026-09-22T00:08:09.705340Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:07:45Z`
- `2026-09-22T00:07:22.291468Z` — **MID**: 1 rows; marker `2026-09-22T00:05:00Z`
- `2026-09-22T00:06:18.989645Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:05:45Z`
- `2026-09-22T00:05:31.191009Z` — **FUELINST**: 80 rows; marker `2026-09-22T00:05:00Z`
- `2026-09-22T00:04:09.405982Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:03:45Z`
- `2026-09-22T00:02:15.352576Z` — **FREQ**: 5761 rows; marker `2026-09-22T00:01:45Z`
