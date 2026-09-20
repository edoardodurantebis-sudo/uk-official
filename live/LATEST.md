# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T07:26:42.913855Z`  
Current process started UTC: `2026-09-20T07:22:42.604358Z`  
1-second metadata polls in this process: **234**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1262** (n=1491, 2026-09-20T07:25:41.583499Z)
- `FUELINST|fuelType=NPSHYD|generation` = **350** (n=1491, 2026-09-20T07:25:41.583499Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3340** (n=1491, 2026-09-20T07:25:41.583499Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1491, 2026-09-20T07:25:41.583499Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1491, 2026-09-20T07:25:41.583499Z)
- `FUELINST|fuelType=OTHER|generation` = **419** (n=1491, 2026-09-20T07:25:41.583499Z)
- `FUELINST|fuelType=PS|generation` = **-805** (n=1491, 2026-09-20T07:25:41.583499Z)
- `FUELINST|fuelType=WIND|generation` = **15670** (n=1491, 2026-09-20T07:25:41.583499Z)
- `IMBALNGC|TOTAL|imbalance` = **-6364** (n=246, 2026-09-20T07:20:39.619957Z)
- `INDDEM|TOTAL|demand` = **-12307** (n=246, 2026-09-20T07:20:39.619957Z)
- `INDGEN|TOTAL|generation` = **13588** (n=246, 2026-09-20T07:20:39.619957Z)
- `MELNGC|TOTAL|margin` = **38029** (n=246, 2026-09-20T07:19:35.864933Z)
- `NDF|TOTAL|demand` = **19452** (n=251, 2026-09-20T07:17:28.599471Z)
- `TSDF|TOTAL|demand` = **19952** (n=251, 2026-09-20T07:17:28.599471Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T07:26:41.934763Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:40.934695Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:39.934580Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:38.934505Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:37.934424Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:36.934306Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:35.934184Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:34.934065Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:33.933986Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:32.930408Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:31.930288Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:29.634266Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:29.634266Z` — **FREQ**: 5761 rows; marker `2026-09-20T07:25:45Z`
- `2026-09-20T07:26:28.634131Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:26:27.634049Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
