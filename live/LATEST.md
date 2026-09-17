# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T18:53:45.992063Z`  
Current process started UTC: `2026-09-17T18:49:45.928295Z`  
1-second metadata polls in this process: **174**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=-2, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=81, delta=-2, z=4.34 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=82, delta=45, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=-1, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=84, delta=7, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=77, delta=66, z=4.46 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=58, delta=2, z=3.72 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.55 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=808, 2026-09-17T18:50:34.530738Z)
- `FUELINST|fuelType=NPSHYD|generation` = **630** (n=808, 2026-09-17T18:50:34.530738Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3321** (n=808, 2026-09-17T18:50:34.530738Z)
- `FUELINST|fuelType=OCGT|generation` = **79** (n=808, 2026-09-17T18:50:34.530738Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=808, 2026-09-17T18:50:34.530738Z)
- `FUELINST|fuelType=OTHER|generation` = **1687** (n=808, 2026-09-17T18:50:34.530738Z)
- `FUELINST|fuelType=PS|generation` = **278** (n=808, 2026-09-17T18:50:34.530738Z)
- `FUELINST|fuelType=WIND|generation` = **15129** (n=808, 2026-09-17T18:50:34.530738Z)
- `IMBALNGC|TOTAL|imbalance` = **9682** (n=133, 2026-09-17T18:24:32.722523Z)
- `INDDEM|TOTAL|demand` = **-11254** (n=133, 2026-09-17T18:24:12.670545Z)
- `INDGEN|TOTAL|generation` = **26496** (n=133, 2026-09-17T18:24:12.670545Z)
- `MELNGC|TOTAL|margin` = **36584** (n=134, 2026-09-17T18:51:06.144242Z)
- `NDF|TOTAL|demand` = **16314** (n=137, 2026-09-17T18:48:33.698047Z)
- `TSDF|TOTAL|demand` = **16814** (n=137, 2026-09-17T18:48:33.698047Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T18:53:44.656392Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:43.370898Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:42.013166Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:40.720672Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:39.385709Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:38.065875Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:36.743552Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:35.417558Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:34.031366Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:32.705575Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:31.087003Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:29.758160Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:28.461426Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:27.111237Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:53:25.674478Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
