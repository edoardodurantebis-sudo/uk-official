# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T01:59:03.578925Z`  
Current process started UTC: `2026-09-18T01:55:03.141033Z`  
1-second metadata polls in this process: **225**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **781** (n=893, 2026-09-18T01:55:34.559454Z)
- `FUELINST|fuelType=NPSHYD|generation` = **418** (n=893, 2026-09-18T01:55:34.559454Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=893, 2026-09-18T01:55:34.559454Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=893, 2026-09-18T01:55:34.559454Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=893, 2026-09-18T01:55:34.559454Z)
- `FUELINST|fuelType=OTHER|generation` = **91** (n=893, 2026-09-18T01:55:34.559454Z)
- `FUELINST|fuelType=PS|generation` = **369** (n=893, 2026-09-18T01:55:34.559454Z)
- `FUELINST|fuelType=WIND|generation` = **14534** (n=893, 2026-09-18T01:55:34.559454Z)
- `IMBALNGC|TOTAL|imbalance` = **10161** (n=148, 2026-09-18T01:51:40.738117Z)
- `INDDEM|TOTAL|demand` = **-11222** (n=148, 2026-09-18T01:51:24.816933Z)
- `INDGEN|TOTAL|generation` = **26975** (n=148, 2026-09-18T01:51:24.816933Z)
- `MELNGC|TOTAL|margin` = **36705** (n=148, 2026-09-18T01:49:25.897354Z)
- `NDF|TOTAL|demand` = **16314** (n=151, 2026-09-18T01:47:48.325279Z)
- `TSDF|TOTAL|demand` = **16814** (n=151, 2026-09-18T01:47:48.325279Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T01:59:02.562432Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:59:00.876242Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:59.849245Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:58.813582Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:57.771944Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:56.763539Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:55.717936Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:54.714330Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:53.714261Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:52.704823Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:51.604034Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:50.572062Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:49.550043Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:48.534555Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:58:47.534440Z` — **MID**: 0 rows; marker `2026-09-18T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
