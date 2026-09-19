# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T09:43:31.345559Z`  
Current process started UTC: `2026-09-19T09:39:30.252530Z`  
1-second metadata polls in this process: **157**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-10744, delta=3052, z=1.92 -> demand pressure up
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **560** (n=1230, 2026-09-19T09:40:37.899290Z)
- `FUELINST|fuelType=NPSHYD|generation` = **330** (n=1230, 2026-09-19T09:40:37.899290Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1230, 2026-09-19T09:40:37.899290Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1230, 2026-09-19T09:40:37.899290Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1230, 2026-09-19T09:40:37.899290Z)
- `FUELINST|fuelType=OTHER|generation` = **413** (n=1230, 2026-09-19T09:40:37.899290Z)
- `FUELINST|fuelType=PS|generation` = **-700** (n=1230, 2026-09-19T09:40:37.899290Z)
- `FUELINST|fuelType=WIND|generation` = **15512** (n=1230, 2026-09-19T09:40:37.899290Z)
- `IMBALNGC|TOTAL|imbalance` = **7771** (n=202, 2026-09-19T09:19:44.569379Z)
- `INDDEM|TOTAL|demand` = **-13216** (n=202, 2026-09-19T09:19:44.569379Z)
- `INDGEN|TOTAL|generation` = **26702** (n=202, 2026-09-19T09:19:44.569379Z)
- `MELNGC|TOTAL|margin` = **36478** (n=202, 2026-09-19T09:18:55.905783Z)
- `NDF|TOTAL|demand` = **15940** (n=207, 2026-09-19T09:17:21.692487Z)
- `TSDF|TOTAL|demand` = **18932** (n=207, 2026-09-19T09:17:21.692487Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T09:43:29.857921Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:28.361301Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:26.899373Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:25.419694Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:23.925774Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:22.164650Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:20.712101Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:19.246254Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:17.803893Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:16.345101Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:14.895235Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:13.428317Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:11.946473Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:10.498101Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:43:09.030061Z` — **MID**: 0 rows; marker `2026-09-19T09:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
