# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-21T04:25:21.514637Z`  
Current process started UTC: `2026-09-21T04:21:20.486866Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3376, delta=22, z=4.20 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=OIL|generation` = **0** (n=1742, 2026-09-21T04:20:22.910736Z)
- `FUELINST|fuelType=OTHER|generation` = **259** (n=1742, 2026-09-21T04:20:22.910736Z)
- `FUELINST|fuelType=PS|generation` = **-235** (n=1742, 2026-09-21T04:20:22.910736Z)
- `FUELINST|fuelType=WIND|generation` = **4113** (n=1742, 2026-09-21T04:20:22.910736Z)
- `IMBALNGC|TOTAL|imbalance` = **-3982** (n=287, 2026-09-21T04:20:22.910736Z)
- `INDDEM|TOTAL|demand` = **-11747** (n=287, 2026-09-21T04:20:06.966217Z)
- `INDGEN|TOTAL|generation` = **16628** (n=287, 2026-09-21T04:20:06.966217Z)
- `MELNGC|TOTAL|margin` = **37528** (n=287, 2026-09-21T04:19:01.805874Z)
- `MID|dataProvider=APXMIDP|price` = **151.5** (n=26, 2026-09-21T04:12:12.897424Z)
- `MID|dataProvider=APXMIDP|volume` = **2228** (n=26, 2026-09-21T04:12:12.897424Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=52, 2026-09-21T04:12:12.897424Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=52, 2026-09-21T04:12:12.897424Z)
- `NDF|TOTAL|demand` = **20110** (n=293, 2026-09-21T04:17:10.171117Z)
- `TSDF|TOTAL|demand` = **20610** (n=293, 2026-09-21T04:17:10.171117Z)
- `WINDFOR|TOTAL|generation` = **8021** (n=49, 2026-09-21T03:30:39.847119Z)

## Latest publication events

- `2026-09-21T04:24:16.727436Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:23:45Z`
- `2026-09-21T04:22:24.494127Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:21:45Z`
- `2026-09-21T04:20:22.910736Z` — **IMBALNGC**: 846 rows; marker `2026-09-21T04:16:00Z`
- `2026-09-21T04:20:22.910736Z` — **FUELINST**: 80 rows; marker `2026-09-21T04:20:00Z`
- `2026-09-21T04:20:22.910736Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:19:45Z`
- `2026-09-21T04:20:06.966217Z` — **INDGEN**: 846 rows; marker `2026-09-21T04:16:00Z`
- `2026-09-21T04:20:06.966217Z` — **INDDEM**: 846 rows; marker `2026-09-21T04:16:00Z`
- `2026-09-21T04:19:01.805874Z` — **MELNGC**: 846 rows; marker `2026-09-21T04:16:00Z`
- `2026-09-21T04:18:14.180738Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:17:45Z`
- `2026-09-21T04:17:10.171117Z` — **TSDF**: 846 rows; marker `2026-09-21T04:16:00Z`
- `2026-09-21T04:17:10.171117Z` — **NDF**: 47 rows; marker `2026-09-21T04:16:00Z`
- `2026-09-21T04:16:12.458267Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:15:45Z`
- `2026-09-21T04:15:24.739505Z` — **FUELINST**: 80 rows; marker `2026-09-21T04:15:00Z`
- `2026-09-21T04:14:20.220052Z` — **FREQ**: 5761 rows; marker `2026-09-21T04:13:45Z`
- `2026-09-21T04:12:12.897424Z` — **MID**: 2 rows; marker `2026-09-21T04:12:03Z`
