# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T08:29:45.070732Z`  
Current process started UTC: `2026-09-20T08:25:44.224680Z`  
1-second metadata polls in this process: **235**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1196** (n=1503, 2026-09-20T08:25:29.997260Z)
- `FUELINST|fuelType=NPSHYD|generation` = **348** (n=1503, 2026-09-20T08:25:29.997260Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1503, 2026-09-20T08:25:29.997260Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1503, 2026-09-20T08:25:29.997260Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1503, 2026-09-20T08:25:29.997260Z)
- `FUELINST|fuelType=OTHER|generation` = **319** (n=1503, 2026-09-20T08:25:29.997260Z)
- `FUELINST|fuelType=PS|generation` = **-936** (n=1503, 2026-09-20T08:25:29.997260Z)
- `FUELINST|fuelType=WIND|generation` = **14950** (n=1503, 2026-09-20T08:25:29.997260Z)
- `IMBALNGC|TOTAL|imbalance` = **-7048** (n=247, 2026-09-20T08:20:30.547622Z)
- `INDDEM|TOTAL|demand` = **-12309** (n=247, 2026-09-20T08:20:30.547622Z)
- `INDGEN|TOTAL|generation` = **13118** (n=247, 2026-09-20T08:20:30.547622Z)
- `MELNGC|TOTAL|margin` = **37453** (n=247, 2026-09-20T08:19:27.585262Z)
- `NDF|TOTAL|demand` = **19666** (n=253, 2026-09-20T08:17:35.777988Z)
- `TSDF|TOTAL|demand` = **20166** (n=253, 2026-09-20T08:17:35.777988Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T08:29:44.101668Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:43.101541Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:42.101422Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:41.101295Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:40.101207Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:39.101119Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:38.100957Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:37.100855Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:36.088805Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:35.088724Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:34.088613Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:33.088525Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:32.088397Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:31.088264Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T08:29:29.850962Z` — **MID**: 0 rows; marker `2026-09-20T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
