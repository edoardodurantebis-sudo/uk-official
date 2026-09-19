# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:00:11.892038Z`  
Current process started UTC: `2026-09-19T13:56:10.225443Z`  
1-second metadata polls in this process: **138**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=41, delta=41, z=94.66 -> generation-mix component moved
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16759, delta=10, z=-3.53 -> state changed
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16749, delta=-28, z=-3.66 -> state changed
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16777, delta=25, z=-3.78 -> state changed
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16752, delta=-9313, z=-3.94 -> state changed

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-18** (n=1281, 2026-09-19T13:55:27.027551Z)
- `FUELINST|fuelType=NPSHYD|generation` = **281** (n=1281, 2026-09-19T13:55:27.027551Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1281, 2026-09-19T13:55:27.027551Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1281, 2026-09-19T13:55:27.027551Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1281, 2026-09-19T13:55:27.027551Z)
- `FUELINST|fuelType=OTHER|generation` = **478** (n=1281, 2026-09-19T13:55:27.027551Z)
- `FUELINST|fuelType=PS|generation` = **-427** (n=1281, 2026-09-19T13:55:27.027551Z)
- `FUELINST|fuelType=WIND|generation` = **14645** (n=1281, 2026-09-19T13:55:27.027551Z)
- `IMBALNGC|TOTAL|imbalance` = **-3239** (n=211, 2026-09-19T13:54:22.026040Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=211, 2026-09-19T13:54:05.855278Z)
- `INDGEN|TOTAL|generation` = **16770** (n=211, 2026-09-19T13:54:22.026040Z)
- `MELNGC|TOTAL|margin` = **36861** (n=211, 2026-09-19T13:51:15.765415Z)
- `NDF|TOTAL|demand` = **19509** (n=216, 2026-09-19T13:48:17.347273Z)
- `TSDF|TOTAL|demand` = **20009** (n=216, 2026-09-19T13:48:17.347273Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:00:10.212288Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:00:08.569098Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:00:06.511427Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:00:04.179617Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:00:01.503928Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:59:59.801179Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:59:58.170316Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:59:56.527203Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:59:54.868976Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:59:53.238943Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:59:51.568785Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:59:49.919704Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:59:48.283140Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:59:46.576227Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:59:44.600375Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
