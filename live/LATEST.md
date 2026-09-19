# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:17:00.178541Z`  
Current process started UTC: `2026-09-19T14:12:59.522095Z`  
1-second metadata polls in this process: **173**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=-15, z=-11.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-89, delta=-179, z=-10.03 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=100, delta=26, z=19.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=90, delta=-13, z=10.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=12.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=13.38 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=14.43 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=15.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=1, z=17.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=74, delta=74, z=126.77 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=102, delta=0, z=19.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=102, delta=0, z=24.13 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=102, delta=0, z=32.77 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=102, delta=61, z=83.31 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1285, 2026-09-19T14:15:27.876240Z)
- `FUELINST|fuelType=NPSHYD|generation` = **281** (n=1285, 2026-09-19T14:15:27.876240Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1285, 2026-09-19T14:15:27.876240Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1285, 2026-09-19T14:15:27.876240Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1285, 2026-09-19T14:15:27.876240Z)
- `FUELINST|fuelType=OTHER|generation` = **585** (n=1285, 2026-09-19T14:15:27.876240Z)
- `FUELINST|fuelType=PS|generation` = **-257** (n=1285, 2026-09-19T14:15:27.876240Z)
- `FUELINST|fuelType=WIND|generation` = **14448** (n=1285, 2026-09-19T14:15:27.876240Z)
- `IMBALNGC|TOTAL|imbalance` = **-3239** (n=211, 2026-09-19T13:54:22.026040Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=211, 2026-09-19T13:54:05.855278Z)
- `INDGEN|TOTAL|generation` = **16770** (n=211, 2026-09-19T13:54:22.026040Z)
- `MELNGC|TOTAL|margin` = **36861** (n=211, 2026-09-19T13:51:15.765415Z)
- `NDF|TOTAL|demand` = **19509** (n=216, 2026-09-19T13:48:17.347273Z)
- `TSDF|TOTAL|demand` = **20009** (n=216, 2026-09-19T13:48:17.347273Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:16:58.858855Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:57.560138Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:56.292743Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:54.965899Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:53.633458Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:52.385219Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:51.066516Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:49.192714Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:47.819777Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:46.488938Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:45.201872Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:43.908108Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:42.601618Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:41.290135Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:16:40.060133Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
