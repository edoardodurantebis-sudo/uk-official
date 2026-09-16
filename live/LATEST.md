# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T17:54:03.397234Z`  
Current process started UTC: `2026-09-16T17:50:03.026994Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=687, delta=0, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.57 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=687, delta=1, z=3.84 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=686, delta=1, z=3.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.76 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=685, delta=-7, z=3.92 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.87 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=689, delta=168, z=4.51 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=70, delta=102, z=5.03 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=692, delta=-1, z=4.09 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=9, z=4.99 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=693, delta=1, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=111, delta=25, z=5.03 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=692, delta=2, z=4.24 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **381** (n=539, 2026-09-16T17:50:35.205499Z)
- `FUELINST|fuelType=NPSHYD|generation` = **687** (n=539, 2026-09-16T17:50:35.205499Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=539, 2026-09-16T17:50:35.205499Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=539, 2026-09-16T17:50:35.205499Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=539, 2026-09-16T17:50:35.205499Z)
- `FUELINST|fuelType=OTHER|generation` = **2270** (n=539, 2026-09-16T17:50:35.205499Z)
- `FUELINST|fuelType=PS|generation` = **1210** (n=539, 2026-09-16T17:50:35.205499Z)
- `FUELINST|fuelType=WIND|generation` = **7542** (n=539, 2026-09-16T17:50:35.205499Z)
- `IMBALNGC|TOTAL|imbalance` = **6470** (n=89, 2026-09-16T17:52:27.704081Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=89, 2026-09-16T17:52:27.704081Z)
- `INDGEN|TOTAL|generation` = **25591** (n=89, 2026-09-16T17:52:27.704081Z)
- `MELNGC|TOTAL|margin` = **34093** (n=89, 2026-09-16T17:50:03.027017Z)
- `NDF|TOTAL|demand` = **18621** (n=91, 2026-09-16T17:47:44.789570Z)
- `TSDF|TOTAL|demand` = **19121** (n=91, 2026-09-16T17:47:59.877265Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T17:52:27.704081Z` — **INDGEN**: 1224 rows; marker `2026-09-16T17:47:00Z`
- `2026-09-16T17:52:27.704081Z` — **INDDEM**: 1224 rows; marker `2026-09-16T17:47:00Z`
- `2026-09-16T17:52:27.704081Z` — **IMBALNGC**: 1224 rows; marker `2026-09-16T17:47:00Z`
- `2026-09-16T17:52:27.704081Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:51:45Z`
- `2026-09-16T17:50:35.205499Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:50:00Z`
- `2026-09-16T17:50:19.212832Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:49:45Z`
- `2026-09-16T17:50:03.027017Z` — **MELNGC**: 1224 rows; marker `2026-09-16T17:47:00Z`
- `2026-09-16T17:48:15.990188Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:47:45Z`
- `2026-09-16T17:47:59.877265Z` — **TSDF**: 1224 rows; marker `2026-09-16T17:47:00Z`
- `2026-09-16T17:47:44.789570Z` — **NDF**: 68 rows; marker `2026-09-16T17:47:00Z`
- `2026-09-16T17:46:25.066853Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:45:45Z`
- `2026-09-16T17:45:52.480160Z` — **FUELINST**: 80 rows; marker `2026-09-16T17:45:00Z`
- `2026-09-16T17:44:17.811983Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:43:45Z`
- `2026-09-16T17:42:25.747557Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:41:45Z`
- `2026-09-16T17:42:10.066250Z` — **MID**: 0 rows; marker `2026-09-16T17:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
