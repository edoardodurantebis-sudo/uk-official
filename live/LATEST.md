# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T03:57:20.295936Z`  
Current process started UTC: `2026-09-18T03:53:19.965431Z`  
1-second metadata polls in this process: **222**  
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

- `FUELINST|fuelType=INTVKL|generation` = **990** (n=917, 2026-09-18T03:55:28.155817Z)
- `FUELINST|fuelType=NPSHYD|generation` = **403** (n=917, 2026-09-18T03:55:28.155817Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=917, 2026-09-18T03:55:28.155817Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=917, 2026-09-18T03:55:28.155817Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=917, 2026-09-18T03:55:28.155817Z)
- `FUELINST|fuelType=OTHER|generation` = **130** (n=917, 2026-09-18T03:55:28.155817Z)
- `FUELINST|fuelType=PS|generation` = **227** (n=917, 2026-09-18T03:55:28.155817Z)
- `FUELINST|fuelType=WIND|generation` = **13737** (n=917, 2026-09-18T03:55:28.155817Z)
- `IMBALNGC|TOTAL|imbalance` = **10690** (n=152, 2026-09-18T03:51:20.747341Z)
- `INDDEM|TOTAL|demand` = **-11249** (n=152, 2026-09-18T03:51:20.747341Z)
- `INDGEN|TOTAL|generation` = **27504** (n=152, 2026-09-18T03:51:20.747341Z)
- `MELNGC|TOTAL|margin` = **38174** (n=152, 2026-09-18T03:49:58.549270Z)
- `NDF|TOTAL|demand` = **16314** (n=155, 2026-09-18T03:48:12.841517Z)
- `TSDF|TOTAL|demand` = **16814** (n=155, 2026-09-18T03:47:55.952290Z)
- `WINDFOR|TOTAL|generation` = **7845** (n=26, 2026-09-18T03:30:37.036559Z)

## Latest publication events

- `2026-09-18T03:57:19.236426Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:18.205333Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:17.201170Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:16.173044Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:15.117080Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:14.092356Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:13.057706Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:12.043316Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:10.797489Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:09.670293Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:08.646203Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:07.507601Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:06.506366Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:05.130229Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:57:04.124973Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
