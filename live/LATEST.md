# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T02:15:53.758459Z`  
Current process started UTC: `2026-09-18T02:11:52.933802Z`  
1-second metadata polls in this process: **157**  
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

- `FUELINST|fuelType=INTVKL|generation` = **976** (n=897, 2026-09-18T02:15:30.629039Z)
- `FUELINST|fuelType=NPSHYD|generation` = **402** (n=897, 2026-09-18T02:15:30.629039Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=897, 2026-09-18T02:15:30.629039Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=897, 2026-09-18T02:15:30.629039Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=897, 2026-09-18T02:15:30.629039Z)
- `FUELINST|fuelType=OTHER|generation` = **273** (n=897, 2026-09-18T02:15:30.629039Z)
- `FUELINST|fuelType=PS|generation` = **295** (n=897, 2026-09-18T02:15:30.629039Z)
- `FUELINST|fuelType=WIND|generation` = **14332** (n=897, 2026-09-18T02:15:30.629039Z)
- `IMBALNGC|TOTAL|imbalance` = **10161** (n=148, 2026-09-18T01:51:40.738117Z)
- `INDDEM|TOTAL|demand` = **-11222** (n=148, 2026-09-18T01:51:24.816933Z)
- `INDGEN|TOTAL|generation` = **26975** (n=148, 2026-09-18T01:51:24.816933Z)
- `MELNGC|TOTAL|margin` = **36705** (n=148, 2026-09-18T01:49:25.897354Z)
- `NDF|TOTAL|demand` = **16314** (n=151, 2026-09-18T01:47:48.325279Z)
- `TSDF|TOTAL|demand` = **16814** (n=151, 2026-09-18T01:47:48.325279Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T02:15:52.315542Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:50.885797Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:49.393507Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:47.944547Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:46.167964Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:44.725516Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:43.300436Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:41.843242Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:40.401162Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:38.949455Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:37.501256Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:36.070670Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:34.619026Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:33.140401Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:15:30.629039Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
