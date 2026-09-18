# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T07:27:20.708861Z`  
Current process started UTC: `2026-09-18T07:23:19.400329Z`  
1-second metadata polls in this process: **172**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=959, 2026-09-18T07:25:30.888628Z)
- `FUELINST|fuelType=NPSHYD|generation` = **379** (n=959, 2026-09-18T07:25:30.888628Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=959, 2026-09-18T07:25:30.888628Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=959, 2026-09-18T07:25:30.888628Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=959, 2026-09-18T07:25:30.888628Z)
- `FUELINST|fuelType=OTHER|generation` = **1803** (n=959, 2026-09-18T07:25:30.888628Z)
- `FUELINST|fuelType=PS|generation` = **599** (n=959, 2026-09-18T07:25:30.888628Z)
- `FUELINST|fuelType=WIND|generation` = **12472** (n=959, 2026-09-18T07:25:30.888628Z)
- `IMBALNGC|TOTAL|imbalance` = **10218** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDDEM|TOTAL|demand` = **-11739** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDGEN|TOTAL|generation` = **27722** (n=159, 2026-09-18T07:19:58.374346Z)
- `MELNGC|TOTAL|margin` = **37765** (n=159, 2026-09-18T07:19:09.419948Z)
- `NDF|TOTAL|demand` = **16314** (n=162, 2026-09-18T07:17:24.178373Z)
- `TSDF|TOTAL|demand` = **17504** (n=162, 2026-09-18T07:17:24.178373Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T07:27:19.382559Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:18.019622Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:16.629854Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:15.281453Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:13.992264Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:12.661950Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:11.312353Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:09.469854Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:08.138788Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:06.759386Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:05.454404Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:04.147299Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:02.804249Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:01.478652Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:27:00.163346Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
