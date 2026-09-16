# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T19:14:02.938652Z`  
Current process started UTC: `2026-09-16T19:10:02.515040Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=692, delta=5, z=3.75 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.97 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=692, delta=2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.03 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=690, delta=4, z=3.53 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **158** (n=555, 2026-09-16T19:10:34.464011Z)
- `FUELINST|fuelType=NPSHYD|generation` = **513** (n=555, 2026-09-16T19:10:34.464011Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3306** (n=555, 2026-09-16T19:10:34.464011Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=555, 2026-09-16T19:10:34.464011Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=555, 2026-09-16T19:10:34.464011Z)
- `FUELINST|fuelType=OTHER|generation` = **1322** (n=555, 2026-09-16T19:10:34.464011Z)
- `FUELINST|fuelType=PS|generation` = **371** (n=555, 2026-09-16T19:10:34.464011Z)
- `FUELINST|fuelType=WIND|generation` = **9061** (n=555, 2026-09-16T19:10:34.464011Z)
- `IMBALNGC|TOTAL|imbalance` = **6597** (n=91, 2026-09-16T18:52:44.831535Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=91, 2026-09-16T18:52:44.831535Z)
- `INDGEN|TOTAL|generation` = **25718** (n=91, 2026-09-16T18:52:44.831535Z)
- `MELNGC|TOTAL|margin` = **33948** (n=91, 2026-09-16T18:50:05.022800Z)
- `NDF|TOTAL|demand` = **18621** (n=93, 2026-09-16T18:48:00.832960Z)
- `TSDF|TOTAL|demand` = **19121** (n=93, 2026-09-16T18:48:00.832960Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T19:12:25.569951Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:11:45Z`
- `2026-09-16T19:12:09.889046Z` — **MID**: 0 rows; marker `2026-09-16T19:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T19:10:34.464011Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:10:00Z`
- `2026-09-16T19:10:18.517189Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:09:45Z`
- `2026-09-16T19:08:32.492580Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:07:45Z`
- `2026-09-16T19:06:39.569809Z` — **MID**: 0 rows; marker `2026-09-16T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T19:06:24.155533Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:05:45Z`
- `2026-09-16T19:05:25.110321Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:05:00Z`
- `2026-09-16T19:04:20.057269Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:03:45Z`
- `2026-09-16T19:02:27.663906Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:01:45Z`
- `2026-09-16T19:01:07.807213Z` — **FUELHH**: 20 rows; marker `2026-09-16T19:00:00Z`
- `2026-09-16T19:01:07.807213Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:00:00Z`
- `2026-09-16T19:00:03.491530Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:59:45Z`
- `2026-09-16T18:58:11.786447Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:57:45Z`
- `2026-09-16T18:56:12.436096Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:55:45Z`
