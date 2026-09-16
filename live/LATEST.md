# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T23:38:04.320557Z`  
Current process started UTC: `2026-09-16T23:34:04.589365Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.82 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=50, delta=50, z=5.13 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=40, delta=-418, z=-3.53 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-4, delta=0, z=-3.54 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.15 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-4, delta=0, z=-3.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=3, z=5.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-4, delta=-68, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=29, z=5.10 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.28 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.55 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-464** (n=577, 2026-09-16T23:35:24.095799Z)
- `FUELINST|fuelType=NPSHYD|generation` = **435** (n=577, 2026-09-16T23:35:24.095799Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3316** (n=577, 2026-09-16T23:35:24.095799Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=577, 2026-09-16T23:35:24.095799Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=577, 2026-09-16T23:35:24.095799Z)
- `FUELINST|fuelType=OTHER|generation` = **443** (n=577, 2026-09-16T23:35:24.095799Z)
- `FUELINST|fuelType=PS|generation` = **-249** (n=577, 2026-09-16T23:35:24.095799Z)
- `FUELINST|fuelType=WIND|generation` = **11406** (n=577, 2026-09-16T23:35:24.095799Z)
- `IMBALNGC|TOTAL|imbalance` = **6603** (n=96, 2026-09-16T23:21:18.839440Z)
- `INDDEM|TOTAL|demand` = **-11763** (n=96, 2026-09-16T23:21:18.839440Z)
- `INDGEN|TOTAL|generation` = **25724** (n=96, 2026-09-16T23:21:18.839440Z)
- `MELNGC|TOTAL|margin` = **34485** (n=96, 2026-09-16T23:19:27.229316Z)
- `NDF|TOTAL|demand` = **18621** (n=98, 2026-09-16T23:17:35.862544Z)
- `TSDF|TOTAL|demand` = **19121** (n=98, 2026-09-16T23:17:52.024896Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-16T23:36:43.640954Z` — **MID**: 0 rows; marker `2026-09-16T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T23:36:12.148546Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:35:45Z`
- `2026-09-16T23:35:24.095799Z` — **FUELINST**: 80 rows; marker `2026-09-16T23:35:00Z`
- `2026-09-16T23:34:04.589377Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:33:45Z`
- `2026-09-16T23:32:17.838048Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:31:45Z`
- `2026-09-16T23:30:41.101363Z` — **WINDFOR**: 73 rows; marker `2026-09-16T23:30:00Z`
- `2026-09-16T23:30:41.101363Z` — **FUELHH**: 20 rows; marker `2026-09-16T23:30:00Z`
- `2026-09-16T23:30:25.797989Z` — **FUELINST**: 80 rows; marker `2026-09-16T23:30:00Z`
- `2026-09-16T23:30:10.033667Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:29:45Z`
- `2026-09-16T23:28:07.672978Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:27:45Z`
- `2026-09-16T23:26:15.765048Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:25:45Z`
- `2026-09-16T23:25:43.412334Z` — **FUELINST**: 80 rows; marker `2026-09-16T23:25:00Z`
- `2026-09-16T23:24:14.321809Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:23:45Z`
- `2026-09-16T23:22:06.454407Z` — **FREQ**: 5761 rows; marker `2026-09-16T23:21:45Z`
- `2026-09-16T23:21:18.839440Z` — **INDGEN**: 1026 rows; marker `2026-09-16T23:17:00Z`
