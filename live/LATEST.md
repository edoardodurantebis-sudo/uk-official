# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T10:54:38.893202Z`  
Current process started UTC: `2026-09-18T10:50:37.279420Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=1000, 2026-09-18T10:50:37.279429Z)
- `FUELINST|fuelType=NPSHYD|generation` = **323** (n=1000, 2026-09-18T10:50:37.279429Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1000, 2026-09-18T10:50:37.279429Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1000, 2026-09-18T10:50:37.279429Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1000, 2026-09-18T10:50:37.279429Z)
- `FUELINST|fuelType=OTHER|generation` = **842** (n=1000, 2026-09-18T10:50:37.279429Z)
- `FUELINST|fuelType=PS|generation` = **-715** (n=1000, 2026-09-18T10:50:37.279429Z)
- `FUELINST|fuelType=WIND|generation` = **12160** (n=1000, 2026-09-18T10:50:37.279429Z)
- `IMBALNGC|TOTAL|imbalance` = **7078** (n=164, 2026-09-18T10:19:52.073787Z)
- `INDDEM|TOTAL|demand` = **-13796** (n=164, 2026-09-18T10:19:35.912100Z)
- `INDGEN|TOTAL|generation` = **26759** (n=164, 2026-09-18T10:19:35.912100Z)
- `MELNGC|TOTAL|margin` = **38126** (n=165, 2026-09-18T10:51:27.792376Z)
- `NDF|TOTAL|demand` = **16170** (n=169, 2026-09-18T10:49:05.046376Z)
- `TSDF|TOTAL|demand` = **16670** (n=169, 2026-09-18T10:49:05.046376Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T10:54:37.156658Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:35.433584Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:33.717290Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:32.008989Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:30.291011Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:28.585755Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:26.511519Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:24.796233Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:23.047940Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:21.336483Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:19.593596Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:17.847008Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:16.148157Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:14.401804Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:54:09.403764Z` — **MID**: 0 rows; marker `2026-09-18T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
