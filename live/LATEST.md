# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:21:11.930848Z`  
Current process started UTC: `2026-09-19T14:17:11.170132Z`  
1-second metadata polls in this process: **157**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.28 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1286, 2026-09-19T14:20:43.701006Z)
- `FUELINST|fuelType=NPSHYD|generation` = **282** (n=1286, 2026-09-19T14:20:43.701006Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1286, 2026-09-19T14:20:43.701006Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1286, 2026-09-19T14:20:43.701006Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1286, 2026-09-19T14:20:43.701006Z)
- `FUELINST|fuelType=OTHER|generation` = **659** (n=1286, 2026-09-19T14:20:43.701006Z)
- `FUELINST|fuelType=PS|generation` = **-254** (n=1286, 2026-09-19T14:20:43.701006Z)
- `FUELINST|fuelType=WIND|generation` = **14259** (n=1286, 2026-09-19T14:20:43.701006Z)
- `IMBALNGC|TOTAL|imbalance` = **-3239** (n=211, 2026-09-19T13:54:22.026040Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=211, 2026-09-19T13:54:05.855278Z)
- `INDGEN|TOTAL|generation` = **16770** (n=211, 2026-09-19T13:54:22.026040Z)
- `MELNGC|TOTAL|margin` = **36925** (n=212, 2026-09-19T14:20:59.619875Z)
- `NDF|TOTAL|demand` = **19509** (n=217, 2026-09-19T14:18:32.720132Z)
- `TSDF|TOTAL|demand` = **20009** (n=217, 2026-09-19T14:18:32.720132Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:21:10.447649Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:21:08.874376Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:21:07.353244Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:21:05.895830Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:21:04.179196Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:21:02.721728Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:20:59.619875Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:20:59.619875Z` — **MELNGC**: 1350 rows; marker `2026-09-19T14:18:00Z`
- `2026-09-19T14:20:58.165042Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:20:56.753402Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:20:55.298179Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:20:53.824161Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:20:52.405686Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:20:50.987462Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:20:49.555661Z` — **MID**: 0 rows; marker `2026-09-19T14:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
