# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T04:46:26.678361Z`  
Current process started UTC: `2026-09-20T04:42:26.611807Z`  
1-second metadata polls in this process: **145**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.38 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.43 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-4.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=3, z=-4.49 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.64 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.78 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **121** (n=1459, 2026-09-20T04:45:29.193848Z)
- `FUELINST|fuelType=NPSHYD|generation` = **298** (n=1459, 2026-09-20T04:45:29.193848Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1459, 2026-09-20T04:45:29.193848Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1459, 2026-09-20T04:45:29.193848Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1459, 2026-09-20T04:45:29.193848Z)
- `FUELINST|fuelType=OTHER|generation` = **157** (n=1459, 2026-09-20T04:45:29.193848Z)
- `FUELINST|fuelType=PS|generation` = **-701** (n=1459, 2026-09-20T04:45:29.193848Z)
- `FUELINST|fuelType=WIND|generation` = **15340** (n=1459, 2026-09-20T04:45:29.193848Z)
- `IMBALNGC|TOTAL|imbalance` = **-6763** (n=240, 2026-09-20T04:20:55.221625Z)
- `INDDEM|TOTAL|demand` = **-12315** (n=240, 2026-09-20T04:20:29.187132Z)
- `INDGEN|TOTAL|generation` = **13189** (n=240, 2026-09-20T04:20:29.187132Z)
- `MELNGC|TOTAL|margin` = **37513** (n=240, 2026-09-20T04:19:08.049420Z)
- `NDF|TOTAL|demand` = **19452** (n=245, 2026-09-20T04:17:31.726312Z)
- `TSDF|TOTAL|demand` = **19952** (n=245, 2026-09-20T04:17:31.726312Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T04:46:25.106163Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:23.532977Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:21.680686Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:18.398285Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:18.398285Z` — **FREQ**: 5761 rows; marker `2026-09-20T04:45:45Z`
- `2026-09-20T04:46:16.846718Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:15.294365Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:13.742108Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:12.169792Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:10.594866Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:08.438681Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:06.856851Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:05.324314Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:03.773899Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:46:01.897407Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
