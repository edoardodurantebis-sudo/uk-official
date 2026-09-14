# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T23:19:39.980667Z`  
Current process started UTC: `2026-09-14T23:15:39.700939Z`  
1-second metadata polls in this process: **236**  
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

- `FUELINST|fuelType=INTNSL|generation` = **1402** (n=28, 2026-09-14T23:15:39.700945Z)
- `FUELINST|fuelType=INTVKL|generation` = **-134** (n=28, 2026-09-14T23:15:39.700945Z)
- `FUELINST|fuelType=NPSHYD|generation` = **429** (n=28, 2026-09-14T23:15:39.700945Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=28, 2026-09-14T23:15:39.700945Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=28, 2026-09-14T23:15:39.700945Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=28, 2026-09-14T23:15:39.700945Z)
- `FUELINST|fuelType=OTHER|generation` = **105** (n=28, 2026-09-14T23:15:39.700945Z)
- `FUELINST|fuelType=PS|generation` = **-137** (n=28, 2026-09-14T23:15:39.700945Z)
- `FUELINST|fuelType=WIND|generation` = **12397** (n=28, 2026-09-14T23:15:39.700945Z)
- `IMBALNGC|TOTAL|imbalance` = **-63** (n=5, 2026-09-14T22:51:15.871339Z)
- `INDDEM|TOTAL|demand` = **-12269** (n=5, 2026-09-14T22:50:59.511453Z)
- `INDGEN|TOTAL|generation` = **20421** (n=5, 2026-09-14T22:50:59.511453Z)
- `MELNGC|TOTAL|margin` = **32482** (n=6, 2026-09-14T23:18:52.547761Z)
- `NDF|TOTAL|demand` = **19934** (n=6, 2026-09-14T23:17:32.159171Z)
- `TSDF|TOTAL|demand` = **20485** (n=6, 2026-09-14T23:17:32.159171Z)

## Latest publication events

- `2026-09-14T23:18:52.547761Z` — **MELNGC**: 1026 rows; marker `2026-09-14T23:17:00Z`
- `2026-09-14T23:18:20.273932Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:17:45Z`
- `2026-09-14T23:17:32.159171Z` — **TSDF**: 1026 rows; marker `2026-09-14T23:17:00Z`
- `2026-09-14T23:17:32.159171Z` — **NDF**: 57 rows; marker `2026-09-14T23:17:00Z`
- `2026-09-14T23:16:28.042310Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:15:45Z`
- `2026-09-14T23:15:39.700945Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:15:00Z`
- `2026-09-14T23:14:24.980469Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:13:45Z`
- `2026-09-14T23:12:17.318479Z` — **MID**: 0 rows; marker `2026-09-14T23:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T23:12:17.318479Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:11:45Z`
- `2026-09-14T23:10:42.141337Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:10:00Z`
- `2026-09-14T23:10:26.397711Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:09:45Z`
- `2026-09-14T23:08:18.297137Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:07:45Z`
- `2026-09-14T23:06:21.242642Z` — **MID**: 0 rows; marker `2026-09-14T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T23:06:21.242642Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:05:45Z`
- `2026-09-14T23:05:33.061812Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:05:00Z`
