# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T11:03:15.732199Z`  
Current process started UTC: `2026-09-22T10:59:15.705525Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2107, 2026-09-22T11:00:35.600728Z)
- `FUELINST|fuelType=OTHER|generation` = **525** (n=2107, 2026-09-22T11:00:35.600728Z)
- `FUELINST|fuelType=PS|generation` = **-167** (n=2107, 2026-09-22T11:00:35.600728Z)
- `FUELINST|fuelType=WIND|generation` = **3665** (n=2107, 2026-09-22T11:00:35.600728Z)
- `IMBALNGC|TOTAL|imbalance` = **-6230** (n=346, 2026-09-22T10:54:06.744257Z)
- `INDDEM|TOTAL|demand` = **-12511** (n=346, 2026-09-22T10:53:50.439841Z)
- `INDGEN|TOTAL|generation` = **14957** (n=346, 2026-09-22T10:53:33.662824Z)
- `MELNGC|TOTAL|margin` = **37005** (n=346, 2026-09-22T10:50:50.389831Z)
- `MID|dataProvider=APXMIDP|price` = **122.98** (n=87, 2026-09-22T10:42:22.231944Z)
- `MID|dataProvider=APXMIDP|volume` = **3749.5** (n=87, 2026-09-22T10:42:22.231944Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=172, 2026-09-22T10:42:22.231944Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=172, 2026-09-22T10:42:22.231944Z)
- `NDF|TOTAL|demand` = **20687** (n=354, 2026-09-22T10:47:59.302342Z)
- `TSDF|TOTAL|demand` = **21187** (n=354, 2026-09-22T10:48:31.251567Z)
- `WINDFOR|TOTAL|generation` = **13007** (n=60, 2026-09-22T10:30:42.618958Z)

## Latest publication events

- `2026-09-22T11:02:12.211706Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:01:45Z`
- `2026-09-22T11:00:35.600728Z` — **FUELHH**: 20 rows; marker `2026-09-22T11:00:00Z`
- `2026-09-22T11:00:35.600728Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:00:00Z`
- `2026-09-22T11:00:19.714920Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:59:45Z`
- `2026-09-22T10:58:15.887590Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:57:45Z`
- `2026-09-22T10:56:22.952342Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:55:45Z`
- `2026-09-22T10:55:35.379687Z` — **FUELINST**: 80 rows; marker `2026-09-22T10:55:00Z`
- `2026-09-22T10:54:06.744257Z` — **IMBALNGC**: 1476 rows; marker `2026-09-22T10:47:00Z`
- `2026-09-22T10:54:06.744257Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:53:45Z`
- `2026-09-22T10:53:50.439841Z` — **INDDEM**: 1476 rows; marker `2026-09-22T10:47:00Z`
- `2026-09-22T10:53:33.662824Z` — **INDGEN**: 1476 rows; marker `2026-09-22T10:47:00Z`
- `2026-09-22T10:52:11.089045Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:51:45Z`
- `2026-09-22T10:50:50.389831Z` — **MELNGC**: 1476 rows; marker `2026-09-22T10:47:00Z`
- `2026-09-22T10:50:22.764253Z` — **FUELINST**: 80 rows; marker `2026-09-22T10:50:00Z`
- `2026-09-22T10:50:07.219175Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:49:45Z`
