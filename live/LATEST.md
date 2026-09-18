# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T02:07:28.764616Z`  
Current process started UTC: `2026-09-18T02:03:28.373937Z`  
1-second metadata polls in this process: **208**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **923** (n=895, 2026-09-18T02:05:36.418409Z)
- `FUELINST|fuelType=NPSHYD|generation` = **411** (n=895, 2026-09-18T02:05:36.418409Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=895, 2026-09-18T02:05:36.418409Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=895, 2026-09-18T02:05:36.418409Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=895, 2026-09-18T02:05:36.418409Z)
- `FUELINST|fuelType=OTHER|generation` = **294** (n=895, 2026-09-18T02:05:36.418409Z)
- `FUELINST|fuelType=PS|generation` = **312** (n=895, 2026-09-18T02:05:36.418409Z)
- `FUELINST|fuelType=WIND|generation` = **14467** (n=895, 2026-09-18T02:05:36.418409Z)
- `IMBALNGC|TOTAL|imbalance` = **10161** (n=148, 2026-09-18T01:51:40.738117Z)
- `INDDEM|TOTAL|demand` = **-11222** (n=148, 2026-09-18T01:51:24.816933Z)
- `INDGEN|TOTAL|generation` = **26975** (n=148, 2026-09-18T01:51:24.816933Z)
- `MELNGC|TOTAL|margin` = **36705** (n=148, 2026-09-18T01:49:25.897354Z)
- `NDF|TOTAL|demand` = **16314** (n=151, 2026-09-18T01:47:48.325279Z)
- `TSDF|TOTAL|demand` = **16814** (n=151, 2026-09-18T01:47:48.325279Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T02:07:27.781298Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:26.731931Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:25.681844Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:24.652170Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:23.610258Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:22.556083Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:21.556013Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:20.553963Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:19.524726Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:18.487816Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:17.453558Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:16.419578Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:15.370643Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:14.351197Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:07:12.860060Z` — **MID**: 0 rows; marker `2026-09-18T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
