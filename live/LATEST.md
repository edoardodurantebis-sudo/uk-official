# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T14:02:15.002591Z`  
Current process started UTC: `2026-09-22T13:58:13.837103Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2143, 2026-09-22T14:00:37.948279Z)
- `FUELINST|fuelType=OTHER|generation` = **692** (n=2143, 2026-09-22T14:00:37.948279Z)
- `FUELINST|fuelType=PS|generation` = **-17** (n=2143, 2026-09-22T14:00:37.948279Z)
- `FUELINST|fuelType=WIND|generation` = **2036** (n=2143, 2026-09-22T14:00:37.948279Z)
- `IMBALNGC|TOTAL|imbalance` = **-7103** (n=352, 2026-09-22T13:53:02.379384Z)
- `INDDEM|TOTAL|demand` = **-12489** (n=352, 2026-09-22T13:53:02.379384Z)
- `INDGEN|TOTAL|generation` = **14055** (n=352, 2026-09-22T13:53:02.379384Z)
- `MELNGC|TOTAL|margin` = **37231** (n=352, 2026-09-22T13:50:22.441443Z)
- `MID|dataProvider=APXMIDP|price` = **127.71** (n=93, 2026-09-22T13:42:13.694515Z)
- `MID|dataProvider=APXMIDP|volume` = **4616.4** (n=93, 2026-09-22T13:42:13.694515Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=184, 2026-09-22T13:42:13.694515Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=184, 2026-09-22T13:42:13.694515Z)
- `NDF|TOTAL|demand` = **20658** (n=360, 2026-09-22T13:48:21.765518Z)
- `TSDF|TOTAL|demand` = **21158** (n=360, 2026-09-22T13:48:21.765518Z)
- `WINDFOR|TOTAL|generation` = **13082** (n=61, 2026-09-22T12:30:43.630179Z)

## Latest publication events

- `2026-09-22T14:02:13.436604Z` — **FREQ**: 5761 rows; marker `2026-09-22T14:01:45Z`
- `2026-09-22T14:00:37.948279Z` — **FUELHH**: 20 rows; marker `2026-09-22T14:00:00Z`
- `2026-09-22T14:00:37.948279Z` — **FUELINST**: 80 rows; marker `2026-09-22T14:00:00Z`
- `2026-09-22T14:00:22.313875Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:59:45Z`
- `2026-09-22T13:58:13.837112Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:57:45Z`
- `2026-09-22T13:56:13.212561Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:55:45Z`
- `2026-09-22T13:55:25.745659Z` — **FUELINST**: 80 rows; marker `2026-09-22T13:55:00Z`
- `2026-09-22T13:54:21.743572Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:53:45Z`
- `2026-09-22T13:53:02.379384Z` — **INDGEN**: 1368 rows; marker `2026-09-22T13:47:00Z`
- `2026-09-22T13:53:02.379384Z` — **INDDEM**: 1368 rows; marker `2026-09-22T13:47:00Z`
- `2026-09-22T13:53:02.379384Z` — **IMBALNGC**: 1368 rows; marker `2026-09-22T13:47:00Z`
- `2026-09-22T13:52:14.834941Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:51:45Z`
- `2026-09-22T13:50:38.729024Z` — **FUELINST**: 80 rows; marker `2026-09-22T13:50:00Z`
- `2026-09-22T13:50:22.441443Z` — **MELNGC**: 1368 rows; marker `2026-09-22T13:47:00Z`
- `2026-09-22T13:50:22.441443Z` — **FREQ**: 5761 rows; marker `2026-09-22T13:49:45Z`
