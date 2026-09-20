# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T12:21:49.764841Z`  
Current process started UTC: `2026-09-20T12:17:48.996581Z`  
1-second metadata polls in this process: **225**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1550, 2026-09-20T12:20:29.957281Z)
- `FUELINST|fuelType=NPSHYD|generation` = **262** (n=1550, 2026-09-20T12:20:29.957281Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1550, 2026-09-20T12:20:29.957281Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1550, 2026-09-20T12:20:29.957281Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1550, 2026-09-20T12:20:29.957281Z)
- `FUELINST|fuelType=OTHER|generation` = **553** (n=1550, 2026-09-20T12:20:29.957281Z)
- `FUELINST|fuelType=PS|generation` = **-676** (n=1550, 2026-09-20T12:20:29.957281Z)
- `FUELINST|fuelType=WIND|generation` = **12668** (n=1550, 2026-09-20T12:20:29.957281Z)
- `IMBALNGC|TOTAL|imbalance` = **-5732** (n=254, 2026-09-20T11:54:11.922528Z)
- `INDDEM|TOTAL|demand` = **-11813** (n=254, 2026-09-20T11:53:56.361979Z)
- `INDGEN|TOTAL|generation` = **15372** (n=254, 2026-09-20T11:53:56.361979Z)
- `MELNGC|TOTAL|margin` = **35780** (n=255, 2026-09-20T12:20:29.957281Z)
- `NDF|TOTAL|demand` = **20604** (n=261, 2026-09-20T12:18:20.759778Z)
- `TSDF|TOTAL|demand` = **21104** (n=261, 2026-09-20T12:18:20.759778Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T12:21:48.414585Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:47.358477Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:46.358356Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:45.155842Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:44.155729Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:43.155618Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:42.155499Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:41.155379Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:40.155272Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:39.155153Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:38.155030Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:37.154908Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:36.154827Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:35.154709Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:21:34.154594Z` — **MID**: 0 rows; marker `2026-09-20T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
