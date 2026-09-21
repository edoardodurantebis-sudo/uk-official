# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T01:19:09.573857Z`  
Current process started UTC: `2026-09-21T01:15:09.588157Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1705, 2026-09-21T01:15:25.852486Z)
- `FUELINST|fuelType=OTHER|generation` = **495** (n=1705, 2026-09-21T01:15:25.852486Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1705, 2026-09-21T01:15:25.852486Z)
- `FUELINST|fuelType=WIND|generation` = **4497** (n=1705, 2026-09-21T01:15:25.852486Z)
- `IMBALNGC|TOTAL|imbalance` = **-4908** (n=280, 2026-09-21T00:50:34.008572Z)
- `INDDEM|TOTAL|demand` = **-11839** (n=280, 2026-09-21T00:50:34.008572Z)
- `INDGEN|TOTAL|generation` = **15702** (n=280, 2026-09-21T00:50:34.008572Z)
- `MELNGC|TOTAL|margin` = **35809** (n=280, 2026-09-21T00:49:13.970934Z)
- `MID|dataProvider=APXMIDP|price` = **137.86** (n=20, 2026-09-21T01:12:16.675388Z)
- `MID|dataProvider=APXMIDP|volume` = **2197.7** (n=20, 2026-09-21T01:12:16.675388Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=40, 2026-09-21T01:12:16.675388Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=40, 2026-09-21T01:12:16.675388Z)
- `NDF|TOTAL|demand` = **20110** (n=287, 2026-09-21T01:17:17.780717Z)
- `TSDF|TOTAL|demand` = **20610** (n=287, 2026-09-21T01:17:17.780717Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T01:18:05.514718Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:17:45Z`
- `2026-09-21T01:17:17.780717Z` — **TSDF**: 954 rows; marker `2026-09-21T01:16:00Z`
- `2026-09-21T01:17:17.780717Z` — **NDF**: 53 rows; marker `2026-09-21T01:16:00Z`
- `2026-09-21T01:16:13.991849Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:15:45Z`
- `2026-09-21T01:15:25.852486Z` — **FUELINST**: 80 rows; marker `2026-09-21T01:15:00Z`
- `2026-09-21T01:14:08.111634Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:13:45Z`
- `2026-09-21T01:12:16.675388Z` — **MID**: 2 rows; marker `2026-09-21T01:12:03Z`
- `2026-09-21T01:12:16.675388Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:11:45Z`
- `2026-09-21T01:10:57.227815Z` — **FUELINST**: 80 rows; marker `2026-09-21T01:10:00Z`
- `2026-09-21T01:10:30.163187Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:09:45Z`
- `2026-09-21T01:08:22.482047Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:07:45Z`
- `2026-09-21T01:06:45.458047Z` — **MID**: 1 rows; marker `2026-09-21T01:05:00Z`
- `2026-09-21T01:06:20.810315Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:05:45Z`
- `2026-09-21T01:05:32.084385Z` — **FUELINST**: 80 rows; marker `2026-09-21T01:05:00Z`
- `2026-09-21T01:04:10.757052Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:03:45Z`
