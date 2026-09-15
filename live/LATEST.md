# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T23:02:54.449333Z`  
Current process started UTC: `2026-09-15T22:58:54.629605Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.36 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **333** (n=313, 2026-09-15T23:00:30.737417Z)
- `FUELINST|fuelType=NPSHYD|generation` = **424** (n=313, 2026-09-15T23:00:30.737417Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=313, 2026-09-15T23:00:30.737417Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=313, 2026-09-15T23:00:30.737417Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=313, 2026-09-15T23:00:30.737417Z)
- `FUELINST|fuelType=OTHER|generation` = **146** (n=313, 2026-09-15T23:00:30.737417Z)
- `FUELINST|fuelType=PS|generation` = **-135** (n=313, 2026-09-15T23:00:30.737417Z)
- `FUELINST|fuelType=WIND|generation` = **11576** (n=313, 2026-09-15T23:00:30.737417Z)
- `IMBALNGC|TOTAL|imbalance` = **5801** (n=52, 2026-09-15T22:51:19.020642Z)
- `INDDEM|TOTAL|demand` = **-12081** (n=52, 2026-09-15T22:51:19.020642Z)
- `INDGEN|TOTAL|generation` = **24922** (n=52, 2026-09-15T22:51:19.020642Z)
- `MELNGC|TOTAL|margin` = **35740** (n=52, 2026-09-15T22:49:19.915312Z)
- `NDF|TOTAL|demand` = **18621** (n=53, 2026-09-15T22:47:44.804584Z)
- `TSDF|TOTAL|demand` = **19121** (n=53, 2026-09-15T22:47:44.804584Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T23:02:22.847297Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:01:45Z`
- `2026-09-15T23:00:30.737417Z` — **FUELHH**: 20 rows; marker `2026-09-15T23:00:00Z`
- `2026-09-15T23:00:30.737417Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:00:00Z`
- `2026-09-15T23:00:14.639724Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:59:45Z`
- `2026-09-15T22:58:14.901306Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:57:45Z`
- `2026-09-15T22:56:07.037598Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:55:45Z`
- `2026-09-15T22:55:18.810969Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:55:00Z`
- `2026-09-15T22:54:15.423524Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:53:45Z`
- `2026-09-15T22:52:06.681428Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:51:45Z`
- `2026-09-15T22:51:19.020642Z` — **INDGEN**: 1044 rows; marker `2026-09-15T22:47:00Z`
- `2026-09-15T22:51:19.020642Z` — **INDDEM**: 1044 rows; marker `2026-09-15T22:47:00Z`
- `2026-09-15T22:51:19.020642Z` — **IMBALNGC**: 1044 rows; marker `2026-09-15T22:47:00Z`
- `2026-09-15T22:50:31.482603Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:50:00Z`
- `2026-09-15T22:50:08.101217Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:49:45Z`
- `2026-09-15T22:49:19.915312Z` — **MELNGC**: 1044 rows; marker `2026-09-15T22:47:00Z`
