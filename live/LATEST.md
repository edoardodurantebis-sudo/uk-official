# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T05:13:14.084030Z`  
Current process started UTC: `2026-09-19T05:09:13.813154Z`  
1-second metadata polls in this process: **231**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-454** (n=1176, 2026-09-19T05:10:34.149076Z)
- `FUELINST|fuelType=NPSHYD|generation` = **352** (n=1176, 2026-09-19T05:10:34.149076Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1176, 2026-09-19T05:10:34.149076Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1176, 2026-09-19T05:10:34.149076Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1176, 2026-09-19T05:10:34.149076Z)
- `FUELINST|fuelType=OTHER|generation` = **239** (n=1176, 2026-09-19T05:10:34.149076Z)
- `FUELINST|fuelType=PS|generation` = **-543** (n=1176, 2026-09-19T05:10:34.149076Z)
- `FUELINST|fuelType=WIND|generation` = **15989** (n=1176, 2026-09-19T05:10:34.149076Z)
- `IMBALNGC|TOTAL|imbalance` = **9720** (n=194, 2026-09-19T04:50:40.433953Z)
- `INDDEM|TOTAL|demand` = **-10865** (n=194, 2026-09-19T04:50:24.373852Z)
- `INDGEN|TOTAL|generation` = **26909** (n=194, 2026-09-19T04:50:24.373852Z)
- `MELNGC|TOTAL|margin` = **38317** (n=194, 2026-09-19T04:49:16.915857Z)
- `NDF|TOTAL|demand` = **16550** (n=198, 2026-09-19T04:47:17.110939Z)
- `TSDF|TOTAL|demand` = **17190** (n=198, 2026-09-19T04:47:17.110939Z)
- `WINDFOR|TOTAL|generation` = **6714** (n=33, 2026-09-19T03:30:33.519312Z)

## Latest publication events

- `2026-09-19T05:13:13.063207Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:12.063103Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:11.061094Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:10.060851Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:09.060748Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:08.060660Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:07.060563Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:06.060494Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:05.060409Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:04.060272Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:03.060150Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:02.060017Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:13:01.059860Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:12:59.523826Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:12:58.523734Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
