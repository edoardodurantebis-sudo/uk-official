# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-22T11:16:31.122263Z`  
Current process started UTC: `2026-09-22T11:12:31.448637Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=2110, 2026-09-22T11:15:44.798615Z)
- `FUELINST|fuelType=OTHER|generation` = **613** (n=2110, 2026-09-22T11:15:44.798615Z)
- `FUELINST|fuelType=PS|generation` = **-165** (n=2110, 2026-09-22T11:15:44.798615Z)
- `FUELINST|fuelType=WIND|generation` = **3920** (n=2110, 2026-09-22T11:15:44.798615Z)
- `IMBALNGC|TOTAL|imbalance` = **-6230** (n=346, 2026-09-22T10:54:06.744257Z)
- `INDDEM|TOTAL|demand` = **-12511** (n=346, 2026-09-22T10:53:50.439841Z)
- `INDGEN|TOTAL|generation` = **14957** (n=346, 2026-09-22T10:53:33.662824Z)
- `MELNGC|TOTAL|margin` = **37005** (n=346, 2026-09-22T10:50:50.389831Z)
- `MID|dataProvider=APXMIDP|price` = **123.62** (n=88, 2026-09-22T11:12:31.448643Z)
- `MID|dataProvider=APXMIDP|volume` = **4392.8** (n=88, 2026-09-22T11:12:31.448643Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=174, 2026-09-22T11:12:31.448643Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=174, 2026-09-22T11:12:31.448643Z)
- `NDF|TOTAL|demand` = **20687** (n=354, 2026-09-22T10:47:59.302342Z)
- `TSDF|TOTAL|demand` = **21187** (n=354, 2026-09-22T10:48:31.251567Z)
- `WINDFOR|TOTAL|generation` = **13007** (n=60, 2026-09-22T10:30:42.618958Z)

## Latest publication events

- `2026-09-22T11:15:44.798615Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:15:00Z`
- `2026-09-22T11:14:24.252209Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:13:45Z`
- `2026-09-22T11:12:31.448643Z` — **MID**: 2 rows; marker `2026-09-22T11:12:04Z`
- `2026-09-22T11:12:31.448643Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:11:45Z`
- `2026-09-22T11:10:25.974997Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:10:00Z`
- `2026-09-22T11:10:25.974997Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:09:45Z`
- `2026-09-22T11:08:34.540904Z` — **MID**: 1 rows; marker `2026-09-22T11:05:00Z`
- `2026-09-22T11:08:18.201813Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:07:45Z`
- `2026-09-22T11:06:14.878827Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:05:45Z`
- `2026-09-22T11:05:41.118839Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:05:00Z`
- `2026-09-22T11:04:21.617854Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:03:45Z`
- `2026-09-22T11:02:12.211706Z` — **FREQ**: 5761 rows; marker `2026-09-22T11:01:45Z`
- `2026-09-22T11:00:35.600728Z` — **FUELHH**: 20 rows; marker `2026-09-22T11:00:00Z`
- `2026-09-22T11:00:35.600728Z` — **FUELINST**: 80 rows; marker `2026-09-22T11:00:00Z`
- `2026-09-22T11:00:19.714920Z` — **FREQ**: 5761 rows; marker `2026-09-22T10:59:45Z`
