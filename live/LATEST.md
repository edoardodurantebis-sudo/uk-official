# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T19:05:39.248537Z`  
Current process started UTC: `2026-09-16T19:01:39.088870Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.09 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **218** (n=554, 2026-09-16T19:05:25.110321Z)
- `FUELINST|fuelType=NPSHYD|generation` = **513** (n=554, 2026-09-16T19:05:25.110321Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3311** (n=554, 2026-09-16T19:05:25.110321Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=554, 2026-09-16T19:05:25.110321Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=554, 2026-09-16T19:05:25.110321Z)
- `FUELINST|fuelType=OTHER|generation` = **1256** (n=554, 2026-09-16T19:05:25.110321Z)
- `FUELINST|fuelType=PS|generation` = **547** (n=554, 2026-09-16T19:05:25.110321Z)
- `FUELINST|fuelType=WIND|generation` = **8934** (n=554, 2026-09-16T19:05:25.110321Z)
- `IMBALNGC|TOTAL|imbalance` = **6597** (n=91, 2026-09-16T18:52:44.831535Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=91, 2026-09-16T18:52:44.831535Z)
- `INDGEN|TOTAL|generation` = **25718** (n=91, 2026-09-16T18:52:44.831535Z)
- `MELNGC|TOTAL|margin` = **33948** (n=91, 2026-09-16T18:50:05.022800Z)
- `NDF|TOTAL|demand` = **18621** (n=93, 2026-09-16T18:48:00.832960Z)
- `TSDF|TOTAL|demand` = **19121** (n=93, 2026-09-16T18:48:00.832960Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T19:05:25.110321Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:05:00Z`
- `2026-09-16T19:04:20.057269Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:03:45Z`
- `2026-09-16T19:02:27.663906Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:01:45Z`
- `2026-09-16T19:01:07.807213Z` — **FUELHH**: 20 rows; marker `2026-09-16T19:00:00Z`
- `2026-09-16T19:01:07.807213Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:00:00Z`
- `2026-09-16T19:00:03.491530Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:59:45Z`
- `2026-09-16T18:58:11.786447Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:57:45Z`
- `2026-09-16T18:56:12.436096Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:55:45Z`
- `2026-09-16T18:55:40.368167Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:55:00Z`
- `2026-09-16T18:54:20.808755Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:53:45Z`
- `2026-09-16T18:52:44.831535Z` — **INDGEN**: 1188 rows; marker `2026-09-16T18:47:00Z`
- `2026-09-16T18:52:44.831535Z` — **INDDEM**: 1188 rows; marker `2026-09-16T18:47:00Z`
- `2026-09-16T18:52:44.831535Z` — **IMBALNGC**: 1188 rows; marker `2026-09-16T18:47:00Z`
- `2026-09-16T18:52:28.784646Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:51:45Z`
- `2026-09-16T18:50:37.397996Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:50:00Z`
