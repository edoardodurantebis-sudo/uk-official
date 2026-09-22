# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T12:16:29.194747Z`  
Current process started UTC: `2026-09-22T12:12:28.586857Z`  
1-second metadata polls in this process: **230**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2122, 2026-09-22T12:15:41.721060Z)
- `FUELINST|fuelType=OTHER|generation` = **638** (n=2122, 2026-09-22T12:15:41.721060Z)
- `FUELINST|fuelType=PS|generation` = **-125** (n=2122, 2026-09-22T12:15:41.721060Z)
- `FUELINST|fuelType=WIND|generation` = **2872** (n=2122, 2026-09-22T12:15:41.721060Z)
- `IMBALNGC|TOTAL|imbalance` = **-7049** (n=348, 2026-09-22T11:53:36.058034Z)
- `INDDEM|TOTAL|demand` = **-12511** (n=348, 2026-09-22T11:53:36.058034Z)
- `INDGEN|TOTAL|generation` = **14109** (n=348, 2026-09-22T11:53:36.058034Z)
- `MELNGC|TOTAL|margin` = **37032** (n=348, 2026-09-22T11:50:13.119103Z)
- `MID|dataProvider=APXMIDP|price` = **122.04** (n=90, 2026-09-22T12:12:28.586866Z)
- `MID|dataProvider=APXMIDP|volume` = **4318.9** (n=90, 2026-09-22T12:12:28.586866Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=178, 2026-09-22T12:12:28.586866Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=178, 2026-09-22T12:12:28.586866Z)
- `NDF|TOTAL|demand` = **20658** (n=356, 2026-09-22T11:48:05.233540Z)
- `TSDF|TOTAL|demand` = **21158** (n=356, 2026-09-22T11:48:05.233540Z)
- `WINDFOR|TOTAL|generation` = **13007** (n=60, 2026-09-22T10:30:42.618958Z)

## Latest publication events

- `2026-09-22T12:15:41.721060Z` — **FUELINST**: 80 rows; marker `2026-09-22T12:15:00Z`
- `2026-09-22T12:14:20.700802Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:13:45Z`
- `2026-09-22T12:12:28.586866Z` — **MID**: 2 rows; marker `2026-09-22T12:12:04Z`
- `2026-09-22T12:12:28.586866Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:11:45Z`
- `2026-09-22T12:10:36.850578Z` — **FUELINST**: 80 rows; marker `2026-09-22T12:10:00Z`
- `2026-09-22T12:10:20.669297Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:09:45Z`
- `2026-09-22T12:08:27.073742Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:07:45Z`
- `2026-09-22T12:07:27.893362Z` — **MID**: 1 rows; marker `2026-09-22T12:05:00Z`
- `2026-09-22T12:06:23.718743Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:05:45Z`
- `2026-09-22T12:05:35.553331Z` — **FUELINST**: 80 rows; marker `2026-09-22T12:05:00Z`
- `2026-09-22T12:04:15.711960Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:03:45Z`
- `2026-09-22T12:02:23.379435Z` — **FREQ**: 5761 rows; marker `2026-09-22T12:01:45Z`
- `2026-09-22T12:00:30.733834Z` — **FUELHH**: 20 rows; marker `2026-09-22T12:00:00Z`
- `2026-09-22T12:00:30.733834Z` — **FUELINST**: 80 rows; marker `2026-09-22T12:00:00Z`
- `2026-09-22T12:00:14.474154Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:59:45Z`
