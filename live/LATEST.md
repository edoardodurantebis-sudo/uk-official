# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T13:55:43.930272Z`  
Current process started UTC: `2026-09-18T13:51:42.682296Z`  
1-second metadata polls in this process: **131**  
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

- `2026-09-18T13:55:42.250992Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:40.560029Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:38.847938Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:37.159736Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:35.489030Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:33.821889Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:32.127074Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:30.469062Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:27.799810Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:27.799810Z` — **FUELINST**: 80 rows; marker `2026-09-18T13:55:00Z`
- `2026-09-18T13:55:25.880046Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:24.214100Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:22.502772Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:20.764650Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:55:18.944554Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
