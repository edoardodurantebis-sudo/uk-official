# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T21:41:52.468272Z`  
Current process started UTC: `2026-09-17T21:37:51.745039Z`  
1-second metadata polls in this process: **189**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=80, delta=-38, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=118, delta=27, z=6.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **424** (n=842, 2026-09-17T21:40:34.373753Z)
- `FUELINST|fuelType=NPSHYD|generation` = **493** (n=842, 2026-09-17T21:40:34.373753Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=842, 2026-09-17T21:40:34.373753Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=842, 2026-09-17T21:40:34.373753Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=842, 2026-09-17T21:40:34.373753Z)
- `FUELINST|fuelType=OTHER|generation` = **1002** (n=842, 2026-09-17T21:40:34.373753Z)
- `FUELINST|fuelType=PS|generation` = **51** (n=842, 2026-09-17T21:40:34.373753Z)
- `FUELINST|fuelType=WIND|generation` = **14685** (n=842, 2026-09-17T21:40:34.373753Z)
- `IMBALNGC|TOTAL|imbalance` = **9702** (n=139, 2026-09-17T21:23:13.923147Z)
- `INDDEM|TOTAL|demand` = **-11159** (n=139, 2026-09-17T21:23:13.923147Z)
- `INDGEN|TOTAL|generation` = **26516** (n=139, 2026-09-17T21:23:13.923147Z)
- `MELNGC|TOTAL|margin` = **36445** (n=139, 2026-09-17T21:20:23.938551Z)
- `NDF|TOTAL|demand` = **16314** (n=142, 2026-09-17T21:17:59.034802Z)
- `TSDF|TOTAL|demand` = **16814** (n=142, 2026-09-17T21:17:59.034802Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T21:41:51.265677Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:50.004622Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:48.761225Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:47.520959Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:46.320334Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:45.077923Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:43.843987Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:42.583312Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:41.359689Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:39.714620Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:38.505778Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:37.291774Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:36.118969Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:34.918120Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T21:41:33.722729Z` — **MID**: 0 rows; marker `2026-09-17T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
