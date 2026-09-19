# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T21:17:59.767602Z`  
Current process started UTC: `2026-09-19T21:13:59.740846Z`  
1-second metadata polls in this process: **174**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1369, 2026-09-19T21:15:37.456388Z)
- `FUELINST|fuelType=NPSHYD|generation` = **455** (n=1369, 2026-09-19T21:15:37.456388Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1369, 2026-09-19T21:15:37.456388Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1369, 2026-09-19T21:15:37.456388Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1369, 2026-09-19T21:15:37.456388Z)
- `FUELINST|fuelType=OTHER|generation` = **701** (n=1369, 2026-09-19T21:15:37.456388Z)
- `FUELINST|fuelType=PS|generation` = **818** (n=1369, 2026-09-19T21:15:37.456388Z)
- `FUELINST|fuelType=WIND|generation` = **14260** (n=1369, 2026-09-19T21:15:37.456388Z)
- `IMBALNGC|TOTAL|imbalance` = **-3851** (n=225, 2026-09-19T20:52:15.629197Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=225, 2026-09-19T20:51:59.237885Z)
- `INDGEN|TOTAL|generation` = **16101** (n=225, 2026-09-19T20:51:59.237885Z)
- `MELNGC|TOTAL|margin` = **36203** (n=225, 2026-09-19T20:49:35.992012Z)
- `NDF|TOTAL|demand` = **19452** (n=230, 2026-09-19T20:47:50.435946Z)
- `TSDF|TOTAL|demand` = **19952** (n=230, 2026-09-19T20:47:50.435946Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T21:17:58.544902Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:57.244737Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:55.936800Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:54.615926Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:53.330006Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:52.017437Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:50.750742Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:48.920204Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:47.623094Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:46.299467Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:45.041928Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:43.750751Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:42.461008Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:41.145854Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T21:17:39.824963Z` — **MID**: 0 rows; marker `2026-09-19T21:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
