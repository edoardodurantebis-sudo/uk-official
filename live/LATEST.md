# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T06:11:42.614939Z`  
Current process started UTC: `2026-09-18T06:07:42.309172Z`  
1-second metadata polls in this process: **231**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=944, 2026-09-18T06:10:42.870531Z)
- `FUELINST|fuelType=NPSHYD|generation` = **460** (n=944, 2026-09-18T06:10:42.870531Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3343** (n=944, 2026-09-18T06:10:42.870531Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=944, 2026-09-18T06:10:42.870531Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=944, 2026-09-18T06:10:42.870531Z)
- `FUELINST|fuelType=OTHER|generation` = **705** (n=944, 2026-09-18T06:10:42.870531Z)
- `FUELINST|fuelType=PS|generation` = **376** (n=944, 2026-09-18T06:10:42.870531Z)
- `FUELINST|fuelType=WIND|generation` = **14342** (n=944, 2026-09-18T06:10:42.870531Z)
- `IMBALNGC|TOTAL|imbalance` = **10719** (n=156, 2026-09-18T05:50:16.495445Z)
- `INDDEM|TOTAL|demand` = **-11168** (n=156, 2026-09-18T05:50:16.495445Z)
- `INDGEN|TOTAL|generation` = **27533** (n=156, 2026-09-18T05:50:16.495445Z)
- `MELNGC|TOTAL|margin` = **38005** (n=156, 2026-09-18T05:49:12.578437Z)
- `NDF|TOTAL|demand` = **16314** (n=159, 2026-09-18T05:47:34.288045Z)
- `TSDF|TOTAL|demand` = **16814** (n=159, 2026-09-18T05:47:18.405461Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T06:11:41.662505Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:40.662421Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:39.662345Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:38.662223Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:37.662085Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:36.661985Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:35.661885Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:34.661768Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:33.661652Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:32.661550Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:31.661440Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:30.378304Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:29.378223Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:28.378144Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:11:27.378023Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
