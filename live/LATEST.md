# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T10:53:09.373943Z`  
Current process started UTC: `2026-09-17T10:49:09.296601Z`  
1-second metadata polls in this process: **145**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=3, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=1, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=17, z=4.30 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-296** (n=712, 2026-09-17T10:50:31.082037Z)
- `FUELINST|fuelType=NPSHYD|generation` = **269** (n=712, 2026-09-17T10:50:31.082037Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3311** (n=712, 2026-09-17T10:50:31.082037Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=712, 2026-09-17T10:50:31.082037Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=712, 2026-09-17T10:50:31.082037Z)
- `FUELINST|fuelType=OTHER|generation` = **536** (n=712, 2026-09-17T10:50:31.082037Z)
- `FUELINST|fuelType=PS|generation` = **-943** (n=712, 2026-09-17T10:50:31.082037Z)
- `FUELINST|fuelType=WIND|generation` = **15647** (n=712, 2026-09-17T10:50:31.082037Z)
- `IMBALNGC|TOTAL|imbalance` = **6691** (n=117, 2026-09-17T10:20:07.587303Z)
- `INDDEM|TOTAL|demand` = **-13036** (n=117, 2026-09-17T10:19:50.932861Z)
- `INDGEN|TOTAL|generation` = **26553** (n=117, 2026-09-17T10:19:50.932861Z)
- `MELNGC|TOTAL|margin` = **36813** (n=118, 2026-09-17T10:51:20.211901Z)
- `NDF|TOTAL|demand` = **16097** (n=121, 2026-09-17T10:49:09.296610Z)
- `TSDF|TOTAL|demand` = **16597** (n=121, 2026-09-17T10:49:09.296610Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T10:53:07.847199Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:53:06.311026Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:53:04.760308Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:53:03.198207Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:53:01.657334Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:53:00.130611Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:52:58.586638Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:52:57.059623Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:52:55.187345Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:52:53.644935Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:52:52.070092Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:52:50.543508Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:52:48.999083Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:52:47.474058Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:52:45.910768Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
