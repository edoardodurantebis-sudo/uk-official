# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T12:12:54.154570Z`  
Current process started UTC: `2026-09-17T12:08:53.593977Z`  
1-second metadata polls in this process: **230**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16043, delta=0, z=-3.76 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=0, z=-3.73 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=-54, z=-3.99 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16043, delta=-54, z=-4.02 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11265, delta=1771, z=1.70 -> demand pressure up
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16597, delta=-3265, z=-4.21 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16097, delta=-2159, z=-4.24 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16658, delta=-2713, z=-4.41 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16158, delta=-2463, z=-4.57 -> demand pressure easing
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=2, delta=-50, z=-0.16 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=-4, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.42 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=49, delta=49, z=4.48 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-618** (n=728, 2026-09-17T12:10:29.082801Z)
- `FUELINST|fuelType=NPSHYD|generation` = **252** (n=728, 2026-09-17T12:10:29.082801Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3304** (n=728, 2026-09-17T12:10:29.082801Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=728, 2026-09-17T12:10:29.082801Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=728, 2026-09-17T12:10:29.082801Z)
- `FUELINST|fuelType=OTHER|generation` = **476** (n=728, 2026-09-17T12:10:29.082801Z)
- `FUELINST|fuelType=PS|generation` = **-951** (n=728, 2026-09-17T12:10:29.082801Z)
- `FUELINST|fuelType=WIND|generation` = **14314** (n=728, 2026-09-17T12:10:29.082801Z)
- `IMBALNGC|TOTAL|imbalance` = **11963** (n=120, 2026-09-17T11:53:31.798888Z)
- `INDDEM|TOTAL|demand` = **-11265** (n=120, 2026-09-17T11:53:31.798888Z)
- `INDGEN|TOTAL|generation` = **28506** (n=120, 2026-09-17T11:53:31.798888Z)
- `MELNGC|TOTAL|margin` = **36723** (n=120, 2026-09-17T11:50:23.103050Z)
- `NDF|TOTAL|demand` = **16043** (n=123, 2026-09-17T11:48:45.810334Z)
- `TSDF|TOTAL|demand` = **16543** (n=123, 2026-09-17T11:48:29.902929Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T12:12:52.811394Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:51.811289Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:50.811172Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:49.811070Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:48.810952Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:47.810833Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:46.810759Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:45.810643Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:44.810527Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:43.810410Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:42.810290Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:41.810170Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:40.810086Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:39.809976Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:12:38.809910Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
