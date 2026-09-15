# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T22:16:37.674240Z`  
Current process started UTC: `2026-09-15T22:12:37.213910Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **354** (n=304, 2026-09-15T22:15:33.366416Z)
- `FUELINST|fuelType=NPSHYD|generation` = **417** (n=304, 2026-09-15T22:15:33.366416Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=304, 2026-09-15T22:15:33.366416Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=304, 2026-09-15T22:15:33.366416Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=304, 2026-09-15T22:15:33.366416Z)
- `FUELINST|fuelType=OTHER|generation` = **190** (n=304, 2026-09-15T22:15:33.366416Z)
- `FUELINST|fuelType=PS|generation` = **-260** (n=304, 2026-09-15T22:15:33.366416Z)
- `FUELINST|fuelType=WIND|generation` = **12116** (n=304, 2026-09-15T22:15:33.366416Z)
- `IMBALNGC|TOTAL|imbalance` = **5771** (n=50, 2026-09-15T21:51:09.362674Z)
- `INDDEM|TOTAL|demand` = **-11914** (n=50, 2026-09-15T21:50:53.239309Z)
- `INDGEN|TOTAL|generation` = **24892** (n=50, 2026-09-15T21:50:53.239309Z)
- `MELNGC|TOTAL|margin` = **35719** (n=50, 2026-09-15T21:49:34.009187Z)
- `NDF|TOTAL|demand` = **18621** (n=51, 2026-09-15T21:47:43.117291Z)
- `TSDF|TOTAL|demand` = **19121** (n=51, 2026-09-15T21:47:43.117291Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T22:16:20.114187Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:15:45Z`
- `2026-09-15T22:15:33.366416Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:15:00Z`
- `2026-09-15T22:14:13.225228Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:13:45Z`
- `2026-09-15T22:12:11.958099Z` — **MID**: 0 rows; marker `2026-09-15T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T22:12:11.958099Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:11:45Z`
- `2026-09-15T22:10:36.597227Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:10:00Z`
- `2026-09-15T22:10:20.321567Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:09:45Z`
- `2026-09-15T22:08:12.826048Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:07:45Z`
- `2026-09-15T22:06:21.524490Z` — **MID**: 0 rows; marker `2026-09-15T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T22:06:05.888738Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:05:45Z`
- `2026-09-15T22:05:33.791118Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:05:00Z`
- `2026-09-15T22:04:13.434076Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:03:45Z`
- `2026-09-15T22:02:26.460298Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:01:45Z`
- `2026-09-15T22:00:49.852864Z` — **FUELHH**: 20 rows; marker `2026-09-15T22:00:00Z`
- `2026-09-15T22:00:33.880831Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:00:00Z`
