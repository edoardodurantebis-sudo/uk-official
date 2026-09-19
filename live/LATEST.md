# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T00:38:55.392299Z`  
Current process started UTC: `2026-09-19T00:34:54.727969Z`  
1-second metadata polls in this process: **144**  
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

- `FUELINST|fuelType=INTVKL|generation` = **126** (n=1121, 2026-09-19T00:35:27.069709Z)
- `FUELINST|fuelType=NPSHYD|generation` = **393** (n=1121, 2026-09-19T00:35:27.069709Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1121, 2026-09-19T00:35:27.069709Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1121, 2026-09-19T00:35:27.069709Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1121, 2026-09-19T00:35:27.069709Z)
- `FUELINST|fuelType=OTHER|generation` = **618** (n=1121, 2026-09-19T00:35:27.069709Z)
- `FUELINST|fuelType=PS|generation` = **-827** (n=1121, 2026-09-19T00:35:27.069709Z)
- `FUELINST|fuelType=WIND|generation` = **16133** (n=1121, 2026-09-19T00:35:27.069709Z)
- `IMBALNGC|TOTAL|imbalance` = **9168** (n=185, 2026-09-19T00:21:52.606846Z)
- `INDDEM|TOTAL|demand` = **-10887** (n=185, 2026-09-19T00:21:36.243148Z)
- `INDGEN|TOTAL|generation` = **26362** (n=185, 2026-09-19T00:21:36.243148Z)
- `MELNGC|TOTAL|margin` = **37515** (n=185, 2026-09-19T00:19:43.103653Z)
- `NDF|TOTAL|demand` = **16550** (n=189, 2026-09-19T00:17:41.916697Z)
- `TSDF|TOTAL|demand` = **17194** (n=189, 2026-09-19T00:17:41.916697Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T00:38:53.811517Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:52.236441Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:50.704553Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:49.143019Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:47.619364Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:45.544636Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:43.996979Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:42.436762Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:40.879191Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:39.319601Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:37.777739Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:36.211552Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:34.659629Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:33.053792Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:38:31.499403Z` — **MID**: 0 rows; marker `2026-09-19T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
