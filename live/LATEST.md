# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T20:14:28.901315Z`  
Current process started UTC: `2026-09-15T20:10:28.912109Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=279, 2026-09-15T20:10:28.912119Z)
- `FUELINST|fuelType=NPSHYD|generation` = **486** (n=279, 2026-09-15T20:10:28.912119Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3321** (n=279, 2026-09-15T20:10:28.912119Z)
- `FUELINST|fuelType=OCGT|generation` = **2** (n=279, 2026-09-15T20:10:28.912119Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=279, 2026-09-15T20:10:28.912119Z)
- `FUELINST|fuelType=OTHER|generation` = **384** (n=279, 2026-09-15T20:10:28.912119Z)
- `FUELINST|fuelType=PS|generation` = **-256** (n=279, 2026-09-15T20:10:28.912119Z)
- `FUELINST|fuelType=WIND|generation` = **11111** (n=279, 2026-09-15T20:10:28.912119Z)
- `IMBALNGC|TOTAL|imbalance` = **5751** (n=46, 2026-09-15T19:51:36.146446Z)
- `INDDEM|TOTAL|demand` = **-11911** (n=46, 2026-09-15T19:51:20.015291Z)
- `INDGEN|TOTAL|generation` = **24872** (n=46, 2026-09-15T19:51:20.015291Z)
- `MELNGC|TOTAL|margin` = **35600** (n=46, 2026-09-15T19:49:27.980644Z)
- `NDF|TOTAL|demand` = **18621** (n=47, 2026-09-15T19:47:36.215259Z)
- `TSDF|TOTAL|demand` = **19121** (n=47, 2026-09-15T19:47:36.215259Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T20:14:12.801226Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:13:45Z`
- `2026-09-15T20:12:20.699947Z` — **MID**: 0 rows; marker `2026-09-15T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T20:12:20.699947Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:11:45Z`
- `2026-09-15T20:10:28.912119Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:10:00Z`
- `2026-09-15T20:10:28.912119Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:09:45Z`
- `2026-09-15T20:08:10.622093Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:07:45Z`
- `2026-09-15T20:06:34.659072Z` — **MID**: 0 rows; marker `2026-09-15T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T20:06:18.319951Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:05:45Z`
- `2026-09-15T20:05:31.199014Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:05:00Z`
- `2026-09-15T20:04:27.678679Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:03:45Z`
- `2026-09-15T20:02:19.034094Z` — **FREQ**: 5761 rows; marker `2026-09-15T20:01:45Z`
- `2026-09-15T20:00:30.549182Z` — **FUELHH**: 20 rows; marker `2026-09-15T20:00:00Z`
- `2026-09-15T20:00:30.549182Z` — **FUELINST**: 80 rows; marker `2026-09-15T20:00:00Z`
- `2026-09-15T20:00:14.548427Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:59:45Z`
- `2026-09-15T19:58:06.058155Z` — **FREQ**: 5761 rows; marker `2026-09-15T19:57:45Z`
