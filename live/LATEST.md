# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T04:38:07.203530Z`  
Current process started UTC: `2026-09-20T04:34:06.401651Z`  
1-second metadata polls in this process: **219**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.87 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **121** (n=1457, 2026-09-20T04:35:26.223504Z)
- `FUELINST|fuelType=NPSHYD|generation` = **299** (n=1457, 2026-09-20T04:35:26.223504Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1457, 2026-09-20T04:35:26.223504Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1457, 2026-09-20T04:35:26.223504Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1457, 2026-09-20T04:35:26.223504Z)
- `FUELINST|fuelType=OTHER|generation` = **167** (n=1457, 2026-09-20T04:35:26.223504Z)
- `FUELINST|fuelType=PS|generation` = **-698** (n=1457, 2026-09-20T04:35:26.223504Z)
- `FUELINST|fuelType=WIND|generation` = **15303** (n=1457, 2026-09-20T04:35:26.223504Z)
- `IMBALNGC|TOTAL|imbalance` = **-6763** (n=240, 2026-09-20T04:20:55.221625Z)
- `INDDEM|TOTAL|demand` = **-12315** (n=240, 2026-09-20T04:20:29.187132Z)
- `INDGEN|TOTAL|generation` = **13189** (n=240, 2026-09-20T04:20:29.187132Z)
- `MELNGC|TOTAL|margin` = **37513** (n=240, 2026-09-20T04:19:08.049420Z)
- `NDF|TOTAL|demand` = **19452** (n=245, 2026-09-20T04:17:31.726312Z)
- `TSDF|TOTAL|demand` = **19952** (n=245, 2026-09-20T04:17:31.726312Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T04:38:06.186476Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:38:05.173195Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:38:03.762530Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:38:02.756188Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:38:01.737643Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:38:00.691372Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:37:59.666535Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:37:58.661836Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:37:57.661766Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:37:56.655776Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:37:55.593991Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:37:54.577117Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:37:53.577046Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:37:52.524899Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:37:51.508664Z` — **MID**: 0 rows; marker `2026-09-20T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
