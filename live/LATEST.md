# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T21:28:00.770581Z`  
Current process started UTC: `2026-09-20T21:24:01.223574Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1659, 2026-09-20T21:25:26.649290Z)
- `FUELINST|fuelType=OTHER|generation` = **86** (n=1659, 2026-09-20T21:25:26.649290Z)
- `FUELINST|fuelType=PS|generation` = **232** (n=1659, 2026-09-20T21:25:26.649290Z)
- `FUELINST|fuelType=WIND|generation` = **6375** (n=1659, 2026-09-20T21:25:26.649290Z)
- `IMBALNGC|TOTAL|imbalance` = **-5554** (n=273, 2026-09-20T21:21:55.689783Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=273, 2026-09-20T21:21:55.689783Z)
- `INDGEN|TOTAL|generation` = **15056** (n=273, 2026-09-20T21:21:55.689783Z)
- `MELNGC|TOTAL|margin` = **35645** (n=273, 2026-09-20T21:19:49.390584Z)
- `MID|dataProvider=APXMIDP|price` = **180.27** (n=12, 2026-09-20T21:12:13.914062Z)
- `MID|dataProvider=APXMIDP|volume` = **2355.1** (n=12, 2026-09-20T21:12:13.914062Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=24, 2026-09-20T21:12:13.914062Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=24, 2026-09-20T21:12:13.914062Z)
- `NDF|TOTAL|demand` = **20110** (n=279, 2026-09-20T21:17:48.121775Z)
- `TSDF|TOTAL|demand` = **20610** (n=279, 2026-09-20T21:17:48.121775Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T21:26:14.054989Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:25:45Z`
- `2026-09-20T21:25:26.649290Z` — **FUELINST**: 80 rows; marker `2026-09-20T21:25:00Z`
- `2026-09-20T21:24:21.225992Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:23:45Z`
- `2026-09-20T21:22:12.768755Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:21:45Z`
- `2026-09-20T21:21:55.689783Z` — **INDGEN**: 1098 rows; marker `2026-09-20T21:17:00Z`
- `2026-09-20T21:21:55.689783Z` — **INDDEM**: 1098 rows; marker `2026-09-20T21:17:00Z`
- `2026-09-20T21:21:55.689783Z` — **IMBALNGC**: 1098 rows; marker `2026-09-20T21:17:00Z`
- `2026-09-20T21:20:36.487431Z` — **FUELINST**: 80 rows; marker `2026-09-20T21:20:00Z`
- `2026-09-20T21:20:20.794392Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:19:45Z`
- `2026-09-20T21:19:49.390584Z` — **MELNGC**: 1098 rows; marker `2026-09-20T21:17:00Z`
- `2026-09-20T21:18:21.616962Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:17:45Z`
- `2026-09-20T21:17:48.121775Z` — **TSDF**: 1098 rows; marker `2026-09-20T21:17:00Z`
- `2026-09-20T21:17:48.121775Z` — **NDF**: 61 rows; marker `2026-09-20T21:17:00Z`
- `2026-09-20T21:16:10.723873Z` — **FREQ**: 5761 rows; marker `2026-09-20T21:15:45Z`
- `2026-09-20T21:15:38.528155Z` — **FUELINST**: 80 rows; marker `2026-09-20T21:15:00Z`
