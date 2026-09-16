# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T19:26:37.248776Z`  
Current process started UTC: `2026-09-16T19:22:37.226537Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.03 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **158** (n=558, 2026-09-16T19:25:38.258695Z)
- `FUELINST|fuelType=NPSHYD|generation` = **512** (n=558, 2026-09-16T19:25:38.258695Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3308** (n=558, 2026-09-16T19:25:38.258695Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=558, 2026-09-16T19:25:38.258695Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=558, 2026-09-16T19:25:38.258695Z)
- `FUELINST|fuelType=OTHER|generation` = **787** (n=558, 2026-09-16T19:25:38.258695Z)
- `FUELINST|fuelType=PS|generation` = **370** (n=558, 2026-09-16T19:25:38.258695Z)
- `FUELINST|fuelType=WIND|generation` = **9334** (n=558, 2026-09-16T19:25:38.258695Z)
- `IMBALNGC|TOTAL|imbalance` = **6644** (n=92, 2026-09-16T19:21:52.909122Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=92, 2026-09-16T19:21:52.909122Z)
- `INDGEN|TOTAL|generation` = **25765** (n=92, 2026-09-16T19:21:52.909122Z)
- `MELNGC|TOTAL|margin` = **33954** (n=92, 2026-09-16T19:19:44.962507Z)
- `NDF|TOTAL|demand` = **18621** (n=94, 2026-09-16T19:17:47.538138Z)
- `TSDF|TOTAL|demand` = **19121** (n=94, 2026-09-16T19:17:47.538138Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T19:26:10.671149Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:25:45Z`
- `2026-09-16T19:25:38.258695Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:25:00Z`
- `2026-09-16T19:24:18.281489Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:23:45Z`
- `2026-09-16T19:22:24.862927Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:21:45Z`
- `2026-09-16T19:21:52.909122Z` — **INDGEN**: 1170 rows; marker `2026-09-16T19:17:00Z`
- `2026-09-16T19:21:52.909122Z` — **INDDEM**: 1170 rows; marker `2026-09-16T19:17:00Z`
- `2026-09-16T19:21:52.909122Z` — **IMBALNGC**: 1170 rows; marker `2026-09-16T19:17:00Z`
- `2026-09-16T19:20:32.272457Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:20:00Z`
- `2026-09-16T19:20:16.455648Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:19:45Z`
- `2026-09-16T19:19:44.962507Z` — **MELNGC**: 1170 rows; marker `2026-09-16T19:17:00Z`
- `2026-09-16T19:18:57.514581Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:17:45Z`
- `2026-09-16T19:17:47.538138Z` — **TSDF**: 1170 rows; marker `2026-09-16T19:17:00Z`
- `2026-09-16T19:17:47.538138Z` — **NDF**: 65 rows; marker `2026-09-16T19:17:00Z`
- `2026-09-16T19:16:11.328358Z` — **FREQ**: 5761 rows; marker `2026-09-16T19:15:45Z`
- `2026-09-16T19:15:37.126667Z` — **FUELINST**: 80 rows; marker `2026-09-16T19:15:00Z`
