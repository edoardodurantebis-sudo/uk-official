# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T03:48:59.188226Z`  
Current process started UTC: `2026-09-18T03:44:58.106967Z`  
1-second metadata polls in this process: **133**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **WINDFOR** `TOTAL` `generation` — wind forecast [TOTAL] generation: value=7845, delta=-11023, z=-4.38 -> renewable cushion down / residual-load pressure up
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **990** (n=915, 2026-09-18T03:45:47.549542Z)
- `FUELINST|fuelType=NPSHYD|generation` = **405** (n=915, 2026-09-18T03:45:47.549542Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=915, 2026-09-18T03:45:47.549542Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=915, 2026-09-18T03:45:47.549542Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=915, 2026-09-18T03:45:47.549542Z)
- `FUELINST|fuelType=OTHER|generation` = **150** (n=915, 2026-09-18T03:45:47.549542Z)
- `FUELINST|fuelType=PS|generation` = **227** (n=915, 2026-09-18T03:45:47.549542Z)
- `FUELINST|fuelType=WIND|generation` = **13658** (n=915, 2026-09-18T03:45:47.549542Z)
- `IMBALNGC|TOTAL|imbalance` = **10169** (n=151, 2026-09-18T03:21:23.504107Z)
- `INDDEM|TOTAL|demand` = **-11249** (n=151, 2026-09-18T03:21:23.504107Z)
- `INDGEN|TOTAL|generation` = **26983** (n=151, 2026-09-18T03:21:23.504107Z)
- `MELNGC|TOTAL|margin` = **38166** (n=151, 2026-09-18T03:19:45.452751Z)
- `NDF|TOTAL|demand` = **16314** (n=155, 2026-09-18T03:48:12.841517Z)
- `TSDF|TOTAL|demand` = **16814** (n=155, 2026-09-18T03:47:55.952290Z)
- `WINDFOR|TOTAL|generation` = **7845** (n=26, 2026-09-18T03:30:37.036559Z)

## Latest publication events

- `2026-09-18T03:48:57.175205Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:55.610957Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:53.899192Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:52.113100Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:50.281369Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:48.393584Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:46.081145Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:44.401082Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:42.565754Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:40.831708Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:38.760781Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:37.198298Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:35.482441Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:33.450318Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:48:31.843313Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
