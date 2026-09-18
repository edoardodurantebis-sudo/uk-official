# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T13:59:56.238813Z`  
Current process started UTC: `2026-09-18T13:55:55.730261Z`  
1-second metadata polls in this process: **187**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-10744, delta=3052, z=1.92 -> demand pressure up
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1037, 2026-09-18T13:55:27.799810Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1037, 2026-09-18T13:55:27.799810Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1037, 2026-09-18T13:55:27.799810Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1037, 2026-09-18T13:55:27.799810Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1037, 2026-09-18T13:55:27.799810Z)
- `FUELINST|fuelType=OTHER|generation` = **437** (n=1037, 2026-09-18T13:55:27.799810Z)
- `FUELINST|fuelType=PS|generation` = **-714** (n=1037, 2026-09-18T13:55:27.799810Z)
- `FUELINST|fuelType=WIND|generation` = **15687** (n=1037, 2026-09-18T13:55:27.799810Z)
- `IMBALNGC|TOTAL|imbalance` = **8928** (n=171, 2026-09-18T13:54:55.533395Z)
- `INDDEM|TOTAL|demand` = **-10745** (n=171, 2026-09-18T13:54:55.533395Z)
- `INDGEN|TOTAL|generation` = **25598** (n=171, 2026-09-18T13:54:55.533395Z)
- `MELNGC|TOTAL|margin` = **38192** (n=171, 2026-09-18T13:51:42.682305Z)
- `NDF|TOTAL|demand` = **16170** (n=175, 2026-09-18T13:49:24.414005Z)
- `TSDF|TOTAL|demand` = **16670** (n=175, 2026-09-18T13:49:41.459837Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T13:59:55.061066Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:53.860582Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:52.648224Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:51.442879Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:50.233688Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:48.726049Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:47.517730Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:46.284184Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:45.063885Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:42.617449Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:41.397684Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:40.206149Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:39.007385Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:37.796099Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:59:36.605948Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
