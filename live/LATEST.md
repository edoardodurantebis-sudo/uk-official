# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T11:44:05.613184Z`  
Current process started UTC: `2026-09-20T11:40:05.245846Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1542, 2026-09-20T11:40:36.806586Z)
- `FUELINST|fuelType=NPSHYD|generation` = **286** (n=1542, 2026-09-20T11:40:36.806586Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1542, 2026-09-20T11:40:36.806586Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1542, 2026-09-20T11:40:36.806586Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1542, 2026-09-20T11:40:36.806586Z)
- `FUELINST|fuelType=OTHER|generation` = **490** (n=1542, 2026-09-20T11:40:36.806586Z)
- `FUELINST|fuelType=PS|generation` = **-663** (n=1542, 2026-09-20T11:40:36.806586Z)
- `FUELINST|fuelType=WIND|generation` = **12828** (n=1542, 2026-09-20T11:40:36.806586Z)
- `IMBALNGC|TOTAL|imbalance` = **-5732** (n=253, 2026-09-20T11:24:21.965190Z)
- `INDDEM|TOTAL|demand` = **-11813** (n=253, 2026-09-20T11:23:50.776605Z)
- `INDGEN|TOTAL|generation` = **15372** (n=253, 2026-09-20T11:23:50.776605Z)
- `MELNGC|TOTAL|margin` = **35780** (n=253, 2026-09-20T11:20:39.027170Z)
- `NDF|TOTAL|demand` = **20604** (n=259, 2026-09-20T11:18:08.138348Z)
- `TSDF|TOTAL|demand` = **21104** (n=259, 2026-09-20T11:18:41.045360Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T11:44:04.669297Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:44:03.669170Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:44:02.669035Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:44:01.668978Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:44:00.668847Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:43:59.668720Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:43:58.668602Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:43:57.668490Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:43:56.668370Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:43:55.668246Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:43:54.668179Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:43:53.668094Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:43:52.667973Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:43:51.667844Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:43:50.661507Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
