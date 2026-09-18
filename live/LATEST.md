# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T00:34:09.971655Z`  
Current process started UTC: `2026-09-18T00:30:09.447099Z`  
1-second metadata polls in this process: **190**  
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

- `FUELINST|fuelType=INTVKL|generation` = **893** (n=876, 2026-09-18T00:30:41.260471Z)
- `FUELINST|fuelType=NPSHYD|generation` = **446** (n=876, 2026-09-18T00:30:41.260471Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=876, 2026-09-18T00:30:41.260471Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=876, 2026-09-18T00:30:41.260471Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=876, 2026-09-18T00:30:41.260471Z)
- `FUELINST|fuelType=OTHER|generation` = **198** (n=876, 2026-09-18T00:30:41.260471Z)
- `FUELINST|fuelType=PS|generation` = **296** (n=876, 2026-09-18T00:30:41.260471Z)
- `FUELINST|fuelType=WIND|generation` = **14275** (n=876, 2026-09-18T00:30:41.260471Z)
- `IMBALNGC|TOTAL|imbalance` = **10114** (n=145, 2026-09-18T00:22:01.705284Z)
- `INDDEM|TOTAL|demand` = **-11187** (n=145, 2026-09-18T00:21:45.296735Z)
- `INDGEN|TOTAL|generation` = **26928** (n=145, 2026-09-18T00:21:45.296735Z)
- `MELNGC|TOTAL|margin` = **36542** (n=145, 2026-09-18T00:20:30.506045Z)
- `NDF|TOTAL|demand` = **16314** (n=148, 2026-09-18T00:17:48.242066Z)
- `TSDF|TOTAL|demand` = **16814** (n=148, 2026-09-18T00:17:48.242066Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T00:34:08.787926Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:34:07.616331Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:34:06.434748Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:34:05.232322Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:34:04.055299Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:34:02.887068Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:34:01.676351Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:34:00.458761Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:33:59.230256Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:33:57.668494Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:33:56.482548Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:33:55.321243Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:33:54.130567Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:33:52.922393Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:33:51.731094Z` — **MID**: 0 rows; marker `2026-09-18T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
