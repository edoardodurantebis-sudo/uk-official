# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T08:09:29.089765Z`  
Current process started UTC: `2026-09-18T08:05:28.492506Z`  
1-second metadata polls in this process: **132**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=967, 2026-09-18T08:05:30.302326Z)
- `FUELINST|fuelType=NPSHYD|generation` = **379** (n=967, 2026-09-18T08:05:30.302326Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=967, 2026-09-18T08:05:30.302326Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=967, 2026-09-18T08:05:30.302326Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=967, 2026-09-18T08:05:30.302326Z)
- `FUELINST|fuelType=OTHER|generation` = **1339** (n=967, 2026-09-18T08:05:30.302326Z)
- `FUELINST|fuelType=PS|generation` = **322** (n=967, 2026-09-18T08:05:30.302326Z)
- `FUELINST|fuelType=WIND|generation` = **12550** (n=967, 2026-09-18T08:05:30.302326Z)
- `IMBALNGC|TOTAL|imbalance` = **10218** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDDEM|TOTAL|demand` = **-11739** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDGEN|TOTAL|generation` = **27722** (n=159, 2026-09-18T07:19:58.374346Z)
- `MELNGC|TOTAL|margin` = **37765** (n=159, 2026-09-18T07:19:09.419948Z)
- `NDF|TOTAL|demand` = **15870** (n=163, 2026-09-18T07:46:04.858619Z)
- `TSDF|TOTAL|demand` = **16370** (n=163, 2026-09-18T07:46:04.858619Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T08:09:27.145212Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:25.419811Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:23.681175Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:21.840902Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:20.106557Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:18.369573Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:16.208296Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:14.475767Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:12.713914Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:11.008198Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:09.281578Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:07.558393Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:05.844517Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:04.057596Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:09:02.355213Z` — **MID**: 0 rows; marker `2026-09-18T08:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
