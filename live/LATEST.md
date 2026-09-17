# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T17:59:06.845319Z`  
Current process started UTC: `2026-09-17T17:55:06.034767Z`  
1-second metadata polls in this process: **148**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1407** (n=797, 2026-09-17T17:55:27.346046Z)
- `FUELINST|fuelType=NPSHYD|generation` = **605** (n=797, 2026-09-17T17:55:27.346046Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=797, 2026-09-17T17:55:27.346046Z)
- `FUELINST|fuelType=OCGT|generation` = **9** (n=797, 2026-09-17T17:55:27.346046Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=797, 2026-09-17T17:55:27.346046Z)
- `FUELINST|fuelType=OTHER|generation` = **1158** (n=797, 2026-09-17T17:55:27.346046Z)
- `FUELINST|fuelType=PS|generation` = **355** (n=797, 2026-09-17T17:55:27.346046Z)
- `FUELINST|fuelType=WIND|generation` = **14624** (n=797, 2026-09-17T17:55:27.346046Z)
- `IMBALNGC|TOTAL|imbalance` = **9672** (n=132, 2026-09-17T17:53:48.152872Z)
- `INDDEM|TOTAL|demand` = **-11283** (n=132, 2026-09-17T17:53:16.406856Z)
- `INDGEN|TOTAL|generation` = **26486** (n=132, 2026-09-17T17:53:16.406856Z)
- `MELNGC|TOTAL|margin` = **36603** (n=132, 2026-09-17T17:50:54.490629Z)
- `NDF|TOTAL|demand` = **16314** (n=135, 2026-09-17T17:48:35.747451Z)
- `TSDF|TOTAL|demand` = **16814** (n=135, 2026-09-17T17:48:35.747451Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T17:59:05.287685Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:59:03.718898Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:59:02.155489Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:59:00.553813Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:58:58.988186Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:58:57.441967Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:58:55.560422Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:58:54.008508Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:58:52.403261Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:58:50.859651Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:58:49.318547Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:58:47.774513Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:58:46.169200Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:58:44.615629Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:58:43.043389Z` — **MID**: 0 rows; marker `2026-09-17T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
