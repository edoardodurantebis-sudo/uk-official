# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T20:40:13.498816Z`  
Current process started UTC: `2026-09-15T20:36:12.943264Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.98 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=284, 2026-09-15T20:35:29.382157Z)
- `FUELINST|fuelType=NPSHYD|generation` = **485** (n=284, 2026-09-15T20:35:29.382157Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3322** (n=284, 2026-09-15T20:35:29.382157Z)
- `FUELINST|fuelType=OCGT|generation` = **2** (n=284, 2026-09-15T20:35:29.382157Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=284, 2026-09-15T20:35:29.382157Z)
- `FUELINST|fuelType=OTHER|generation` = **103** (n=284, 2026-09-15T20:35:29.382157Z)
- `FUELINST|fuelType=PS|generation` = **-262** (n=284, 2026-09-15T20:35:29.382157Z)
- `FUELINST|fuelType=WIND|generation` = **11928** (n=284, 2026-09-15T20:35:29.382157Z)
- `IMBALNGC|TOTAL|imbalance` = **5788** (n=47, 2026-09-15T20:21:44.851897Z)
- `INDDEM|TOTAL|demand` = **-11914** (n=47, 2026-09-15T20:21:44.851897Z)
- `INDGEN|TOTAL|generation` = **24909** (n=47, 2026-09-15T20:21:44.851897Z)
- `MELNGC|TOTAL|margin` = **35696** (n=47, 2026-09-15T20:19:53.455183Z)
- `NDF|TOTAL|demand` = **18621** (n=48, 2026-09-15T20:17:38.969739Z)
- `TSDF|TOTAL|demand` = **19121** (n=48, 2026-09-15T20:17:38.969739Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T20:38:20.514436Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:37:45Z`
- `2026-09-15T20:37:16.417641Z` — **MID**: 0 rows; marker `2026-09-15T20:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T20:36:12.943273Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:35:45Z`
- `2026-09-15T20:35:29.382157Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:35:00Z`
- `2026-09-15T20:34:41.537395Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:33:45Z`
- `2026-09-15T20:32:17.305541Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:31:45Z`
- `2026-09-15T20:30:32.681465Z` — **FUELHH**: 20 rows; marker `2026-09-15T20:30:00Z`
- `2026-09-15T20:30:32.681465Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:30:00Z`
- `2026-09-15T20:30:17.199345Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:29:45Z`
- `2026-09-15T20:28:25.742384Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:27:45Z`
- `2026-09-15T20:26:18.545119Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:25:45Z`
- `2026-09-15T20:25:30.521311Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:25:00Z`
- `2026-09-15T20:24:11.064600Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:23:45Z`
- `2026-09-15T20:22:16.390991Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:21:45Z`
- `2026-09-15T20:21:44.851897Z` — **INDGEN**: 1134 rows; marker `2026-09-15T20:17:00Z`
