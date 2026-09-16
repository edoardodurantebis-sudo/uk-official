# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T18:02:36.975683Z`  
Current process started UTC: `2026-09-16T17:58:36.965923Z`  
1-second metadata polls in this process: **229**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=687, delta=-2, z=4.02 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=50, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=689, delta=2, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.39 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=687, delta=0, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.48 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=687, delta=0, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.57 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=687, delta=1, z=3.84 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=686, delta=1, z=3.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.76 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=685, delta=-7, z=3.92 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.87 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=689, delta=168, z=4.51 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **383** (n=541, 2026-09-16T18:00:44.953992Z)
- `FUELINST|fuelType=NPSHYD|generation` = **689** (n=541, 2026-09-16T18:00:44.953992Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3304** (n=541, 2026-09-16T18:00:44.953992Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=541, 2026-09-16T18:00:44.953992Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=541, 2026-09-16T18:00:44.953992Z)
- `FUELINST|fuelType=OTHER|generation` = **2009** (n=541, 2026-09-16T18:00:44.953992Z)
- `FUELINST|fuelType=PS|generation` = **1107** (n=541, 2026-09-16T18:00:44.953992Z)
- `FUELINST|fuelType=WIND|generation` = **7798** (n=541, 2026-09-16T18:00:44.953992Z)
- `IMBALNGC|TOTAL|imbalance` = **6470** (n=89, 2026-09-16T17:52:27.704081Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=89, 2026-09-16T17:52:27.704081Z)
- `INDGEN|TOTAL|generation` = **25591** (n=89, 2026-09-16T17:52:27.704081Z)
- `MELNGC|TOTAL|margin` = **34093** (n=89, 2026-09-16T17:50:03.027017Z)
- `NDF|TOTAL|demand` = **18621** (n=91, 2026-09-16T17:47:44.789570Z)
- `TSDF|TOTAL|demand` = **19121** (n=91, 2026-09-16T17:47:59.877265Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T18:02:05.217404Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:01:45Z`
- `2026-09-16T18:00:44.953992Z` — **FUELHH**: 20 rows; marker `2026-09-16T18:00:00Z`
- `2026-09-16T18:00:44.953992Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:00:00Z`
- `2026-09-16T18:00:12.619884Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:59:45Z`
- `2026-09-16T17:58:36.965934Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:57:45Z`
- `2026-09-16T17:56:29.471594Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:55:45Z`
- `2026-09-16T17:55:41.789011Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:55:00Z`
- `2026-09-16T17:54:21.895098Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:53:45Z`
- `2026-09-16T17:52:27.704081Z` — **INDGEN**: 1224 rows; marker `2026-09-16T17:47:00Z`
- `2026-09-16T17:52:27.704081Z` — **INDDEM**: 1224 rows; marker `2026-09-16T17:47:00Z`
- `2026-09-16T17:52:27.704081Z` — **IMBALNGC**: 1224 rows; marker `2026-09-16T17:47:00Z`
- `2026-09-16T17:52:27.704081Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:51:45Z`
- `2026-09-16T17:50:35.205499Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:50:00Z`
- `2026-09-16T17:50:19.212832Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:49:45Z`
- `2026-09-16T17:50:03.027017Z` — **MELNGC**: 1224 rows; marker `2026-09-16T17:47:00Z`
