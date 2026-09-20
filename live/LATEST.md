# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T01:55:42.936831Z`  
Current process started UTC: `2026-09-20T01:51:41.800500Z`  
1-second metadata polls in this process: **133**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-6.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.08 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-6.17 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-6.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.34 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-7.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.44 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-6.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-6.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=1, z=-6.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=3, z=-6.97 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-7.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1016, delta=-2, z=-7.12 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.24 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **651** (n=1425, 2026-09-20T01:55:26.391871Z)
- `FUELINST|fuelType=NPSHYD|generation` = **322** (n=1425, 2026-09-20T01:55:26.391871Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1425, 2026-09-20T01:55:26.391871Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1425, 2026-09-20T01:55:26.391871Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1425, 2026-09-20T01:55:26.391871Z)
- `FUELINST|fuelType=OTHER|generation` = **236** (n=1425, 2026-09-20T01:55:26.391871Z)
- `FUELINST|fuelType=PS|generation` = **-815** (n=1425, 2026-09-20T01:55:26.391871Z)
- `FUELINST|fuelType=WIND|generation` = **15283** (n=1425, 2026-09-20T01:55:26.391871Z)
- `IMBALNGC|TOTAL|imbalance` = **-3757** (n=235, 2026-09-20T01:51:00.792913Z)
- `INDDEM|TOTAL|demand` = **-12197** (n=235, 2026-09-20T01:51:00.792913Z)
- `INDGEN|TOTAL|generation` = **16195** (n=235, 2026-09-20T01:51:00.792913Z)
- `MELNGC|TOTAL|margin` = **36018** (n=235, 2026-09-20T01:49:39.512104Z)
- `NDF|TOTAL|demand` = **19452** (n=240, 2026-09-20T01:47:46.889825Z)
- `TSDF|TOTAL|demand` = **19952** (n=240, 2026-09-20T01:47:46.889825Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T01:55:41.239848Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:39.530736Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:37.835600Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:36.150486Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:34.428657Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:32.743702Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:31.033349Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:29.324408Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:26.391871Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:26.391871Z` — **FUELINST**: 80 rows; marker `2026-09-20T01:55:00Z`
- `2026-09-20T01:55:24.704063Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:22.996714Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:21.300402Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:19.607919Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:55:17.899913Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
