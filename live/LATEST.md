# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T20:16:46.090828Z`  
Current process started UTC: `2026-09-16T20:12:45.798919Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.28 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=692, delta=5, z=3.75 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.97 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **292** (n=568, 2026-09-16T20:15:26.329200Z)
- `FUELINST|fuelType=NPSHYD|generation` = **445** (n=568, 2026-09-16T20:15:26.329200Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3303** (n=568, 2026-09-16T20:15:26.329200Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=568, 2026-09-16T20:15:26.329200Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=568, 2026-09-16T20:15:26.329200Z)
- `FUELINST|fuelType=OTHER|generation` = **724** (n=568, 2026-09-16T20:15:26.329200Z)
- `FUELINST|fuelType=PS|generation` = **360** (n=568, 2026-09-16T20:15:26.329200Z)
- `FUELINST|fuelType=WIND|generation` = **10167** (n=568, 2026-09-16T20:15:26.329200Z)
- `IMBALNGC|TOTAL|imbalance` = **6640** (n=93, 2026-09-16T19:52:04.923339Z)
- `INDDEM|TOTAL|demand` = **-11763** (n=93, 2026-09-16T19:51:48.845809Z)
- `INDGEN|TOTAL|generation` = **25761** (n=93, 2026-09-16T19:51:48.845809Z)
- `MELNGC|TOTAL|margin` = **34409** (n=93, 2026-09-16T19:50:18.787094Z)
- `NDF|TOTAL|demand` = **18621** (n=95, 2026-09-16T19:47:38.979377Z)
- `TSDF|TOTAL|demand` = **19121** (n=95, 2026-09-16T19:47:38.979377Z)
- `WINDFOR|TOTAL|generation` = **19445** (n=16, 2026-09-16T19:30:31.948327Z)

## Latest publication events

- `2026-09-16T20:16:14.091636Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:15:45Z`
- `2026-09-16T20:15:26.329200Z` — **FUELINST**: 80 rows; marker `2026-09-16T20:15:00Z`
- `2026-09-16T20:14:21.961354Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:13:45Z`
- `2026-09-16T20:12:20.994012Z` — **MID**: 0 rows; marker `2026-09-16T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T20:12:20.994012Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:11:45Z`
- `2026-09-16T20:10:28.741211Z` — **FUELINST**: 80 rows; marker `2026-09-16T20:10:00Z`
- `2026-09-16T20:10:12.534392Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:09:45Z`
- `2026-09-16T20:08:20.183721Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:07:45Z`
- `2026-09-16T20:06:28.289834Z` — **MID**: 0 rows; marker `2026-09-16T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T20:06:12.276431Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:05:45Z`
- `2026-09-16T20:05:24.711363Z` — **FUELINST**: 80 rows; marker `2026-09-16T20:05:00Z`
- `2026-09-16T20:04:20.458460Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:03:45Z`
- `2026-09-16T20:02:06.256919Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:01:45Z`
- `2026-09-16T20:00:45.875613Z` — **FUELINST**: 80 rows; marker `2026-09-16T20:00:00Z`
- `2026-09-16T20:00:29.702793Z` — **FUELHH**: 20 rows; marker `2026-09-16T20:00:00Z`
