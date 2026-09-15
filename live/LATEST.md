# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T21:05:23.545610Z`  
Current process started UTC: `2026-09-15T21:01:23.456728Z`  
1-second metadata polls in this process: **239**  
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

- `FUELINST|fuelType=INTVKL|generation` = **86** (n=289, 2026-09-15T21:00:24.999418Z)
- `FUELINST|fuelType=NPSHYD|generation` = **465** (n=289, 2026-09-15T21:00:24.999418Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=289, 2026-09-15T21:00:24.999418Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=289, 2026-09-15T21:00:24.999418Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=289, 2026-09-15T21:00:24.999418Z)
- `FUELINST|fuelType=OTHER|generation` = **118** (n=289, 2026-09-15T21:00:24.999418Z)
- `FUELINST|fuelType=PS|generation` = **-261** (n=289, 2026-09-15T21:00:24.999418Z)
- `FUELINST|fuelType=WIND|generation` = **12328** (n=289, 2026-09-15T21:00:24.999418Z)
- `IMBALNGC|TOTAL|imbalance` = **5722** (n=48, 2026-09-15T20:51:45.997446Z)
- `INDDEM|TOTAL|demand` = **-11914** (n=48, 2026-09-15T20:51:45.997446Z)
- `INDGEN|TOTAL|generation` = **24843** (n=48, 2026-09-15T20:51:45.997446Z)
- `MELNGC|TOTAL|margin` = **35714** (n=48, 2026-09-15T20:49:36.958587Z)
- `NDF|TOTAL|demand` = **18621** (n=49, 2026-09-15T20:47:37.139317Z)
- `TSDF|TOTAL|demand` = **19121** (n=49, 2026-09-15T20:47:37.139317Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T21:04:08.811808Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:03:45Z`
- `2026-09-15T21:02:33.353678Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:01:45Z`
- `2026-09-15T21:00:41.077544Z` — **FUELHH**: 20 rows; marker `2026-09-15T21:00:00Z`
- `2026-09-15T21:00:24.999418Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:00:00Z`
- `2026-09-15T21:00:09.516134Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:59:45Z`
- `2026-09-15T20:58:18.048163Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:57:45Z`
- `2026-09-15T20:56:16.092744Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:55:45Z`
- `2026-09-15T20:55:28.605600Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:55:00Z`
- `2026-09-15T20:54:06.626569Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:53:45Z`
- `2026-09-15T20:52:02.190897Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:51:45Z`
- `2026-09-15T20:51:45.997446Z` — **INDGEN**: 1116 rows; marker `2026-09-15T20:47:00Z`
- `2026-09-15T20:51:45.997446Z` — **INDDEM**: 1116 rows; marker `2026-09-15T20:47:00Z`
- `2026-09-15T20:51:45.997446Z` — **IMBALNGC**: 1116 rows; marker `2026-09-15T20:47:00Z`
- `2026-09-15T20:50:42.435715Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:50:00Z`
- `2026-09-15T20:50:10.298965Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:49:45Z`
