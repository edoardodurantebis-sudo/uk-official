# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T22:50:17.292322Z`  
Current process started UTC: `2026-09-14T22:46:16.929887Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=542, delta=109, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=1193, delta=90, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-889, delta=-56, z=-4.14 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=1, delta=-96, z=-5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-833, delta=-111, z=-5.27 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=97, delta=-182, z=-28.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=279, delta=-26, z=-14.31 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTNSL|generation` = **1238** (n=22, 2026-09-14T22:45:47.392447Z)
- `FUELINST|fuelType=INTVKL|generation` = **-668** (n=22, 2026-09-14T22:45:47.392447Z)
- `FUELINST|fuelType=NPSHYD|generation` = **544** (n=22, 2026-09-14T22:45:47.392447Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3314** (n=22, 2026-09-14T22:45:47.392447Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=22, 2026-09-14T22:45:47.392447Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=22, 2026-09-14T22:45:47.392447Z)
- `FUELINST|fuelType=OTHER|generation` = **531** (n=22, 2026-09-14T22:45:47.392447Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=22, 2026-09-14T22:45:47.392447Z)
- `FUELINST|fuelType=WIND|generation` = **12385** (n=22, 2026-09-14T22:45:47.392447Z)
- `IMBALNGC|TOTAL|imbalance` = **-84** (n=4, 2026-09-14T22:22:33.144668Z)
- `INDDEM|TOTAL|demand` = **-12253** (n=4, 2026-09-14T22:22:17.341437Z)
- `INDGEN|TOTAL|generation` = **20400** (n=4, 2026-09-14T22:22:33.144668Z)
- `MELNGC|TOTAL|margin` = **32473** (n=5, 2026-09-14T22:49:32.967588Z)
- `NDF|TOTAL|demand` = **19934** (n=5, 2026-09-14T22:47:25.340833Z)
- `TSDF|TOTAL|demand` = **20485** (n=5, 2026-09-14T22:47:25.340833Z)

## Latest publication events

- `2026-09-14T22:49:32.967588Z` — **MELNGC**: 1044 rows; marker `2026-09-14T22:47:00Z`
- `2026-09-14T22:48:12.835394Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:47:45Z`
- `2026-09-14T22:47:25.340833Z` — **TSDF**: 1044 rows; marker `2026-09-14T22:47:00Z`
- `2026-09-14T22:47:25.340833Z` — **NDF**: 58 rows; marker `2026-09-14T22:47:00Z`
- `2026-09-14T22:46:20.930519Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:45:45Z`
- `2026-09-14T22:45:47.392447Z` — **FUELINST**: 80 rows; marker `2026-09-14T22:45:00Z`
- `2026-09-14T22:44:11.554497Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:43:45Z`
- `2026-09-14T22:42:19.939065Z` — **MID**: 0 rows; marker `2026-09-14T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T22:42:19.939065Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:41:45Z`
- `2026-09-14T22:40:35.895433Z` — **FUELINST**: 80 rows; marker `2026-09-14T22:40:00Z`
- `2026-09-14T22:40:20.156883Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:39:45Z`
- `2026-09-14T22:38:12.432889Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:37:45Z`
- `2026-09-14T22:36:37.545819Z` — **MID**: 0 rows; marker `2026-09-14T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-14T22:36:21.918273Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:35:45Z`
- `2026-09-14T22:35:49.778406Z` — **FUELINST**: 80 rows; marker `2026-09-14T22:35:00Z`
