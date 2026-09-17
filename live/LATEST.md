# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T10:31:30.035977Z`  
Current process started UTC: `2026-09-17T10:27:28.903314Z`  
1-second metadata polls in this process: **129**  
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

- `2026-09-17T10:31:28.274648Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:26.531599Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:24.628434Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:22.836449Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:20.775506Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:18.519165Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:16.294186Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:14.527232Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:12.784946Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:10.895947Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:09.127477Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:07.327637Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:05.632831Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:03.841768Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:31:01.443065Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
