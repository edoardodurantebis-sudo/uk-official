# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T09:36:45.322259Z`  
Current process started UTC: `2026-09-17T09:32:44.251194Z`  
1-second metadata polls in this process: **188**  
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

- `FUELINST|fuelType=INTVKL|generation` = **741** (n=697, 2026-09-17T09:35:38.010777Z)
- `FUELINST|fuelType=NPSHYD|generation` = **322** (n=697, 2026-09-17T09:35:38.010777Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3313** (n=697, 2026-09-17T09:35:38.010777Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=697, 2026-09-17T09:35:38.010777Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=697, 2026-09-17T09:35:38.010777Z)
- `FUELINST|fuelType=OTHER|generation` = **847** (n=697, 2026-09-17T09:35:38.010777Z)
- `FUELINST|fuelType=PS|generation` = **-944** (n=697, 2026-09-17T09:35:38.010777Z)
- `FUELINST|fuelType=WIND|generation` = **15730** (n=697, 2026-09-17T09:35:38.010777Z)
- `IMBALNGC|TOTAL|imbalance` = **6637** (n=115, 2026-09-17T09:19:38.465517Z)
- `INDDEM|TOTAL|demand` = **-12983** (n=115, 2026-09-17T09:19:38.465517Z)
- `INDGEN|TOTAL|generation` = **26499** (n=115, 2026-09-17T09:19:38.465517Z)
- `MELNGC|TOTAL|margin` = **34471** (n=115, 2026-09-17T09:18:52.055279Z)
- `NDF|TOTAL|demand` = **18256** (n=118, 2026-09-17T09:16:59.146967Z)
- `TSDF|TOTAL|demand` = **19862** (n=118, 2026-09-17T09:16:59.146967Z)
- `WINDFOR|TOTAL|generation` = **19255** (n=20, 2026-09-17T08:30:43.563030Z)

## Latest publication events

- `2026-09-17T09:36:43.702388Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:42.502261Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:41.295893Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:40.104351Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:38.917977Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:37.730699Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:36.549017Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:35.345132Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:34.169667Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:32.943325Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:31.759411Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:30.563430Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:27.889772Z` — **MID**: 0 rows; marker `2026-09-17T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:36:27.889772Z` — **FREQ**: 5761 rows; marker `2026-09-17T09:35:45Z`
- `2026-09-17T09:36:26.697604Z` — **MID**: 0 rows; marker `2026-09-17T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
