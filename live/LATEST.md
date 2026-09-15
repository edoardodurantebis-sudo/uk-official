# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T21:43:02.645530Z`  
Current process started UTC: `2026-09-15T21:39:03.043688Z`  
1-second metadata polls in this process: **233**  
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

- `FUELINST|fuelType=INTVKL|generation` = **344** (n=297, 2026-09-15T21:40:29.542850Z)
- `FUELINST|fuelType=NPSHYD|generation` = **431** (n=297, 2026-09-15T21:40:29.542850Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=297, 2026-09-15T21:40:29.542850Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=297, 2026-09-15T21:40:29.542850Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=297, 2026-09-15T21:40:29.542850Z)
- `FUELINST|fuelType=OTHER|generation` = **332** (n=297, 2026-09-15T21:40:29.542850Z)
- `FUELINST|fuelType=PS|generation` = **-256** (n=297, 2026-09-15T21:40:29.542850Z)
- `FUELINST|fuelType=WIND|generation` = **12275** (n=297, 2026-09-15T21:40:29.542850Z)
- `IMBALNGC|TOTAL|imbalance` = **5769** (n=49, 2026-09-15T21:21:18.653976Z)
- `INDDEM|TOTAL|demand` = **-11914** (n=49, 2026-09-15T21:21:18.653976Z)
- `INDGEN|TOTAL|generation` = **24890** (n=49, 2026-09-15T21:21:18.653976Z)
- `MELNGC|TOTAL|margin` = **35719** (n=49, 2026-09-15T21:19:11.341888Z)
- `NDF|TOTAL|demand` = **18621** (n=50, 2026-09-15T21:17:24.696002Z)
- `TSDF|TOTAL|demand` = **19121** (n=50, 2026-09-15T21:17:24.696002Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T21:42:22.229443Z` — **MID**: 0 rows; marker `2026-09-15T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T21:42:22.229443Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:41:45Z`
- `2026-09-15T21:40:29.542850Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:40:00Z`
- `2026-09-15T21:40:29.542850Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:39:45Z`
- `2026-09-15T21:38:18.747616Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:37:45Z`
- `2026-09-15T21:37:15.047037Z` — **MID**: 0 rows; marker `2026-09-15T21:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T21:36:27.025683Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:35:45Z`
- `2026-09-15T21:35:39.657917Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:35:00Z`
- `2026-09-15T21:34:13.553687Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:33:45Z`
- `2026-09-15T21:32:21.536166Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:31:45Z`
- `2026-09-15T21:30:28.787144Z` — **FUELHH**: 20 rows; marker `2026-09-15T21:30:00Z`
- `2026-09-15T21:30:28.787144Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:30:00Z`
- `2026-09-15T21:30:12.900566Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:29:45Z`
- `2026-09-15T21:28:21.040692Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:27:45Z`
- `2026-09-15T21:26:29.120234Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:25:45Z`
