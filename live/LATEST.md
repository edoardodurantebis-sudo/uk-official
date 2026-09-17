# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T17:54:55.700098Z`  
Current process started UTC: `2026-09-17T17:50:54.490619Z`  
1-second metadata polls in this process: **220**  
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
- `IMBALNGC|TOTAL|imbalance` = **9672** (n=132, 2026-09-17T17:53:48.152872Z)
- `INDDEM|TOTAL|demand` = **-11283** (n=132, 2026-09-17T17:53:16.406856Z)
- `INDGEN|TOTAL|generation` = **26486** (n=132, 2026-09-17T17:53:16.406856Z)
- `MELNGC|TOTAL|margin` = **36603** (n=132, 2026-09-17T17:50:54.490629Z)
- `NDF|TOTAL|demand` = **16314** (n=135, 2026-09-17T17:48:35.747451Z)
- `TSDF|TOTAL|demand` = **16814** (n=135, 2026-09-17T17:48:35.747451Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T17:54:54.241587Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:53.241517Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:52.224154Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:51.217800Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:50.203559Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:49.144284Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:48.139471Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:47.139415Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:46.132925Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:45.102026Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:44.101950Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:43.098116Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:42.093634Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:41.089810Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:54:40.076582Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
