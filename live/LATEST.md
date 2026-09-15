# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T16:59:47.263091Z`  
Current process started UTC: `2026-09-15T16:55:47.462631Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=3.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=3.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.09 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.26 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=7, delta=2, z=5.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.44 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.65 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.90 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=5.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=5.54 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=5.96 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=5, delta=5, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=2, z=6.51 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=5, delta=0, z=4.82 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-938** (n=240, 2026-09-15T16:55:21.633809Z)
- `FUELINST|fuelType=NPSHYD|generation` = **476** (n=240, 2026-09-15T16:55:21.633809Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3322** (n=240, 2026-09-15T16:55:21.633809Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=240, 2026-09-15T16:55:21.633809Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=240, 2026-09-15T16:55:21.633809Z)
- `FUELINST|fuelType=OTHER|generation` = **658** (n=240, 2026-09-15T16:55:21.633809Z)
- `FUELINST|fuelType=PS|generation` = **429** (n=240, 2026-09-15T16:55:21.633809Z)
- `FUELINST|fuelType=WIND|generation` = **10352** (n=240, 2026-09-15T16:55:21.633809Z)
- `IMBALNGC|TOTAL|imbalance` = **5835** (n=40, 2026-09-15T16:52:09.948622Z)
- `INDDEM|TOTAL|demand` = **-11918** (n=40, 2026-09-15T16:51:53.487426Z)
- `INDGEN|TOTAL|generation` = **24956** (n=40, 2026-09-15T16:52:09.948622Z)
- `MELNGC|TOTAL|margin` = **34829** (n=40, 2026-09-15T16:49:49.790208Z)
- `NDF|TOTAL|demand` = **18621** (n=41, 2026-09-15T16:47:58.073768Z)
- `TSDF|TOTAL|demand` = **19121** (n=41, 2026-09-15T16:47:58.073768Z)
- `WINDFOR|TOTAL|generation` = **17795** (n=7, 2026-09-15T16:30:51.506988Z)

## Latest publication events

- `2026-09-15T16:58:12.344691Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:57:45Z`
- `2026-09-15T16:56:19.727652Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:55:45Z`
- `2026-09-15T16:55:21.633809Z` — **FUELINST**: 80 rows; marker `2026-09-15T16:55:00Z`
- `2026-09-15T16:54:17.955851Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:53:45Z`
- `2026-09-15T16:52:09.948622Z` — **INDGEN**: 1260 rows; marker `2026-09-15T16:47:00Z`
- `2026-09-15T16:52:09.948622Z` — **IMBALNGC**: 1260 rows; marker `2026-09-15T16:47:00Z`
- `2026-09-15T16:52:09.948622Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:51:45Z`
- `2026-09-15T16:51:53.487426Z` — **INDDEM**: 1260 rows; marker `2026-09-15T16:47:00Z`
- `2026-09-15T16:50:20.905810Z` — **FUELINST**: 80 rows; marker `2026-09-15T16:50:00Z`
- `2026-09-15T16:50:05.208876Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:49:45Z`
- `2026-09-15T16:49:49.790208Z` — **MELNGC**: 1260 rows; marker `2026-09-15T16:47:00Z`
- `2026-09-15T16:48:14.213739Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:47:45Z`
- `2026-09-15T16:47:58.073768Z` — **TSDF**: 1260 rows; marker `2026-09-15T16:47:00Z`
- `2026-09-15T16:47:58.073768Z` — **NDF**: 70 rows; marker `2026-09-15T16:47:00Z`
- `2026-09-15T16:46:23.160365Z` — **FREQ**: 5761 rows; marker `2026-09-15T16:45:45Z`
