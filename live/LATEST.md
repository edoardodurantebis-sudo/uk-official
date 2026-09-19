# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T04:52:14.039010Z`  
Current process started UTC: `2026-09-19T04:48:12.774515Z`  
1-second metadata polls in this process: **168**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-10744, delta=3052, z=1.92 -> demand pressure up
- **WINDFOR** `TOTAL` `generation` — wind forecast [TOTAL] generation: value=7845, delta=-11023, z=-4.38 -> renewable cushion down / residual-load pressure up
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-578** (n=1172, 2026-09-19T04:50:40.433953Z)
- `FUELINST|fuelType=NPSHYD|generation` = **351** (n=1172, 2026-09-19T04:50:40.433953Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3344** (n=1172, 2026-09-19T04:50:40.433953Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1172, 2026-09-19T04:50:40.433953Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1172, 2026-09-19T04:50:40.433953Z)
- `FUELINST|fuelType=OTHER|generation` = **175** (n=1172, 2026-09-19T04:50:40.433953Z)
- `FUELINST|fuelType=PS|generation` = **-542** (n=1172, 2026-09-19T04:50:40.433953Z)
- `FUELINST|fuelType=WIND|generation` = **16046** (n=1172, 2026-09-19T04:50:40.433953Z)
- `IMBALNGC|TOTAL|imbalance` = **9720** (n=194, 2026-09-19T04:50:40.433953Z)
- `INDDEM|TOTAL|demand` = **-10865** (n=194, 2026-09-19T04:50:24.373852Z)
- `INDGEN|TOTAL|generation` = **26909** (n=194, 2026-09-19T04:50:24.373852Z)
- `MELNGC|TOTAL|margin` = **38317** (n=194, 2026-09-19T04:49:16.915857Z)
- `NDF|TOTAL|demand` = **16550** (n=198, 2026-09-19T04:47:17.110939Z)
- `TSDF|TOTAL|demand` = **17190** (n=198, 2026-09-19T04:47:17.110939Z)
- `WINDFOR|TOTAL|generation` = **6714** (n=33, 2026-09-19T03:30:33.519312Z)

## Latest publication events

- `2026-09-19T04:52:12.713871Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:52:11.395897Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:52:09.712687Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:52:08.352156Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:52:06.983933Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:52:05.674707Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:52:04.375417Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:52:02.663720Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:52:01.331852Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:52:00.021412Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:51:58.714895Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:51:57.446044Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:51:56.138730Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:51:54.812128Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:51:53.507199Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
