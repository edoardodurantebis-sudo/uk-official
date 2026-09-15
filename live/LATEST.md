# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T21:09:33.606066Z`  
Current process started UTC: `2026-09-15T21:05:33.409393Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **256** (n=290, 2026-09-15T21:05:33.409402Z)
- `FUELINST|fuelType=NPSHYD|generation` = **430** (n=290, 2026-09-15T21:05:33.409402Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=290, 2026-09-15T21:05:33.409402Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=290, 2026-09-15T21:05:33.409402Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=290, 2026-09-15T21:05:33.409402Z)
- `FUELINST|fuelType=OTHER|generation` = **117** (n=290, 2026-09-15T21:05:33.409402Z)
- `FUELINST|fuelType=PS|generation` = **-260** (n=290, 2026-09-15T21:05:33.409402Z)
- `FUELINST|fuelType=WIND|generation` = **12440** (n=290, 2026-09-15T21:05:33.409402Z)
- `IMBALNGC|TOTAL|imbalance` = **5722** (n=48, 2026-09-15T20:51:45.997446Z)
- `INDDEM|TOTAL|demand` = **-11914** (n=48, 2026-09-15T20:51:45.997446Z)
- `INDGEN|TOTAL|generation` = **24843** (n=48, 2026-09-15T20:51:45.997446Z)
- `MELNGC|TOTAL|margin` = **35714** (n=48, 2026-09-15T20:49:36.958587Z)
- `NDF|TOTAL|demand` = **18621** (n=49, 2026-09-15T20:47:37.139317Z)
- `TSDF|TOTAL|demand` = **19121** (n=49, 2026-09-15T20:47:37.139317Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T21:08:13.564335Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:07:45Z`
- `2026-09-15T21:07:25.198899Z` — **MID**: 0 rows; marker `2026-09-15T21:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T21:06:05.426187Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:05:45Z`
- `2026-09-15T21:05:33.409402Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:05:00Z`
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
