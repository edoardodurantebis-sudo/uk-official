# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T23:48:58.460391Z`  
Current process started UTC: `2026-09-14T23:44:59.137197Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2683, delta=11, z=5.04 -> generation-mix component moved
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2672, delta=95, z=11.64 -> generation-mix component moved
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2560, delta=-26, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=542, delta=109, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=1193, delta=90, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-889, delta=-56, z=-4.14 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=1, delta=-96, z=-5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-833, delta=-111, z=-5.27 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=97, delta=-182, z=-28.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=279, delta=-26, z=-14.31 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-134** (n=34, 2026-09-14T23:45:30.645819Z)
- `FUELINST|fuelType=NPSHYD|generation` = **367** (n=34, 2026-09-14T23:45:30.645819Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3314** (n=34, 2026-09-14T23:45:30.645819Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=34, 2026-09-14T23:45:30.645819Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=34, 2026-09-14T23:45:30.645819Z)
- `FUELINST|fuelType=OTHER|generation` = **308** (n=34, 2026-09-14T23:45:30.645819Z)
- `FUELINST|fuelType=PS|generation` = **-16** (n=34, 2026-09-14T23:45:30.645819Z)
- `FUELINST|fuelType=WIND|generation` = **12132** (n=34, 2026-09-14T23:45:30.645819Z)
- `IMBALNGC|TOTAL|imbalance` = **187** (n=6, 2026-09-14T23:20:54.895864Z)
- `INDDEM|TOTAL|demand` = **-12270** (n=6, 2026-09-14T23:20:54.895864Z)
- `INDGEN|TOTAL|generation` = **20672** (n=6, 2026-09-14T23:20:54.895864Z)
- `MELNGC|TOTAL|margin` = **32482** (n=6, 2026-09-14T23:18:52.547761Z)
- `NDF|TOTAL|demand` = **19934** (n=7, 2026-09-14T23:47:40.313990Z)
- `TSDF|TOTAL|demand` = **20485** (n=7, 2026-09-14T23:47:40.313990Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-14T23:48:12.094454Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:47:45Z`
- `2026-09-14T23:47:40.313990Z` — **TSDF**: 1008 rows; marker `2026-09-14T23:47:00Z`
- `2026-09-14T23:47:40.313990Z` — **NDF**: 56 rows; marker `2026-09-14T23:47:00Z`
- `2026-09-14T23:46:19.232396Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:45:45Z`
- `2026-09-14T23:45:30.645819Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:45:00Z`
- `2026-09-14T23:44:59.137207Z` — **MID**: 0 rows; marker `2026-09-14T23:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T23:44:59.137207Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:40:00Z`
- `2026-09-14T23:44:59.137207Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:43:45Z`
- `2026-09-14T23:40:20.530356Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:39:45Z`
- `2026-09-14T23:38:12.742433Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:37:45Z`
- `2026-09-14T23:36:37.295095Z` — **MID**: 0 rows; marker `2026-09-14T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T23:36:21.104351Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:35:45Z`
- `2026-09-14T23:35:33.531913Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:35:00Z`
- `2026-09-14T23:34:14.084163Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:33:45Z`
- `2026-09-14T23:32:21.313740Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:31:45Z`
