# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T19:51:38.680647Z`  
Current process started UTC: `2026-09-16T19:47:38.979369Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=692, delta=5, z=3.75 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.97 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=692, delta=2, z=3.51 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **158** (n=563, 2026-09-16T19:50:18.787094Z)
- `FUELINST|fuelType=NPSHYD|generation` = **512** (n=563, 2026-09-16T19:50:18.787094Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3311** (n=563, 2026-09-16T19:50:18.787094Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=563, 2026-09-16T19:50:18.787094Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=563, 2026-09-16T19:50:18.787094Z)
- `FUELINST|fuelType=OTHER|generation` = **526** (n=563, 2026-09-16T19:50:18.787094Z)
- `FUELINST|fuelType=PS|generation` = **228** (n=563, 2026-09-16T19:50:18.787094Z)
- `FUELINST|fuelType=WIND|generation` = **9887** (n=563, 2026-09-16T19:50:18.787094Z)
- `IMBALNGC|TOTAL|imbalance` = **6644** (n=92, 2026-09-16T19:21:52.909122Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=92, 2026-09-16T19:21:52.909122Z)
- `INDGEN|TOTAL|generation` = **25765** (n=92, 2026-09-16T19:21:52.909122Z)
- `MELNGC|TOTAL|margin` = **34409** (n=93, 2026-09-16T19:50:18.787094Z)
- `NDF|TOTAL|demand` = **18621** (n=95, 2026-09-16T19:47:38.979377Z)
- `TSDF|TOTAL|demand` = **19121** (n=95, 2026-09-16T19:47:38.979377Z)
- `WINDFOR|TOTAL|generation` = **19445** (n=16, 2026-09-16T19:30:31.948327Z)

## Latest publication events

- `2026-09-16T19:50:18.787094Z` — **MELNGC**: 1152 rows; marker `2026-09-16T19:47:00Z`
- `2026-09-16T19:50:18.787094Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:50:00Z`
- `2026-09-16T19:50:18.787094Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:49:45Z`
- `2026-09-16T19:48:26.747129Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:47:45Z`
- `2026-09-16T19:47:38.979377Z` — **TSDF**: 1152 rows; marker `2026-09-16T19:47:00Z`
- `2026-09-16T19:47:38.979377Z` — **NDF**: 64 rows; marker `2026-09-16T19:47:00Z`
- `2026-09-16T19:46:25.273029Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:45:45Z`
- `2026-09-16T19:45:37.125234Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:45:00Z`
- `2026-09-16T19:44:17.220712Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:43:45Z`
- `2026-09-16T19:42:16.646650Z` — **MID**: 0 rows; marker `2026-09-16T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T19:42:16.646650Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:41:45Z`
- `2026-09-16T19:40:39.254776Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:40:00Z`
- `2026-09-16T19:40:23.411822Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:39:45Z`
- `2026-09-16T19:38:06.185551Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:37:45Z`
- `2026-09-16T19:36:29.978717Z` — **MID**: 0 rows; marker `2026-09-16T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
