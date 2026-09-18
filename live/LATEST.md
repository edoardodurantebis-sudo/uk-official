# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T21:44:41.916014Z`  
Current process started UTC: `2026-09-18T21:40:41.608906Z`  
1-second metadata polls in this process: **168**  
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

- `FUELINST|fuelType=INTVKL|generation` = **696** (n=1086, 2026-09-18T21:40:41.608914Z)
- `FUELINST|fuelType=NPSHYD|generation` = **427** (n=1086, 2026-09-18T21:40:41.608914Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3345** (n=1086, 2026-09-18T21:40:41.608914Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1086, 2026-09-18T21:40:41.608914Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1086, 2026-09-18T21:40:41.608914Z)
- `FUELINST|fuelType=OTHER|generation` = **368** (n=1086, 2026-09-18T21:40:41.608914Z)
- `FUELINST|fuelType=PS|generation` = **113** (n=1086, 2026-09-18T21:40:41.608914Z)
- `FUELINST|fuelType=WIND|generation` = **16895** (n=1086, 2026-09-18T21:40:41.608914Z)
- `IMBALNGC|TOTAL|imbalance` = **9049** (n=179, 2026-09-18T19:52:38.744964Z)
- `INDDEM|TOTAL|demand` = **-10891** (n=179, 2026-09-18T19:52:38.744964Z)
- `INDGEN|TOTAL|generation` = **26243** (n=179, 2026-09-18T19:52:38.744964Z)
- `MELNGC|TOTAL|margin` = **37531** (n=179, 2026-09-18T19:49:58.654655Z)
- `NDF|TOTAL|demand` = **16550** (n=183, 2026-09-18T19:47:55.702271Z)
- `TSDF|TOTAL|demand` = **17194** (n=183, 2026-09-18T19:47:55.702271Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T21:44:40.602220Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:39.233743Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:37.914616Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:36.610200Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:35.293788Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:33.955493Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:32.657295Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:30.522011Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:29.205061Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:27.851531Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:26.503755Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:25.212732Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:23.839686Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:22.485530Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T21:44:21.148212Z` — **MID**: 0 rows; marker `2026-09-18T21:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
