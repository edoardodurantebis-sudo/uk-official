# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T07:17:45.460507Z`  
Current process started UTC: `2026-09-17T07:13:45.043103Z`  
1-second metadata polls in this process: **152**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.42 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=49, delta=49, z=4.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=3, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=1, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=17, z=4.30 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-1134, delta=10, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1114, delta=62, z=-3.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.73 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.82 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1370** (n=669, 2026-09-17T07:15:37.343215Z)
- `FUELINST|fuelType=NPSHYD|generation` = **417** (n=669, 2026-09-17T07:15:37.343215Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=669, 2026-09-17T07:15:37.343215Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=669, 2026-09-17T07:15:37.343215Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=669, 2026-09-17T07:15:37.343215Z)
- `FUELINST|fuelType=OTHER|generation` = **459** (n=669, 2026-09-17T07:15:37.343215Z)
- `FUELINST|fuelType=PS|generation` = **223** (n=669, 2026-09-17T07:15:37.343215Z)
- `FUELINST|fuelType=WIND|generation` = **14080** (n=669, 2026-09-17T07:15:37.343215Z)
- `IMBALNGC|TOTAL|imbalance` = **7338** (n=111, 2026-09-17T06:49:53.327366Z)
- `INDDEM|TOTAL|demand` = **-12129** (n=111, 2026-09-17T06:49:37.422907Z)
- `INDGEN|TOTAL|generation` = **26459** (n=111, 2026-09-17T06:49:37.422907Z)
- `MELNGC|TOTAL|margin` = **35731** (n=111, 2026-09-17T06:48:49.093378Z)
- `NDF|TOTAL|demand` = **18621** (n=114, 2026-09-17T07:16:55.100548Z)
- `TSDF|TOTAL|demand` = **19371** (n=114, 2026-09-17T07:17:11.420731Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T07:17:43.526325Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:42.038927Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:40.564874Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:39.053065Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:37.546271Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:36.061944Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:34.545318Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:33.036699Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:31.410601Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:29.918491Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:28.026949Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:26.556771Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:25.036497Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:23.523580Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:17:22.044700Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
