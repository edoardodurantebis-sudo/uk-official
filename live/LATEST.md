# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T19:43:19.412385Z`  
Current process started UTC: `2026-09-16T19:39:19.402283Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.51 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **158** (n=561, 2026-09-16T19:40:39.254776Z)
- `FUELINST|fuelType=NPSHYD|generation` = **513** (n=561, 2026-09-16T19:40:39.254776Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=561, 2026-09-16T19:40:39.254776Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=561, 2026-09-16T19:40:39.254776Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=561, 2026-09-16T19:40:39.254776Z)
- `FUELINST|fuelType=OTHER|generation` = **574** (n=561, 2026-09-16T19:40:39.254776Z)
- `FUELINST|fuelType=PS|generation` = **399** (n=561, 2026-09-16T19:40:39.254776Z)
- `FUELINST|fuelType=WIND|generation` = **9739** (n=561, 2026-09-16T19:40:39.254776Z)
- `IMBALNGC|TOTAL|imbalance` = **6644** (n=92, 2026-09-16T19:21:52.909122Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=92, 2026-09-16T19:21:52.909122Z)
- `INDGEN|TOTAL|generation` = **25765** (n=92, 2026-09-16T19:21:52.909122Z)
- `MELNGC|TOTAL|margin` = **33954** (n=92, 2026-09-16T19:19:44.962507Z)
- `NDF|TOTAL|demand` = **18621** (n=94, 2026-09-16T19:17:47.538138Z)
- `TSDF|TOTAL|demand` = **19121** (n=94, 2026-09-16T19:17:47.538138Z)
- `WINDFOR|TOTAL|generation` = **19445** (n=16, 2026-09-16T19:30:31.948327Z)

## Latest publication events

- `2026-09-16T19:42:16.646650Z` — **MID**: 0 rows; marker `2026-09-16T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T19:42:16.646650Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:41:45Z`
- `2026-09-16T19:40:39.254776Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:40:00Z`
- `2026-09-16T19:40:23.411822Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:39:45Z`
- `2026-09-16T19:38:06.185551Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:37:45Z`
- `2026-09-16T19:36:29.978717Z` — **MID**: 0 rows; marker `2026-09-16T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T19:36:29.978717Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:35:45Z`
- `2026-09-16T19:35:41.611465Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:35:00Z`
- `2026-09-16T19:34:16.306659Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:33:45Z`
- `2026-09-16T19:32:24.382255Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:31:45Z`
- `2026-09-16T19:30:31.948327Z` — **WINDFOR**: 73 rows; marker `2026-09-16T19:30:00Z`
- `2026-09-16T19:30:31.948327Z` — **FUELHH**: 20 rows; marker `2026-09-16T19:30:00Z`
- `2026-09-16T19:30:31.948327Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:30:00Z`
- `2026-09-16T19:30:16.438509Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:29:45Z`
- `2026-09-16T19:28:08.433979Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:27:45Z`
