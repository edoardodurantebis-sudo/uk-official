# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T10:23:03.692470Z`  
Current process started UTC: `2026-09-17T10:19:02.583838Z`  
1-second metadata polls in this process: **141**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-296** (n=706, 2026-09-17T10:20:24.605523Z)
- `FUELINST|fuelType=NPSHYD|generation` = **268** (n=706, 2026-09-17T10:20:24.605523Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=706, 2026-09-17T10:20:24.605523Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=706, 2026-09-17T10:20:24.605523Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=706, 2026-09-17T10:20:24.605523Z)
- `FUELINST|fuelType=OTHER|generation` = **1058** (n=706, 2026-09-17T10:20:24.605523Z)
- `FUELINST|fuelType=PS|generation` = **-940** (n=706, 2026-09-17T10:20:24.605523Z)
- `FUELINST|fuelType=WIND|generation` = **15675** (n=706, 2026-09-17T10:20:24.605523Z)
- `IMBALNGC|TOTAL|imbalance` = **6691** (n=117, 2026-09-17T10:20:07.587303Z)
- `INDDEM|TOTAL|demand` = **-13036** (n=117, 2026-09-17T10:19:50.932861Z)
- `INDGEN|TOTAL|generation` = **26553** (n=117, 2026-09-17T10:19:50.932861Z)
- `MELNGC|TOTAL|margin` = **34438** (n=117, 2026-09-17T10:19:19.197280Z)
- `NDF|TOTAL|demand` = **18256** (n=120, 2026-09-17T10:17:16.694941Z)
- `TSDF|TOTAL|demand` = **19862** (n=120, 2026-09-17T10:17:16.694941Z)
- `WINDFOR|TOTAL|generation` = **19255** (n=20, 2026-09-17T08:30:43.563030Z)

## Latest publication events

- `2026-09-17T10:23:02.100752Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:59.814404Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:58.258253Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:56.641831Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:55.034383Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:52.933412Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:51.330702Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:49.759768Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:48.151547Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:46.546840Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:44.983947Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:43.419698Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:41.839692Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:40.260505Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:22:38.653818Z` — **MID**: 0 rows; marker `2026-09-17T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
