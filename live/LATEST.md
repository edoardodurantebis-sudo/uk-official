# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T09:46:43.410682Z`  
Current process started UTC: `2026-09-22T09:42:43.558810Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2092, 2026-09-22T09:45:25.285483Z)
- `FUELINST|fuelType=OTHER|generation` = **476** (n=2092, 2026-09-22T09:45:25.285483Z)
- `FUELINST|fuelType=PS|generation` = **-170** (n=2092, 2026-09-22T09:45:25.285483Z)
- `FUELINST|fuelType=WIND|generation` = **3718** (n=2092, 2026-09-22T09:45:25.285483Z)
- `IMBALNGC|TOTAL|imbalance` = **2430** (n=343, 2026-09-22T09:19:17.697388Z)
- `INDDEM|TOTAL|demand` = **-12801** (n=343, 2026-09-22T09:19:01.822080Z)
- `INDGEN|TOTAL|generation` = **23498** (n=343, 2026-09-22T09:19:01.822080Z)
- `MELNGC|TOTAL|margin` = **40334** (n=343, 2026-09-22T09:18:29.864815Z)
- `MID|dataProvider=APXMIDP|price` = **129.11** (n=85, 2026-09-22T09:42:13.470430Z)
- `MID|dataProvider=APXMIDP|volume` = **3364.7** (n=85, 2026-09-22T09:42:13.470430Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=168, 2026-09-22T09:42:13.470430Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=168, 2026-09-22T09:42:13.470430Z)
- `NDF|TOTAL|demand` = **20320** (n=351, 2026-09-22T09:16:54.603659Z)
- `TSDF|TOTAL|demand` = **21068** (n=351, 2026-09-22T09:16:54.603659Z)
- `WINDFOR|TOTAL|generation` = **12393** (n=59, 2026-09-22T08:31:02.929426Z)

## Latest publication events

- `2026-09-22T09:46:13.639595Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:45:45Z`
- `2026-09-22T09:45:25.285483Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:45:00Z`
- `2026-09-22T09:44:05.569092Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:43:45Z`
- `2026-09-22T09:42:13.470430Z` — **MID**: 2 rows; marker `2026-09-22T09:42:03Z`
- `2026-09-22T09:42:13.470430Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:41:45Z`
- `2026-09-22T09:40:22.196288Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:40:00Z`
- `2026-09-22T09:40:06.181767Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:39:45Z`
- `2026-09-22T09:38:30.003158Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:37:45Z`
- `2026-09-22T09:36:25.311291Z` — **MID**: 1 rows; marker `2026-09-22T09:35:00Z`
- `2026-09-22T09:36:09.910741Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:35:45Z`
- `2026-09-22T09:35:21.728070Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:35:00Z`
- `2026-09-22T09:34:18.140132Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:33:45Z`
- `2026-09-22T09:32:30.300160Z` — **FREQ**: 5761 rows; marker `2026-09-22T09:31:45Z`
- `2026-09-22T09:30:38.288528Z` — **FUELHH**: 20 rows; marker `2026-09-22T09:30:00Z`
- `2026-09-22T09:30:38.288528Z` — **FUELINST**: 80 rows; marker `2026-09-22T09:30:00Z`
