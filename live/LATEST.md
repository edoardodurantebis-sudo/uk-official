# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T04:30:58.267988Z`  
Current process started UTC: `2026-09-18T04:26:57.075009Z`  
1-second metadata polls in this process: **141**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **451** (n=924, 2026-09-18T04:30:48.669653Z)
- `FUELINST|fuelType=NPSHYD|generation` = **419** (n=924, 2026-09-18T04:30:48.669653Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=924, 2026-09-18T04:30:48.669653Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=924, 2026-09-18T04:30:48.669653Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=924, 2026-09-18T04:30:48.669653Z)
- `FUELINST|fuelType=OTHER|generation` = **468** (n=924, 2026-09-18T04:30:48.669653Z)
- `FUELINST|fuelType=PS|generation` = **279** (n=924, 2026-09-18T04:30:48.669653Z)
- `FUELINST|fuelType=WIND|generation` = **13816** (n=924, 2026-09-18T04:30:48.669653Z)
- `IMBALNGC|TOTAL|imbalance` = **10739** (n=153, 2026-09-18T04:21:04.507489Z)
- `INDDEM|TOTAL|demand` = **-11164** (n=153, 2026-09-18T04:21:04.507489Z)
- `INDGEN|TOTAL|generation` = **27553** (n=153, 2026-09-18T04:21:04.507489Z)
- `MELNGC|TOTAL|margin` = **38162** (n=153, 2026-09-18T04:19:58.441718Z)
- `NDF|TOTAL|demand` = **16314** (n=156, 2026-09-18T04:17:41.570570Z)
- `TSDF|TOTAL|demand` = **16814** (n=156, 2026-09-18T04:17:41.570570Z)
- `WINDFOR|TOTAL|generation` = **7845** (n=26, 2026-09-18T03:30:37.036559Z)

## Latest publication events

- `2026-09-18T04:30:56.549751Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:55.008094Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:53.455293Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:51.573119Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:48.669653Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:48.669653Z` — **FUELINST**: 80 rows; marker `2026-09-18T04:30:00Z`
- `2026-09-18T04:30:46.734809Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:44.977091Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:43.351985Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:41.779098Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:40.204446Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:38.424991Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:36.869512Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:32.503988Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:30:32.503988Z` — **FUELHH**: 20 rows; marker `2026-09-18T04:30:00Z`
