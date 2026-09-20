# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T10:41:06.946516Z`  
Current process started UTC: `2026-09-20T10:37:05.648647Z`  
1-second metadata polls in this process: **178**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1530, 2026-09-20T10:40:37.170307Z)
- `FUELINST|fuelType=NPSHYD|generation` = **271** (n=1530, 2026-09-20T10:40:37.170307Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1530, 2026-09-20T10:40:37.170307Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1530, 2026-09-20T10:40:37.170307Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1530, 2026-09-20T10:40:37.170307Z)
- `FUELINST|fuelType=OTHER|generation` = **550** (n=1530, 2026-09-20T10:40:37.170307Z)
- `FUELINST|fuelType=PS|generation` = **-927** (n=1530, 2026-09-20T10:40:37.170307Z)
- `FUELINST|fuelType=WIND|generation` = **13927** (n=1530, 2026-09-20T10:40:37.170307Z)
- `IMBALNGC|TOTAL|imbalance` = **-4140** (n=251, 2026-09-20T10:19:35.299200Z)
- `INDDEM|TOTAL|demand` = **-12466** (n=251, 2026-09-20T10:19:35.299200Z)
- `INDGEN|TOTAL|generation` = **16026** (n=251, 2026-09-20T10:19:35.299200Z)
- `MELNGC|TOTAL|margin` = **39778** (n=251, 2026-09-20T10:19:19.340337Z)
- `NDF|TOTAL|demand` = **19666** (n=257, 2026-09-20T10:17:11.038096Z)
- `TSDF|TOTAL|demand` = **20166** (n=257, 2026-09-20T10:17:11.038096Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T10:41:05.616753Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:41:04.320185Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:41:02.986715Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:41:01.684880Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:41:00.363441Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:40:59.044829Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:40:57.762591Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:40:56.476807Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:40:55.174348Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:40:53.568321Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:40:52.312940Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:40:50.976221Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:40:49.692850Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:40:48.416454Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:40:47.120307Z` — **MID**: 0 rows; marker `2026-09-20T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
