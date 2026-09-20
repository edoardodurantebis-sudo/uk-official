# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T20:33:22.812124Z`  
Current process started UTC: `2026-09-20T20:29:23.083836Z`  
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

- `FUELINST|fuelType=OIL|generation` = **0** (n=1648, 2026-09-20T20:30:32.364185Z)
- `FUELINST|fuelType=OTHER|generation` = **384** (n=1648, 2026-09-20T20:30:32.364185Z)
- `FUELINST|fuelType=PS|generation` = **230** (n=1648, 2026-09-20T20:30:32.364185Z)
- `FUELINST|fuelType=WIND|generation` = **6320** (n=1648, 2026-09-20T20:30:32.364185Z)
- `IMBALNGC|TOTAL|imbalance` = **-5360** (n=271, 2026-09-20T20:22:08.658879Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=271, 2026-09-20T20:22:08.658879Z)
- `INDGEN|TOTAL|generation` = **15250** (n=271, 2026-09-20T20:22:08.658879Z)
- `MELNGC|TOTAL|margin` = **35544** (n=271, 2026-09-20T20:20:00.509188Z)
- `MID|dataProvider=APXMIDP|price` = **197.83** (n=10, 2026-09-20T20:12:10.359672Z)
- `MID|dataProvider=APXMIDP|volume` = **2294.3** (n=10, 2026-09-20T20:12:10.359672Z)
- `MID|dataProvider=N2EXMIDP|price` = **0** (n=20, 2026-09-20T20:12:10.359672Z)
- `MID|dataProvider=N2EXMIDP|volume` = **0** (n=20, 2026-09-20T20:12:10.359672Z)
- `NDF|TOTAL|demand` = **20110** (n=277, 2026-09-20T20:18:07.466271Z)
- `TSDF|TOTAL|demand` = **20610** (n=277, 2026-09-20T20:18:07.466271Z)
- `WINDFOR|TOTAL|generation` = **1726** (n=47, 2026-09-20T19:30:32.161891Z)

## Latest publication events

- `2026-09-20T20:32:24.097022Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:31:45Z`
- `2026-09-20T20:30:32.364185Z` — **FUELHH**: 20 rows; marker `2026-09-20T20:30:00Z`
- `2026-09-20T20:30:32.364185Z` — **FUELINST**: 80 rows; marker `2026-09-20T20:30:00Z`
- `2026-09-20T20:30:16.259580Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:29:45Z`
- `2026-09-20T20:28:24.602111Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:27:45Z`
- `2026-09-20T20:26:16.828345Z` — **FUELINST**: 80 rows; marker `2026-09-20T20:25:00Z`
- `2026-09-20T20:26:16.828345Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:25:45Z`
- `2026-09-20T20:24:17.327168Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:23:45Z`
- `2026-09-20T20:22:25.098628Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:21:45Z`
- `2026-09-20T20:22:08.658879Z` — **INDGEN**: 1134 rows; marker `2026-09-20T20:17:00Z`
- `2026-09-20T20:22:08.658879Z` — **INDDEM**: 1134 rows; marker `2026-09-20T20:17:00Z`
- `2026-09-20T20:22:08.658879Z` — **IMBALNGC**: 1134 rows; marker `2026-09-20T20:17:00Z`
- `2026-09-20T20:20:32.671367Z` — **FUELINST**: 80 rows; marker `2026-09-20T20:20:00Z`
- `2026-09-20T20:20:16.514436Z` — **FREQ**: 5761 rows; marker `2026-09-20T20:19:45Z`
- `2026-09-20T20:20:00.509188Z` — **MELNGC**: 1134 rows; marker `2026-09-20T20:17:00Z`
