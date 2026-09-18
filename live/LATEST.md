# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T08:34:36.527148Z`  
Current process started UTC: `2026-09-18T08:30:36.379141Z`  
1-second metadata polls in this process: **209**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=972, 2026-09-18T08:30:36.379150Z)
- `FUELINST|fuelType=NPSHYD|generation` = **375** (n=972, 2026-09-18T08:30:36.379150Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=972, 2026-09-18T08:30:36.379150Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=972, 2026-09-18T08:30:36.379150Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=972, 2026-09-18T08:30:36.379150Z)
- `FUELINST|fuelType=OTHER|generation` = **1395** (n=972, 2026-09-18T08:30:36.379150Z)
- `FUELINST|fuelType=PS|generation` = **374** (n=972, 2026-09-18T08:30:36.379150Z)
- `FUELINST|fuelType=WIND|generation` = **12239** (n=972, 2026-09-18T08:30:36.379150Z)
- `IMBALNGC|TOTAL|imbalance` = **9625** (n=160, 2026-09-18T08:20:46.536994Z)
- `INDDEM|TOTAL|demand` = **-11736** (n=160, 2026-09-18T08:20:29.773738Z)
- `INDGEN|TOTAL|generation` = **27269** (n=160, 2026-09-18T08:20:29.773738Z)
- `MELNGC|TOTAL|margin` = **37653** (n=160, 2026-09-18T08:19:40.681819Z)
- `NDF|TOTAL|demand` = **16454** (n=164, 2026-09-18T08:17:38.545846Z)
- `TSDF|TOTAL|demand` = **17644** (n=164, 2026-09-18T08:17:38.545846Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T08:34:35.560358Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:34.560247Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:33.560137Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:32.459884Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:31.459769Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:30.459656Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:29.459576Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:28.443601Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:27.443477Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:26.192102Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:25.192034Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:24.191915Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:23.085821Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:22.085697Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:34:21.085632Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
