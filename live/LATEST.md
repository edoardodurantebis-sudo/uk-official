# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T01:49:08.679365Z`  
Current process started UTC: `2026-09-21T01:45:08.966744Z`  
1-second metadata polls in this process: **234**  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1711, 2026-09-21T01:45:43.971308Z)
- `FUELINST|fuelType=OTHER|generation` = **100** (n=1711, 2026-09-21T01:45:43.971308Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1711, 2026-09-21T01:45:43.971308Z)
- `FUELINST|fuelType=WIND|generation` = **3967** (n=1711, 2026-09-21T01:45:43.971308Z)
- `IMBALNGC|TOTAL|imbalance` = **-4906** (n=281, 2026-09-21T01:21:12.562889Z)
- `INDDEM|TOTAL|demand` = **-11829** (n=281, 2026-09-21T01:20:56.801364Z)
- `INDGEN|TOTAL|generation` = **15704** (n=281, 2026-09-21T01:20:56.801364Z)
- `MELNGC|TOTAL|margin` = **35823** (n=281, 2026-09-21T01:19:37.807446Z)
- `MID|dataProvider=APXMIDP|price` = **136.55** (n=21, 2026-09-21T01:42:17.205696Z)
- `MID|dataProvider=APXMIDP|volume` = **2153.9** (n=21, 2026-09-21T01:42:17.205696Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=42, 2026-09-21T01:42:17.205696Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=42, 2026-09-21T01:42:17.205696Z)
- `NDF|TOTAL|demand` = **20110** (n=288, 2026-09-21T01:47:19.722935Z)
- `TSDF|TOTAL|demand` = **20610** (n=288, 2026-09-21T01:47:19.722935Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T01:48:22.880036Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:47:45Z`
- `2026-09-21T01:47:19.722935Z` — **TSDF**: 936 rows; marker `2026-09-21T01:47:00Z`
- `2026-09-21T01:47:19.722935Z` — **NDF**: 52 rows; marker `2026-09-21T01:47:00Z`
- `2026-09-21T01:46:15.508779Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:45:45Z`
- `2026-09-21T01:45:43.971308Z` — **FUELINST**: 80 rows; marker `2026-09-21T01:45:00Z`
- `2026-09-21T01:44:25.099239Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:43:45Z`
- `2026-09-21T01:42:17.205696Z` — **MID**: 2 rows; marker `2026-09-21T01:42:03Z`
- `2026-09-21T01:42:17.205696Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:41:45Z`
- `2026-09-21T01:40:30.521848Z` — **FUELINST**: 80 rows; marker `2026-09-21T01:40:00Z`
- `2026-09-21T01:40:14.495911Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:39:45Z`
- `2026-09-21T01:38:22.645183Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:37:45Z`
- `2026-09-21T01:36:45.956108Z` — **MID**: 1 rows; marker `2026-09-21T01:35:00Z`
- `2026-09-21T01:36:17.453902Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:35:45Z`
- `2026-09-21T01:35:29.141641Z` — **FUELINST**: 80 rows; marker `2026-09-21T01:35:00Z`
- `2026-09-21T01:34:25.483189Z` — **FREQ**: 5761 rows; marker `2026-09-21T01:33:45Z`
