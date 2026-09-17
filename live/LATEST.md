# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T10:35:44.159200Z`  
Current process started UTC: `2026-09-17T10:31:43.357497Z`  
1-second metadata polls in this process: **169**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-296** (n=708, 2026-09-17T10:30:28.835736Z)
- `FUELINST|fuelType=NPSHYD|generation` = **266** (n=708, 2026-09-17T10:30:28.835736Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=708, 2026-09-17T10:30:28.835736Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=708, 2026-09-17T10:30:28.835736Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=708, 2026-09-17T10:30:28.835736Z)
- `FUELINST|fuelType=OTHER|generation` = **978** (n=708, 2026-09-17T10:30:28.835736Z)
- `FUELINST|fuelType=PS|generation` = **-960** (n=708, 2026-09-17T10:30:28.835736Z)
- `FUELINST|fuelType=WIND|generation` = **15918** (n=708, 2026-09-17T10:30:28.835736Z)
- `IMBALNGC|TOTAL|imbalance` = **6691** (n=117, 2026-09-17T10:20:07.587303Z)
- `INDDEM|TOTAL|demand` = **-13036** (n=117, 2026-09-17T10:19:50.932861Z)
- `INDGEN|TOTAL|generation` = **26553** (n=117, 2026-09-17T10:19:50.932861Z)
- `MELNGC|TOTAL|margin` = **34438** (n=117, 2026-09-17T10:19:19.197280Z)
- `NDF|TOTAL|demand` = **18256** (n=120, 2026-09-17T10:17:16.694941Z)
- `TSDF|TOTAL|demand` = **19862** (n=120, 2026-09-17T10:17:16.694941Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T10:35:42.863070Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:41.573048Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:40.284745Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:38.981029Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:37.697567Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:36.435879Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:35.146659Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:33.823015Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:32.509484Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:31.205502Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:29.465743Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:28.194631Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:26.908082Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:25.547083Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:35:24.245247Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
