# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:12:47.311475Z`  
Current process started UTC: `2026-09-19T14:08:46.037238Z`  
1-second metadata polls in this process: **133**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=41, delta=41, z=94.66 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1284, 2026-09-19T14:10:37.889096Z)
- `FUELINST|fuelType=NPSHYD|generation` = **281** (n=1284, 2026-09-19T14:10:37.889096Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1284, 2026-09-19T14:10:37.889096Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1284, 2026-09-19T14:10:37.889096Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1284, 2026-09-19T14:10:37.889096Z)
- `FUELINST|fuelType=OTHER|generation` = **588** (n=1284, 2026-09-19T14:10:37.889096Z)
- `FUELINST|fuelType=PS|generation` = **-460** (n=1284, 2026-09-19T14:10:37.889096Z)
- `FUELINST|fuelType=WIND|generation` = **14514** (n=1284, 2026-09-19T14:10:37.889096Z)
- `IMBALNGC|TOTAL|imbalance` = **-3239** (n=211, 2026-09-19T13:54:22.026040Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=211, 2026-09-19T13:54:05.855278Z)
- `INDGEN|TOTAL|generation` = **16770** (n=211, 2026-09-19T13:54:22.026040Z)
- `MELNGC|TOTAL|margin` = **36861** (n=211, 2026-09-19T13:51:15.765415Z)
- `NDF|TOTAL|demand` = **19509** (n=216, 2026-09-19T13:48:17.347273Z)
- `TSDF|TOTAL|demand` = **20009** (n=216, 2026-09-19T13:48:17.347273Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:12:45.562926Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:43.845401Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:42.137704Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:40.377384Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:38.661377Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:36.955197Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:35.246639Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:33.526674Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:31.279230Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:29.561162Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:27.822795Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:26.097278Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:24.370893Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:22.668015Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:12:20.960879Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
