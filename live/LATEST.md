# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T23:15:27.903261Z`  
Current process started UTC: `2026-09-14T23:11:27.312190Z`  
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

- `FUELINST|fuelType=INTNSL|generation` = **1381** (n=27, 2026-09-14T23:10:42.141337Z)
- `FUELINST|fuelType=INTVKL|generation` = **-134** (n=27, 2026-09-14T23:10:42.141337Z)
- `FUELINST|fuelType=NPSHYD|generation` = **428** (n=27, 2026-09-14T23:10:42.141337Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3314** (n=27, 2026-09-14T23:10:42.141337Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=27, 2026-09-14T23:10:42.141337Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=27, 2026-09-14T23:10:42.141337Z)
- `FUELINST|fuelType=OTHER|generation` = **89** (n=27, 2026-09-14T23:10:42.141337Z)
- `FUELINST|fuelType=PS|generation` = **-138** (n=27, 2026-09-14T23:10:42.141337Z)
- `FUELINST|fuelType=WIND|generation` = **12395** (n=27, 2026-09-14T23:10:42.141337Z)
- `IMBALNGC|TOTAL|imbalance` = **-63** (n=5, 2026-09-14T22:51:15.871339Z)
- `INDDEM|TOTAL|demand` = **-12269** (n=5, 2026-09-14T22:50:59.511453Z)
- `INDGEN|TOTAL|generation` = **20421** (n=5, 2026-09-14T22:50:59.511453Z)
- `MELNGC|TOTAL|margin` = **32473** (n=5, 2026-09-14T22:49:32.967588Z)
- `NDF|TOTAL|demand` = **19934** (n=5, 2026-09-14T22:47:25.340833Z)
- `TSDF|TOTAL|demand` = **20485** (n=5, 2026-09-14T22:47:25.340833Z)

## Latest publication events

- `2026-09-14T23:14:24.980469Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:13:45Z`
- `2026-09-14T23:12:17.318479Z` — **MID**: 0 rows; marker `2026-09-14T23:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T23:12:17.318479Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:11:45Z`
- `2026-09-14T23:10:42.141337Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:10:00Z`
- `2026-09-14T23:10:26.397711Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:09:45Z`
- `2026-09-14T23:08:18.297137Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:07:45Z`
- `2026-09-14T23:06:21.242642Z` — **MID**: 0 rows; marker `2026-09-14T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T23:06:21.242642Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:05:45Z`
- `2026-09-14T23:05:33.061812Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:05:00Z`
- `2026-09-14T23:04:29.297283Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:03:45Z`
- `2026-09-14T23:02:18.328320Z` — **FREQ**: 5761 rows; marker `2026-09-14T23:01:45Z`
- `2026-09-14T23:00:58.840472Z` — **FUELHH**: 20 rows; marker `2026-09-14T23:00:00Z`
- `2026-09-14T23:00:26.749419Z` — **FUELINST**: 80 rows; marker `2026-09-14T23:00:00Z`
- `2026-09-14T23:00:26.749419Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:59:45Z`
- `2026-09-14T22:58:23.331491Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:57:45Z`
