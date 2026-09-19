# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:04:22.993810Z`  
Current process started UTC: `2026-09-19T14:00:22.874766Z`  
1-second metadata polls in this process: **208**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=41, delta=41, z=94.66 -> generation-mix component moved
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16759, delta=10, z=-3.53 -> state changed
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16749, delta=-28, z=-3.66 -> state changed

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-8** (n=1282, 2026-09-19T14:00:22.874776Z)
- `FUELINST|fuelType=NPSHYD|generation` = **280** (n=1282, 2026-09-19T14:00:22.874776Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1282, 2026-09-19T14:00:22.874776Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1282, 2026-09-19T14:00:22.874776Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1282, 2026-09-19T14:00:22.874776Z)
- `FUELINST|fuelType=OTHER|generation` = **497** (n=1282, 2026-09-19T14:00:22.874776Z)
- `FUELINST|fuelType=PS|generation` = **-636** (n=1282, 2026-09-19T14:00:22.874776Z)
- `FUELINST|fuelType=WIND|generation` = **14486** (n=1282, 2026-09-19T14:00:22.874776Z)
- `IMBALNGC|TOTAL|imbalance` = **-3239** (n=211, 2026-09-19T13:54:22.026040Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=211, 2026-09-19T13:54:05.855278Z)
- `INDGEN|TOTAL|generation` = **16770** (n=211, 2026-09-19T13:54:22.026040Z)
- `MELNGC|TOTAL|margin` = **36861** (n=211, 2026-09-19T13:51:15.765415Z)
- `NDF|TOTAL|demand` = **19509** (n=216, 2026-09-19T13:48:17.347273Z)
- `TSDF|TOTAL|demand` = **20009** (n=216, 2026-09-19T13:48:17.347273Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:04:21.673297Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:20.673228Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:19.422171Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:17.649630Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:16.030673Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:14.725802Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:13.474534Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:12.228628Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:11.228515Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:10.228405Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:07.647561Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:07.647561Z` — **FREQ**: 5761 rows; marker `2026-09-19T14:03:45Z`
- `2026-09-19T14:04:06.647464Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:05.612060Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:04:04.611961Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
