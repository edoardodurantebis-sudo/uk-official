# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T08:37:10.245830Z`  
Current process started UTC: `2026-09-15T08:33:10.053946Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=3.52 -> generation-mix component moved
- **FUELHH** `fuelType=INTNEM` `generation` — half-hour generation mix [fuelType=INTNEM] generation: value=1016, delta=192, z=3.59 -> generation-mix component moved
- **FUELHH** `fuelType=INTIFA2` `generation` — half-hour generation mix [fuelType=INTIFA2] generation: value=828, delta=552, z=3.62 -> generation-mix component moved
- **FUELHH** `fuelType=INTFR` `generation` — half-hour generation mix [fuelType=INTFR] generation: value=674, delta=468, z=4.35 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=3.70 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=3.92 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=4.18 -> generation-mix component moved
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=20619, delta=1396, z=0.72 -> demand pressure up
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=20069, delta=1346, z=0.74 -> demand pressure up
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=0, z=4.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=162, z=4.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=538, delta=280, z=3.81 -> generation-mix component moved
- **FUELHH** `fuelType=INTNEM` `generation` — half-hour generation mix [fuelType=INTNEM] generation: value=824, delta=70, z=4.21 -> generation-mix component moved
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=19223, delta=-1261, z=-2941.66 -> demand pressure easing
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=822, delta=0, z=3.60 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=140, 2026-09-15T08:35:34.406191Z)
- `FUELINST|fuelType=NPSHYD|generation` = **431** (n=140, 2026-09-15T08:35:34.406191Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=140, 2026-09-15T08:35:34.406191Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=140, 2026-09-15T08:35:34.406191Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=140, 2026-09-15T08:35:34.406191Z)
- `FUELINST|fuelType=OTHER|generation` = **850** (n=140, 2026-09-15T08:35:34.406191Z)
- `FUELINST|fuelType=PS|generation` = **-540** (n=140, 2026-09-15T08:35:34.406191Z)
- `FUELINST|fuelType=WIND|generation` = **12608** (n=140, 2026-09-15T08:35:34.406191Z)
- `IMBALNGC|TOTAL|imbalance` = **-475** (n=23, 2026-09-15T08:19:48.895221Z)
- `INDDEM|TOTAL|demand` = **-12308** (n=23, 2026-09-15T08:19:48.895221Z)
- `INDGEN|TOTAL|generation` = **20144** (n=23, 2026-09-15T08:19:48.895221Z)
- `MELNGC|TOTAL|margin` = **34045** (n=23, 2026-09-15T08:19:16.718059Z)
- `NDF|TOTAL|demand` = **20069** (n=24, 2026-09-15T08:17:09.102894Z)
- `TSDF|TOTAL|demand` = **20619** (n=24, 2026-09-15T08:17:25.048682Z)
- `WINDFOR|TOTAL|generation` = **16741** (n=4, 2026-09-15T08:30:37.267850Z)

## Latest publication events

- `2026-09-15T08:36:21.631802Z` — **MID**: 0 rows; marker `2026-09-15T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T08:36:21.631802Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:35:45Z`
- `2026-09-15T08:35:34.406191Z` — **FUELINST**: 80 rows; marker `2026-09-15T08:35:00Z`
- `2026-09-15T08:34:14.403090Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:33:45Z`
- `2026-09-15T08:32:29.930948Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:31:45Z`
- `2026-09-15T08:30:37.267850Z` — **WINDFOR**: 73 rows; marker `2026-09-15T08:30:00Z`
- `2026-09-15T08:30:37.267850Z` — **FUELHH**: 20 rows; marker `2026-09-15T08:30:00Z`
- `2026-09-15T08:30:37.267850Z` — **FUELINST**: 80 rows; marker `2026-09-15T08:30:00Z`
- `2026-09-15T08:30:21.055218Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:29:45Z`
- `2026-09-15T08:28:12.918764Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:27:45Z`
- `2026-09-15T08:26:21.336889Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:25:45Z`
- `2026-09-15T08:25:33.250501Z` — **FUELINST**: 80 rows; marker `2026-09-15T08:25:00Z`
- `2026-09-15T08:24:22.948930Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:23:45Z`
- `2026-09-15T08:22:14.882532Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:21:45Z`
- `2026-09-15T08:20:37.700628Z` — **FUELINST**: 80 rows; marker `2026-09-15T08:20:00Z`
