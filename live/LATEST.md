# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T21:19:38.386071Z`  
Current process started UTC: `2026-09-20T21:15:38.528148Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1657, 2026-09-20T21:15:38.528155Z)
- `FUELINST|fuelType=OTHER|generation` = **96** (n=1657, 2026-09-20T21:15:38.528155Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=1657, 2026-09-20T21:15:38.528155Z)
- `FUELINST|fuelType=WIND|generation` = **6593** (n=1657, 2026-09-20T21:15:38.528155Z)
- `IMBALNGC|TOTAL|imbalance` = **-5405** (n=272, 2026-09-20T20:52:02.810373Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=272, 2026-09-20T20:52:02.810373Z)
- `INDGEN|TOTAL|generation` = **15205** (n=272, 2026-09-20T20:52:02.810373Z)
- `MELNGC|TOTAL|margin` = **35539** (n=272, 2026-09-20T20:49:45.480150Z)
- `MID|dataProvider=APXMIDP|price` = **180.27** (n=12, 2026-09-20T21:12:13.914062Z)
- `MID|dataProvider=APXMIDP|volume` = **2355.1** (n=12, 2026-09-20T21:12:13.914062Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=24, 2026-09-20T21:12:13.914062Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=24, 2026-09-20T21:12:13.914062Z)
- `NDF|TOTAL|demand` = **20110** (n=279, 2026-09-20T21:17:48.121775Z)
- `TSDF|TOTAL|demand` = **20610** (n=279, 2026-09-20T21:17:48.121775Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T21:18:21.616962Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:17:45Z`
- `2026-09-20T21:17:48.121775Z` — **TSDF**: 1098 rows; marker `2026-09-20T21:17:00Z`
- `2026-09-20T21:17:48.121775Z` — **NDF**: 61 rows; marker `2026-09-20T21:17:00Z`
- `2026-09-20T21:16:10.723873Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:15:45Z`
- `2026-09-20T21:15:38.528155Z` — **FUELINST**: 80 rows; marker `2026-09-20T21:15:00Z`
- `2026-09-20T21:14:21.586557Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:13:45Z`
- `2026-09-20T21:12:13.914062Z` — **MID**: 2 rows; marker `2026-09-20T21:12:02Z`
- `2026-09-20T21:12:13.914062Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:11:45Z`
- `2026-09-20T21:10:30.574034Z` — **FUELINST**: 80 rows; marker `2026-09-20T21:10:00Z`
- `2026-09-20T21:10:14.641479Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:09:45Z`
- `2026-09-20T21:08:21.312940Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:07:45Z`
- `2026-09-20T21:07:48.779168Z` — **MID**: 1 rows; marker `2026-09-20T21:05:00Z`
- `2026-09-20T21:06:13.508386Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:05:45Z`
- `2026-09-20T21:05:40.771740Z` — **FUELINST**: 80 rows; marker `2026-09-20T21:05:00Z`
- `2026-09-20T21:04:05.260097Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:03:45Z`
