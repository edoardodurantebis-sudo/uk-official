# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T09:51:56.484625Z`  
Current process started UTC: `2026-09-19T09:47:56.369403Z`  
1-second metadata polls in this process: **225**  
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

- `FUELINST|fuelType=INTVKL|generation` = **560** (n=1232, 2026-09-19T09:50:37.268038Z)
- `FUELINST|fuelType=NPSHYD|generation` = **331** (n=1232, 2026-09-19T09:50:37.268038Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1232, 2026-09-19T09:50:37.268038Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1232, 2026-09-19T09:50:37.268038Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1232, 2026-09-19T09:50:37.268038Z)
- `FUELINST|fuelType=OTHER|generation` = **300** (n=1232, 2026-09-19T09:50:37.268038Z)
- `FUELINST|fuelType=PS|generation` = **-700** (n=1232, 2026-09-19T09:50:37.268038Z)
- `FUELINST|fuelType=WIND|generation` = **15707** (n=1232, 2026-09-19T09:50:37.268038Z)
- `IMBALNGC|TOTAL|imbalance` = **7793** (n=203, 2026-09-19T09:50:05.454220Z)
- `INDDEM|TOTAL|demand` = **-13214** (n=203, 2026-09-19T09:49:49.613301Z)
- `INDGEN|TOTAL|generation` = **26724** (n=203, 2026-09-19T09:49:49.613301Z)
- `MELNGC|TOTAL|margin` = **36451** (n=203, 2026-09-19T09:48:44.462675Z)
- `NDF|TOTAL|demand` = **15940** (n=208, 2026-09-19T09:47:30.580399Z)
- `TSDF|TOTAL|demand` = **18932** (n=208, 2026-09-19T09:47:30.580399Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T09:51:55.531262Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:54.531116Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:53.530964Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:52.530840Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:51.530694Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:50.530621Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:49.530512Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:48.530368Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:47.530222Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:46.530134Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:45.529996Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:44.529854Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:43.529759Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:41.991343Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:51:40.991251Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
