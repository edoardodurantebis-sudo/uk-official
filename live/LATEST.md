# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T08:50:43.885882Z`  
Current process started UTC: `2026-09-20T08:46:42.638230Z`  
1-second metadata polls in this process: **140**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1196** (n=1508, 2026-09-20T08:50:29.175857Z)
- `FUELINST|fuelType=NPSHYD|generation` = **298** (n=1508, 2026-09-20T08:50:29.175857Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1508, 2026-09-20T08:50:29.175857Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1508, 2026-09-20T08:50:29.175857Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1508, 2026-09-20T08:50:29.175857Z)
- `FUELINST|fuelType=OTHER|generation` = **478** (n=1508, 2026-09-20T08:50:29.175857Z)
- `FUELINST|fuelType=PS|generation` = **-935** (n=1508, 2026-09-20T08:50:29.175857Z)
- `FUELINST|fuelType=WIND|generation` = **14998** (n=1508, 2026-09-20T08:50:29.175857Z)
- `IMBALNGC|TOTAL|imbalance` = **-7095** (n=248, 2026-09-20T08:50:29.175857Z)
- `INDDEM|TOTAL|demand` = **-12299** (n=248, 2026-09-20T08:50:12.768299Z)
- `INDGEN|TOTAL|generation` = **13071** (n=248, 2026-09-20T08:50:12.768299Z)
- `MELNGC|TOTAL|margin` = **37489** (n=248, 2026-09-20T08:49:24.398354Z)
- `NDF|TOTAL|demand` = **19666** (n=254, 2026-09-20T08:47:31.013284Z)
- `TSDF|TOTAL|demand` = **20166** (n=254, 2026-09-20T08:47:31.013284Z)
- `WINDFOR|TOTAL|generation` = **2453** (n=43, 2026-09-20T08:30:44.975647Z)

## Latest publication events

- `2026-09-20T08:50:42.299088Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:40.737468Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:39.065390Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:37.465480Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:35.907948Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:34.310093Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:32.694384Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:29.175857Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:29.175857Z` — **IMBALNGC**: 684 rows; marker `2026-09-20T08:47:00Z`
- `2026-09-20T08:50:29.175857Z` — **FUELINST**: 80 rows; marker `2026-09-20T08:50:00Z`
- `2026-09-20T08:50:27.548165Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:26.028354Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:24.412523Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:22.733725Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:50:21.100168Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
