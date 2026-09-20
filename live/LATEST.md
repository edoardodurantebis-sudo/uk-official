# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T10:02:41.812478Z`  
Current process started UTC: `2026-09-20T09:58:40.666948Z`  
1-second metadata polls in this process: **152**  
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

- `FUELINST|fuelType=INTVKL|generation` = **329** (n=1522, 2026-09-20T10:00:33.764831Z)
- `FUELINST|fuelType=NPSHYD|generation` = **272** (n=1522, 2026-09-20T10:00:33.764831Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3340** (n=1522, 2026-09-20T10:00:33.764831Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1522, 2026-09-20T10:00:33.764831Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1522, 2026-09-20T10:00:33.764831Z)
- `FUELINST|fuelType=OTHER|generation` = **542** (n=1522, 2026-09-20T10:00:33.764831Z)
- `FUELINST|fuelType=PS|generation` = **-928** (n=1522, 2026-09-20T10:00:33.764831Z)
- `FUELINST|fuelType=WIND|generation` = **14350** (n=1522, 2026-09-20T10:00:33.764831Z)
- `IMBALNGC|TOTAL|imbalance` = **-4154** (n=250, 2026-09-20T09:49:58.854824Z)
- `INDDEM|TOTAL|demand` = **-12359** (n=250, 2026-09-20T09:49:41.948249Z)
- `INDGEN|TOTAL|generation` = **16012** (n=250, 2026-09-20T09:49:41.948249Z)
- `MELNGC|TOTAL|margin` = **39288** (n=250, 2026-09-20T09:49:14.645349Z)
- `NDF|TOTAL|demand` = **19666** (n=256, 2026-09-20T09:47:20.517011Z)
- `TSDF|TOTAL|demand` = **20166** (n=256, 2026-09-20T09:47:20.517011Z)
- `WINDFOR|TOTAL|generation` = **2453** (n=43, 2026-09-20T08:30:44.975647Z)

## Latest publication events

- `2026-09-20T10:02:40.348740Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:38.838246Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:37.363195Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:35.595490Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:33.779405Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:31.907932Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:30.220810Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:26.934429Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:26.934429Z` — **FREQ**: 5761 rows; marker `2026-09-20T10:01:45Z`
- `2026-09-20T10:02:25.482076Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:23.848806Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:22.354940Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:20.652077Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:18.948807Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:02:17.319024Z` — **MID**: 0 rows; marker `2026-09-20T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
