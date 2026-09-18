# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T06:20:10.099545Z`  
Current process started UTC: `2026-09-18T06:16:08.863855Z`  
1-second metadata polls in this process: **144**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=945, 2026-09-18T06:15:27.733076Z)
- `FUELINST|fuelType=NPSHYD|generation` = **453** (n=945, 2026-09-18T06:15:27.733076Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=945, 2026-09-18T06:15:27.733076Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=945, 2026-09-18T06:15:27.733076Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=945, 2026-09-18T06:15:27.733076Z)
- `FUELINST|fuelType=OTHER|generation` = **727** (n=945, 2026-09-18T06:15:27.733076Z)
- `FUELINST|fuelType=PS|generation` = **373** (n=945, 2026-09-18T06:15:27.733076Z)
- `FUELINST|fuelType=WIND|generation` = **14373** (n=945, 2026-09-18T06:15:27.733076Z)
- `IMBALNGC|TOTAL|imbalance` = **10719** (n=156, 2026-09-18T05:50:16.495445Z)
- `INDDEM|TOTAL|demand` = **-11168** (n=156, 2026-09-18T05:50:16.495445Z)
- `INDGEN|TOTAL|generation` = **27533** (n=156, 2026-09-18T05:50:16.495445Z)
- `MELNGC|TOTAL|margin` = **37963** (n=157, 2026-09-18T06:19:23.801804Z)
- `NDF|TOTAL|demand` = **16314** (n=160, 2026-09-18T06:17:14.273486Z)
- `TSDF|TOTAL|demand` = **16814** (n=160, 2026-09-18T06:17:14.273486Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T06:20:08.637962Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:20:07.143626Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:20:05.267546Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:20:03.810691Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:20:02.322489Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:20:00.814472Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:19:59.220968Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:19:57.742441Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:19:55.184837Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:19:53.687468Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:19:52.160415Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:19:50.640084Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:19:49.145596Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:19:47.667632Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:19:46.188963Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
