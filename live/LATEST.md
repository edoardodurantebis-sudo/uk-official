# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T11:45:51.150029Z`  
Current process started UTC: `2026-09-19T11:41:49.726368Z`  
1-second metadata polls in this process: **157**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16777, delta=25, z=-3.78 -> state changed
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16752, delta=-9313, z=-3.94 -> state changed
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **333** (n=1255, 2026-09-19T11:45:24.660810Z)
- `FUELINST|fuelType=NPSHYD|generation` = **303** (n=1255, 2026-09-19T11:45:24.660810Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1255, 2026-09-19T11:45:24.660810Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1255, 2026-09-19T11:45:24.660810Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1255, 2026-09-19T11:45:24.660810Z)
- `FUELINST|fuelType=OTHER|generation` = **660** (n=1255, 2026-09-19T11:45:24.660810Z)
- `FUELINST|fuelType=PS|generation` = **-939** (n=1255, 2026-09-19T11:45:24.660810Z)
- `FUELINST|fuelType=WIND|generation` = **15633** (n=1255, 2026-09-19T11:45:24.660810Z)
- `IMBALNGC|TOTAL|imbalance` = **-3354** (n=206, 2026-09-19T11:25:26.544383Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=206, 2026-09-19T11:25:10.722520Z)
- `INDGEN|TOTAL|generation` = **16777** (n=206, 2026-09-19T11:24:54.717962Z)
- `MELNGC|TOTAL|margin` = **36659** (n=206, 2026-09-19T11:21:14.136124Z)
- `NDF|TOTAL|demand` = **19631** (n=211, 2026-09-19T11:18:50.597516Z)
- `TSDF|TOTAL|demand` = **20131** (n=211, 2026-09-19T11:18:50.597516Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T11:45:49.620949Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:48.176754Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:46.557705Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:45.086878Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:43.502741Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:41.644360Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:39.939016Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:38.487306Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:36.892536Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:35.039931Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:33.554095Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:32.060186Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:30.631986Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:29.177970Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:45:27.390129Z` — **MID**: 0 rows; marker `2026-09-19T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
