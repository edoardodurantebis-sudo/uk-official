# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T09:11:43.685076Z`  
Current process started UTC: `2026-09-20T09:07:42.816188Z`  
1-second metadata polls in this process: **181**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-986, delta=2, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-983, delta=3, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.72 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-988, delta=26, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.79 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=2, z=-3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-989, delta=24, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.13 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **437** (n=1512, 2026-09-20T09:10:35.169561Z)
- `FUELINST|fuelType=NPSHYD|generation` = **273** (n=1512, 2026-09-20T09:10:35.169561Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1512, 2026-09-20T09:10:35.169561Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1512, 2026-09-20T09:10:35.169561Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1512, 2026-09-20T09:10:35.169561Z)
- `FUELINST|fuelType=OTHER|generation` = **666** (n=1512, 2026-09-20T09:10:35.169561Z)
- `FUELINST|fuelType=PS|generation` = **-923** (n=1512, 2026-09-20T09:10:35.169561Z)
- `FUELINST|fuelType=WIND|generation` = **14981** (n=1512, 2026-09-20T09:10:35.169561Z)
- `IMBALNGC|TOTAL|imbalance` = **-7095** (n=248, 2026-09-20T08:50:29.175857Z)
- `INDDEM|TOTAL|demand` = **-12299** (n=248, 2026-09-20T08:50:12.768299Z)
- `INDGEN|TOTAL|generation` = **13071** (n=248, 2026-09-20T08:50:12.768299Z)
- `MELNGC|TOTAL|margin` = **37489** (n=248, 2026-09-20T08:49:24.398354Z)
- `NDF|TOTAL|demand` = **19666** (n=254, 2026-09-20T08:47:31.013284Z)
- `TSDF|TOTAL|demand` = **20166** (n=254, 2026-09-20T08:47:31.013284Z)
- `WINDFOR|TOTAL|generation` = **2453** (n=43, 2026-09-20T08:30:44.975647Z)

## Latest publication events

- `2026-09-20T09:11:42.398070Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:41.115895Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:39.580889Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:38.322584Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:36.988383Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:35.635365Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:34.324936Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:33.021136Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:31.794935Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:30.497638Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:29.210358Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:27.929429Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:26.611414Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:25.355290Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:11:23.847583Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
