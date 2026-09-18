# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T00:59:16.442619Z`  
Current process started UTC: `2026-09-18T00:55:15.985535Z`  
1-second metadata polls in this process: **193**  
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

- `FUELINST|fuelType=INTVKL|generation` = **893** (n=881, 2026-09-18T00:55:33.471472Z)
- `FUELINST|fuelType=NPSHYD|generation` = **445** (n=881, 2026-09-18T00:55:33.471472Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=881, 2026-09-18T00:55:33.471472Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=881, 2026-09-18T00:55:33.471472Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=881, 2026-09-18T00:55:33.471472Z)
- `FUELINST|fuelType=OTHER|generation` = **296** (n=881, 2026-09-18T00:55:33.471472Z)
- `FUELINST|fuelType=PS|generation` = **296** (n=881, 2026-09-18T00:55:33.471472Z)
- `FUELINST|fuelType=WIND|generation` = **14095** (n=881, 2026-09-18T00:55:33.471472Z)
- `IMBALNGC|TOTAL|imbalance` = **10129** (n=146, 2026-09-18T00:52:58.334256Z)
- `INDDEM|TOTAL|demand` = **-11223** (n=146, 2026-09-18T00:52:41.814421Z)
- `INDGEN|TOTAL|generation` = **26943** (n=146, 2026-09-18T00:52:41.814421Z)
- `MELNGC|TOTAL|margin` = **36604** (n=146, 2026-09-18T00:50:24.422617Z)
- `NDF|TOTAL|demand` = **16314** (n=149, 2026-09-18T00:47:57.164547Z)
- `TSDF|TOTAL|demand` = **16814** (n=149, 2026-09-18T00:47:57.164547Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T00:59:15.244474Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:14.065194Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:12.876895Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:11.713705Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:10.535658Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:09.331192Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:08.179169Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:07.019468Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:05.827826Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:04.647365Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:03.480322Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:02.316969Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:59:00.667651Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:58:59.487575Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:58:58.300418Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
