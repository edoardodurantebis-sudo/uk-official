# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T07:56:50.866083Z`  
Current process started UTC: `2026-09-18T07:52:48.819135Z`  
1-second metadata polls in this process: **134**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=965, 2026-09-18T07:55:27.374471Z)
- `FUELINST|fuelType=NPSHYD|generation` = **378** (n=965, 2026-09-18T07:55:27.374471Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=965, 2026-09-18T07:55:27.374471Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=965, 2026-09-18T07:55:27.374471Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=965, 2026-09-18T07:55:27.374471Z)
- `FUELINST|fuelType=OTHER|generation` = **1154** (n=965, 2026-09-18T07:55:27.374471Z)
- `FUELINST|fuelType=PS|generation` = **598** (n=965, 2026-09-18T07:55:27.374471Z)
- `FUELINST|fuelType=WIND|generation` = **12445** (n=965, 2026-09-18T07:55:27.374471Z)
- `IMBALNGC|TOTAL|imbalance` = **10218** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDDEM|TOTAL|demand` = **-11739** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDGEN|TOTAL|generation` = **27722** (n=159, 2026-09-18T07:19:58.374346Z)
- `MELNGC|TOTAL|margin` = **37765** (n=159, 2026-09-18T07:19:09.419948Z)
- `NDF|TOTAL|demand` = **15870** (n=163, 2026-09-18T07:46:04.858619Z)
- `TSDF|TOTAL|demand` = **16370** (n=163, 2026-09-18T07:46:04.858619Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T07:56:48.432560Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:46.714502Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:44.984312Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:43.266855Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:41.563265Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:39.869303Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:38.154436Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:36.414063Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:32.711143Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:32.711143Z` — **FREQ**: 5761 rows; marker `2026-09-18T07:55:45Z`
- `2026-09-18T07:56:31.007577Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:29.279907Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:27.570758Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:25.865058Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:56:24.138641Z` — **MID**: 0 rows; marker `2026-09-18T07:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
