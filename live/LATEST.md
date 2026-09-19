# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T09:08:46.154728Z`  
Current process started UTC: `2026-09-19T09:04:45.222527Z`  
1-second metadata polls in this process: **156**  
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

- `FUELINST|fuelType=INTVKL|generation` = **649** (n=1223, 2026-09-19T09:05:38.163195Z)
- `FUELINST|fuelType=NPSHYD|generation` = **337** (n=1223, 2026-09-19T09:05:38.163195Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=1223, 2026-09-19T09:05:38.163195Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1223, 2026-09-19T09:05:38.163195Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1223, 2026-09-19T09:05:38.163195Z)
- `FUELINST|fuelType=OTHER|generation` = **463** (n=1223, 2026-09-19T09:05:38.163195Z)
- `FUELINST|fuelType=PS|generation` = **-680** (n=1223, 2026-09-19T09:05:38.163195Z)
- `FUELINST|fuelType=WIND|generation` = **15071** (n=1223, 2026-09-19T09:05:38.163195Z)
- `IMBALNGC|TOTAL|imbalance` = **8932** (n=201, 2026-09-19T08:50:08.297112Z)
- `INDDEM|TOTAL|demand` = **-12086** (n=201, 2026-09-19T08:50:08.297112Z)
- `INDGEN|TOTAL|generation` = **26734** (n=201, 2026-09-19T08:50:08.297112Z)
- `MELNGC|TOTAL|margin` = **37592** (n=201, 2026-09-19T08:49:20.449715Z)
- `NDF|TOTAL|demand` = **15940** (n=206, 2026-09-19T08:47:31.231970Z)
- `TSDF|TOTAL|demand` = **17802** (n=206, 2026-09-19T08:47:59.721944Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T09:08:44.567587Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:43.102486Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:41.115166Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:39.628249Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:38.153768Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:36.688384Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:35.214411Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:33.752535Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:32.272453Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:30.797927Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:29.320187Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:27.851683Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:24.596537Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:08:24.596537Z` — **FREQ**: 5761 rows; marker `2026-09-19T09:07:45Z`
- `2026-09-19T09:08:23.127001Z` — **MID**: 0 rows; marker `2026-09-19T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
