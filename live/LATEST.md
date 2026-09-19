# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T15:28:20.736821Z`  
Current process started UTC: `2026-09-19T15:24:20.408769Z`  
1-second metadata polls in this process: **228**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-92, delta=10, z=-8.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-31, delta=73, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.20 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-102, delta=-202, z=-12.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=-15, z=-11.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-89, delta=-179, z=-10.03 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=100, delta=26, z=19.67 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **702** (n=1299, 2026-09-19T15:25:41.581336Z)
- `FUELINST|fuelType=NPSHYD|generation` = **308** (n=1299, 2026-09-19T15:25:41.581336Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=1299, 2026-09-19T15:25:41.581336Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1299, 2026-09-19T15:25:41.581336Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1299, 2026-09-19T15:25:41.581336Z)
- `FUELINST|fuelType=OTHER|generation` = **1252** (n=1299, 2026-09-19T15:25:41.581336Z)
- `FUELINST|fuelType=PS|generation` = **-438** (n=1299, 2026-09-19T15:25:41.581336Z)
- `FUELINST|fuelType=WIND|generation` = **14136** (n=1299, 2026-09-19T15:25:41.581336Z)
- `IMBALNGC|TOTAL|imbalance` = **-3172** (n=214, 2026-09-19T15:25:41.581336Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=214, 2026-09-19T15:25:25.854929Z)
- `INDGEN|TOTAL|generation` = **16780** (n=214, 2026-09-19T15:25:25.854929Z)
- `MELNGC|TOTAL|margin` = **37039** (n=214, 2026-09-19T15:22:01.787811Z)
- `NDF|TOTAL|demand` = **19452** (n=219, 2026-09-19T15:19:13.284533Z)
- `TSDF|TOTAL|demand` = **19952** (n=219, 2026-09-19T15:19:13.284533Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T15:28:19.789762Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:18.789633Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:17.789536Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:16.789431Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:15.787029Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:14.786911Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:13.786790Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:12.786667Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:11.786551Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:10.786443Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:09.786334Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:08.786226Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:07.786088Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:05.514790Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:28:05.514790Z` — **FREQ**: 5761 rows; marker `2026-09-19T15:27:45Z`
