# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T07:48:27.344898Z`  
Current process started UTC: `2026-09-18T07:44:26.355821Z`  
1-second metadata polls in this process: **187**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=963, 2026-09-18T07:45:47.849394Z)
- `FUELINST|fuelType=NPSHYD|generation` = **376** (n=963, 2026-09-18T07:45:47.849394Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=963, 2026-09-18T07:45:47.849394Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=963, 2026-09-18T07:45:47.849394Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=963, 2026-09-18T07:45:47.849394Z)
- `FUELINST|fuelType=OTHER|generation` = **1357** (n=963, 2026-09-18T07:45:47.849394Z)
- `FUELINST|fuelType=PS|generation` = **598** (n=963, 2026-09-18T07:45:47.849394Z)
- `FUELINST|fuelType=WIND|generation` = **12423** (n=963, 2026-09-18T07:45:47.849394Z)
- `IMBALNGC|TOTAL|imbalance` = **10218** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDDEM|TOTAL|demand` = **-11739** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDGEN|TOTAL|generation` = **27722** (n=159, 2026-09-18T07:19:58.374346Z)
- `MELNGC|TOTAL|margin` = **37765** (n=159, 2026-09-18T07:19:09.419948Z)
- `NDF|TOTAL|demand` = **15870** (n=163, 2026-09-18T07:46:04.858619Z)
- `TSDF|TOTAL|demand` = **16370** (n=163, 2026-09-18T07:46:04.858619Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T07:48:26.169969Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:24.964765Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:23.753407Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:22.556059Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:21.401635Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:20.086271Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:18.887232Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:17.712002Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:15.002922Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:15.002922Z` — **FREQ**: 5761 rows; marker `2026-09-18T07:47:45Z`
- `2026-09-18T07:48:13.794366Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:12.616444Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:11.418331Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:10.196862Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:48:09.026545Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
