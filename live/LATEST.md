# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T02:20:05.301901Z`  
Current process started UTC: `2026-09-18T02:16:04.353913Z`  
1-second metadata polls in this process: **212**  
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
- `MELNGC|TOTAL|margin` = **38212** (n=149, 2026-09-18T02:19:51.484596Z)
- `NDF|TOTAL|demand` = **16314** (n=152, 2026-09-18T02:17:25.911508Z)
- `TSDF|TOTAL|demand` = **16814** (n=152, 2026-09-18T02:17:25.911508Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T02:20:04.252224Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:20:03.072017Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:20:01.984453Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:20:00.944151Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:19:59.751327Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:19:58.735824Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:19:57.668979Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:19:56.668905Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:19:55.640116Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:19:54.586112Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:19:53.558868Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:19:51.484596Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:19:51.484596Z` — **MELNGC**: 918 rows; marker `2026-09-18T02:17:00Z`
- `2026-09-18T02:19:50.446783Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:19:49.389076Z` — **MID**: 0 rows; marker `2026-09-18T02:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
