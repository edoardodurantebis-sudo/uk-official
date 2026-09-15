# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T09:41:45.289203Z`  
Current process started UTC: `2026-09-15T09:37:44.832622Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=153, 2026-09-15T09:40:24.893460Z)
- `FUELINST|fuelType=NPSHYD|generation` = **431** (n=153, 2026-09-15T09:40:24.893460Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3322** (n=153, 2026-09-15T09:40:24.893460Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=153, 2026-09-15T09:40:24.893460Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=153, 2026-09-15T09:40:24.893460Z)
- `FUELINST|fuelType=OTHER|generation` = **632** (n=153, 2026-09-15T09:40:24.893460Z)
- `FUELINST|fuelType=PS|generation` = **-1206** (n=153, 2026-09-15T09:40:24.893460Z)
- `FUELINST|fuelType=WIND|generation` = **11621** (n=153, 2026-09-15T09:40:24.893460Z)
- `IMBALNGC|TOTAL|imbalance` = **-92** (n=25, 2026-09-15T09:19:33.423977Z)
- `INDDEM|TOTAL|demand` = **-12254** (n=25, 2026-09-15T09:19:16.999957Z)
- `INDGEN|TOTAL|generation` = **20477** (n=25, 2026-09-15T09:19:16.999957Z)
- `MELNGC|TOTAL|margin` = **34498** (n=25, 2026-09-15T09:18:50.361079Z)
- `NDF|TOTAL|demand` = **20069** (n=26, 2026-09-15T09:16:58.629698Z)
- `TSDF|TOTAL|demand` = **20569** (n=26, 2026-09-15T09:16:58.629698Z)
- `WINDFOR|TOTAL|generation` = **16741** (n=4, 2026-09-15T08:30:37.267850Z)

## Latest publication events

- `2026-09-15T09:40:24.893460Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:40:00Z`
- `2026-09-15T09:40:09.441365Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:39:45Z`
- `2026-09-15T09:38:00.839946Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:37:45Z`
- `2026-09-15T09:36:27.690964Z` — **MID**: 0 rows; marker `2026-09-15T09:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T09:36:27.690964Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:35:45Z`
- `2026-09-15T09:35:39.625319Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:35:00Z`
- `2026-09-15T09:34:19.873141Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:33:45Z`
- `2026-09-15T09:32:27.295891Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:31:45Z`
- `2026-09-15T09:30:35.426819Z` — **FUELHH**: 20 rows; marker `2026-09-15T09:30:00Z`
- `2026-09-15T09:30:35.426819Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:30:00Z`
- `2026-09-15T09:30:20.079605Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:29:45Z`
- `2026-09-15T09:29:15.720570Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:27:45Z`
- `2026-09-15T09:26:25.646347Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:25:45Z`
- `2026-09-15T09:25:37.971146Z` — **FUELINST**: 80 rows; marker `2026-09-15T09:25:00Z`
- `2026-09-15T09:24:18.359451Z` — **FREQ**: 5761 rows; marker `2026-09-15T09:23:45Z`
