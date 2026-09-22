# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T11:54:40.695495Z`  
Current process started UTC: `2026-09-22T11:50:40.281121Z`  
1-second metadata polls in this process: **233**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2117, 2026-09-22T11:50:40.281131Z)
- `FUELINST|fuelType=OTHER|generation` = **539** (n=2117, 2026-09-22T11:50:40.281131Z)
- `FUELINST|fuelType=PS|generation` = **-10** (n=2117, 2026-09-22T11:50:40.281131Z)
- `FUELINST|fuelType=WIND|generation` = **3482** (n=2117, 2026-09-22T11:50:40.281131Z)
- `IMBALNGC|TOTAL|imbalance` = **-7049** (n=348, 2026-09-22T11:53:36.058034Z)
- `INDDEM|TOTAL|demand` = **-12511** (n=348, 2026-09-22T11:53:36.058034Z)
- `INDGEN|TOTAL|generation` = **14109** (n=348, 2026-09-22T11:53:36.058034Z)
- `MELNGC|TOTAL|margin` = **37032** (n=348, 2026-09-22T11:50:13.119103Z)
- `MID|dataProvider=APXMIDP|price` = **123.37** (n=89, 2026-09-22T11:42:13.045091Z)
- `MID|dataProvider=APXMIDP|volume` = **4764.3** (n=89, 2026-09-22T11:42:13.045091Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=176, 2026-09-22T11:42:13.045091Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=176, 2026-09-22T11:42:13.045091Z)
- `NDF|TOTAL|demand` = **20658** (n=356, 2026-09-22T11:48:05.233540Z)
- `TSDF|TOTAL|demand` = **21158** (n=356, 2026-09-22T11:48:05.233540Z)
- `WINDFOR|TOTAL|generation` = **13007** (n=60, 2026-09-22T10:30:42.618958Z)

## Latest publication events

- `2026-09-22T11:54:23.467779Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:53:45Z`
- `2026-09-22T11:53:36.058034Z` — **INDGEN**: 1440 rows; marker `2026-09-22T11:47:00Z`
- `2026-09-22T11:53:36.058034Z` — **INDDEM**: 1440 rows; marker `2026-09-22T11:47:00Z`
- `2026-09-22T11:53:36.058034Z` — **IMBALNGC**: 1440 rows; marker `2026-09-22T11:47:00Z`
- `2026-09-22T11:52:16.182691Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:51:45Z`
- `2026-09-22T11:50:40.281131Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:50:00Z`
- `2026-09-22T11:50:13.119103Z` — **MELNGC**: 1440 rows; marker `2026-09-22T11:47:00Z`
- `2026-09-22T11:50:13.119103Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:49:45Z`
- `2026-09-22T11:48:20.970262Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:47:45Z`
- `2026-09-22T11:48:05.233540Z` — **TSDF**: 1440 rows; marker `2026-09-22T11:47:00Z`
- `2026-09-22T11:48:05.233540Z` — **NDF**: 80 rows; marker `2026-09-22T11:47:00Z`
- `2026-09-22T11:46:13.026682Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:45:45Z`
- `2026-09-22T11:45:24.596936Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:45:00Z`
- `2026-09-22T11:44:20.793591Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:43:45Z`
- `2026-09-22T11:42:13.045091Z` — **MID**: 2 rows; marker `2026-09-22T11:42:03Z`
