# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T00:28:47.568463Z`  
Current process started UTC: `2026-09-21T00:24:47.710087Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1695, 2026-09-21T00:25:35.715753Z)
- `FUELINST|fuelType=OTHER|generation` = **103** (n=1695, 2026-09-21T00:25:35.715753Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1695, 2026-09-21T00:25:35.715753Z)
- `FUELINST|fuelType=WIND|generation` = **5073** (n=1695, 2026-09-21T00:25:35.715753Z)
- `IMBALNGC|TOTAL|imbalance` = **-4890** (n=279, 2026-09-21T00:20:52.151209Z)
- `INDDEM|TOTAL|demand` = **-11840** (n=279, 2026-09-21T00:20:52.151209Z)
- `INDGEN|TOTAL|generation` = **15720** (n=279, 2026-09-21T00:20:52.151209Z)
- `MELNGC|TOTAL|margin` = **35784** (n=279, 2026-09-21T00:19:06.302567Z)
- `MID|dataProvider=APXMIDP|price` = **138.2** (n=18, 2026-09-21T00:12:09.501502Z)
- `MID|dataProvider=APXMIDP|volume` = **1990.5** (n=18, 2026-09-21T00:12:09.501502Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=36, 2026-09-21T00:12:09.501502Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=36, 2026-09-21T00:12:09.501502Z)
- `NDF|TOTAL|demand` = **20110** (n=285, 2026-09-21T00:17:29.179731Z)
- `TSDF|TOTAL|demand` = **20610** (n=285, 2026-09-21T00:17:29.179731Z)
- `WINDFOR|TOTAL|generation` = **1603** (n=48, 2026-09-20T23:30:37.519891Z)

## Latest publication events

- `2026-09-21T00:28:15.913142Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:27:45Z`
- `2026-09-21T00:26:23.182192Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:25:45Z`
- `2026-09-21T00:25:35.715753Z` — **FUELINST**: 80 rows; marker `2026-09-21T00:25:00Z`
- `2026-09-21T00:24:20.300738Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:23:45Z`
- `2026-09-21T00:22:12.107526Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:21:45Z`
- `2026-09-21T00:20:52.151209Z` — **INDGEN**: 990 rows; marker `2026-09-21T00:17:00Z`
- `2026-09-21T00:20:52.151209Z` — **INDDEM**: 990 rows; marker `2026-09-21T00:17:00Z`
- `2026-09-21T00:20:52.151209Z` — **IMBALNGC**: 990 rows; marker `2026-09-21T00:17:00Z`
- `2026-09-21T00:20:35.366916Z` — **FUELINST**: 80 rows; marker `2026-09-21T00:20:00Z`
- `2026-09-21T00:20:35.366916Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:19:45Z`
- `2026-09-21T00:19:06.302567Z` — **MELNGC**: 990 rows; marker `2026-09-21T00:17:00Z`
- `2026-09-21T00:18:18.189939Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:17:45Z`
- `2026-09-21T00:17:29.179731Z` — **TSDF**: 990 rows; marker `2026-09-21T00:17:00Z`
- `2026-09-21T00:17:29.179731Z` — **NDF**: 55 rows; marker `2026-09-21T00:17:00Z`
- `2026-09-21T00:16:08.964776Z` — **FREQ**: 5761 rows; marker `2026-09-21T00:15:45Z`
