# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T03:23:46.427664Z`  
Current process started UTC: `2026-09-18T03:19:45.452743Z`  
1-second metadata polls in this process: **137**  
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

- `FUELINST|fuelType=INTVKL|generation` = **988** (n=910, 2026-09-18T03:20:35.413134Z)
- `FUELINST|fuelType=NPSHYD|generation` = **404** (n=910, 2026-09-18T03:20:35.413134Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=910, 2026-09-18T03:20:35.413134Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=910, 2026-09-18T03:20:35.413134Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=910, 2026-09-18T03:20:35.413134Z)
- `FUELINST|fuelType=OTHER|generation` = **374** (n=910, 2026-09-18T03:20:35.413134Z)
- `FUELINST|fuelType=PS|generation` = **462** (n=910, 2026-09-18T03:20:35.413134Z)
- `FUELINST|fuelType=WIND|generation` = **13629** (n=910, 2026-09-18T03:20:35.413134Z)
- `IMBALNGC|TOTAL|imbalance` = **10169** (n=151, 2026-09-18T03:21:23.504107Z)
- `INDDEM|TOTAL|demand` = **-11249** (n=151, 2026-09-18T03:21:23.504107Z)
- `INDGEN|TOTAL|generation` = **26983** (n=151, 2026-09-18T03:21:23.504107Z)
- `MELNGC|TOTAL|margin` = **38166** (n=151, 2026-09-18T03:19:45.452751Z)
- `NDF|TOTAL|demand` = **16314** (n=154, 2026-09-18T03:17:28.449836Z)
- `TSDF|TOTAL|demand` = **16814** (n=154, 2026-09-18T03:17:28.449836Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T03:23:44.828656Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:43.182287Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:41.571172Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:39.902545Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:38.197012Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:36.633209Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:35.032181Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:32.554591Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:30.889254Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:29.270249Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:27.665439Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:25.854465Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:24.154028Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:22.613386Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:23:21.030636Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
