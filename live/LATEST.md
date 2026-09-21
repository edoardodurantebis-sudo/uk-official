# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T02:10:04.980982Z`  
Current process started UTC: `2026-09-21T02:06:04.656119Z`  
1-second metadata polls in this process: **240**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=994, delta=146, z=3.51 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2793, delta=365, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2736, delta=-158, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2894, delta=-83, z=3.94 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2977, delta=12, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2965, delta=268, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2697, delta=209, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2791, delta=35, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=2756, delta=187, z=3.80 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=938, delta=-6, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=0, z=3.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=946, delta=-1, z=3.57 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=947, delta=3, z=3.59 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1715, 2026-09-21T02:05:26.654484Z)
- `FUELINST|fuelType=OTHER|generation` = **108** (n=1715, 2026-09-21T02:05:26.654484Z)
- `FUELINST|fuelType=PS|generation` = **-71** (n=1715, 2026-09-21T02:05:26.654484Z)
- `FUELINST|fuelType=WIND|generation` = **3872** (n=1715, 2026-09-21T02:05:26.654484Z)
- `IMBALNGC|TOTAL|imbalance` = **-4899** (n=282, 2026-09-21T01:50:40.930054Z)
- `INDDEM|TOTAL|demand` = **-11828** (n=282, 2026-09-21T01:50:40.930054Z)
- `INDGEN|TOTAL|generation` = **15711** (n=282, 2026-09-21T01:50:40.930054Z)
- `MELNGC|TOTAL|margin` = **35830** (n=282, 2026-09-21T01:49:21.112247Z)
- `MID|dataProvider=APXMIDP|price` = **136.55** (n=21, 2026-09-21T01:42:17.205696Z)
- `MID|dataProvider=APXMIDP|volume` = **2153.9** (n=21, 2026-09-21T01:42:17.205696Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=43, 2026-09-21T02:06:36.060462Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=43, 2026-09-21T02:06:36.060462Z)
- `NDF|TOTAL|demand` = **20110** (n=288, 2026-09-21T01:47:19.722935Z)
- `TSDF|TOTAL|demand` = **20610** (n=288, 2026-09-21T01:47:19.722935Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T02:08:12.249012Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:07:45Z`
- `2026-09-21T02:06:36.060462Z` — **MID**: 1 rows; marker `2026-09-21T02:05:00Z`
- `2026-09-21T02:06:20.657986Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:05:45Z`
- `2026-09-21T02:05:26.654484Z` — **FUELINST**: 80 rows; marker `2026-09-21T02:05:00Z`
- `2026-09-21T02:04:07.136498Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:03:45Z`
- `2026-09-21T02:02:14.365833Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:01:45Z`
- `2026-09-21T02:00:22.050798Z` — **FUELHH**: 20 rows; marker `2026-09-21T02:00:00Z`
- `2026-09-21T02:00:22.050798Z` — **FUELINST**: 80 rows; marker `2026-09-21T02:00:00Z`
- `2026-09-21T02:00:06.111786Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:59:45Z`
- `2026-09-21T01:58:14.167354Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:57:45Z`
- `2026-09-21T01:56:15.916216Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:55:45Z`
- `2026-09-21T01:55:43.628940Z` — **FUELINST**: 80 rows; marker `2026-09-21T01:55:00Z`
- `2026-09-21T01:54:07.497702Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:53:45Z`
- `2026-09-21T01:52:16.553476Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:51:45Z`
- `2026-09-21T01:50:40.930054Z` — **INDGEN**: 936 rows; marker `2026-09-21T01:47:00Z`
