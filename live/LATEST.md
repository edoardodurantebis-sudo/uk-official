# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T01:51:09.888705Z`  
Current process started UTC: `2026-09-19T01:47:08.880629Z`  
1-second metadata polls in this process: **137**  
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
- `IMBALNGC|TOTAL|imbalance` = **9206** (n=187, 2026-09-19T01:21:41.895741Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=187, 2026-09-19T01:21:41.895741Z)
- `INDGEN|TOTAL|generation` = **26401** (n=187, 2026-09-19T01:21:41.895741Z)
- `MELNGC|TOTAL|margin` = **37111** (n=188, 2026-09-19T01:49:54.147817Z)
- `NDF|TOTAL|demand` = **16550** (n=192, 2026-09-19T01:47:41.604873Z)
- `TSDF|TOTAL|demand` = **17194** (n=192, 2026-09-19T01:47:41.604873Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T01:51:08.225997Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:51:06.438881Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:51:04.855985Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:51:03.167304Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:51:01.111173Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:50:59.497535Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:50:57.824460Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:50:56.200142Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:50:54.653915Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:50:52.916100Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:50:51.318624Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:50:49.713696Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:50:48.027993Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:50:45.284209Z` — **MID**: 0 rows; marker `2026-09-19T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:50:45.284209Z` — **FUELINST**: 80 rows; marker `2026-09-19T01:50:00Z`
