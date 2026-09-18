# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T07:18:56.752628Z`  
Current process started UTC: `2026-09-18T07:14:55.897644Z`  
1-second metadata polls in this process: **151**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=957, 2026-09-18T07:15:29.657151Z)
- `FUELINST|fuelType=NPSHYD|generation` = **378** (n=957, 2026-09-18T07:15:29.657151Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=957, 2026-09-18T07:15:29.657151Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=957, 2026-09-18T07:15:29.657151Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=957, 2026-09-18T07:15:29.657151Z)
- `FUELINST|fuelType=OTHER|generation` = **1573** (n=957, 2026-09-18T07:15:29.657151Z)
- `FUELINST|fuelType=PS|generation` = **644** (n=957, 2026-09-18T07:15:29.657151Z)
- `FUELINST|fuelType=WIND|generation` = **12654** (n=957, 2026-09-18T07:15:29.657151Z)
- `IMBALNGC|TOTAL|imbalance` = **10565** (n=158, 2026-09-18T06:50:20.667031Z)
- `INDDEM|TOTAL|demand` = **-11405** (n=158, 2026-09-18T06:50:04.574079Z)
- `INDGEN|TOTAL|generation` = **27379** (n=158, 2026-09-18T06:50:04.574079Z)
- `MELNGC|TOTAL|margin` = **37954** (n=158, 2026-09-18T06:49:07.667660Z)
- `NDF|TOTAL|demand` = **16314** (n=162, 2026-09-18T07:17:24.178373Z)
- `TSDF|TOTAL|demand` = **17504** (n=162, 2026-09-18T07:17:24.178373Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T07:18:55.138396Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:53.682045Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:52.223374Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:50.777523Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:49.308788Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:47.843940Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:46.012529Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:44.562296Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:43.063110Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:41.602798Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:40.139107Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:38.682601Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:37.226793Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:35.750700Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:18:34.255902Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
