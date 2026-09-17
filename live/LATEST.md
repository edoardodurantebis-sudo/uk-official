# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T17:08:32.885310Z`  
Current process started UTC: `2026-09-17T17:04:32.923864Z`  
1-second metadata polls in this process: **223**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.13 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1102** (n=787, 2026-09-17T17:05:26.669073Z)
- `FUELINST|fuelType=NPSHYD|generation` = **466** (n=787, 2026-09-17T17:05:26.669073Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=787, 2026-09-17T17:05:26.669073Z)
- `FUELINST|fuelType=OCGT|generation` = **57** (n=787, 2026-09-17T17:05:26.669073Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=787, 2026-09-17T17:05:26.669073Z)
- `FUELINST|fuelType=OTHER|generation` = **1000** (n=787, 2026-09-17T17:05:26.669073Z)
- `FUELINST|fuelType=PS|generation` = **350** (n=787, 2026-09-17T17:05:26.669073Z)
- `FUELINST|fuelType=WIND|generation` = **14429** (n=787, 2026-09-17T17:05:26.669073Z)
- `IMBALNGC|TOTAL|imbalance` = **11597** (n=130, 2026-09-17T16:54:05.472885Z)
- `INDDEM|TOTAL|demand` = **-11282** (n=130, 2026-09-17T16:53:49.929273Z)
- `INDGEN|TOTAL|generation` = **28411** (n=130, 2026-09-17T16:53:49.929273Z)
- `MELNGC|TOTAL|margin` = **36588** (n=130, 2026-09-17T16:50:53.787200Z)
- `NDF|TOTAL|demand` = **16314** (n=133, 2026-09-17T16:48:29.094169Z)
- `TSDF|TOTAL|demand` = **16814** (n=133, 2026-09-17T16:48:29.094169Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T17:08:31.929997Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:30.929911Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:29.929836Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:28.929723Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:27.920529Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:26.920408Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:25.920282Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:24.920162Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:23.920053Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:21.602513Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:21.602513Z` — **FREQ**: 5761 rows; marker `2026-09-17T17:07:45Z`
- `2026-09-17T17:08:20.602386Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:19.602269Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:18.602138Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:08:17.602058Z` — **MID**: 0 rows; marker `2026-09-17T17:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
