# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T00:18:17.512884Z`  
Current process started UTC: `2026-09-15T00:14:17.709448Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=3.56 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=3.86 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=-299, delta=8, z=3.95 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=4.25 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=4.80 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=5.62 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=INTNEM` `generation` — instantaneous generation mix [fuelType=INTNEM] generation: value=-307, delta=170, z=4.89 -> generation-mix component moved
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0, z=7.11 -> frequency excursion; balancing stress check
- **FREQ** `TOTAL` `frequency` — system frequency [TOTAL] frequency: value=50.088, delta=0.004, z=11.23 -> frequency excursion; balancing stress check
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2683, delta=11, z=5.04 -> generation-mix component moved
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2672, delta=95, z=11.64 -> generation-mix component moved
- **FUELINST** `fuelType=BIOMASS` `generation` — instantaneous generation mix [fuelType=BIOMASS] generation: value=2560, delta=-26, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=542, delta=109, z=4.43 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=1193, delta=90, z=3.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTIFA2` `generation` — instantaneous generation mix [fuelType=INTIFA2] generation: value=-889, delta=-56, z=-4.14 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-134** (n=40, 2026-09-15T00:15:37.695089Z)
- `FUELINST|fuelType=NPSHYD|generation` = **367** (n=40, 2026-09-15T00:15:37.695089Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3314** (n=40, 2026-09-15T00:15:37.695089Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=40, 2026-09-15T00:15:37.695089Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=40, 2026-09-15T00:15:37.695089Z)
- `FUELINST|fuelType=OTHER|generation` = **328** (n=40, 2026-09-15T00:15:37.695089Z)
- `FUELINST|fuelType=PS|generation` = **-14** (n=40, 2026-09-15T00:15:37.695089Z)
- `FUELINST|fuelType=WIND|generation` = **11926** (n=40, 2026-09-15T00:15:37.695089Z)
- `IMBALNGC|TOTAL|imbalance` = **210** (n=7, 2026-09-14T23:51:32.096612Z)
- `INDDEM|TOTAL|demand` = **-12270** (n=7, 2026-09-14T23:51:48.749871Z)
- `INDGEN|TOTAL|generation` = **20695** (n=7, 2026-09-14T23:51:32.096612Z)
- `MELNGC|TOTAL|margin` = **32721** (n=7, 2026-09-14T23:49:56.529171Z)
- `NDF|TOTAL|demand` = **19934** (n=8, 2026-09-15T00:17:29.827613Z)
- `TSDF|TOTAL|demand` = **20485** (n=8, 2026-09-15T00:17:29.827613Z)
- `WINDFOR|TOTAL|generation` = **7851** (n=1, 2026-09-14T23:30:39.804378Z)

## Latest publication events

- `2026-09-15T00:17:29.827613Z` — **TSDF**: 990 rows; marker `2026-09-15T00:17:00Z`
- `2026-09-15T00:17:29.827613Z` — **NDF**: 55 rows; marker `2026-09-15T00:17:00Z`
- `2026-09-15T00:16:09.760722Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:15:45Z`
- `2026-09-15T00:15:37.695089Z` — **FUELINST**: 80 rows; marker `2026-09-15T00:15:00Z`
- `2026-09-15T00:14:17.709456Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:13:45Z`
- `2026-09-15T00:12:15.854336Z` — **MID**: 0 rows; marker `2026-09-15T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T00:12:15.854336Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:11:45Z`
- `2026-09-15T00:10:39.605897Z` — **FUELINST**: 80 rows; marker `2026-09-15T00:10:00Z`
- `2026-09-15T00:10:07.440700Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:09:45Z`
- `2026-09-15T00:08:16.640532Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:07:45Z`
- `2026-09-15T00:06:24.444661Z` — **MID**: 0 rows; marker `2026-09-15T00:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T00:06:24.444661Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:05:45Z`
- `2026-09-15T00:05:52.121224Z` — **FUELINST**: 80 rows; marker `2026-09-15T00:05:00Z`
- `2026-09-15T00:04:24.497031Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:03:45Z`
- `2026-09-15T00:02:32.006452Z` — **FREQ**: 5761 rows; marker `2026-09-15T00:01:45Z`
