# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T09:03:20.049531Z`  
Current process started UTC: `2026-09-20T08:59:19.651306Z`  
1-second metadata polls in this process: **222**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1011** (n=1510, 2026-09-20T09:00:38.589626Z)
- `FUELINST|fuelType=NPSHYD|generation` = **297** (n=1510, 2026-09-20T09:00:38.589626Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1510, 2026-09-20T09:00:38.589626Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1510, 2026-09-20T09:00:38.589626Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1510, 2026-09-20T09:00:38.589626Z)
- `FUELINST|fuelType=OTHER|generation` = **504** (n=1510, 2026-09-20T09:00:38.589626Z)
- `FUELINST|fuelType=PS|generation` = **-926** (n=1510, 2026-09-20T09:00:38.589626Z)
- `FUELINST|fuelType=WIND|generation` = **14963** (n=1510, 2026-09-20T09:00:38.589626Z)
- `IMBALNGC|TOTAL|imbalance` = **-7095** (n=248, 2026-09-20T08:50:29.175857Z)
- `INDDEM|TOTAL|demand` = **-12299** (n=248, 2026-09-20T08:50:12.768299Z)
- `INDGEN|TOTAL|generation` = **13071** (n=248, 2026-09-20T08:50:12.768299Z)
- `MELNGC|TOTAL|margin` = **37489** (n=248, 2026-09-20T08:49:24.398354Z)
- `NDF|TOTAL|demand` = **19666** (n=254, 2026-09-20T08:47:31.013284Z)
- `TSDF|TOTAL|demand` = **20166** (n=254, 2026-09-20T08:47:31.013284Z)
- `WINDFOR|TOTAL|generation` = **2453** (n=43, 2026-09-20T08:30:44.975647Z)

## Latest publication events

- `2026-09-20T09:03:18.775199Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:17.748539Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:16.730533Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:15.676312Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:14.666027Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:13.665957Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:12.605774Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:11.596552Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:10.574247Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:09.535118Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:08.520171Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:07.510909Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:06.508927Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:05.430245Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T09:03:04.282105Z` — **MID**: 0 rows; marker `2026-09-20T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
