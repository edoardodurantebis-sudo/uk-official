# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T04:35:10.165496Z`  
Current process started UTC: `2026-09-18T04:31:09.252073Z`  
1-second metadata polls in this process: **131**  
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

- `2026-09-18T04:35:08.516372Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:35:06.858624Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:35:05.195847Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:35:03.332310Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:35:01.694962Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:34:58.765912Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:34:57.123297Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:34:55.435475Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:34:53.775463Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:34:52.029103Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:34:50.377913Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:34:48.703528Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:34:47.066682Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:34:45.344080Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:34:43.317311Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
