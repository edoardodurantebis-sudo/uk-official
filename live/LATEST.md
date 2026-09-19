# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T06:50:01.722283Z`  
Current process started UTC: `2026-09-19T06:46:00.841075Z`  
1-second metadata polls in this process: **163**  
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

- `FUELINST|fuelType=INTVKL|generation` = **357** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=NPSHYD|generation` = **367** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=OTHER|generation` = **900** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=PS|generation` = **-301** (n=1195, 2026-09-19T06:45:30.221571Z)
- `FUELINST|fuelType=WIND|generation` = **15886** (n=1195, 2026-09-19T06:45:30.221571Z)
- `IMBALNGC|TOTAL|imbalance` = **9725** (n=197, 2026-09-19T06:21:03.713324Z)
- `INDDEM|TOTAL|demand` = **-10863** (n=197, 2026-09-19T06:20:47.840036Z)
- `INDGEN|TOTAL|generation` = **26914** (n=197, 2026-09-19T06:21:03.713324Z)
- `MELNGC|TOTAL|margin` = **38030** (n=198, 2026-09-19T06:49:00.398728Z)
- `NDF|TOTAL|demand` = **16550** (n=202, 2026-09-19T06:47:06.856404Z)
- `TSDF|TOTAL|demand` = **17429** (n=202, 2026-09-19T06:47:06.856404Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T06:50:00.365105Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:58.973656Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:57.637523Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:56.367084Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:55.087096Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:53.771982Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:52.471181Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:51.136744Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:49.231142Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:47.894229Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:46.612216Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:45.302985Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:43.964955Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:42.666553Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:49:41.362039Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
