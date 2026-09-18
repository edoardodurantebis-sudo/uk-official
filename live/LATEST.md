# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T03:28:00.149071Z`  
Current process started UTC: `2026-09-18T03:23:58.994388Z`  
1-second metadata polls in this process: **133**  
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

- `FUELINST|fuelType=INTVKL|generation` = **990** (n=911, 2026-09-18T03:25:35.065506Z)
- `FUELINST|fuelType=NPSHYD|generation` = **403** (n=911, 2026-09-18T03:25:35.065506Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=911, 2026-09-18T03:25:35.065506Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=911, 2026-09-18T03:25:35.065506Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=911, 2026-09-18T03:25:35.065506Z)
- `FUELINST|fuelType=OTHER|generation` = **290** (n=911, 2026-09-18T03:25:35.065506Z)
- `FUELINST|fuelType=PS|generation` = **460** (n=911, 2026-09-18T03:25:35.065506Z)
- `FUELINST|fuelType=WIND|generation` = **13631** (n=911, 2026-09-18T03:25:35.065506Z)
- `IMBALNGC|TOTAL|imbalance` = **10169** (n=151, 2026-09-18T03:21:23.504107Z)
- `INDDEM|TOTAL|demand` = **-11249** (n=151, 2026-09-18T03:21:23.504107Z)
- `INDGEN|TOTAL|generation` = **26983** (n=151, 2026-09-18T03:21:23.504107Z)
- `MELNGC|TOTAL|margin` = **38166** (n=151, 2026-09-18T03:19:45.452751Z)
- `NDF|TOTAL|demand` = **16314** (n=154, 2026-09-18T03:17:28.449836Z)
- `TSDF|TOTAL|demand` = **16814** (n=154, 2026-09-18T03:17:28.449836Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T03:27:58.433874Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:56.735060Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:55.038532Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:53.321072Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:51.458403Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:49.734690Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:48.023655Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:46.244363Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:44.075502Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:42.375892Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:40.677152Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:38.938539Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:37.249385Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:35.537254Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:27:33.779928Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
