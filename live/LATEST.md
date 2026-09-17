# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T16:04:55.310339Z`  
Current process started UTC: `2026-09-17T16:00:54.608215Z`  
1-second metadata polls in this process: **222**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=-2, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=0, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=57, delta=1, z=4.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=14, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.03 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.13 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.23 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=42, delta=42, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=2, z=4.25 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-240** (n=774, 2026-09-17T16:00:31.716983Z)
- `FUELINST|fuelType=NPSHYD|generation` = **370** (n=774, 2026-09-17T16:00:31.716983Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3313** (n=774, 2026-09-17T16:00:31.716983Z)
- `FUELINST|fuelType=OCGT|generation` = **51** (n=774, 2026-09-17T16:00:31.716983Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=774, 2026-09-17T16:00:31.716983Z)
- `FUELINST|fuelType=OTHER|generation` = **907** (n=774, 2026-09-17T16:00:31.716983Z)
- `FUELINST|fuelType=PS|generation` = **-255** (n=774, 2026-09-17T16:00:31.716983Z)
- `FUELINST|fuelType=WIND|generation` = **13941** (n=774, 2026-09-17T16:00:31.716983Z)
- `IMBALNGC|TOTAL|imbalance` = **11642** (n=128, 2026-09-17T15:54:55.997739Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=128, 2026-09-17T15:54:24.168455Z)
- `INDGEN|TOTAL|generation` = **28456** (n=128, 2026-09-17T15:54:40.409047Z)
- `MELNGC|TOTAL|margin` = **36684** (n=128, 2026-09-17T15:51:59.800251Z)
- `NDF|TOTAL|demand` = **16314** (n=131, 2026-09-17T15:48:34.023613Z)
- `TSDF|TOTAL|demand` = **16814** (n=131, 2026-09-17T15:48:34.023613Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T16:04:53.906364Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:52.906255Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:51.159812Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:50.159717Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:49.159596Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:48.159501Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:46.916895Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:45.628851Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:44.628727Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:43.567887Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:42.567776Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:41.279626Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:40.279504Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:39.279394Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:04:37.927807Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
