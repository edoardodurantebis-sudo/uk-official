# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T09:09:00.363274Z`  
Current process started UTC: `2026-09-18T09:04:59.825401Z`  
1-second metadata polls in this process: **171**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=979, 2026-09-18T09:05:31.255113Z)
- `FUELINST|fuelType=NPSHYD|generation` = **344** (n=979, 2026-09-18T09:05:31.255113Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=979, 2026-09-18T09:05:31.255113Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=979, 2026-09-18T09:05:31.255113Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=979, 2026-09-18T09:05:31.255113Z)
- `FUELINST|fuelType=OTHER|generation` = **767** (n=979, 2026-09-18T09:05:31.255113Z)
- `FUELINST|fuelType=PS|generation` = **163** (n=979, 2026-09-18T09:05:31.255113Z)
- `FUELINST|fuelType=WIND|generation` = **11909** (n=979, 2026-09-18T09:05:31.255113Z)
- `IMBALNGC|TOTAL|imbalance` = **9602** (n=161, 2026-09-18T08:50:11.206473Z)
- `INDDEM|TOTAL|demand` = **-11735** (n=161, 2026-09-18T08:50:26.889076Z)
- `INDGEN|TOTAL|generation` = **27246** (n=161, 2026-09-18T08:50:26.889076Z)
- `MELNGC|TOTAL|margin` = **37681** (n=161, 2026-09-18T08:49:38.558944Z)
- `NDF|TOTAL|demand` = **16454** (n=165, 2026-09-18T08:47:27.012958Z)
- `TSDF|TOTAL|demand` = **17644** (n=165, 2026-09-18T08:47:27.012958Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T09:08:58.998816Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:57.707267Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:56.357115Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:54.753944Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:53.436406Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:52.140619Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:50.805116Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:49.449456Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:48.118577Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:46.785931Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:45.088627Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:43.759951Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:42.390012Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:41.067426Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:08:39.724133Z` — **MID**: 0 rows; marker `2026-09-18T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
