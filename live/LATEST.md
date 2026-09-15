# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T21:51:27.031083Z`  
Current process started UTC: `2026-09-15T21:47:27.115358Z`  
1-second metadata polls in this process: **231**  
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

- `FUELINST|fuelType=INTVKL|generation` = **344** (n=299, 2026-09-15T21:50:37.659301Z)
- `FUELINST|fuelType=NPSHYD|generation` = **432** (n=299, 2026-09-15T21:50:37.659301Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=299, 2026-09-15T21:50:37.659301Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=299, 2026-09-15T21:50:37.659301Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=299, 2026-09-15T21:50:37.659301Z)
- `FUELINST|fuelType=OTHER|generation` = **459** (n=299, 2026-09-15T21:50:37.659301Z)
- `FUELINST|fuelType=PS|generation` = **-259** (n=299, 2026-09-15T21:50:37.659301Z)
- `FUELINST|fuelType=WIND|generation` = **12082** (n=299, 2026-09-15T21:50:37.659301Z)
- `IMBALNGC|TOTAL|imbalance` = **5771** (n=50, 2026-09-15T21:51:09.362674Z)
- `INDDEM|TOTAL|demand` = **-11914** (n=50, 2026-09-15T21:50:53.239309Z)
- `INDGEN|TOTAL|generation` = **24892** (n=50, 2026-09-15T21:50:53.239309Z)
- `MELNGC|TOTAL|margin` = **35719** (n=50, 2026-09-15T21:49:34.009187Z)
- `NDF|TOTAL|demand` = **18621** (n=51, 2026-09-15T21:47:43.117291Z)
- `TSDF|TOTAL|demand` = **19121** (n=51, 2026-09-15T21:47:43.117291Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T21:51:09.362674Z` — **IMBALNGC**: 1080 rows; marker `2026-09-15T21:47:00Z`
- `2026-09-15T21:50:53.239309Z` — **INDGEN**: 1080 rows; marker `2026-09-15T21:47:00Z`
- `2026-09-15T21:50:53.239309Z` — **INDDEM**: 1080 rows; marker `2026-09-15T21:47:00Z`
- `2026-09-15T21:50:37.659301Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:50:00Z`
- `2026-09-15T21:50:06.059703Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:49:45Z`
- `2026-09-15T21:49:34.009187Z` — **MELNGC**: 1080 rows; marker `2026-09-15T21:47:00Z`
- `2026-09-15T21:48:14.698254Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:47:45Z`
- `2026-09-15T21:47:43.117291Z` — **TSDF**: 1080 rows; marker `2026-09-15T21:47:00Z`
- `2026-09-15T21:47:43.117291Z` — **NDF**: 60 rows; marker `2026-09-15T21:47:00Z`
- `2026-09-15T21:46:27.102277Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:45:45Z`
- `2026-09-15T21:45:38.787554Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:45:00Z`
- `2026-09-15T21:44:18.792551Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:43:45Z`
- `2026-09-15T21:42:22.229443Z` — **MID**: 0 rows; marker `2026-09-15T21:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T21:42:22.229443Z` — **FREQ**: 5761 rows; marker `2026-09-15T21:41:45Z`
- `2026-09-15T21:40:29.542850Z` — **FUELINST**: 80 rows; marker `2026-09-15T21:40:00Z`
