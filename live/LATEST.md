# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T09:28:21.132411Z`  
Current process started UTC: `2026-09-17T09:24:20.922714Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16658, delta=-2713, z=-4.41 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16158, delta=-2463, z=-4.57 -> demand pressure easing
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=2, delta=-50, z=-0.16 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=-4, z=3.91 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **741** (n=695, 2026-09-17T09:25:41.032439Z)
- `FUELINST|fuelType=NPSHYD|generation` = **362** (n=695, 2026-09-17T09:25:41.032439Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=695, 2026-09-17T09:25:41.032439Z)
- `FUELINST|fuelType=OCGT|generation` = **1** (n=695, 2026-09-17T09:25:41.032439Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=695, 2026-09-17T09:25:41.032439Z)
- `FUELINST|fuelType=OTHER|generation` = **695** (n=695, 2026-09-17T09:25:41.032439Z)
- `FUELINST|fuelType=PS|generation` = **-946** (n=695, 2026-09-17T09:25:41.032439Z)
- `FUELINST|fuelType=WIND|generation` = **15741** (n=695, 2026-09-17T09:25:41.032439Z)
- `IMBALNGC|TOTAL|imbalance` = **6637** (n=115, 2026-09-17T09:19:38.465517Z)
- `INDDEM|TOTAL|demand` = **-12983** (n=115, 2026-09-17T09:19:38.465517Z)
- `INDGEN|TOTAL|generation` = **26499** (n=115, 2026-09-17T09:19:38.465517Z)
- `MELNGC|TOTAL|margin` = **34471** (n=115, 2026-09-17T09:18:52.055279Z)
- `NDF|TOTAL|demand` = **18256** (n=118, 2026-09-17T09:16:59.146967Z)
- `TSDF|TOTAL|demand` = **19862** (n=118, 2026-09-17T09:16:59.146967Z)
- `WINDFOR|TOTAL|generation` = **19255** (n=20, 2026-09-17T08:30:43.563030Z)

## Latest publication events

- `2026-09-17T09:28:20.168838Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:19.168736Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:18.168636Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:17.168555Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:16.168468Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:15.168367Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:14.168271Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:13.168171Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:12.168068Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:11.168009Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:10.167907Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:09.167804Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:08.167693Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:06.870536Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:28:05.870447Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
