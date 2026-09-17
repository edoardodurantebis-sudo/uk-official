# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T09:45:11.479805Z`  
Current process started UTC: `2026-09-17T09:41:11.103658Z`  
1-second metadata polls in this process: **229**  
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

- `FUELINST|fuelType=INTVKL|generation` = **741** (n=698, 2026-09-17T09:40:40.772775Z)
- `FUELINST|fuelType=NPSHYD|generation` = **322** (n=698, 2026-09-17T09:40:40.772775Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=698, 2026-09-17T09:40:40.772775Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=698, 2026-09-17T09:40:40.772775Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=698, 2026-09-17T09:40:40.772775Z)
- `FUELINST|fuelType=OTHER|generation` = **704** (n=698, 2026-09-17T09:40:40.772775Z)
- `FUELINST|fuelType=PS|generation` = **-948** (n=698, 2026-09-17T09:40:40.772775Z)
- `FUELINST|fuelType=WIND|generation` = **15698** (n=698, 2026-09-17T09:40:40.772775Z)
- `IMBALNGC|TOTAL|imbalance` = **6637** (n=115, 2026-09-17T09:19:38.465517Z)
- `INDDEM|TOTAL|demand` = **-12983** (n=115, 2026-09-17T09:19:38.465517Z)
- `INDGEN|TOTAL|generation` = **26499** (n=115, 2026-09-17T09:19:38.465517Z)
- `MELNGC|TOTAL|margin` = **34471** (n=115, 2026-09-17T09:18:52.055279Z)
- `NDF|TOTAL|demand` = **18256** (n=118, 2026-09-17T09:16:59.146967Z)
- `TSDF|TOTAL|demand` = **19862** (n=118, 2026-09-17T09:16:59.146967Z)
- `WINDFOR|TOTAL|generation` = **19255** (n=20, 2026-09-17T08:30:43.563030Z)

## Latest publication events

- `2026-09-17T09:45:10.473309Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:45:09.460396Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:45:08.087800Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:45:07.087727Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:45:06.086862Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:45:05.084176Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:45:04.055317Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:45:03.010356Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:45:02.010280Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:45:00.951489Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:44:59.732272Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:44:58.730301Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:44:57.724379Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:44:56.724311Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:44:55.724239Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
