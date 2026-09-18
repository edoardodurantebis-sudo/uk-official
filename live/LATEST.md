# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T01:20:09.938601Z`  
Current process started UTC: `2026-09-18T01:16:08.464919Z`  
1-second metadata polls in this process: **127**  
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

- `FUELINST|fuelType=INTVKL|generation` = **781** (n=885, 2026-09-18T01:15:31.702941Z)
- `FUELINST|fuelType=NPSHYD|generation` = **418** (n=885, 2026-09-18T01:15:31.702941Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=885, 2026-09-18T01:15:31.702941Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=885, 2026-09-18T01:15:31.702941Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=885, 2026-09-18T01:15:31.702941Z)
- `FUELINST|fuelType=OTHER|generation` = **206** (n=885, 2026-09-18T01:15:31.702941Z)
- `FUELINST|fuelType=PS|generation` = **532** (n=885, 2026-09-18T01:15:31.702941Z)
- `FUELINST|fuelType=WIND|generation` = **14115** (n=885, 2026-09-18T01:15:31.702941Z)
- `IMBALNGC|TOTAL|imbalance` = **10129** (n=146, 2026-09-18T00:52:58.334256Z)
- `INDDEM|TOTAL|demand` = **-11223** (n=146, 2026-09-18T00:52:41.814421Z)
- `INDGEN|TOTAL|generation` = **26943** (n=146, 2026-09-18T00:52:41.814421Z)
- `MELNGC|TOTAL|margin` = **36604** (n=146, 2026-09-18T00:50:24.422617Z)
- `NDF|TOTAL|demand` = **16314** (n=150, 2026-09-18T01:17:48.779698Z)
- `TSDF|TOTAL|demand` = **16814** (n=150, 2026-09-18T01:17:48.779698Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T01:20:08.109168Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:20:06.393542Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:20:04.694430Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:20:02.929529Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:19:59.643882Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:19:57.930393Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:19:56.231786Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:19:54.516632Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:19:52.799895Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:19:51.089969Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:19:49.387884Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:19:47.680814Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:19:45.963336Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:19:43.841535Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T01:19:42.090659Z` — **MID**: 0 rows; marker `2026-09-18T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
