# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T13:17:03.321941Z`  
Current process started UTC: `2026-09-20T13:13:02.543590Z`  
1-second metadata polls in this process: **146**  
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

- `FUELINST|fuelType=INTVKL|generation` = **129** (n=1561, 2026-09-20T13:15:27.676465Z)
- `FUELINST|fuelType=NPSHYD|generation` = **262** (n=1561, 2026-09-20T13:15:27.676465Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1561, 2026-09-20T13:15:27.676465Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1561, 2026-09-20T13:15:27.676465Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1561, 2026-09-20T13:15:27.676465Z)
- `FUELINST|fuelType=OTHER|generation` = **306** (n=1561, 2026-09-20T13:15:27.676465Z)
- `FUELINST|fuelType=PS|generation` = **-675** (n=1561, 2026-09-20T13:15:27.676465Z)
- `FUELINST|fuelType=WIND|generation` = **12077** (n=1561, 2026-09-20T13:15:27.676465Z)
- `IMBALNGC|TOTAL|imbalance` = **-5731** (n=256, 2026-09-20T12:54:13.127676Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=256, 2026-09-20T12:53:56.150495Z)
- `INDGEN|TOTAL|generation` = **15373** (n=256, 2026-09-20T12:53:56.150495Z)
- `MELNGC|TOTAL|margin` = **35771** (n=256, 2026-09-20T12:50:50.610978Z)
- `NDF|TOTAL|demand` = **20604** (n=262, 2026-09-20T12:48:26.154558Z)
- `TSDF|TOTAL|demand` = **21104** (n=262, 2026-09-20T12:48:26.154558Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T13:17:01.708333Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:17:00.167228Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:58.614691Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:57.062977Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:55.544590Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:53.723076Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:52.046054Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:50.217579Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:48.420750Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:46.593525Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:44.163143Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:42.541514Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:40.974672Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:39.457285Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:16:37.872543Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
