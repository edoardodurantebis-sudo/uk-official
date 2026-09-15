# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T20:52:49.934589Z`  
Current process started UTC: `2026-09-15T20:48:49.606672Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=287, 2026-09-15T20:50:42.435715Z)
- `FUELINST|fuelType=NPSHYD|generation` = **470** (n=287, 2026-09-15T20:50:42.435715Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3322** (n=287, 2026-09-15T20:50:42.435715Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=287, 2026-09-15T20:50:42.435715Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=287, 2026-09-15T20:50:42.435715Z)
- `FUELINST|fuelType=OTHER|generation` = **100** (n=287, 2026-09-15T20:50:42.435715Z)
- `FUELINST|fuelType=PS|generation` = **-264** (n=287, 2026-09-15T20:50:42.435715Z)
- `FUELINST|fuelType=WIND|generation` = **12288** (n=287, 2026-09-15T20:50:42.435715Z)
- `IMBALNGC|TOTAL|imbalance` = **5722** (n=48, 2026-09-15T20:51:45.997446Z)
- `INDDEM|TOTAL|demand` = **-11914** (n=48, 2026-09-15T20:51:45.997446Z)
- `INDGEN|TOTAL|generation` = **24843** (n=48, 2026-09-15T20:51:45.997446Z)
- `MELNGC|TOTAL|margin` = **35714** (n=48, 2026-09-15T20:49:36.958587Z)
- `NDF|TOTAL|demand` = **18621** (n=49, 2026-09-15T20:47:37.139317Z)
- `TSDF|TOTAL|demand` = **19121** (n=49, 2026-09-15T20:47:37.139317Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T20:52:02.190897Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:51:45Z`
- `2026-09-15T20:51:45.997446Z` — **INDGEN**: 1116 rows; marker `2026-09-15T20:47:00Z`
- `2026-09-15T20:51:45.997446Z` — **INDDEM**: 1116 rows; marker `2026-09-15T20:47:00Z`
- `2026-09-15T20:51:45.997446Z` — **IMBALNGC**: 1116 rows; marker `2026-09-15T20:47:00Z`
- `2026-09-15T20:50:42.435715Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:50:00Z`
- `2026-09-15T20:50:10.298965Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:49:45Z`
- `2026-09-15T20:49:36.958587Z` — **MELNGC**: 1116 rows; marker `2026-09-15T20:47:00Z`
- `2026-09-15T20:48:08.646012Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:47:45Z`
- `2026-09-15T20:47:37.139317Z` — **TSDF**: 1116 rows; marker `2026-09-15T20:47:00Z`
- `2026-09-15T20:47:37.139317Z` — **NDF**: 62 rows; marker `2026-09-15T20:47:00Z`
- `2026-09-15T20:46:15.666163Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:45:45Z`
- `2026-09-15T20:45:44.013501Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:45:00Z`
- `2026-09-15T20:44:24.761922Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:43:45Z`
- `2026-09-15T20:42:16.650254Z` — **MID**: 0 rows; marker `2026-09-15T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T20:42:16.650254Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:41:45Z`
