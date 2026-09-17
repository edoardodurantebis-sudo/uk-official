# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T17:04:23.691633Z`  
Current process started UTC: `2026-09-17T17:00:22.999613Z`  
1-second metadata polls in this process: **225**  
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

- `FUELINST|fuelType=INTVKL|generation` = **682** (n=786, 2026-09-17T17:00:38.690977Z)
- `FUELINST|fuelType=NPSHYD|generation` = **434** (n=786, 2026-09-17T17:00:38.690977Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3313** (n=786, 2026-09-17T17:00:38.690977Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=786, 2026-09-17T17:00:38.690977Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=786, 2026-09-17T17:00:38.690977Z)
- `FUELINST|fuelType=OTHER|generation` = **988** (n=786, 2026-09-17T17:00:38.690977Z)
- `FUELINST|fuelType=PS|generation` = **352** (n=786, 2026-09-17T17:00:38.690977Z)
- `FUELINST|fuelType=WIND|generation` = **14379** (n=786, 2026-09-17T17:00:38.690977Z)
- `IMBALNGC|TOTAL|imbalance` = **11597** (n=130, 2026-09-17T16:54:05.472885Z)
- `INDDEM|TOTAL|demand` = **-11282** (n=130, 2026-09-17T16:53:49.929273Z)
- `INDGEN|TOTAL|generation` = **28411** (n=130, 2026-09-17T16:53:49.929273Z)
- `MELNGC|TOTAL|margin` = **36588** (n=130, 2026-09-17T16:50:53.787200Z)
- `NDF|TOTAL|demand` = **16314** (n=133, 2026-09-17T16:48:29.094169Z)
- `TSDF|TOTAL|demand` = **16814** (n=133, 2026-09-17T16:48:29.094169Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T17:04:21.190941Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:21.190941Z` — **FREQ**: 5761 rows; marker `2026-09-17T17:03:45Z`
- `2026-09-17T17:04:20.190829Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:19.190669Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:18.190558Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:17.190445Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:16.173568Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:15.173457Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:14.173343Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:13.173247Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:12.173126Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:11.173053Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:09.366770Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:08.366657Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T17:04:06.880044Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
