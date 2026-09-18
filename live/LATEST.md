# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T11:49:18.736473Z`  
Current process started UTC: `2026-09-18T11:45:17.600699Z`  
1-second metadata polls in this process: **158**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=1011, 2026-09-18T11:45:33.563127Z)
- `FUELINST|fuelType=NPSHYD|generation` = **332** (n=1011, 2026-09-18T11:45:33.563127Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3342** (n=1011, 2026-09-18T11:45:33.563127Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1011, 2026-09-18T11:45:33.563127Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1011, 2026-09-18T11:45:33.563127Z)
- `FUELINST|fuelType=OTHER|generation` = **861** (n=1011, 2026-09-18T11:45:33.563127Z)
- `FUELINST|fuelType=PS|generation` = **-715** (n=1011, 2026-09-18T11:45:33.563127Z)
- `FUELINST|fuelType=WIND|generation` = **12896** (n=1011, 2026-09-18T11:45:33.563127Z)
- `IMBALNGC|TOTAL|imbalance` = **8997** (n=166, 2026-09-18T11:27:14.159590Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=166, 2026-09-18T11:26:58.717077Z)
- `INDGEN|TOTAL|generation` = **25667** (n=166, 2026-09-18T11:26:58.717077Z)
- `MELNGC|TOTAL|margin` = **38124** (n=166, 2026-09-18T11:22:30.597764Z)
- `NDF|TOTAL|demand` = **16170** (n=171, 2026-09-18T11:49:04.559776Z)
- `TSDF|TOTAL|demand` = **16670** (n=170, 2026-09-18T11:20:04.075631Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T11:49:17.427052Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:16.109210Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:14.745460Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:13.402232Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:12.061638Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:10.746775Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:09.387220Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:08.042894Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:06.698028Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:04.559776Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:04.559776Z` — **NDF**: 80 rows; marker `2026-09-18T11:48:00Z`
- `2026-09-18T11:49:03.235658Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:01.891858Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:49:00.556449Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:48:59.208093Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
