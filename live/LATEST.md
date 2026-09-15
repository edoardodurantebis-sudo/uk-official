# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T17:29:14.778925Z`  
Current process started UTC: `2026-09-15T17:25:14.081478Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=3.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=3.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.09 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.26 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=7, delta=2, z=5.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.44 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.65 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.90 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=5.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=5.54 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=5.96 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=5, delta=5, z=4.84 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-777** (n=246, 2026-09-15T17:25:30.086199Z)
- `FUELINST|fuelType=NPSHYD|generation` = **486** (n=246, 2026-09-15T17:25:30.086199Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=246, 2026-09-15T17:25:30.086199Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=246, 2026-09-15T17:25:30.086199Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=246, 2026-09-15T17:25:30.086199Z)
- `FUELINST|fuelType=OTHER|generation` = **1756** (n=246, 2026-09-15T17:25:30.086199Z)
- `FUELINST|fuelType=PS|generation` = **500** (n=246, 2026-09-15T17:25:30.086199Z)
- `FUELINST|fuelType=WIND|generation` = **10609** (n=246, 2026-09-15T17:25:30.086199Z)
- `IMBALNGC|TOTAL|imbalance` = **5772** (n=41, 2026-09-15T17:22:39.607287Z)
- `INDDEM|TOTAL|demand` = **-11918** (n=41, 2026-09-15T17:22:07.980324Z)
- `INDGEN|TOTAL|generation` = **24893** (n=41, 2026-09-15T17:22:07.980324Z)
- `MELNGC|TOTAL|margin` = **34820** (n=41, 2026-09-15T17:19:45.087710Z)
- `NDF|TOTAL|demand` = **18621** (n=42, 2026-09-15T17:17:52.476807Z)
- `TSDF|TOTAL|demand` = **19121** (n=42, 2026-09-15T17:17:52.476807Z)
- `WINDFOR|TOTAL|generation` = **17795** (n=7, 2026-09-15T16:30:51.506988Z)

## Latest publication events

- `2026-09-15T17:28:26.140972Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:27:45Z`
- `2026-09-15T17:26:17.928221Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:25:45Z`
- `2026-09-15T17:25:30.086199Z` — **FUELINST**: 80 rows; marker `2026-09-15T17:25:00Z`
- `2026-09-15T17:24:15.262861Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:23:45Z`
- `2026-09-15T17:22:39.607287Z` — **IMBALNGC**: 1242 rows; marker `2026-09-15T17:17:00Z`
- `2026-09-15T17:22:23.722206Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:21:45Z`
- `2026-09-15T17:22:07.980324Z` — **INDGEN**: 1242 rows; marker `2026-09-15T17:17:00Z`
- `2026-09-15T17:22:07.980324Z` — **INDDEM**: 1242 rows; marker `2026-09-15T17:17:00Z`
- `2026-09-15T17:20:32.993335Z` — **FUELINST**: 80 rows; marker `2026-09-15T17:20:00Z`
- `2026-09-15T17:20:16.816576Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:19:45Z`
- `2026-09-15T17:19:45.087710Z` — **MELNGC**: 1242 rows; marker `2026-09-15T17:17:00Z`
- `2026-09-15T17:18:24.842003Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:17:45Z`
- `2026-09-15T17:17:52.476807Z` — **TSDF**: 1242 rows; marker `2026-09-15T17:17:00Z`
- `2026-09-15T17:17:52.476807Z` — **NDF**: 69 rows; marker `2026-09-15T17:17:00Z`
- `2026-09-15T17:16:23.450294Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:15:45Z`
