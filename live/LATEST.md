# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T02:33:25.728519Z`  
Current process started UTC: `2026-09-20T02:29:24.885445Z`  
1-second metadata polls in this process: **141**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-7.04 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **329** (n=1432, 2026-09-20T02:30:36.249553Z)
- `FUELINST|fuelType=NPSHYD|generation` = **308** (n=1432, 2026-09-20T02:30:36.249553Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1432, 2026-09-20T02:30:36.249553Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1432, 2026-09-20T02:30:36.249553Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1432, 2026-09-20T02:30:36.249553Z)
- `FUELINST|fuelType=OTHER|generation` = **188** (n=1432, 2026-09-20T02:30:36.249553Z)
- `FUELINST|fuelType=PS|generation` = **-703** (n=1432, 2026-09-20T02:30:36.249553Z)
- `FUELINST|fuelType=WIND|generation` = **15354** (n=1432, 2026-09-20T02:30:36.249553Z)
- `IMBALNGC|TOTAL|imbalance` = **-3755** (n=236, 2026-09-20T02:21:16.829176Z)
- `INDDEM|TOTAL|demand` = **-12197** (n=236, 2026-09-20T02:21:16.829176Z)
- `INDGEN|TOTAL|generation` = **16197** (n=236, 2026-09-20T02:21:16.829176Z)
- `MELNGC|TOTAL|margin` = **37606** (n=236, 2026-09-20T02:19:46.154039Z)
- `NDF|TOTAL|demand` = **19452** (n=241, 2026-09-20T02:17:36.584473Z)
- `TSDF|TOTAL|demand` = **19952** (n=241, 2026-09-20T02:17:36.584473Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T02:33:24.056112Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:22.403066Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:20.527000Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:18.839912Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:17.173908Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:15.544928Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:13.912246Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:12.270089Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:10.616169Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:08.953795Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:07.319006Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:05.629262Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:03.682432Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:02.062656Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:33:00.398147Z` — **MID**: 0 rows; marker `2026-09-20T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
