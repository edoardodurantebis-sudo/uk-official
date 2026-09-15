# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T22:24:59.987292Z`  
Current process started UTC: `2026-09-15T22:20:59.983019Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=-1, z=3.74 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.30 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=54, delta=-1, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=17, z=8.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.39 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **354** (n=305, 2026-09-15T22:20:36.141491Z)
- `FUELINST|fuelType=NPSHYD|generation` = **417** (n=305, 2026-09-15T22:20:36.141491Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=305, 2026-09-15T22:20:36.141491Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=305, 2026-09-15T22:20:36.141491Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=305, 2026-09-15T22:20:36.141491Z)
- `FUELINST|fuelType=OTHER|generation` = **186** (n=305, 2026-09-15T22:20:36.141491Z)
- `FUELINST|fuelType=PS|generation` = **-261** (n=305, 2026-09-15T22:20:36.141491Z)
- `FUELINST|fuelType=WIND|generation` = **12146** (n=305, 2026-09-15T22:20:36.141491Z)
- `IMBALNGC|TOTAL|imbalance` = **5815** (n=51, 2026-09-15T22:21:16.013291Z)
- `INDDEM|TOTAL|demand` = **-11915** (n=51, 2026-09-15T22:21:16.013291Z)
- `INDGEN|TOTAL|generation` = **24936** (n=51, 2026-09-15T22:21:16.013291Z)
- `MELNGC|TOTAL|margin` = **35753** (n=51, 2026-09-15T22:19:15.823893Z)
- `NDF|TOTAL|demand` = **18621** (n=52, 2026-09-15T22:17:24.476756Z)
- `TSDF|TOTAL|demand` = **19121** (n=52, 2026-09-15T22:17:24.476756Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T22:24:11.115350Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:23:45Z`
- `2026-09-15T22:22:19.742698Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:21:45Z`
- `2026-09-15T22:21:16.013291Z` — **INDGEN**: 1062 rows; marker `2026-09-15T22:17:00Z`
- `2026-09-15T22:21:16.013291Z` — **INDDEM**: 1062 rows; marker `2026-09-15T22:17:00Z`
- `2026-09-15T22:21:16.013291Z` — **IMBALNGC**: 1062 rows; marker `2026-09-15T22:17:00Z`
- `2026-09-15T22:20:36.141491Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:20:00Z`
- `2026-09-15T22:20:20.566230Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:19:45Z`
- `2026-09-15T22:19:15.823893Z` — **MELNGC**: 1062 rows; marker `2026-09-15T22:17:00Z`
- `2026-09-15T22:18:12.310515Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:17:45Z`
- `2026-09-15T22:17:24.476756Z` — **TSDF**: 1062 rows; marker `2026-09-15T22:17:00Z`
- `2026-09-15T22:17:24.476756Z` — **NDF**: 59 rows; marker `2026-09-15T22:17:00Z`
- `2026-09-15T22:16:20.114187Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:15:45Z`
- `2026-09-15T22:15:33.366416Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:15:00Z`
- `2026-09-15T22:14:13.225228Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:13:45Z`
- `2026-09-15T22:12:11.958099Z` — **MID**: 0 rows; marker `2026-09-15T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
