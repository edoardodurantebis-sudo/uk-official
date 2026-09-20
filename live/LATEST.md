# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T09:07:30.951003Z`  
Current process started UTC: `2026-09-20T09:03:30.327371Z`  
1-second metadata polls in this process: **143**  
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

- `FUELINST|fuelType=INTVKL|generation` = **637** (n=1511, 2026-09-20T09:05:29.277064Z)
- `FUELINST|fuelType=NPSHYD|generation` = **274** (n=1511, 2026-09-20T09:05:29.277064Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1511, 2026-09-20T09:05:29.277064Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1511, 2026-09-20T09:05:29.277064Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1511, 2026-09-20T09:05:29.277064Z)
- `FUELINST|fuelType=OTHER|generation` = **583** (n=1511, 2026-09-20T09:05:29.277064Z)
- `FUELINST|fuelType=PS|generation` = **-919** (n=1511, 2026-09-20T09:05:29.277064Z)
- `FUELINST|fuelType=WIND|generation` = **15019** (n=1511, 2026-09-20T09:05:29.277064Z)
- `IMBALNGC|TOTAL|imbalance` = **-7095** (n=248, 2026-09-20T08:50:29.175857Z)
- `INDDEM|TOTAL|demand` = **-12299** (n=248, 2026-09-20T08:50:12.768299Z)
- `INDGEN|TOTAL|generation` = **13071** (n=248, 2026-09-20T08:50:12.768299Z)
- `MELNGC|TOTAL|margin` = **37489** (n=248, 2026-09-20T08:49:24.398354Z)
- `NDF|TOTAL|demand` = **19666** (n=254, 2026-09-20T08:47:31.013284Z)
- `TSDF|TOTAL|demand` = **20166** (n=254, 2026-09-20T08:47:31.013284Z)
- `WINDFOR|TOTAL|generation` = **2453** (n=43, 2026-09-20T08:30:44.975647Z)

## Latest publication events

- `2026-09-20T09:07:29.299475Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:27.682599Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:26.103839Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:24.476692Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:22.582128Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:21.046282Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:19.341018Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:17.758729Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:16.163388Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:14.519986Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:12.908010Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:11.346979Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:09.785665Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:08.195434Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:07:06.257243Z` — **MID**: 0 rows; marker `2026-09-20T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
