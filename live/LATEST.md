# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T09:39:05.142563Z`  
Current process started UTC: `2026-09-18T09:35:05.039818Z`  
1-second metadata polls in this process: **223**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=985, 2026-09-18T09:35:36.686205Z)
- `FUELINST|fuelType=NPSHYD|generation` = **345** (n=985, 2026-09-18T09:35:36.686205Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=985, 2026-09-18T09:35:36.686205Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=985, 2026-09-18T09:35:36.686205Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=985, 2026-09-18T09:35:36.686205Z)
- `FUELINST|fuelType=OTHER|generation` = **904** (n=985, 2026-09-18T09:35:36.686205Z)
- `FUELINST|fuelType=PS|generation` = **-423** (n=985, 2026-09-18T09:35:36.686205Z)
- `FUELINST|fuelType=WIND|generation` = **11746** (n=985, 2026-09-18T09:35:36.686205Z)
- `IMBALNGC|TOTAL|imbalance` = **8100** (n=162, 2026-09-18T09:20:18.018457Z)
- `INDDEM|TOTAL|demand` = **-13185** (n=162, 2026-09-18T09:19:45.552785Z)
- `INDGEN|TOTAL|generation` = **27193** (n=162, 2026-09-18T09:19:45.552785Z)
- `MELNGC|TOTAL|margin` = **36209** (n=162, 2026-09-18T09:19:13.657509Z)
- `NDF|TOTAL|demand` = **16454** (n=166, 2026-09-18T09:17:04.819417Z)
- `TSDF|TOTAL|demand` = **19093** (n=166, 2026-09-18T09:17:21.227303Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T09:39:03.840544Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:39:02.812430Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:39:01.763700Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:39:00.722634Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:38:59.722565Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:38:58.710488Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:38:57.704602Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:38:56.689908Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:38:55.677309Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:38:54.616899Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:38:53.574041Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:38:52.568394Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:38:51.559363Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:38:50.525762Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:38:49.505469Z` — **MID**: 0 rows; marker `2026-09-18T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
