# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T10:23:40.716473Z`  
Current process started UTC: `2026-09-15T10:19:41.069476Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTFR` `generation` — half-hour generation mix [fuelType=INTFR] generation: value=984, delta=278, z=4.11 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=999, delta=-1, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=1000, delta=1, z=3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=999, delta=86, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=913, delta=181, z=3.84 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=161, 2026-09-15T10:20:45.581792Z)
- `FUELINST|fuelType=NPSHYD|generation` = **381** (n=161, 2026-09-15T10:20:45.581792Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=161, 2026-09-15T10:20:45.581792Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=161, 2026-09-15T10:20:45.581792Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=161, 2026-09-15T10:20:45.581792Z)
- `FUELINST|fuelType=OTHER|generation` = **588** (n=161, 2026-09-15T10:20:45.581792Z)
- `FUELINST|fuelType=PS|generation` = **-1206** (n=161, 2026-09-15T10:20:45.581792Z)
- `FUELINST|fuelType=WIND|generation` = **11516** (n=161, 2026-09-15T10:20:45.581792Z)
- `IMBALNGC|TOTAL|imbalance` = **-832** (n=27, 2026-09-15T10:19:25.748675Z)
- `INDDEM|TOTAL|demand` = **-12270** (n=27, 2026-09-15T10:19:25.748675Z)
- `INDGEN|TOTAL|generation` = **19737** (n=27, 2026-09-15T10:19:25.748675Z)
- `MELNGC|TOTAL|margin` = **34489** (n=27, 2026-09-15T10:18:37.997581Z)
- `NDF|TOTAL|demand` = **20069** (n=28, 2026-09-15T10:17:02.596245Z)
- `TSDF|TOTAL|demand` = **20569** (n=28, 2026-09-15T10:17:02.596245Z)
- `WINDFOR|TOTAL|generation` = **16741** (n=4, 2026-09-15T08:30:37.267850Z)

## Latest publication events

- `2026-09-15T10:22:22.680731Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:21:45Z`
- `2026-09-15T10:20:45.581792Z` — **FUELINST**: 80 rows; marker `2026-09-15T10:20:00Z`
- `2026-09-15T10:20:30.076436Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:19:45Z`
- `2026-09-15T10:19:25.748675Z` — **INDGEN**: 630 rows; marker `2026-09-15T10:16:00Z`
- `2026-09-15T10:19:25.748675Z` — **INDDEM**: 630 rows; marker `2026-09-15T10:16:00Z`
- `2026-09-15T10:19:25.748675Z` — **IMBALNGC**: 630 rows; marker `2026-09-15T10:16:00Z`
- `2026-09-15T10:18:37.997581Z` — **MELNGC**: 630 rows; marker `2026-09-15T10:16:00Z`
- `2026-09-15T10:18:21.652278Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:17:45Z`
- `2026-09-15T10:17:02.596245Z` — **TSDF**: 630 rows; marker `2026-09-15T10:16:00Z`
- `2026-09-15T10:17:02.596245Z` — **NDF**: 35 rows; marker `2026-09-15T10:16:00Z`
- `2026-09-15T10:16:14.817334Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:15:45Z`
- `2026-09-15T10:15:43.297085Z` — **FUELINST**: 80 rows; marker `2026-09-15T10:15:00Z`
- `2026-09-15T10:14:28.469286Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:13:45Z`
- `2026-09-15T10:12:19.166927Z` — **MID**: 0 rows; marker `2026-09-15T10:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T10:12:19.166927Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:11:45Z`
