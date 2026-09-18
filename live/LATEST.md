# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T07:39:57.957969Z`  
Current process started UTC: `2026-09-18T07:35:56.642097Z`  
1-second metadata polls in this process: **133**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=NPSHYD|generation` = **377** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=OTHER|generation` = **1492** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=PS|generation` = **599** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=WIND|generation` = **12343** (n=961, 2026-09-18T07:35:35.258798Z)
- `IMBALNGC|TOTAL|imbalance` = **10218** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDDEM|TOTAL|demand` = **-11739** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDGEN|TOTAL|generation` = **27722** (n=159, 2026-09-18T07:19:58.374346Z)
- `MELNGC|TOTAL|margin` = **37765** (n=159, 2026-09-18T07:19:09.419948Z)
- `NDF|TOTAL|demand` = **16314** (n=162, 2026-09-18T07:17:24.178373Z)
- `TSDF|TOTAL|demand` = **17504** (n=162, 2026-09-18T07:17:24.178373Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T07:39:56.233535Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:54.520951Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:52.824566Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:51.091498Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:49.367378Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:47.653701Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:45.941720Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:44.197613Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:42.043428Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:40.329683Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:38.533270Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:36.832211Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:35.114345Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:33.372505Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:39:31.595920Z` — **MID**: 0 rows; marker `2026-09-18T07:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
