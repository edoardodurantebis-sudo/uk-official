# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T21:30:31.122140Z`  
Current process started UTC: `2026-09-15T21:26:29.120224Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=INTVKL|generation` = **344** (n=295, 2026-09-15T21:30:28.787144Z)
- `FUELINST|fuelType=NPSHYD|generation` = **431** (n=295, 2026-09-15T21:30:28.787144Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3322** (n=295, 2026-09-15T21:30:28.787144Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=295, 2026-09-15T21:30:28.787144Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=295, 2026-09-15T21:30:28.787144Z)
- `FUELINST|fuelType=OTHER|generation` = **130** (n=295, 2026-09-15T21:30:28.787144Z)
- `FUELINST|fuelType=PS|generation` = **-258** (n=295, 2026-09-15T21:30:28.787144Z)
- `FUELINST|fuelType=WIND|generation` = **12383** (n=295, 2026-09-15T21:30:28.787144Z)
- `IMBALNGC|TOTAL|imbalance` = **5769** (n=49, 2026-09-15T21:21:18.653976Z)
- `INDDEM|TOTAL|demand` = **-11914** (n=49, 2026-09-15T21:21:18.653976Z)
- `INDGEN|TOTAL|generation` = **24890** (n=49, 2026-09-15T21:21:18.653976Z)
- `MELNGC|TOTAL|margin` = **35719** (n=49, 2026-09-15T21:19:11.341888Z)
- `NDF|TOTAL|demand` = **18621** (n=50, 2026-09-15T21:17:24.696002Z)
- `TSDF|TOTAL|demand` = **19121** (n=50, 2026-09-15T21:17:24.696002Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T21:30:28.787144Z` — **FUELHH**: 20 rows; marker `2026-09-15T21:30:00Z`
- `2026-09-15T21:30:28.787144Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:30:00Z`
- `2026-09-15T21:30:12.900566Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:29:45Z`
- `2026-09-15T21:28:21.040692Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:27:45Z`
- `2026-09-15T21:26:29.120234Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:25:45Z`
- `2026-09-15T21:25:34.441325Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:25:00Z`
- `2026-09-15T21:24:14.511125Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:23:45Z`
- `2026-09-15T21:22:22.188811Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:21:45Z`
- `2026-09-15T21:21:18.653976Z` — **INDGEN**: 1098 rows; marker `2026-09-15T21:17:00Z`
- `2026-09-15T21:21:18.653976Z` — **INDDEM**: 1098 rows; marker `2026-09-15T21:17:00Z`
- `2026-09-15T21:21:18.653976Z` — **IMBALNGC**: 1098 rows; marker `2026-09-15T21:17:00Z`
- `2026-09-15T21:20:31.362984Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:20:00Z`
- `2026-09-15T21:20:15.401323Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:19:45Z`
- `2026-09-15T21:19:11.341888Z` — **MELNGC**: 1098 rows; marker `2026-09-15T21:17:00Z`
- `2026-09-15T21:18:23.446634Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:17:45Z`
