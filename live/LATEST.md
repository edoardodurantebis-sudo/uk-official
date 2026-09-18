# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T06:32:47.087995Z`  
Current process started UTC: `2026-09-18T06:28:46.620579Z`  
1-second metadata polls in this process: **130**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=948, 2026-09-18T06:30:39.176465Z)
- `FUELINST|fuelType=NPSHYD|generation` = **413** (n=948, 2026-09-18T06:30:39.176465Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=948, 2026-09-18T06:30:39.176465Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=948, 2026-09-18T06:30:39.176465Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=948, 2026-09-18T06:30:39.176465Z)
- `FUELINST|fuelType=OTHER|generation` = **952** (n=948, 2026-09-18T06:30:39.176465Z)
- `FUELINST|fuelType=PS|generation` = **675** (n=948, 2026-09-18T06:30:39.176465Z)
- `FUELINST|fuelType=WIND|generation` = **14437** (n=948, 2026-09-18T06:30:39.176465Z)
- `IMBALNGC|TOTAL|imbalance` = **10652** (n=157, 2026-09-18T06:20:37.859791Z)
- `INDDEM|TOTAL|demand` = **-11168** (n=157, 2026-09-18T06:20:37.859791Z)
- `INDGEN|TOTAL|generation` = **27466** (n=157, 2026-09-18T06:20:37.859791Z)
- `MELNGC|TOTAL|margin` = **37963** (n=157, 2026-09-18T06:19:23.801804Z)
- `NDF|TOTAL|demand` = **16314** (n=160, 2026-09-18T06:17:14.273486Z)
- `TSDF|TOTAL|demand` = **16814** (n=160, 2026-09-18T06:17:14.273486Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T06:32:45.375562Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:43.663847Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:41.877667Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:40.169553Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:38.413488Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:34.534120Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:34.534120Z` — **FREQ**: 5761 rows; marker `2026-09-18T06:31:45Z`
- `2026-09-18T06:32:32.835137Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:31.124732Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:29.419325Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:27.711133Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:25.720427Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:23.983718Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:22.276259Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:32:20.401442Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
