# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T03:19:33.248950Z`  
Current process started UTC: `2026-09-18T03:15:32.077495Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **987** (n=909, 2026-09-18T03:15:33.928806Z)
- `FUELINST|fuelType=NPSHYD|generation` = **404** (n=909, 2026-09-18T03:15:33.928806Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=909, 2026-09-18T03:15:33.928806Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=909, 2026-09-18T03:15:33.928806Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=909, 2026-09-18T03:15:33.928806Z)
- `FUELINST|fuelType=OTHER|generation` = **487** (n=909, 2026-09-18T03:15:33.928806Z)
- `FUELINST|fuelType=PS|generation` = **463** (n=909, 2026-09-18T03:15:33.928806Z)
- `FUELINST|fuelType=WIND|generation` = **13618** (n=909, 2026-09-18T03:15:33.928806Z)
- `IMBALNGC|TOTAL|imbalance` = **10172** (n=150, 2026-09-18T02:52:59.574452Z)
- `INDDEM|TOTAL|demand` = **-11243** (n=150, 2026-09-18T02:52:44.009177Z)
- `INDGEN|TOTAL|generation` = **26986** (n=150, 2026-09-18T02:52:44.009177Z)
- `MELNGC|TOTAL|margin` = **38180** (n=150, 2026-09-18T02:50:47.579617Z)
- `NDF|TOTAL|demand` = **16314** (n=154, 2026-09-18T03:17:28.449836Z)
- `TSDF|TOTAL|demand` = **16814** (n=154, 2026-09-18T03:17:28.449836Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T03:19:31.580685Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:29.684623Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:28.016624Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:26.188430Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:24.535245Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:22.432909Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:20.312949Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:18.288266Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:16.179191Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:14.416512Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:12.499838Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:10.819561Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:08.411116Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:06.041553Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:19:04.128462Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
