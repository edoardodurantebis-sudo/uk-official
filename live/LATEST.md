# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T17:50:43.124035Z`  
Current process started UTC: `2026-09-17T17:46:41.862438Z`  
1-second metadata polls in this process: **131**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=58, delta=2, z=3.72 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=52, delta=-3, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.58 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=-2, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=0, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=57, delta=1, z=4.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=14, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.03 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.08 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1407** (n=796, 2026-09-17T17:50:28.038146Z)
- `FUELINST|fuelType=NPSHYD|generation` = **592** (n=796, 2026-09-17T17:50:28.038146Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3319** (n=796, 2026-09-17T17:50:28.038146Z)
- `FUELINST|fuelType=OCGT|generation` = **28** (n=796, 2026-09-17T17:50:28.038146Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=796, 2026-09-17T17:50:28.038146Z)
- `FUELINST|fuelType=OTHER|generation` = **1075** (n=796, 2026-09-17T17:50:28.038146Z)
- `FUELINST|fuelType=PS|generation` = **356** (n=796, 2026-09-17T17:50:28.038146Z)
- `FUELINST|fuelType=WIND|generation` = **14689** (n=796, 2026-09-17T17:50:28.038146Z)
- `IMBALNGC|TOTAL|imbalance` = **9664** (n=131, 2026-09-17T17:23:21.966440Z)
- `INDDEM|TOTAL|demand` = **-11283** (n=131, 2026-09-17T17:23:21.966440Z)
- `INDGEN|TOTAL|generation` = **26478** (n=131, 2026-09-17T17:23:21.966440Z)
- `MELNGC|TOTAL|margin` = **36582** (n=131, 2026-09-17T17:20:41.323525Z)
- `NDF|TOTAL|demand` = **16314** (n=135, 2026-09-17T17:48:35.747451Z)
- `TSDF|TOTAL|demand` = **16814** (n=135, 2026-09-17T17:48:35.747451Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T17:50:41.413579Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:39.695964Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:37.985571Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:36.273091Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:34.562883Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:32.844699Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:30.936536Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:28.038146Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:28.038146Z` — **FUELINST**: 80 rows; marker `2026-09-17T17:50:00Z`
- `2026-09-17T17:50:26.330971Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:24.603664Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:22.883129Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:21.175378Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:19.471465Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:50:17.739370Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
