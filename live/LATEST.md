# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T16:59:15.827923Z`  
Current process started UTC: `2026-09-16T16:55:16.101628Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-1, delta=7, z=4.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-8, delta=24, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-32, delta=24, z=4.45 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-56, delta=26, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-82, delta=26, z=4.07 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-108, delta=25, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=-133, delta=24, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=0, z=-3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=-3, z=-3.63 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3286, delta=2, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3285, delta=6, z=-3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3279, delta=-1, z=-4.31 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3284, delta=-5, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3280, delta=-3, z=-4.29 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3283, delta=-4, z=-4.06 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **164** (n=528, 2026-09-16T16:55:48.106451Z)
- `FUELINST|fuelType=NPSHYD|generation` = **515** (n=528, 2026-09-16T16:55:48.106451Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=528, 2026-09-16T16:55:48.106451Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=528, 2026-09-16T16:55:48.106451Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=528, 2026-09-16T16:55:48.106451Z)
- `FUELINST|fuelType=OTHER|generation` = **1034** (n=528, 2026-09-16T16:55:48.106451Z)
- `FUELINST|fuelType=PS|generation` = **1186** (n=528, 2026-09-16T16:55:48.106451Z)
- `FUELINST|fuelType=WIND|generation` = **6503** (n=528, 2026-09-16T16:55:48.106451Z)
- `IMBALNGC|TOTAL|imbalance` = **6467** (n=87, 2026-09-16T16:52:45.452564Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=87, 2026-09-16T16:52:29.961835Z)
- `INDGEN|TOTAL|generation` = **25588** (n=87, 2026-09-16T16:52:29.961835Z)
- `MELNGC|TOTAL|margin` = **34116** (n=87, 2026-09-16T16:49:49.939625Z)
- `NDF|TOTAL|demand` = **18621** (n=89, 2026-09-16T16:47:42.628101Z)
- `TSDF|TOTAL|demand` = **19121** (n=89, 2026-09-16T16:47:59.156053Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T16:58:28.608890Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:57:45Z`
- `2026-09-16T16:56:20.382105Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:55:45Z`
- `2026-09-16T16:55:48.106451Z` — **FUELINST**: 80 rows; marker `2026-09-16T16:55:00Z`
- `2026-09-16T16:54:22.577327Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:53:45Z`
- `2026-09-16T16:52:45.452564Z` — **IMBALNGC**: 1260 rows; marker `2026-09-16T16:47:00Z`
- `2026-09-16T16:52:29.961835Z` — **INDGEN**: 1260 rows; marker `2026-09-16T16:47:00Z`
- `2026-09-16T16:52:29.961835Z` — **INDDEM**: 1260 rows; marker `2026-09-16T16:47:00Z`
- `2026-09-16T16:52:29.961835Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:51:45Z`
- `2026-09-16T16:50:37.910190Z` — **FUELINST**: 80 rows; marker `2026-09-16T16:50:00Z`
- `2026-09-16T16:50:22.391885Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:49:45Z`
- `2026-09-16T16:49:49.939625Z` — **MELNGC**: 1260 rows; marker `2026-09-16T16:47:00Z`
- `2026-09-16T16:48:14.520829Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:47:45Z`
- `2026-09-16T16:47:59.156053Z` — **TSDF**: 1260 rows; marker `2026-09-16T16:47:00Z`
- `2026-09-16T16:47:42.628101Z` — **NDF**: 70 rows; marker `2026-09-16T16:47:00Z`
- `2026-09-16T16:46:12.753290Z` — **FREQ**: 5761 rows; marker `2026-09-16T16:45:45Z`
