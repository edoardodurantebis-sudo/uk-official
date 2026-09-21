# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T02:18:29.666961Z`  
Current process started UTC: `2026-09-21T02:14:29.008902Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1717, 2026-09-21T02:15:32.435766Z)
- `FUELINST|fuelType=OTHER|generation` = **95** (n=1717, 2026-09-21T02:15:32.435766Z)
- `FUELINST|fuelType=PS|generation` = **-131** (n=1717, 2026-09-21T02:15:32.435766Z)
- `FUELINST|fuelType=WIND|generation` = **3963** (n=1717, 2026-09-21T02:15:32.435766Z)
- `IMBALNGC|TOTAL|imbalance` = **-4899** (n=282, 2026-09-21T01:50:40.930054Z)
- `INDDEM|TOTAL|demand` = **-11828** (n=282, 2026-09-21T01:50:40.930054Z)
- `INDGEN|TOTAL|generation` = **15711** (n=282, 2026-09-21T01:50:40.930054Z)
- `MELNGC|TOTAL|margin` = **35830** (n=282, 2026-09-21T01:49:21.112247Z)
- `MID|dataProvider=APXMIDP|price` = **148.62** (n=22, 2026-09-21T02:12:10.973392Z)
- `MID|dataProvider=APXMIDP|volume` = **2271.3** (n=22, 2026-09-21T02:12:10.973392Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=44, 2026-09-21T02:12:10.973392Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=44, 2026-09-21T02:12:10.973392Z)
- `NDF|TOTAL|demand` = **20110** (n=289, 2026-09-21T02:17:23.986288Z)
- `TSDF|TOTAL|demand` = **20610** (n=289, 2026-09-21T02:17:23.986288Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T02:18:28.202490Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:17:45Z`
- `2026-09-21T02:17:23.986288Z` — **TSDF**: 918 rows; marker `2026-09-21T02:16:00Z`
- `2026-09-21T02:17:23.986288Z` — **NDF**: 51 rows; marker `2026-09-21T02:16:00Z`
- `2026-09-21T02:16:20.496788Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:15:45Z`
- `2026-09-21T02:15:32.435766Z` — **FUELINST**: 80 rows; marker `2026-09-21T02:15:00Z`
- `2026-09-21T02:14:29.008912Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:13:45Z`
- `2026-09-21T02:12:27.150010Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:11:45Z`
- `2026-09-21T02:12:10.973392Z` — **MID**: 2 rows; marker `2026-09-21T02:12:03Z`
- `2026-09-21T02:10:35.641803Z` — **FUELINST**: 80 rows; marker `2026-09-21T02:10:00Z`
- `2026-09-21T02:10:19.511240Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:09:45Z`
- `2026-09-21T02:08:12.249012Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:07:45Z`
- `2026-09-21T02:06:36.060462Z` — **MID**: 1 rows; marker `2026-09-21T02:05:00Z`
- `2026-09-21T02:06:20.657986Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:05:45Z`
- `2026-09-21T02:05:26.654484Z` — **FUELINST**: 80 rows; marker `2026-09-21T02:05:00Z`
- `2026-09-21T02:04:07.136498Z` — **FREQ**: 5761 rows; marker `2026-09-21T02:03:45Z`
