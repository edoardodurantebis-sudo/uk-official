# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T11:46:14.925666Z`  
Current process started UTC: `2026-09-22T11:42:13.045084Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2116, 2026-09-22T11:45:24.596936Z)
- `FUELINST|fuelType=OTHER|generation` = **535** (n=2116, 2026-09-22T11:45:24.596936Z)
- `FUELINST|fuelType=PS|generation` = **-7** (n=2116, 2026-09-22T11:45:24.596936Z)
- `FUELINST|fuelType=WIND|generation` = **3551** (n=2116, 2026-09-22T11:45:24.596936Z)
- `IMBALNGC|TOTAL|imbalance` = **-6224** (n=347, 2026-09-22T11:23:24.230167Z)
- `INDDEM|TOTAL|demand` = **-12511** (n=347, 2026-09-22T11:23:24.230167Z)
- `INDGEN|TOTAL|generation` = **14934** (n=347, 2026-09-22T11:23:07.676153Z)
- `MELNGC|TOTAL|margin` = **37032** (n=347, 2026-09-22T11:20:43.853741Z)
- `MID|dataProvider=APXMIDP|price` = **123.37** (n=89, 2026-09-22T11:42:13.045091Z)
- `MID|dataProvider=APXMIDP|volume` = **4764.3** (n=89, 2026-09-22T11:42:13.045091Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=176, 2026-09-22T11:42:13.045091Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=176, 2026-09-22T11:42:13.045091Z)
- `NDF|TOTAL|demand` = **20658** (n=355, 2026-09-22T11:18:03.969802Z)
- `TSDF|TOTAL|demand` = **21158** (n=355, 2026-09-22T11:18:03.969802Z)
- `WINDFOR|TOTAL|generation` = **13007** (n=60, 2026-09-22T10:30:42.618958Z)

## Latest publication events

- `2026-09-22T11:46:13.026682Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:45:45Z`
- `2026-09-22T11:45:24.596936Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:45:00Z`
- `2026-09-22T11:44:20.793591Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:43:45Z`
- `2026-09-22T11:42:13.045091Z` — **MID**: 2 rows; marker `2026-09-22T11:42:03Z`
- `2026-09-22T11:42:13.045091Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:41:45Z`
- `2026-09-22T11:40:34.386333Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:40:00Z`
- `2026-09-22T11:40:17.226953Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:39:45Z`
- `2026-09-22T11:38:09.062801Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:37:45Z`
- `2026-09-22T11:37:25.563734Z` — **MID**: 1 rows; marker `2026-09-22T11:35:00Z`
- `2026-09-22T11:36:06.092894Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:35:45Z`
- `2026-09-22T11:35:18.452559Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:35:00Z`
- `2026-09-22T11:34:14.038660Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:33:45Z`
- `2026-09-22T11:32:06.078860Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:31:45Z`
- `2026-09-22T11:30:46.071801Z` — **FUELHH**: 20 rows; marker `2026-09-22T11:30:00Z`
- `2026-09-22T11:30:46.071801Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:30:00Z`
