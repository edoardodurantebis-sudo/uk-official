# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T22:58:38.298907Z`  
Current process started UTC: `2026-09-14T22:54:38.226940Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2560, delta=-26, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=542, delta=109, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=1193, delta=90, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-889, delta=-56, z=-4.14 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=1, delta=-96, z=-5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-833, delta=-111, z=-5.27 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=97, delta=-182, z=-28.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=279, delta=-26, z=-14.31 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTNSL|generation` = **1258** (n=24, 2026-09-14T22:55:26.232397Z)
- `FUELINST|fuelType=INTVKL|generation` = **-668** (n=24, 2026-09-14T22:55:26.232397Z)
- `FUELINST|fuelType=NPSHYD|generation` = **496** (n=24, 2026-09-14T22:55:26.232397Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3311** (n=24, 2026-09-14T22:55:26.232397Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=24, 2026-09-14T22:55:26.232397Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=24, 2026-09-14T22:55:26.232397Z)
- `FUELINST|fuelType=OTHER|generation` = **504** (n=24, 2026-09-14T22:55:26.232397Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=24, 2026-09-14T22:55:26.232397Z)
- `FUELINST|fuelType=WIND|generation` = **12424** (n=24, 2026-09-14T22:55:26.232397Z)
- `IMBALNGC|TOTAL|imbalance` = **-63** (n=5, 2026-09-14T22:51:15.871339Z)
- `INDDEM|TOTAL|demand` = **-12269** (n=5, 2026-09-14T22:50:59.511453Z)
- `INDGEN|TOTAL|generation` = **20421** (n=5, 2026-09-14T22:50:59.511453Z)
- `MELNGC|TOTAL|margin` = **32473** (n=5, 2026-09-14T22:49:32.967588Z)
- `NDF|TOTAL|demand` = **19934** (n=5, 2026-09-14T22:47:25.340833Z)
- `TSDF|TOTAL|demand` = **20485** (n=5, 2026-09-14T22:47:25.340833Z)

## Latest publication events

- `2026-09-14T22:58:23.331491Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:57:45Z`
- `2026-09-14T22:56:14.670770Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:55:45Z`
- `2026-09-14T22:55:26.232397Z` — **FUELINST**: 80 rows; marker `2026-09-14T22:55:00Z`
- `2026-09-14T22:54:12.789329Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:53:45Z`
- `2026-09-14T22:52:19.345196Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:51:45Z`
- `2026-09-14T22:51:15.871339Z` — **IMBALNGC**: 1044 rows; marker `2026-09-14T22:47:00Z`
- `2026-09-14T22:50:59.511453Z` — **INDGEN**: 1044 rows; marker `2026-09-14T22:47:00Z`
- `2026-09-14T22:50:59.511453Z` — **INDDEM**: 1044 rows; marker `2026-09-14T22:47:00Z`
- `2026-09-14T22:50:28.081314Z` — **FUELINST**: 80 rows; marker `2026-09-14T22:50:00Z`
- `2026-09-14T22:50:28.081314Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:49:45Z`
- `2026-09-14T22:49:32.967588Z` — **MELNGC**: 1044 rows; marker `2026-09-14T22:47:00Z`
- `2026-09-14T22:48:12.835394Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:47:45Z`
- `2026-09-14T22:47:25.340833Z` — **TSDF**: 1044 rows; marker `2026-09-14T22:47:00Z`
- `2026-09-14T22:47:25.340833Z` — **NDF**: 58 rows; marker `2026-09-14T22:47:00Z`
- `2026-09-14T22:46:20.930519Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:45:45Z`
