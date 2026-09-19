# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T21:55:47.858834Z`  
Current process started UTC: `2026-09-19T21:51:47.802626Z`  
1-second metadata polls in this process: **227**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=94, delta=-6, z=4.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=-378, z=-0.09 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=92, delta=-14, z=4.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.97 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=5.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=1, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=-250, z=-0.07 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=100, delta=4, z=5.22 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=378, delta=4, z=13.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=105, delta=5, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=251, delta=-152, z=6.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=100, delta=1, z=4.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=11.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.84 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1377, 2026-09-19T21:55:34.954788Z)
- `FUELINST|fuelType=NPSHYD|generation` = **454** (n=1377, 2026-09-19T21:55:34.954788Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1377, 2026-09-19T21:55:34.954788Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1377, 2026-09-19T21:55:34.954788Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1377, 2026-09-19T21:55:34.954788Z)
- `FUELINST|fuelType=OTHER|generation` = **251** (n=1377, 2026-09-19T21:55:34.954788Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1377, 2026-09-19T21:55:34.954788Z)
- `FUELINST|fuelType=WIND|generation` = **15003** (n=1377, 2026-09-19T21:55:34.954788Z)
- `IMBALNGC|TOTAL|imbalance` = **-3893** (n=227, 2026-09-19T21:52:20.831514Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=227, 2026-09-19T21:52:04.466257Z)
- `INDGEN|TOTAL|generation` = **16059** (n=227, 2026-09-19T21:52:20.831514Z)
- `MELNGC|TOTAL|margin` = **36067** (n=227, 2026-09-19T21:50:19.664425Z)
- `NDF|TOTAL|demand` = **19452** (n=232, 2026-09-19T21:48:07.682988Z)
- `TSDF|TOTAL|demand` = **19952** (n=232, 2026-09-19T21:48:07.682988Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T21:55:46.895614Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:45.895504Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:44.895400Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:43.895283Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:42.895171Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:41.895054Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:40.894935Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:39.894819Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:38.894700Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:37.894621Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:36.894508Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:34.954788Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:34.954788Z` — **FUELINST**: 80 rows; marker `2026-09-19T21:55:00Z`
- `2026-09-19T21:55:33.954661Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:55:32.954541Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
