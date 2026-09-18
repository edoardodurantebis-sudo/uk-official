# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T09:30:05.385296Z`  
Current process started UTC: `2026-09-18T09:26:03.406106Z`  
1-second metadata polls in this process: **134**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=983, 2026-09-18T09:25:30.002968Z)
- `FUELINST|fuelType=NPSHYD|generation` = **344** (n=983, 2026-09-18T09:25:30.002968Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=983, 2026-09-18T09:25:30.002968Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=983, 2026-09-18T09:25:30.002968Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=983, 2026-09-18T09:25:30.002968Z)
- `FUELINST|fuelType=OTHER|generation` = **944** (n=983, 2026-09-18T09:25:30.002968Z)
- `FUELINST|fuelType=PS|generation` = **-427** (n=983, 2026-09-18T09:25:30.002968Z)
- `FUELINST|fuelType=WIND|generation` = **11607** (n=983, 2026-09-18T09:25:30.002968Z)
- `IMBALNGC|TOTAL|imbalance` = **8100** (n=162, 2026-09-18T09:20:18.018457Z)
- `INDDEM|TOTAL|demand` = **-13185** (n=162, 2026-09-18T09:19:45.552785Z)
- `INDGEN|TOTAL|generation` = **27193** (n=162, 2026-09-18T09:19:45.552785Z)
- `MELNGC|TOTAL|margin` = **36209** (n=162, 2026-09-18T09:19:13.657509Z)
- `NDF|TOTAL|demand` = **16454** (n=166, 2026-09-18T09:17:04.819417Z)
- `TSDF|TOTAL|demand` = **19093** (n=166, 2026-09-18T09:17:21.227303Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T09:30:02.711152Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:30:00.974286Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:59.072270Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:57.339025Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:55.621404Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:53.885150Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:52.197547Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:50.486815Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:48.717710Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:46.474211Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:44.761435Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:43.048296Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:41.331452Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:39.605548Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:29:37.898292Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
