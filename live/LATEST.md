# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T21:04:09.152730Z`  
Current process started UTC: `2026-09-17T21:00:08.013923Z`  
1-second metadata polls in this process: **224**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=80, delta=-38, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=118, delta=27, z=6.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **655** (n=834, 2026-09-17T21:00:24.472385Z)
- `FUELINST|fuelType=NPSHYD|generation` = **561** (n=834, 2026-09-17T21:00:24.472385Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=834, 2026-09-17T21:00:24.472385Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=834, 2026-09-17T21:00:24.472385Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=834, 2026-09-17T21:00:24.472385Z)
- `FUELINST|fuelType=OTHER|generation` = **251** (n=834, 2026-09-17T21:00:24.472385Z)
- `FUELINST|fuelType=PS|generation` = **355** (n=834, 2026-09-17T21:00:24.472385Z)
- `FUELINST|fuelType=WIND|generation` = **15089** (n=834, 2026-09-17T21:00:24.472385Z)
- `IMBALNGC|TOTAL|imbalance` = **9702** (n=138, 2026-09-17T20:52:31.535620Z)
- `INDDEM|TOTAL|demand` = **-11159** (n=138, 2026-09-17T20:52:15.731180Z)
- `INDGEN|TOTAL|generation` = **26516** (n=138, 2026-09-17T20:52:15.731180Z)
- `MELNGC|TOTAL|margin` = **36461** (n=138, 2026-09-17T20:50:14.374453Z)
- `NDF|TOTAL|demand` = **16314** (n=141, 2026-09-17T20:47:47.507721Z)
- `TSDF|TOTAL|demand` = **16814** (n=141, 2026-09-17T20:47:47.507721Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T21:04:06.858309Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:04:06.858309Z` — **FREQ**: 5761 rows; marker `2026-09-17T21:03:45Z`
- `2026-09-17T21:04:05.858239Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:04:04.858117Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:04:03.858008Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:04:02.857874Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:04:01.857759Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:04:00.857648Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:03:59.857539Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:03:58.857425Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:03:57.857309Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:03:56.857194Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:03:55.857077Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:03:54.856956Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:03:53.856840Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
