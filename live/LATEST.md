# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T21:51:35.989780Z`  
Current process started UTC: `2026-09-19T21:47:34.662152Z`  
1-second metadata polls in this process: **128**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1376, 2026-09-19T21:50:36.487238Z)
- `FUELINST|fuelType=NPSHYD|generation` = **455** (n=1376, 2026-09-19T21:50:36.487238Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1376, 2026-09-19T21:50:36.487238Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1376, 2026-09-19T21:50:36.487238Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1376, 2026-09-19T21:50:36.487238Z)
- `FUELINST|fuelType=OTHER|generation` = **394** (n=1376, 2026-09-19T21:50:36.487238Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=1376, 2026-09-19T21:50:36.487238Z)
- `FUELINST|fuelType=WIND|generation` = **14873** (n=1376, 2026-09-19T21:50:36.487238Z)
- `IMBALNGC|TOTAL|imbalance` = **-3899** (n=226, 2026-09-19T21:22:23.160034Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=226, 2026-09-19T21:22:23.160034Z)
- `INDGEN|TOTAL|generation` = **16053** (n=226, 2026-09-19T21:22:23.160034Z)
- `MELNGC|TOTAL|margin` = **36067** (n=227, 2026-09-19T21:50:19.664425Z)
- `NDF|TOTAL|demand` = **19452** (n=232, 2026-09-19T21:48:07.682988Z)
- `TSDF|TOTAL|demand` = **19952** (n=232, 2026-09-19T21:48:07.682988Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T21:51:34.227649Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:32.522916Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:30.816433Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:29.100358Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:27.394488Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:25.250868Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:23.546779Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:21.841779Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:20.062757Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:18.362907Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:16.665220Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:14.942003Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:12.821763Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:11.096743Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:51:08.487635Z` — **MID**: 0 rows; marker `2026-09-19T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
