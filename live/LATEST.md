# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T03:47:21.678765Z`  
Current process started UTC: `2026-09-17T03:43:21.351630Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.73 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.82 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-1144, delta=-306, z=-4.09 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.92 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=-48, z=-4.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1128, delta=-92, z=-4.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1036, delta=-93, z=-3.88 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-838, delta=-46, z=-3.77 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-943, delta=-91, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-852, delta=-43, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-809, delta=0, z=-3.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-809, delta=0, z=-3.62 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=627, 2026-09-17T03:45:49.561009Z)
- `FUELINST|fuelType=NPSHYD|generation` = **424** (n=627, 2026-09-17T03:45:49.561009Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=627, 2026-09-17T03:45:49.561009Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=627, 2026-09-17T03:45:49.561009Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=627, 2026-09-17T03:45:49.561009Z)
- `FUELINST|fuelType=OTHER|generation` = **379** (n=627, 2026-09-17T03:45:49.561009Z)
- `FUELINST|fuelType=PS|generation` = **-300** (n=627, 2026-09-17T03:45:49.561009Z)
- `FUELINST|fuelType=WIND|generation` = **13856** (n=627, 2026-09-17T03:45:49.561009Z)
- `IMBALNGC|TOTAL|imbalance` = **6527** (n=104, 2026-09-17T03:20:43.155529Z)
- `INDDEM|TOTAL|demand` = **-11516** (n=104, 2026-09-17T03:20:27.781104Z)
- `INDGEN|TOTAL|generation` = **25648** (n=104, 2026-09-17T03:20:27.781104Z)
- `MELNGC|TOTAL|margin` = **35852** (n=104, 2026-09-17T03:19:22.995166Z)
- `NDF|TOTAL|demand` = **18621** (n=106, 2026-09-17T03:17:28.635447Z)
- `TSDF|TOTAL|demand` = **19121** (n=106, 2026-09-17T03:17:28.635447Z)
- `WINDFOR|TOTAL|generation` = **18976** (n=18, 2026-09-17T03:30:42.708765Z)

## Latest publication events

- `2026-09-17T03:46:20.869512Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:45:45Z`
- `2026-09-17T03:45:49.561009Z` — **FUELINST**: 80 rows; marker `2026-09-17T03:45:00Z`
- `2026-09-17T03:44:13.357171Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:43:45Z`
- `2026-09-17T03:42:21.364757Z` — **MID**: 0 rows; marker `2026-09-17T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T03:42:21.364757Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:41:45Z`
- `2026-09-17T03:40:29.451867Z` — **FUELINST**: 80 rows; marker `2026-09-17T03:40:00Z`
- `2026-09-17T03:40:13.221508Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:39:45Z`
- `2026-09-17T03:38:22.963509Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:37:45Z`
- `2026-09-17T03:36:30.826147Z` — **MID**: 0 rows; marker `2026-09-17T03:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T03:36:14.591938Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:35:45Z`
- `2026-09-17T03:35:26.967018Z` — **FUELINST**: 80 rows; marker `2026-09-17T03:35:00Z`
- `2026-09-17T03:34:12.487438Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:33:45Z`
- `2026-09-17T03:32:19.631387Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:31:45Z`
- `2026-09-17T03:30:42.708765Z` — **WINDFOR**: 73 rows; marker `2026-09-17T03:30:00Z`
- `2026-09-17T03:30:42.708765Z` — **FUELHH**: 20 rows; marker `2026-09-17T03:30:00Z`
