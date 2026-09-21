# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T01:53:20.721769Z`  
Current process started UTC: `2026-09-21T01:49:21.112235Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1712, 2026-09-21T01:50:24.928303Z)
- `FUELINST|fuelType=OTHER|generation` = **125** (n=1712, 2026-09-21T01:50:24.928303Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1712, 2026-09-21T01:50:24.928303Z)
- `FUELINST|fuelType=WIND|generation` = **3927** (n=1712, 2026-09-21T01:50:24.928303Z)
- `IMBALNGC|TOTAL|imbalance` = **-4899** (n=282, 2026-09-21T01:50:40.930054Z)
- `INDDEM|TOTAL|demand` = **-11828** (n=282, 2026-09-21T01:50:40.930054Z)
- `INDGEN|TOTAL|generation` = **15711** (n=282, 2026-09-21T01:50:40.930054Z)
- `MELNGC|TOTAL|margin` = **35830** (n=282, 2026-09-21T01:49:21.112247Z)
- `MID|dataProvider=APXMIDP|price` = **136.55** (n=21, 2026-09-21T01:42:17.205696Z)
- `MID|dataProvider=APXMIDP|volume` = **2153.9** (n=21, 2026-09-21T01:42:17.205696Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=42, 2026-09-21T01:42:17.205696Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=42, 2026-09-21T01:42:17.205696Z)
- `NDF|TOTAL|demand` = **20110** (n=288, 2026-09-21T01:47:19.722935Z)
- `TSDF|TOTAL|demand` = **20610** (n=288, 2026-09-21T01:47:19.722935Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T01:52:16.553476Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:51:45Z`
- `2026-09-21T01:50:40.930054Z` — **INDGEN**: 936 rows; marker `2026-09-21T01:47:00Z`
- `2026-09-21T01:50:40.930054Z` — **INDDEM**: 936 rows; marker `2026-09-21T01:47:00Z`
- `2026-09-21T01:50:40.930054Z` — **IMBALNGC**: 936 rows; marker `2026-09-21T01:47:00Z`
- `2026-09-21T01:50:24.928303Z` — **FUELINST**: 80 rows; marker `2026-09-21T01:50:00Z`
- `2026-09-21T01:50:09.419313Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:49:45Z`
- `2026-09-21T01:49:21.112247Z` — **MELNGC**: 936 rows; marker `2026-09-21T01:47:00Z`
- `2026-09-21T01:48:22.880036Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:47:45Z`
- `2026-09-21T01:47:19.722935Z` — **TSDF**: 936 rows; marker `2026-09-21T01:47:00Z`
- `2026-09-21T01:47:19.722935Z` — **NDF**: 52 rows; marker `2026-09-21T01:47:00Z`
- `2026-09-21T01:46:15.508779Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:45:45Z`
- `2026-09-21T01:45:43.971308Z` — **FUELINST**: 80 rows; marker `2026-09-21T01:45:00Z`
- `2026-09-21T01:44:25.099239Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:43:45Z`
- `2026-09-21T01:42:17.205696Z` — **MID**: 2 rows; marker `2026-09-21T01:42:03Z`
- `2026-09-21T01:42:17.205696Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:41:45Z`
