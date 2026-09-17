# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T09:03:08.348808Z`  
Current process started UTC: `2026-09-17T08:59:08.077053Z`  
1-second metadata polls in this process: **139**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1192** (n=690, 2026-09-17T09:00:46.893223Z)
- `FUELINST|fuelType=NPSHYD|generation` = **417** (n=690, 2026-09-17T09:00:46.893223Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=690, 2026-09-17T09:00:46.893223Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=690, 2026-09-17T09:00:46.893223Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=690, 2026-09-17T09:00:46.893223Z)
- `FUELINST|fuelType=OTHER|generation` = **300** (n=690, 2026-09-17T09:00:46.893223Z)
- `FUELINST|fuelType=PS|generation` = **-774** (n=690, 2026-09-17T09:00:46.893223Z)
- `FUELINST|fuelType=WIND|generation` = **15649** (n=690, 2026-09-17T09:00:46.893223Z)
- `IMBALNGC|TOTAL|imbalance` = **7441** (n=114, 2026-09-17T08:49:36.456573Z)
- `INDDEM|TOTAL|demand` = **-12127** (n=114, 2026-09-17T08:49:19.589745Z)
- `INDGEN|TOTAL|generation` = **26447** (n=114, 2026-09-17T08:49:36.456573Z)
- `MELNGC|TOTAL|margin` = **36058** (n=114, 2026-09-17T08:49:03.558387Z)
- `NDF|TOTAL|demand` = **18256** (n=117, 2026-09-17T08:46:53.329886Z)
- `TSDF|TOTAL|demand` = **19006** (n=117, 2026-09-17T08:46:53.329886Z)
- `WINDFOR|TOTAL|generation` = **19255** (n=20, 2026-09-17T08:30:43.563030Z)

## Latest publication events

- `2026-09-17T09:03:06.575455Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:03:04.777210Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:03:02.996896Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:03:01.208286Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:02:59.076811Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:02:57.475348Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:02:55.857581Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:02:53.666735Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:02:52.089785Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:02:50.284217Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:02:48.646855Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:02:47.093599Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:02:45.500958Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:02:43.054650Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:02:41.383264Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
