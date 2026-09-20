# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T07:39:23.527525Z`  
Current process started UTC: `2026-09-20T07:35:23.477746Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1262** (n=1493, 2026-09-20T07:35:25.494464Z)
- `FUELINST|fuelType=NPSHYD|generation` = **351** (n=1493, 2026-09-20T07:35:25.494464Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1493, 2026-09-20T07:35:25.494464Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1493, 2026-09-20T07:35:25.494464Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1493, 2026-09-20T07:35:25.494464Z)
- `FUELINST|fuelType=OTHER|generation` = **423** (n=1493, 2026-09-20T07:35:25.494464Z)
- `FUELINST|fuelType=PS|generation` = **-927** (n=1493, 2026-09-20T07:35:25.494464Z)
- `FUELINST|fuelType=WIND|generation` = **15653** (n=1493, 2026-09-20T07:35:25.494464Z)
- `IMBALNGC|TOTAL|imbalance` = **-6364** (n=246, 2026-09-20T07:20:39.619957Z)
- `INDDEM|TOTAL|demand` = **-12307** (n=246, 2026-09-20T07:20:39.619957Z)
- `INDGEN|TOTAL|generation` = **13588** (n=246, 2026-09-20T07:20:39.619957Z)
- `MELNGC|TOTAL|margin` = **38029** (n=246, 2026-09-20T07:19:35.864933Z)
- `NDF|TOTAL|demand` = **19452** (n=251, 2026-09-20T07:17:28.599471Z)
- `TSDF|TOTAL|demand` = **19952** (n=251, 2026-09-20T07:17:28.599471Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T07:39:22.574192Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:21.574076Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:20.573966Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:19.573849Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:18.573727Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:17.573617Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:16.573498Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:15.573417Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:14.573285Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:13.541409Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:12.541281Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:11.541165Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:10.297400Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:09.297330Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:39:08.297197Z` — **MID**: 0 rows; marker `2026-09-20T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
