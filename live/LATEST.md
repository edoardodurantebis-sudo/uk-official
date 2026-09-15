# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T10:06:53.198479Z`  
Current process started UTC: `2026-09-15T10:02:53.522841Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=158, 2026-09-15T10:05:39.597660Z)
- `FUELINST|fuelType=NPSHYD|generation` = **378** (n=158, 2026-09-15T10:05:39.597660Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=158, 2026-09-15T10:05:39.597660Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=158, 2026-09-15T10:05:39.597660Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=158, 2026-09-15T10:05:39.597660Z)
- `FUELINST|fuelType=OTHER|generation` = **524** (n=158, 2026-09-15T10:05:39.597660Z)
- `FUELINST|fuelType=PS|generation` = **-1232** (n=158, 2026-09-15T10:05:39.597660Z)
- `FUELINST|fuelType=WIND|generation` = **11814** (n=158, 2026-09-15T10:05:39.597660Z)
- `IMBALNGC|TOTAL|imbalance` = **-365** (n=26, 2026-09-15T09:49:52.093125Z)
- `INDDEM|TOTAL|demand` = **-12382** (n=26, 2026-09-15T09:49:52.093125Z)
- `INDGEN|TOTAL|generation` = **20204** (n=26, 2026-09-15T09:49:52.093125Z)
- `MELNGC|TOTAL|margin` = **34344** (n=26, 2026-09-15T09:49:19.900257Z)
- `NDF|TOTAL|demand` = **20069** (n=27, 2026-09-15T09:46:55.089447Z)
- `TSDF|TOTAL|demand` = **20569** (n=27, 2026-09-15T09:46:55.089447Z)
- `WINDFOR|TOTAL|generation` = **16741** (n=4, 2026-09-15T08:30:37.267850Z)

## Latest publication events

- `2026-09-15T10:06:11.670343Z` — **MID**: 0 rows; marker `2026-09-15T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T10:06:11.670343Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:05:45Z`
- `2026-09-15T10:05:39.597660Z` — **FUELINST**: 80 rows; marker `2026-09-15T10:05:00Z`
- `2026-09-15T10:04:18.615375Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:03:45Z`
- `2026-09-15T10:02:10.463168Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:01:45Z`
- `2026-09-15T10:00:50.162330Z` — **FUELHH**: 20 rows; marker `2026-09-15T10:00:00Z`
- `2026-09-15T10:00:34.158120Z` — **FUELINST**: 80 rows; marker `2026-09-15T10:00:00Z`
- `2026-09-15T10:00:18.075292Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:59:45Z`
- `2026-09-15T09:58:16.547358Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:57:45Z`
- `2026-09-15T09:56:24.980327Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:55:45Z`
- `2026-09-15T09:55:37.344316Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:55:00Z`
- `2026-09-15T09:54:16.850837Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:53:45Z`
- `2026-09-15T09:52:09.416105Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:51:45Z`
- `2026-09-15T09:50:33.056428Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:50:00Z`
- `2026-09-15T09:50:33.056428Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:49:45Z`
