# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T02:25:01.526484Z`  
Current process started UTC: `2026-09-20T02:21:01.264037Z`  
1-second metadata polls in this process: **198**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-5.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-6.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.08 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-6.17 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-6.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.34 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-7.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.44 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-6.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.63 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **329** (n=1430, 2026-09-20T02:20:18.650388Z)
- `FUELINST|fuelType=NPSHYD|generation` = **308** (n=1430, 2026-09-20T02:20:18.650388Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1430, 2026-09-20T02:20:18.650388Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1430, 2026-09-20T02:20:18.650388Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1430, 2026-09-20T02:20:18.650388Z)
- `FUELINST|fuelType=OTHER|generation` = **200** (n=1430, 2026-09-20T02:20:18.650388Z)
- `FUELINST|fuelType=PS|generation` = **-703** (n=1430, 2026-09-20T02:20:18.650388Z)
- `FUELINST|fuelType=WIND|generation` = **15492** (n=1430, 2026-09-20T02:20:18.650388Z)
- `IMBALNGC|TOTAL|imbalance` = **-3755** (n=236, 2026-09-20T02:21:16.829176Z)
- `INDDEM|TOTAL|demand` = **-12197** (n=236, 2026-09-20T02:21:16.829176Z)
- `INDGEN|TOTAL|generation` = **16197** (n=236, 2026-09-20T02:21:16.829176Z)
- `MELNGC|TOTAL|margin` = **37606** (n=236, 2026-09-20T02:19:46.154039Z)
- `NDF|TOTAL|demand` = **19452** (n=241, 2026-09-20T02:17:36.584473Z)
- `TSDF|TOTAL|demand` = **19952** (n=241, 2026-09-20T02:17:36.584473Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T02:25:00.262550Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:59.100811Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:57.907853Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:56.724210Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:55.552408Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:54.171812Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:52.965095Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:51.800479Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:50.621428Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:49.466234Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:48.293561Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:47.138903Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:45.965874Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:44.813335Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:24:43.613697Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
