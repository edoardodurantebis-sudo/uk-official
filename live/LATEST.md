# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T15:02:07.635102Z`  
Current process started UTC: `2026-09-22T14:58:08.000319Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2155, 2026-09-22T15:00:32.158850Z)
- `FUELINST|fuelType=OTHER|generation` = **733** (n=2155, 2026-09-22T15:00:32.158850Z)
- `FUELINST|fuelType=PS|generation` = **19** (n=2155, 2026-09-22T15:00:32.158850Z)
- `FUELINST|fuelType=WIND|generation` = **1620** (n=2155, 2026-09-22T15:00:32.158850Z)
- `IMBALNGC|TOTAL|imbalance` = **-7961** (n=354, 2026-09-22T14:53:01.821911Z)
- `INDDEM|TOTAL|demand` = **-12481** (n=354, 2026-09-22T14:52:45.550953Z)
- `INDGEN|TOTAL|generation` = **13212** (n=354, 2026-09-22T14:52:45.550953Z)
- `MELNGC|TOTAL|margin` = **37097** (n=354, 2026-09-22T14:50:21.926312Z)
- `MID|dataProvider=APXMIDP|price` = **135.36** (n=95, 2026-09-22T14:42:07.626642Z)
- `MID|dataProvider=APXMIDP|volume` = **2983.6** (n=95, 2026-09-22T14:42:07.626642Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=188, 2026-09-22T14:42:07.626642Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=188, 2026-09-22T14:42:07.626642Z)
- `NDF|TOTAL|demand` = **20673** (n=362, 2026-09-22T14:48:14.726596Z)
- `TSDF|TOTAL|demand` = **21173** (n=362, 2026-09-22T14:48:14.726596Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T15:00:32.158850Z` — **FUELHH**: 20 rows; marker `2026-09-22T15:00:00Z`
- `2026-09-22T15:00:32.158850Z` — **FUELINST**: 80 rows; marker `2026-09-22T15:00:00Z`
- `2026-09-22T15:00:15.969182Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:59:45Z`
- `2026-09-22T14:58:24.033724Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:57:45Z`
- `2026-09-22T14:56:12.465812Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:55:45Z`
- `2026-09-22T14:55:24.880737Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:55:00Z`
- `2026-09-22T14:54:20.771330Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:53:45Z`
- `2026-09-22T14:53:01.821911Z` — **IMBALNGC**: 1332 rows; marker `2026-09-22T14:47:00Z`
- `2026-09-22T14:52:45.550953Z` — **INDGEN**: 1332 rows; marker `2026-09-22T14:47:00Z`
- `2026-09-22T14:52:45.550953Z` — **INDDEM**: 1332 rows; marker `2026-09-22T14:47:00Z`
- `2026-09-22T14:52:13.241640Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:51:45Z`
- `2026-09-22T14:50:37.529516Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:50:00Z`
- `2026-09-22T14:50:21.926312Z` — **MELNGC**: 1332 rows; marker `2026-09-22T14:47:00Z`
- `2026-09-22T14:50:21.926312Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:49:45Z`
- `2026-09-22T14:48:14.726596Z` — **TSDF**: 1332 rows; marker `2026-09-22T14:47:00Z`
