# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T06:27:23.489878Z`  
Current process started UTC: `2026-09-17T06:23:22.845624Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-113** (n=659, 2026-09-17T06:25:31.065449Z)
- `FUELINST|fuelType=NPSHYD|generation` = **440** (n=659, 2026-09-17T06:25:31.065449Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=659, 2026-09-17T06:25:31.065449Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=659, 2026-09-17T06:25:31.065449Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=659, 2026-09-17T06:25:31.065449Z)
- `FUELINST|fuelType=OTHER|generation` = **1850** (n=659, 2026-09-17T06:25:31.065449Z)
- `FUELINST|fuelType=PS|generation` = **531** (n=659, 2026-09-17T06:25:31.065449Z)
- `FUELINST|fuelType=WIND|generation` = **13871** (n=659, 2026-09-17T06:25:31.065449Z)
- `IMBALNGC|TOTAL|imbalance` = **7359** (n=110, 2026-09-17T06:20:20.000035Z)
- `INDDEM|TOTAL|demand` = **-11818** (n=110, 2026-09-17T06:19:48.949687Z)
- `INDGEN|TOTAL|generation` = **26480** (n=110, 2026-09-17T06:20:04.422650Z)
- `MELNGC|TOTAL|margin` = **35773** (n=110, 2026-09-17T06:19:01.245120Z)
- `NDF|TOTAL|demand` = **18621** (n=112, 2026-09-17T06:17:10.019795Z)
- `TSDF|TOTAL|demand` = **19121** (n=112, 2026-09-17T06:17:10.019795Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T06:26:18.659559Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:25:45Z`
- `2026-09-17T06:25:31.065449Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:25:00Z`
- `2026-09-17T06:24:10.955878Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:23:45Z`
- `2026-09-17T06:22:28.959109Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:21:45Z`
- `2026-09-17T06:20:20.000035Z` — **IMBALNGC**: 774 rows; marker `2026-09-17T06:16:00Z`
- `2026-09-17T06:20:20.000035Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:20:00Z`
- `2026-09-17T06:20:20.000035Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:19:45Z`
- `2026-09-17T06:20:04.422650Z` — **INDGEN**: 774 rows; marker `2026-09-17T06:16:00Z`
- `2026-09-17T06:19:48.949687Z` — **INDDEM**: 774 rows; marker `2026-09-17T06:16:00Z`
- `2026-09-17T06:19:01.245120Z` — **MELNGC**: 774 rows; marker `2026-09-17T06:16:00Z`
- `2026-09-17T06:18:29.805530Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:17:45Z`
- `2026-09-17T06:17:10.019795Z` — **TSDF**: 774 rows; marker `2026-09-17T06:16:00Z`
- `2026-09-17T06:17:10.019795Z` — **NDF**: 43 rows; marker `2026-09-17T06:16:00Z`
- `2026-09-17T06:16:22.330486Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:15:45Z`
- `2026-09-17T06:15:34.252894Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:15:00Z`
