# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:08:33.765597Z`  
Current process started UTC: `2026-09-19T14:04:33.431899Z`  
1-second metadata polls in this process: **173**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16759, delta=10, z=-3.53 -> state changed

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1283, 2026-09-19T14:05:38.055577Z)
- `FUELINST|fuelType=NPSHYD|generation` = **282** (n=1283, 2026-09-19T14:05:38.055577Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1283, 2026-09-19T14:05:38.055577Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1283, 2026-09-19T14:05:38.055577Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1283, 2026-09-19T14:05:38.055577Z)
- `FUELINST|fuelType=OTHER|generation` = **711** (n=1283, 2026-09-19T14:05:38.055577Z)
- `FUELINST|fuelType=PS|generation` = **-751** (n=1283, 2026-09-19T14:05:38.055577Z)
- `FUELINST|fuelType=WIND|generation` = **14529** (n=1283, 2026-09-19T14:05:38.055577Z)
- `IMBALNGC|TOTAL|imbalance` = **-3239** (n=211, 2026-09-19T13:54:22.026040Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=211, 2026-09-19T13:54:05.855278Z)
- `INDGEN|TOTAL|generation` = **16770** (n=211, 2026-09-19T13:54:22.026040Z)
- `MELNGC|TOTAL|margin` = **36861** (n=211, 2026-09-19T13:51:15.765415Z)
- `NDF|TOTAL|demand` = **19509** (n=216, 2026-09-19T13:48:17.347273Z)
- `TSDF|TOTAL|demand` = **20009** (n=216, 2026-09-19T13:48:17.347273Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:08:32.410315Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:31.100221Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:29.846694Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:28.589136Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:27.263379Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:25.996254Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:24.731948Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:23.508959Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:20.469998Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:20.469998Z` — **FREQ**: 5761 rows; marker `2026-09-19T14:07:45Z`
- `2026-09-19T14:08:19.206023Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:17.903353Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:16.540220Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:15.265414Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:08:13.972047Z` — **MID**: 0 rows; marker `2026-09-19T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
