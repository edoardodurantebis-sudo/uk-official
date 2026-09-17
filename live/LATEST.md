# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T17:38:02.649029Z`  
Current process started UTC: `2026-09-17T17:34:01.920249Z`  
1-second metadata polls in this process: **135**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1407** (n=793, 2026-09-17T17:35:36.042434Z)
- `FUELINST|fuelType=NPSHYD|generation` = **561** (n=793, 2026-09-17T17:35:36.042434Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3316** (n=793, 2026-09-17T17:35:36.042434Z)
- `FUELINST|fuelType=OCGT|generation` = **58** (n=793, 2026-09-17T17:35:36.042434Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=793, 2026-09-17T17:35:36.042434Z)
- `FUELINST|fuelType=OTHER|generation` = **1065** (n=793, 2026-09-17T17:35:36.042434Z)
- `FUELINST|fuelType=PS|generation` = **356** (n=793, 2026-09-17T17:35:36.042434Z)
- `FUELINST|fuelType=WIND|generation` = **14670** (n=793, 2026-09-17T17:35:36.042434Z)
- `IMBALNGC|TOTAL|imbalance` = **9664** (n=131, 2026-09-17T17:23:21.966440Z)
- `INDDEM|TOTAL|demand` = **-11283** (n=131, 2026-09-17T17:23:21.966440Z)
- `INDGEN|TOTAL|generation` = **26478** (n=131, 2026-09-17T17:23:21.966440Z)
- `MELNGC|TOTAL|margin` = **36582** (n=131, 2026-09-17T17:20:41.323525Z)
- `NDF|TOTAL|demand` = **16314** (n=134, 2026-09-17T17:18:17.399296Z)
- `TSDF|TOTAL|demand` = **16814** (n=134, 2026-09-17T17:18:17.399296Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T17:38:00.922455Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:58.870479Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:57.133695Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:55.428774Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:53.737935Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:52.040667Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:50.312791Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:48.602139Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:46.898468Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:45.172968Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:43.058959Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:41.300333Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:39.603568Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:37.882517Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:37:36.139132Z` — **MID**: 0 rows; marker `2026-09-17T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
