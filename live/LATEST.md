# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T04:33:26.835046Z`  
Current process started UTC: `2026-09-17T04:29:27.113495Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-1134, delta=10, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1114, delta=62, z=-3.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.69 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=636, 2026-09-17T04:30:36.381746Z)
- `FUELINST|fuelType=NPSHYD|generation` = **426** (n=636, 2026-09-17T04:30:36.381746Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=636, 2026-09-17T04:30:36.381746Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=636, 2026-09-17T04:30:36.381746Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=636, 2026-09-17T04:30:36.381746Z)
- `FUELINST|fuelType=OTHER|generation` = **422** (n=636, 2026-09-17T04:30:36.381746Z)
- `FUELINST|fuelType=PS|generation` = **-354** (n=636, 2026-09-17T04:30:36.381746Z)
- `FUELINST|fuelType=WIND|generation` = **13922** (n=636, 2026-09-17T04:30:36.381746Z)
- `IMBALNGC|TOTAL|imbalance` = **7239** (n=106, 2026-09-17T04:20:39.839492Z)
- `INDDEM|TOTAL|demand` = **-11454** (n=106, 2026-09-17T04:20:23.631444Z)
- `INDGEN|TOTAL|generation` = **26360** (n=106, 2026-09-17T04:20:23.631444Z)
- `MELNGC|TOTAL|margin` = **35848** (n=106, 2026-09-17T04:19:02.911009Z)
- `NDF|TOTAL|demand` = **18621** (n=108, 2026-09-17T04:17:26.094802Z)
- `TSDF|TOTAL|demand` = **19121** (n=108, 2026-09-17T04:17:26.094802Z)
- `WINDFOR|TOTAL|generation` = **18976** (n=18, 2026-09-17T03:30:42.708765Z)

## Latest publication events

- `2026-09-17T04:32:14.130721Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:31:45Z`
- `2026-09-17T04:30:36.381746Z` — **FUELHH**: 20 rows; marker `2026-09-17T04:30:00Z`
- `2026-09-17T04:30:36.381746Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:30:00Z`
- `2026-09-17T04:30:03.842220Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:29:45Z`
- `2026-09-17T04:28:11.802208Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:27:45Z`
- `2026-09-17T04:26:20.045643Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:25:45Z`
- `2026-09-17T04:25:31.621853Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:25:00Z`
- `2026-09-17T04:24:18.154842Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:23:45Z`
- `2026-09-17T04:22:26.060025Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:21:45Z`
- `2026-09-17T04:20:39.839492Z` — **IMBALNGC**: 846 rows; marker `2026-09-17T04:16:00Z`
- `2026-09-17T04:20:39.839492Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:20:00Z`
- `2026-09-17T04:20:23.631444Z` — **INDGEN**: 846 rows; marker `2026-09-17T04:16:00Z`
- `2026-09-17T04:20:23.631444Z` — **INDDEM**: 846 rows; marker `2026-09-17T04:16:00Z`
- `2026-09-17T04:20:23.631444Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:19:45Z`
- `2026-09-17T04:19:02.911009Z` — **MELNGC**: 846 rows; marker `2026-09-17T04:16:00Z`
