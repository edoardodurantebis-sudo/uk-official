# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T09:24:18.811113Z`  
Current process started UTC: `2026-09-20T09:20:18.610220Z`  
1-second metadata polls in this process: **189**  
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

- `FUELINST|fuelType=INTVKL|generation` = **436** (n=1514, 2026-09-20T09:20:18.610230Z)
- `FUELINST|fuelType=NPSHYD|generation` = **272** (n=1514, 2026-09-20T09:20:18.610230Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1514, 2026-09-20T09:20:18.610230Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1514, 2026-09-20T09:20:18.610230Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1514, 2026-09-20T09:20:18.610230Z)
- `FUELINST|fuelType=OTHER|generation` = **589** (n=1514, 2026-09-20T09:20:18.610230Z)
- `FUELINST|fuelType=PS|generation` = **-932** (n=1514, 2026-09-20T09:20:18.610230Z)
- `FUELINST|fuelType=WIND|generation` = **14949** (n=1514, 2026-09-20T09:20:18.610230Z)
- `IMBALNGC|TOTAL|imbalance` = **-4187** (n=249, 2026-09-20T09:19:38.522404Z)
- `INDDEM|TOTAL|demand` = **-12376** (n=249, 2026-09-20T09:19:38.522404Z)
- `INDGEN|TOTAL|generation` = **15979** (n=249, 2026-09-20T09:19:38.522404Z)
- `MELNGC|TOTAL|margin` = **38889** (n=249, 2026-09-20T09:18:50.964137Z)
- `NDF|TOTAL|demand` = **19666** (n=255, 2026-09-20T09:17:13.268530Z)
- `TSDF|TOTAL|demand` = **20166** (n=255, 2026-09-20T09:17:13.268530Z)
- `WINDFOR|TOTAL|generation` = **2453** (n=43, 2026-09-20T08:30:44.975647Z)

## Latest publication events

- `2026-09-20T09:24:17.599241Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:16.404565Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:15.193391Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:13.975864Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:12.744839Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:11.530936Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:10.334304Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:09.169418Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:07.958367Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:04.633337Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:04.633337Z` — **FREQ**: 5761 rows; marker `2026-09-20T09:23:45Z`
- `2026-09-20T09:24:03.425633Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:02.186173Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:24:00.962902Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:23:59.720847Z` — **MID**: 0 rows; marker `2026-09-20T09:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
