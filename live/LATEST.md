# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T23:32:10.679296Z`  
Current process started UTC: `2026-09-14T23:28:11.106784Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-134** (n=31, 2026-09-14T23:30:39.804378Z)
- `FUELINST|fuelType=NPSHYD|generation` = **405** (n=31, 2026-09-14T23:30:39.804378Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=31, 2026-09-14T23:30:39.804378Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=31, 2026-09-14T23:30:39.804378Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=31, 2026-09-14T23:30:39.804378Z)
- `FUELINST|fuelType=OTHER|generation` = **245** (n=31, 2026-09-14T23:30:39.804378Z)
- `FUELINST|fuelType=PS|generation` = **-123** (n=31, 2026-09-14T23:30:39.804378Z)
- `FUELINST|fuelType=WIND|generation` = **12289** (n=31, 2026-09-14T23:30:39.804378Z)
- `IMBALNGC|TOTAL|imbalance` = **187** (n=6, 2026-09-14T23:20:54.895864Z)
- `INDDEM|TOTAL|demand` = **-12270** (n=6, 2026-09-14T23:20:54.895864Z)
- `INDGEN|TOTAL|generation` = **20672** (n=6, 2026-09-14T23:20:54.895864Z)
- `MELNGC|TOTAL|margin` = **32482** (n=6, 2026-09-14T23:18:52.547761Z)
- `NDF|TOTAL|demand` = **19934** (n=6, 2026-09-14T23:17:32.159171Z)
- `TSDF|TOTAL|demand` = **20485** (n=6, 2026-09-14T23:17:32.159171Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-14T23:30:39.804378Z` — **WINDFOR**: 73 rows; marker `2026-09-14T23:30:00Z`
- `2026-09-14T23:30:39.804378Z` — **FUELHH**: 20 rows; marker `2026-09-14T23:30:00Z`
- `2026-09-14T23:30:39.804378Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:30:00Z`
- `2026-09-14T23:30:08.195019Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:29:45Z`
- `2026-09-14T23:28:16.107378Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:27:45Z`
- `2026-09-14T23:26:08.251877Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:25:45Z`
- `2026-09-14T23:25:20.231248Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:25:00Z`
- `2026-09-14T23:24:16.716256Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:23:45Z`
- `2026-09-14T23:22:14.954456Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:21:45Z`
- `2026-09-14T23:20:54.895864Z` — **INDGEN**: 1026 rows; marker `2026-09-14T23:17:00Z`
- `2026-09-14T23:20:54.895864Z` — **INDDEM**: 1026 rows; marker `2026-09-14T23:17:00Z`
- `2026-09-14T23:20:54.895864Z` — **IMBALNGC**: 1026 rows; marker `2026-09-14T23:17:00Z`
- `2026-09-14T23:20:38.765539Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:20:00Z`
- `2026-09-14T23:20:22.690683Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:19:45Z`
- `2026-09-14T23:18:52.547761Z` — **MELNGC**: 1026 rows; marker `2026-09-14T23:17:00Z`
