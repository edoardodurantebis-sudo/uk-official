# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T09:10:39.887168Z`  
Current process started UTC: `2026-09-15T09:06:39.503704Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=700, delta=162, z=4.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTFR` `generation` — instantaneous generation mix [fuelType=INTFR] generation: value=538, delta=280, z=3.81 -> generation-mix component moved
- **FUELHH** `fuelType=INTNEM` `generation` — half-hour generation mix [fuelType=INTNEM] generation: value=824, delta=70, z=4.21 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=147, 2026-09-15T09:10:23.307837Z)
- `FUELINST|fuelType=NPSHYD|generation` = **419** (n=147, 2026-09-15T09:10:23.307837Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3314** (n=147, 2026-09-15T09:10:23.307837Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=147, 2026-09-15T09:10:23.307837Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=147, 2026-09-15T09:10:23.307837Z)
- `FUELINST|fuelType=OTHER|generation` = **561** (n=147, 2026-09-15T09:10:23.307837Z)
- `FUELINST|fuelType=PS|generation` = **-986** (n=147, 2026-09-15T09:10:23.307837Z)
- `FUELINST|fuelType=WIND|generation` = **12001** (n=147, 2026-09-15T09:10:23.307837Z)
- `IMBALNGC|TOTAL|imbalance` = **-135** (n=24, 2026-09-15T08:49:57.718820Z)
- `INDDEM|TOTAL|demand` = **-12399** (n=24, 2026-09-15T08:49:57.718820Z)
- `INDGEN|TOTAL|generation` = **20434** (n=24, 2026-09-15T08:49:57.718820Z)
- `MELNGC|TOTAL|margin` = **34078** (n=24, 2026-09-15T08:49:01.671175Z)
- `NDF|TOTAL|demand` = **20069** (n=25, 2026-09-15T08:47:08.938044Z)
- `TSDF|TOTAL|demand` = **20569** (n=25, 2026-09-15T08:47:08.938044Z)
- `WINDFOR|TOTAL|generation` = **16741** (n=4, 2026-09-15T08:30:37.267850Z)

## Latest publication events

- `2026-09-15T09:10:23.307837Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:10:00Z`
- `2026-09-15T09:10:23.307837Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:09:45Z`
- `2026-09-15T09:08:15.816522Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:07:45Z`
- `2026-09-15T09:06:39.503711Z` — **MID**: 0 rows; marker `2026-09-15T09:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T09:06:17.502812Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:05:45Z`
- `2026-09-15T09:05:29.446639Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:05:00Z`
- `2026-09-15T09:04:09.961204Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:03:45Z`
- `2026-09-15T09:02:17.601383Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:01:45Z`
- `2026-09-15T09:00:25.735569Z` — **FUELHH**: 20 rows; marker `2026-09-15T09:00:00Z`
- `2026-09-15T09:00:25.735569Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:00:00Z`
- `2026-09-15T09:00:10.157849Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:59:45Z`
- `2026-09-15T08:58:18.724418Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:57:45Z`
- `2026-09-15T08:56:17.293115Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:55:45Z`
- `2026-09-15T08:55:28.724460Z` — **FUELINST**: 80 rows; marker `2026-09-15T08:55:00Z`
- `2026-09-15T08:54:08.662410Z` — **FREQ**: 5761 rows; marker `2026-09-15T08:53:45Z`
