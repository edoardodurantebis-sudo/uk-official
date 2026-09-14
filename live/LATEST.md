# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-14T22:25:10.719092Z`  
Current process started UTC: `2026-09-14T22:21:10.596728Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=1193, delta=90, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-889, delta=-56, z=-4.14 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=1, delta=-96, z=-5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-833, delta=-111, z=-5.27 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=97, delta=-182, z=-28.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=279, delta=-26, z=-14.31 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTNSL|generation` = **1238** (n=17, 2026-09-14T22:20:40.664052Z)
- `FUELINST|fuelType=INTVKL|generation` = **-668** (n=17, 2026-09-14T22:20:40.664052Z)
- `FUELINST|fuelType=NPSHYD|generation` = **417** (n=17, 2026-09-14T22:20:40.664052Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3311** (n=17, 2026-09-14T22:20:40.664052Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=17, 2026-09-14T22:20:40.664052Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=17, 2026-09-14T22:20:40.664052Z)
- `FUELINST|fuelType=OTHER|generation` = **336** (n=17, 2026-09-14T22:20:40.664052Z)
- `FUELINST|fuelType=PS|generation` = **-12** (n=17, 2026-09-14T22:20:40.664052Z)
- `FUELINST|fuelType=WIND|generation` = **12712** (n=17, 2026-09-14T22:20:40.664052Z)
- `IMBALNGC|TOTAL|imbalance` = **-84** (n=4, 2026-09-14T22:22:33.144668Z)
- `INDDEM|TOTAL|demand` = **-12253** (n=4, 2026-09-14T22:22:17.341437Z)
- `INDGEN|TOTAL|generation` = **20400** (n=4, 2026-09-14T22:22:33.144668Z)
- `MELNGC|TOTAL|margin` = **32423** (n=4, 2026-09-14T22:20:08.999532Z)
- `NDF|TOTAL|demand` = **19934** (n=4, 2026-09-14T22:17:45.947912Z)
- `TSDF|TOTAL|demand` = **20485** (n=4, 2026-09-14T22:18:01.053049Z)

## Latest publication events

- `2026-09-14T22:24:09.139681Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:23:45Z`
- `2026-09-14T22:22:33.144668Z` — **INDGEN**: 1062 rows; marker `2026-09-14T22:17:00Z`
- `2026-09-14T22:22:33.144668Z` — **IMBALNGC**: 1062 rows; marker `2026-09-14T22:17:00Z`
- `2026-09-14T22:22:17.341437Z` — **INDDEM**: 1062 rows; marker `2026-09-14T22:17:00Z`
- `2026-09-14T22:22:00.601783Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:21:45Z`
- `2026-09-14T22:20:40.664052Z` — **FUELINST**: 80 rows; marker `2026-09-14T22:20:00Z`
- `2026-09-14T22:20:24.848929Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:19:45Z`
- `2026-09-14T22:20:08.999532Z` — **MELNGC**: 1062 rows; marker `2026-09-14T22:17:00Z`
- `2026-09-14T22:18:16.723114Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:17:45Z`
- `2026-09-14T22:18:01.053049Z` — **TSDF**: 1062 rows; marker `2026-09-14T22:17:00Z`
- `2026-09-14T22:17:45.947912Z` — **NDF**: 59 rows; marker `2026-09-14T22:17:00Z`
- `2026-09-14T22:16:14.167638Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:15:45Z`
- `2026-09-14T22:15:42.357185Z` — **FUELINST**: 80 rows; marker `2026-09-14T22:15:00Z`
- `2026-09-14T22:14:22.113187Z` — **FREQ**: 5761 rows; marker `2026-09-14T22:13:45Z`
- `2026-09-14T22:12:21.198449Z` — **MID**: 0 rows; marker `2026-09-14T22:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
