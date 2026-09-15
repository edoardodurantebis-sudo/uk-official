# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T20:01:50.029079Z`  
Current process started UTC: `2026-09-15T19:57:50.038218Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=-1, z=3.74 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.30 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=54, delta=-1, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=17, z=8.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.39 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.98 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-219** (n=277, 2026-09-15T20:00:30.549182Z)
- `FUELINST|fuelType=NPSHYD|generation` = **476** (n=277, 2026-09-15T20:00:30.549182Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=277, 2026-09-15T20:00:30.549182Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=277, 2026-09-15T20:00:30.549182Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=277, 2026-09-15T20:00:30.549182Z)
- `FUELINST|fuelType=OTHER|generation` = **614** (n=277, 2026-09-15T20:00:30.549182Z)
- `FUELINST|fuelType=PS|generation` = **35** (n=277, 2026-09-15T20:00:30.549182Z)
- `FUELINST|fuelType=WIND|generation` = **10867** (n=277, 2026-09-15T20:00:30.549182Z)
- `IMBALNGC|TOTAL|imbalance` = **5751** (n=46, 2026-09-15T19:51:36.146446Z)
- `INDDEM|TOTAL|demand` = **-11911** (n=46, 2026-09-15T19:51:20.015291Z)
- `INDGEN|TOTAL|generation` = **24872** (n=46, 2026-09-15T19:51:20.015291Z)
- `MELNGC|TOTAL|margin` = **35600** (n=46, 2026-09-15T19:49:27.980644Z)
- `NDF|TOTAL|demand` = **18621** (n=47, 2026-09-15T19:47:36.215259Z)
- `TSDF|TOTAL|demand` = **19121** (n=47, 2026-09-15T19:47:36.215259Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T20:00:30.549182Z` — **FUELHH**: 20 rows; marker `2026-09-15T20:00:00Z`
- `2026-09-15T20:00:30.549182Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:00:00Z`
- `2026-09-15T20:00:14.548427Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:59:45Z`
- `2026-09-15T19:58:06.058155Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:57:45Z`
- `2026-09-15T19:56:14.847858Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:55:45Z`
- `2026-09-15T19:55:42.550434Z` — **FUELINST**: 80 rows; marker `2026-09-15T19:55:00Z`
- `2026-09-15T19:54:22.793169Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:53:45Z`
- `2026-09-15T19:52:24.208682Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:51:45Z`
- `2026-09-15T19:51:36.146446Z` — **IMBALNGC**: 1152 rows; marker `2026-09-15T19:47:00Z`
- `2026-09-15T19:51:20.015291Z` — **INDGEN**: 1152 rows; marker `2026-09-15T19:47:00Z`
- `2026-09-15T19:51:20.015291Z` — **INDDEM**: 1152 rows; marker `2026-09-15T19:47:00Z`
- `2026-09-15T19:50:32.411520Z` — **FUELINST**: 80 rows; marker `2026-09-15T19:50:00Z`
- `2026-09-15T19:50:16.215928Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:49:45Z`
- `2026-09-15T19:49:27.980644Z` — **MELNGC**: 1152 rows; marker `2026-09-15T19:47:00Z`
- `2026-09-15T19:48:24.281180Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:47:45Z`
