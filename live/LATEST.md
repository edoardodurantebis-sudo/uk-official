# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T10:50:36.867467Z`  
Current process started UTC: `2026-09-22T10:46:37.256432Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2105, 2026-09-22T10:50:22.764253Z)
- `FUELINST|fuelType=OTHER|generation` = **540** (n=2105, 2026-09-22T10:50:22.764253Z)
- `FUELINST|fuelType=PS|generation` = **-167** (n=2105, 2026-09-22T10:50:22.764253Z)
- `FUELINST|fuelType=WIND|generation` = **3487** (n=2105, 2026-09-22T10:50:22.764253Z)
- `IMBALNGC|TOTAL|imbalance` = **5167** (n=345, 2026-09-22T10:19:32.170249Z)
- `INDDEM|TOTAL|demand` = **-13862** (n=345, 2026-09-22T10:19:16.023000Z)
- `INDGEN|TOTAL|generation` = **26115** (n=345, 2026-09-22T10:19:16.023000Z)
- `MELNGC|TOTAL|margin` = **40386** (n=345, 2026-09-22T10:19:00.047508Z)
- `MID|dataProvider=APXMIDP|price` = **122.98** (n=87, 2026-09-22T10:42:22.231944Z)
- `MID|dataProvider=APXMIDP|volume` = **3749.5** (n=87, 2026-09-22T10:42:22.231944Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=172, 2026-09-22T10:42:22.231944Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=172, 2026-09-22T10:42:22.231944Z)
- `NDF|TOTAL|demand` = **20687** (n=354, 2026-09-22T10:47:59.302342Z)
- `TSDF|TOTAL|demand` = **21187** (n=354, 2026-09-22T10:48:31.251567Z)
- `WINDFOR|TOTAL|generation` = **13007** (n=60, 2026-09-22T10:30:42.618958Z)

## Latest publication events

- `2026-09-22T10:50:22.764253Z` — **FUELINST**: 80 rows; marker `2026-09-22T10:50:00Z`
- `2026-09-22T10:50:07.219175Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:49:45Z`
- `2026-09-22T10:48:31.251567Z` — **TSDF**: 1476 rows; marker `2026-09-22T10:47:00Z`
- `2026-09-22T10:48:31.251567Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:47:45Z`
- `2026-09-22T10:47:59.302342Z` — **NDF**: 82 rows; marker `2026-09-22T10:47:00Z`
- `2026-09-22T10:46:07.971250Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:45:45Z`
- `2026-09-22T10:45:19.812940Z` — **FUELINST**: 80 rows; marker `2026-09-22T10:45:00Z`
- `2026-09-22T10:44:14.450696Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:43:45Z`
- `2026-09-22T10:42:22.231944Z` — **MID**: 2 rows; marker `2026-09-22T10:42:03Z`
- `2026-09-22T10:42:22.231944Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:41:45Z`
- `2026-09-22T10:40:30.064746Z` — **FUELINST**: 80 rows; marker `2026-09-22T10:40:00Z`
- `2026-09-22T10:40:14.267597Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:39:45Z`
- `2026-09-22T10:38:06.281694Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:37:45Z`
- `2026-09-22T10:36:18.542032Z` — **MID**: 1 rows; marker `2026-09-22T10:35:00Z`
- `2026-09-22T10:36:02.342292Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:35:45Z`
