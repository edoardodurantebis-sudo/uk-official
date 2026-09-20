# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T00:01:48.160172Z`  
Current process started UTC: `2026-09-19T23:57:47.037000Z`  
1-second metadata polls in this process: **133**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-894, delta=-4, z=-9.66 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-897, delta=-5, z=-8.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-892, delta=1, z=-8.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-8.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-8.96 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=1, z=-9.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-894, delta=-1, z=-9.54 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-890, delta=-204, z=-12.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=0, z=-9.86 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=-1, z=-10.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-892, delta=1, z=-10.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-893, delta=-2, z=-11.11 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-891, delta=-12, z=-11.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-879, delta=-185, z=-12.04 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-686, delta=-60, z=-12.25 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **985** (n=1402, 2026-09-20T00:01:00.912120Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=1402, 2026-09-20T00:01:00.912120Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3340** (n=1402, 2026-09-20T00:01:00.912120Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1402, 2026-09-20T00:01:00.912120Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1402, 2026-09-20T00:01:00.912120Z)
- `FUELINST|fuelType=OTHER|generation` = **351** (n=1402, 2026-09-20T00:01:00.912120Z)
- `FUELINST|fuelType=PS|generation` = **-253** (n=1402, 2026-09-20T00:01:00.912120Z)
- `FUELINST|fuelType=WIND|generation` = **16137** (n=1402, 2026-09-20T00:01:00.912120Z)
- `IMBALNGC|TOTAL|imbalance` = **-3708** (n=231, 2026-09-19T23:51:59.807396Z)
- `INDDEM|TOTAL|demand` = **-11889** (n=231, 2026-09-19T23:51:59.807396Z)
- `INDGEN|TOTAL|generation` = **16244** (n=231, 2026-09-19T23:51:59.807396Z)
- `MELNGC|TOTAL|margin` = **35994** (n=231, 2026-09-19T23:49:51.036521Z)
- `NDF|TOTAL|demand` = **19452** (n=236, 2026-09-19T23:47:47.316209Z)
- `TSDF|TOTAL|demand` = **19952** (n=236, 2026-09-19T23:47:47.316209Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T00:01:46.471416Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:44.806608Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:43.048841Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:41.361833Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:39.683462Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:38.005954Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:36.293908Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:33.686077Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:32.003630Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:30.271144Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:28.600829Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:26.906192Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:25.217802Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:23.529940Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T00:01:21.862031Z` — **MID**: 0 rows; marker `2026-09-19T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
