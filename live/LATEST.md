# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T10:15:54.661314Z`  
Current process started UTC: `2026-09-20T10:11:54.202552Z`  
1-second metadata polls in this process: **228**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1525, 2026-09-20T10:15:35.213204Z)
- `FUELINST|fuelType=NPSHYD|generation` = **273** (n=1525, 2026-09-20T10:15:35.213204Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1525, 2026-09-20T10:15:35.213204Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1525, 2026-09-20T10:15:35.213204Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1525, 2026-09-20T10:15:35.213204Z)
- `FUELINST|fuelType=OTHER|generation` = **488** (n=1525, 2026-09-20T10:15:35.213204Z)
- `FUELINST|fuelType=PS|generation` = **-585** (n=1525, 2026-09-20T10:15:35.213204Z)
- `FUELINST|fuelType=WIND|generation` = **13953** (n=1525, 2026-09-20T10:15:35.213204Z)
- `IMBALNGC|TOTAL|imbalance` = **-4154** (n=250, 2026-09-20T09:49:58.854824Z)
- `INDDEM|TOTAL|demand` = **-12359** (n=250, 2026-09-20T09:49:41.948249Z)
- `INDGEN|TOTAL|generation` = **16012** (n=250, 2026-09-20T09:49:41.948249Z)
- `MELNGC|TOTAL|margin` = **39288** (n=250, 2026-09-20T09:49:14.645349Z)
- `NDF|TOTAL|demand` = **19666** (n=256, 2026-09-20T09:47:20.517011Z)
- `TSDF|TOTAL|demand` = **20166** (n=256, 2026-09-20T09:47:20.517011Z)
- `WINDFOR|TOTAL|generation` = **2453** (n=43, 2026-09-20T08:30:44.975647Z)

## Latest publication events

- `2026-09-20T10:15:53.664400Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:52.623602Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:51.374381Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:50.356416Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:49.355716Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:48.328823Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:47.275817Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:46.252030Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:45.219385Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:44.179798Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:43.167597Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:42.160752Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:41.129090Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:40.117268Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:15:39.080889Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
