# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T10:36:19.374873Z`  
Current process started UTC: `2026-09-15T10:32:19.749107Z`  
1-second metadata polls in this process: **236**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=164, 2026-09-15T10:35:49.353263Z)
- `FUELINST|fuelType=NPSHYD|generation` = **404** (n=164, 2026-09-15T10:35:49.353263Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=164, 2026-09-15T10:35:49.353263Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=164, 2026-09-15T10:35:49.353263Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=164, 2026-09-15T10:35:49.353263Z)
- `FUELINST|fuelType=OTHER|generation` = **722** (n=164, 2026-09-15T10:35:49.353263Z)
- `FUELINST|fuelType=PS|generation` = **-1204** (n=164, 2026-09-15T10:35:49.353263Z)
- `FUELINST|fuelType=WIND|generation` = **11516** (n=164, 2026-09-15T10:35:49.353263Z)
- `IMBALNGC|TOTAL|imbalance` = **-832** (n=27, 2026-09-15T10:19:25.748675Z)
- `INDDEM|TOTAL|demand` = **-12270** (n=27, 2026-09-15T10:19:25.748675Z)
- `INDGEN|TOTAL|generation` = **19737** (n=27, 2026-09-15T10:19:25.748675Z)
- `MELNGC|TOTAL|margin` = **34489** (n=27, 2026-09-15T10:18:37.997581Z)
- `NDF|TOTAL|demand` = **20069** (n=28, 2026-09-15T10:17:02.596245Z)
- `TSDF|TOTAL|demand` = **20569** (n=28, 2026-09-15T10:17:02.596245Z)
- `WINDFOR|TOTAL|generation` = **17599** (n=5, 2026-09-15T10:30:45.227650Z)

## Latest publication events

- `2026-09-15T10:36:04.814007Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:35:45Z`
- `2026-09-15T10:35:49.353263Z` — **FUELINST**: 80 rows; marker `2026-09-15T10:35:00Z`
- `2026-09-15T10:34:12.764008Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:33:45Z`
- `2026-09-15T10:32:05.111024Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:31:45Z`
- `2026-09-15T10:30:45.227650Z` — **WINDFOR**: 73 rows; marker `2026-09-15T10:30:00Z`
- `2026-09-15T10:30:45.227650Z` — **FUELHH**: 20 rows; marker `2026-09-15T10:30:00Z`
- `2026-09-15T10:30:29.800951Z` — **FUELINST**: 80 rows; marker `2026-09-15T10:30:00Z`
- `2026-09-15T10:30:13.509475Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:29:45Z`
- `2026-09-15T10:28:21.259637Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:27:45Z`
- `2026-09-15T10:26:17.619217Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:25:45Z`
- `2026-09-15T10:25:46.016608Z` — **FUELINST**: 80 rows; marker `2026-09-15T10:25:00Z`
- `2026-09-15T10:24:23.724093Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:23:45Z`
- `2026-09-15T10:22:22.680731Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:21:45Z`
- `2026-09-15T10:20:45.581792Z` — **FUELINST**: 80 rows; marker `2026-09-15T10:20:00Z`
- `2026-09-15T10:20:30.076436Z` — **FREQ**: 5761 rows; marker `2026-09-15T10:19:45Z`
