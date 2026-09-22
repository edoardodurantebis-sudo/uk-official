# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T14:15:02.239233Z`  
Current process started UTC: `2026-09-22T14:11:02.704961Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2145, 2026-09-22T14:11:02.704971Z)
- `FUELINST|fuelType=OTHER|generation` = **474** (n=2145, 2026-09-22T14:11:02.704971Z)
- `FUELINST|fuelType=PS|generation` = **-19** (n=2145, 2026-09-22T14:11:02.704971Z)
- `FUELINST|fuelType=WIND|generation` = **1930** (n=2145, 2026-09-22T14:11:02.704971Z)
- `IMBALNGC|TOTAL|imbalance` = **-7103** (n=352, 2026-09-22T13:53:02.379384Z)
- `INDDEM|TOTAL|demand` = **-12489** (n=352, 2026-09-22T13:53:02.379384Z)
- `INDGEN|TOTAL|generation` = **14055** (n=352, 2026-09-22T13:53:02.379384Z)
- `MELNGC|TOTAL|margin` = **37231** (n=352, 2026-09-22T13:50:22.441443Z)
- `MID|dataProvider=APXMIDP|price` = **132.53** (n=94, 2026-09-22T14:12:07.191375Z)
- `MID|dataProvider=APXMIDP|volume` = **3780.7** (n=94, 2026-09-22T14:12:07.191375Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=186, 2026-09-22T14:12:07.191375Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=186, 2026-09-22T14:12:07.191375Z)
- `NDF|TOTAL|demand` = **20658** (n=360, 2026-09-22T13:48:21.765518Z)
- `TSDF|TOTAL|demand` = **21158** (n=360, 2026-09-22T13:48:21.765518Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T14:14:31.198708Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:13:45Z`
- `2026-09-22T14:12:23.225053Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:11:45Z`
- `2026-09-22T14:12:07.191375Z` — **MID**: 2 rows; marker `2026-09-22T14:12:03Z`
- `2026-09-22T14:11:02.704971Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:10:00Z`
- `2026-09-22T14:10:13.274255Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:09:45Z`
- `2026-09-22T14:08:19.931477Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:07:45Z`
- `2026-09-22T14:07:15.592323Z` — **MID**: 1 rows; marker `2026-09-22T14:05:00Z`
- `2026-09-22T14:06:13.592043Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:05:45Z`
- `2026-09-22T14:05:41.378541Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:05:00Z`
- `2026-09-22T14:04:21.390844Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:03:45Z`
- `2026-09-22T14:02:13.436604Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:01:45Z`
- `2026-09-22T14:00:37.948279Z` — **FUELHH**: 20 rows; marker `2026-09-22T14:00:00Z`
- `2026-09-22T14:00:37.948279Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:00:00Z`
- `2026-09-22T14:00:22.313875Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:59:45Z`
- `2026-09-22T13:58:13.837112Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:57:45Z`
