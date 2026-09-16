# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T15:28:42.333642Z`  
Current process started UTC: `2026-09-16T15:24:42.175259Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=0, z=-3.58 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3282, delta=-3, z=-3.63 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3286, delta=2, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3285, delta=6, z=-3.64 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3279, delta=-1, z=-4.31 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3284, delta=-5, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3280, delta=-3, z=-4.29 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3283, delta=-4, z=-4.06 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3287, delta=3, z=-3.70 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3284, delta=0, z=-4.09 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3284, delta=-3, z=-4.16 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3287, delta=-2, z=-3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NUCLEAR` `generation` — half-hour generation mix [fuelType=NUCLEAR] generation: value=3289, delta=-4, z=-4.11 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3289, delta=-1, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=NUCLEAR` `generation` — instantaneous generation mix [fuelType=NUCLEAR] generation: value=3290, delta=2, z=-3.69 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **777** (n=510, 2026-09-16T15:25:32.180309Z)
- `FUELINST|fuelType=NPSHYD|generation` = **391** (n=510, 2026-09-16T15:25:32.180309Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3294** (n=510, 2026-09-16T15:25:32.180309Z)
- `FUELINST|fuelType=OCGT|generation` = **2** (n=510, 2026-09-16T15:25:32.180309Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=510, 2026-09-16T15:25:32.180309Z)
- `FUELINST|fuelType=OTHER|generation` = **498** (n=510, 2026-09-16T15:25:32.180309Z)
- `FUELINST|fuelType=PS|generation` = **233** (n=510, 2026-09-16T15:25:32.180309Z)
- `FUELINST|fuelType=WIND|generation` = **5707** (n=510, 2026-09-16T15:25:32.180309Z)
- `IMBALNGC|TOTAL|imbalance` = **6392** (n=84, 2026-09-16T15:26:51.642180Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=84, 2026-09-16T15:26:51.642180Z)
- `INDGEN|TOTAL|generation` = **25513** (n=84, 2026-09-16T15:26:51.642180Z)
- `MELNGC|TOTAL|margin` = **34317** (n=84, 2026-09-16T15:24:28.473061Z)
- `NDF|TOTAL|demand` = **18621** (n=86, 2026-09-16T15:22:05.343567Z)
- `TSDF|TOTAL|demand` = **19121** (n=86, 2026-09-16T15:22:05.343567Z)
- `WINDFOR|TOTAL|generation` = **19561** (n=14, 2026-09-16T12:30:25.126294Z)

## Latest publication events

- `2026-09-16T15:28:27.080231Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:27:45Z`
- `2026-09-16T15:26:51.642180Z` — **INDGEN**: 1314 rows; marker `2026-09-16T15:21:00Z`
- `2026-09-16T15:26:51.642180Z` — **INDDEM**: 1314 rows; marker `2026-09-16T15:21:00Z`
- `2026-09-16T15:26:51.642180Z` — **IMBALNGC**: 1314 rows; marker `2026-09-16T15:21:00Z`
- `2026-09-16T15:26:19.819688Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:25:45Z`
- `2026-09-16T15:25:32.180309Z` — **FUELINST**: 80 rows; marker `2026-09-16T15:25:00Z`
- `2026-09-16T15:24:28.473061Z` — **MELNGC**: 1314 rows; marker `2026-09-16T15:21:00Z`
- `2026-09-16T15:24:28.473061Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:23:45Z`
- `2026-09-16T15:22:20.589164Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:21:45Z`
- `2026-09-16T15:22:05.343567Z` — **TSDF**: 1314 rows; marker `2026-09-16T15:21:00Z`
- `2026-09-16T15:22:05.343567Z` — **NDF**: 73 rows; marker `2026-09-16T15:21:00Z`
- `2026-09-16T15:20:29.536679Z` — **FUELINST**: 80 rows; marker `2026-09-16T15:20:00Z`
- `2026-09-16T15:20:29.536679Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:19:45Z`
- `2026-09-16T15:18:22.547719Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:17:45Z`
- `2026-09-16T15:16:13.847548Z` — **FREQ**: 5761 rows; marker `2026-09-16T15:15:45Z`
