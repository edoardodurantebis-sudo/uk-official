# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T04:58:57.950627Z`  
Current process started UTC: `2026-09-20T04:54:57.685575Z`  
1-second metadata polls in this process: **145**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.34 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **121** (n=1461, 2026-09-20T04:55:30.527908Z)
- `FUELINST|fuelType=NPSHYD|generation` = **299** (n=1461, 2026-09-20T04:55:30.527908Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1461, 2026-09-20T04:55:30.527908Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1461, 2026-09-20T04:55:30.527908Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1461, 2026-09-20T04:55:30.527908Z)
- `FUELINST|fuelType=OTHER|generation` = **141** (n=1461, 2026-09-20T04:55:30.527908Z)
- `FUELINST|fuelType=PS|generation` = **-698** (n=1461, 2026-09-20T04:55:30.527908Z)
- `FUELINST|fuelType=WIND|generation` = **15378** (n=1461, 2026-09-20T04:55:30.527908Z)
- `IMBALNGC|TOTAL|imbalance` = **-6777** (n=241, 2026-09-20T04:50:32.525251Z)
- `INDDEM|TOTAL|demand` = **-12177** (n=241, 2026-09-20T04:50:32.525251Z)
- `INDGEN|TOTAL|generation` = **13175** (n=241, 2026-09-20T04:50:32.525251Z)
- `MELNGC|TOTAL|margin` = **37516** (n=241, 2026-09-20T04:49:13.726695Z)
- `NDF|TOTAL|demand` = **19452** (n=246, 2026-09-20T04:47:23.759382Z)
- `TSDF|TOTAL|demand` = **19952** (n=246, 2026-09-20T04:47:23.759382Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T04:58:56.331530Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:54.723987Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:53.035977Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:51.458578Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:49.751555Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:48.142889Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:46.260906Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:44.647973Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:43.067629Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:41.445077Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:39.847174Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:38.221317Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:36.608619Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:35.029471Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:58:33.408602Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
