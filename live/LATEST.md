# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T02:37:39.124613Z`  
Current process started UTC: `2026-09-20T02:33:37.811952Z`  
1-second metadata polls in this process: **149**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-5.46 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-5.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.58 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **329** (n=1433, 2026-09-20T02:35:29.133215Z)
- `FUELINST|fuelType=NPSHYD|generation` = **309** (n=1433, 2026-09-20T02:35:29.133215Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1433, 2026-09-20T02:35:29.133215Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1433, 2026-09-20T02:35:29.133215Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1433, 2026-09-20T02:35:29.133215Z)
- `FUELINST|fuelType=OTHER|generation` = **278** (n=1433, 2026-09-20T02:35:29.133215Z)
- `FUELINST|fuelType=PS|generation` = **-700** (n=1433, 2026-09-20T02:35:29.133215Z)
- `FUELINST|fuelType=WIND|generation` = **15332** (n=1433, 2026-09-20T02:35:29.133215Z)
- `IMBALNGC|TOTAL|imbalance` = **-3755** (n=236, 2026-09-20T02:21:16.829176Z)
- `INDDEM|TOTAL|demand` = **-12197** (n=236, 2026-09-20T02:21:16.829176Z)
- `INDGEN|TOTAL|generation` = **16197** (n=236, 2026-09-20T02:21:16.829176Z)
- `MELNGC|TOTAL|margin` = **37606** (n=236, 2026-09-20T02:19:46.154039Z)
- `NDF|TOTAL|demand` = **19452** (n=241, 2026-09-20T02:17:36.584473Z)
- `TSDF|TOTAL|demand` = **19952** (n=241, 2026-09-20T02:17:36.584473Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T02:37:37.316182Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:35.755269Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:34.199907Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:32.659783Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:31.112388Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:29.538671Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:28.005996Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:26.458002Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:24.887371Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:23.340200Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:21.508285Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:19.972015Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:18.374346Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:16.819383Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:37:15.263830Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
