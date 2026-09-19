# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T01:55:24.133241Z`  
Current process started UTC: `2026-09-19T01:51:23.194168Z`  
1-second metadata polls in this process: **136**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-604** (n=1136, 2026-09-19T01:50:45.284209Z)
- `FUELINST|fuelType=NPSHYD|generation` = **370** (n=1136, 2026-09-19T01:50:45.284209Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1136, 2026-09-19T01:50:45.284209Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1136, 2026-09-19T01:50:45.284209Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1136, 2026-09-19T01:50:45.284209Z)
- `FUELINST|fuelType=OTHER|generation` = **217** (n=1136, 2026-09-19T01:50:45.284209Z)
- `FUELINST|fuelType=PS|generation` = **-825** (n=1136, 2026-09-19T01:50:45.284209Z)
- `FUELINST|fuelType=WIND|generation` = **16448** (n=1136, 2026-09-19T01:50:45.284209Z)
- `IMBALNGC|TOTAL|imbalance` = **9241** (n=188, 2026-09-19T01:51:39.036034Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=188, 2026-09-19T01:51:39.036034Z)
- `INDGEN|TOTAL|generation` = **26435** (n=188, 2026-09-19T01:51:39.036034Z)
- `MELNGC|TOTAL|margin` = **37111** (n=188, 2026-09-19T01:49:54.147817Z)
- `NDF|TOTAL|demand` = **16550** (n=192, 2026-09-19T01:47:41.604873Z)
- `TSDF|TOTAL|demand` = **17194** (n=192, 2026-09-19T01:47:41.604873Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T01:55:22.486311Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:20.810336Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:19.126033Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:17.490481Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:15.837131Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:13.773553Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:12.108895Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:10.468149Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:08.835103Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:07.191823Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:05.545302Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:03.886658Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:02.227396Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:55:00.468184Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:54:58.307626Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
