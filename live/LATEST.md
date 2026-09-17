# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T20:51:32.554843Z`  
Current process started UTC: `2026-09-17T20:47:31.621816Z`  
1-second metadata polls in this process: **167**  
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

- `FUELINST|fuelType=INTVKL|generation` = **728** (n=832, 2026-09-17T20:50:46.750094Z)
- `FUELINST|fuelType=NPSHYD|generation` = **561** (n=832, 2026-09-17T20:50:46.750094Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=832, 2026-09-17T20:50:46.750094Z)
- `FUELINST|fuelType=OCGT|generation` = **37** (n=832, 2026-09-17T20:50:46.750094Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=832, 2026-09-17T20:50:46.750094Z)
- `FUELINST|fuelType=OTHER|generation` = **308** (n=832, 2026-09-17T20:50:46.750094Z)
- `FUELINST|fuelType=PS|generation` = **355** (n=832, 2026-09-17T20:50:46.750094Z)
- `FUELINST|fuelType=WIND|generation` = **15248** (n=832, 2026-09-17T20:50:46.750094Z)
- `IMBALNGC|TOTAL|imbalance` = **9686** (n=137, 2026-09-17T20:23:01.759732Z)
- `INDDEM|TOTAL|demand` = **-11161** (n=137, 2026-09-17T20:22:29.150648Z)
- `INDGEN|TOTAL|generation` = **26500** (n=137, 2026-09-17T20:22:29.150648Z)
- `MELNGC|TOTAL|margin` = **36461** (n=138, 2026-09-17T20:50:14.374453Z)
- `NDF|TOTAL|demand` = **16314** (n=141, 2026-09-17T20:47:47.507721Z)
- `TSDF|TOTAL|demand` = **16814** (n=141, 2026-09-17T20:47:47.507721Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T20:51:31.181601Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:29.852833Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:28.482167Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:27.189475Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:25.811865Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:24.543853Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:23.220000Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:21.861305Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:19.895162Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:18.542311Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:17.225947Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:15.859927Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:14.518656Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:13.203606Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:51:11.906113Z` — **MID**: 0 rows; marker `2026-09-17T20:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
