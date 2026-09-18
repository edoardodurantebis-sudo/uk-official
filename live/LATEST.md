# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T03:11:05.260800Z`  
Current process started UTC: `2026-09-18T03:07:04.140915Z`  
1-second metadata polls in this process: **133**  
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

- `FUELINST|fuelType=INTVKL|generation` = **987** (n=908, 2026-09-18T03:10:32.244746Z)
- `FUELINST|fuelType=NPSHYD|generation` = **406** (n=908, 2026-09-18T03:10:32.244746Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=908, 2026-09-18T03:10:32.244746Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=908, 2026-09-18T03:10:32.244746Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=908, 2026-09-18T03:10:32.244746Z)
- `FUELINST|fuelType=OTHER|generation` = **506** (n=908, 2026-09-18T03:10:32.244746Z)
- `FUELINST|fuelType=PS|generation` = **513** (n=908, 2026-09-18T03:10:32.244746Z)
- `FUELINST|fuelType=WIND|generation` = **13699** (n=908, 2026-09-18T03:10:32.244746Z)
- `IMBALNGC|TOTAL|imbalance` = **10172** (n=150, 2026-09-18T02:52:59.574452Z)
- `INDDEM|TOTAL|demand` = **-11243** (n=150, 2026-09-18T02:52:44.009177Z)
- `INDGEN|TOTAL|generation` = **26986** (n=150, 2026-09-18T02:52:44.009177Z)
- `MELNGC|TOTAL|margin` = **38180** (n=150, 2026-09-18T02:50:47.579617Z)
- `NDF|TOTAL|demand` = **16314** (n=153, 2026-09-18T02:48:27.577132Z)
- `TSDF|TOTAL|demand` = **16814** (n=153, 2026-09-18T02:48:44.860725Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T03:11:03.551601Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:11:01.839273Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:11:00.129442Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:57.878686Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:56.189404Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:54.462142Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:52.741140Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:51.047434Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:48.872408Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:47.157536Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:45.438229Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:43.743796Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:42.038067Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:40.344664Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:10:38.644809Z` — **MID**: 0 rows; marker `2026-09-18T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
