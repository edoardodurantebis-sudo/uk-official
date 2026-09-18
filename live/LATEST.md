# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T00:55:05.132071Z`  
Current process started UTC: `2026-09-18T00:51:03.805618Z`  
1-second metadata polls in this process: **131**  
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

- `FUELINST|fuelType=INTVKL|generation` = **893** (n=880, 2026-09-18T00:50:41.374331Z)
- `FUELINST|fuelType=NPSHYD|generation` = **449** (n=880, 2026-09-18T00:50:41.374331Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=880, 2026-09-18T00:50:41.374331Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=880, 2026-09-18T00:50:41.374331Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=880, 2026-09-18T00:50:41.374331Z)
- `FUELINST|fuelType=OTHER|generation` = **404** (n=880, 2026-09-18T00:50:41.374331Z)
- `FUELINST|fuelType=PS|generation` = **296** (n=880, 2026-09-18T00:50:41.374331Z)
- `FUELINST|fuelType=WIND|generation` = **14099** (n=880, 2026-09-18T00:50:41.374331Z)
- `IMBALNGC|TOTAL|imbalance` = **10129** (n=146, 2026-09-18T00:52:58.334256Z)
- `INDDEM|TOTAL|demand` = **-11223** (n=146, 2026-09-18T00:52:41.814421Z)
- `INDGEN|TOTAL|generation` = **26943** (n=146, 2026-09-18T00:52:41.814421Z)
- `MELNGC|TOTAL|margin` = **36604** (n=146, 2026-09-18T00:50:24.422617Z)
- `NDF|TOTAL|demand` = **16314** (n=149, 2026-09-18T00:47:57.164547Z)
- `TSDF|TOTAL|demand` = **16814** (n=149, 2026-09-18T00:47:57.164547Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T00:55:03.434049Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:55:01.721198Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:59.998339Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:58.306600Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:56.593052Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:54.894612Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:53.190414Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:50.744406Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:49.028565Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:47.327539Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:45.608735Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:43.910647Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:42.205581Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:40.497953Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:54:38.782188Z` — **MID**: 0 rows; marker `2026-09-18T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
