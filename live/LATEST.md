# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T08:53:57.253848Z`  
Current process started UTC: `2026-09-15T08:49:57.718812Z`  
1-second metadata polls in this process: **236**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=143, 2026-09-15T08:50:29.464436Z)
- `FUELINST|fuelType=NPSHYD|generation` = **430** (n=143, 2026-09-15T08:50:29.464436Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3317** (n=143, 2026-09-15T08:50:29.464436Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=143, 2026-09-15T08:50:29.464436Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=143, 2026-09-15T08:50:29.464436Z)
- `FUELINST|fuelType=OTHER|generation` = **809** (n=143, 2026-09-15T08:50:29.464436Z)
- `FUELINST|fuelType=PS|generation` = **-538** (n=143, 2026-09-15T08:50:29.464436Z)
- `FUELINST|fuelType=WIND|generation` = **12062** (n=143, 2026-09-15T08:50:29.464436Z)
- `IMBALNGC|TOTAL|imbalance` = **-135** (n=24, 2026-09-15T08:49:57.718820Z)
- `INDDEM|TOTAL|demand` = **-12399** (n=24, 2026-09-15T08:49:57.718820Z)
- `INDGEN|TOTAL|generation` = **20434** (n=24, 2026-09-15T08:49:57.718820Z)
- `MELNGC|TOTAL|margin` = **34078** (n=24, 2026-09-15T08:49:01.671175Z)
- `NDF|TOTAL|demand` = **20069** (n=25, 2026-09-15T08:47:08.938044Z)
- `TSDF|TOTAL|demand` = **20569** (n=25, 2026-09-15T08:47:08.938044Z)
- `WINDFOR|TOTAL|generation` = **16741** (n=4, 2026-09-15T08:30:37.267850Z)

## Latest publication events

- `2026-09-15T08:52:05.660153Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:51:45Z`
- `2026-09-15T08:50:29.464436Z` — **FUELINST**: 80 rows; marker `2026-09-15T08:50:00Z`
- `2026-09-15T08:50:13.527258Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:49:45Z`
- `2026-09-15T08:49:57.718820Z` — **INDGEN**: 684 rows; marker `2026-09-15T08:46:00Z`
- `2026-09-15T08:49:57.718820Z` — **INDDEM**: 684 rows; marker `2026-09-15T08:46:00Z`
- `2026-09-15T08:49:57.718820Z` — **IMBALNGC**: 684 rows; marker `2026-09-15T08:46:00Z`
- `2026-09-15T08:49:01.671175Z` — **MELNGC**: 684 rows; marker `2026-09-15T08:46:00Z`
- `2026-09-15T08:48:13.411375Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:47:45Z`
- `2026-09-15T08:47:08.938044Z` — **TSDF**: 684 rows; marker `2026-09-15T08:46:00Z`
- `2026-09-15T08:47:08.938044Z` — **NDF**: 38 rows; marker `2026-09-15T08:46:00Z`
- `2026-09-15T08:46:04.079358Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:45:45Z`
- `2026-09-15T08:45:48.427484Z` — **FUELINST**: 80 rows; marker `2026-09-15T08:45:00Z`
- `2026-09-15T08:44:28.040825Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:43:45Z`
- `2026-09-15T08:42:20.092781Z` — **MID**: 0 rows; marker `2026-09-15T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T08:42:20.092781Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:41:45Z`
