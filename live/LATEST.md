# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T09:56:10.009457Z`  
Current process started UTC: `2026-09-19T09:52:09.194795Z`  
1-second metadata polls in this process: **174**  
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

- `FUELINST|fuelType=INTVKL|generation` = **560** (n=1233, 2026-09-19T09:55:41.935549Z)
- `FUELINST|fuelType=NPSHYD|generation` = **331** (n=1233, 2026-09-19T09:55:41.935549Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1233, 2026-09-19T09:55:41.935549Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1233, 2026-09-19T09:55:41.935549Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1233, 2026-09-19T09:55:41.935549Z)
- `FUELINST|fuelType=OTHER|generation` = **279** (n=1233, 2026-09-19T09:55:41.935549Z)
- `FUELINST|fuelType=PS|generation` = **-699** (n=1233, 2026-09-19T09:55:41.935549Z)
- `FUELINST|fuelType=WIND|generation` = **15730** (n=1233, 2026-09-19T09:55:41.935549Z)
- `IMBALNGC|TOTAL|imbalance` = **7793** (n=203, 2026-09-19T09:50:05.454220Z)
- `INDDEM|TOTAL|demand` = **-13214** (n=203, 2026-09-19T09:49:49.613301Z)
- `INDGEN|TOTAL|generation` = **26724** (n=203, 2026-09-19T09:49:49.613301Z)
- `MELNGC|TOTAL|margin` = **36451** (n=203, 2026-09-19T09:48:44.462675Z)
- `NDF|TOTAL|demand` = **15940** (n=208, 2026-09-19T09:47:30.580399Z)
- `TSDF|TOTAL|demand` = **18932** (n=208, 2026-09-19T09:47:30.580399Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T09:56:08.710433Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:56:07.389066Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:56:06.098708Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:56:04.760537Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:56:03.371546Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:56:02.077468Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:56:00.656654Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:55:59.331895Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:55:57.491614Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:55:56.179433Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:55:54.852347Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:55:53.538677Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:55:52.154216Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:55:50.764698Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:55:49.438667Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
