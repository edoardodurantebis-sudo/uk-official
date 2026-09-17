# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T03:51:34.113592Z`  
Current process started UTC: `2026-09-17T03:47:34.420289Z`  
1-second metadata polls in this process: **230**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-852, delta=-43, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-809, delta=0, z=-3.58 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=628, 2026-09-17T03:50:30.348943Z)
- `FUELINST|fuelType=NPSHYD|generation` = **424** (n=628, 2026-09-17T03:50:30.348943Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=628, 2026-09-17T03:50:30.348943Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=628, 2026-09-17T03:50:30.348943Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=628, 2026-09-17T03:50:30.348943Z)
- `FUELINST|fuelType=OTHER|generation` = **256** (n=628, 2026-09-17T03:50:30.348943Z)
- `FUELINST|fuelType=PS|generation` = **-298** (n=628, 2026-09-17T03:50:30.348943Z)
- `FUELINST|fuelType=WIND|generation` = **13776** (n=628, 2026-09-17T03:50:30.348943Z)
- `IMBALNGC|TOTAL|imbalance` = **7273** (n=105, 2026-09-17T03:50:14.413779Z)
- `INDDEM|TOTAL|demand` = **-11505** (n=105, 2026-09-17T03:49:58.525513Z)
- `INDGEN|TOTAL|generation` = **26394** (n=105, 2026-09-17T03:50:14.413779Z)
- `MELNGC|TOTAL|margin` = **35843** (n=105, 2026-09-17T03:48:53.933230Z)
- `NDF|TOTAL|demand` = **18621** (n=107, 2026-09-17T03:47:34.420298Z)
- `TSDF|TOTAL|demand` = **19121** (n=107, 2026-09-17T03:47:34.420298Z)
- `WINDFOR|TOTAL|generation` = **18976** (n=18, 2026-09-17T03:30:42.708765Z)

## Latest publication events

- `2026-09-17T03:50:30.348943Z` — **FUELINST**: 80 rows; marker `2026-09-17T03:50:00Z`
- `2026-09-17T03:50:30.348943Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:49:45Z`
- `2026-09-17T03:50:14.413779Z` — **INDGEN**: 864 rows; marker `2026-09-17T03:46:00Z`
- `2026-09-17T03:50:14.413779Z` — **IMBALNGC**: 864 rows; marker `2026-09-17T03:46:00Z`
- `2026-09-17T03:49:58.525513Z` — **INDDEM**: 864 rows; marker `2026-09-17T03:46:00Z`
- `2026-09-17T03:48:53.933230Z` — **MELNGC**: 864 rows; marker `2026-09-17T03:46:00Z`
- `2026-09-17T03:48:22.517518Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:47:45Z`
- `2026-09-17T03:47:34.420298Z` — **TSDF**: 864 rows; marker `2026-09-17T03:46:00Z`
- `2026-09-17T03:47:34.420298Z` — **NDF**: 48 rows; marker `2026-09-17T03:46:00Z`
- `2026-09-17T03:46:20.869512Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:45:45Z`
- `2026-09-17T03:45:49.561009Z` — **FUELINST**: 80 rows; marker `2026-09-17T03:45:00Z`
- `2026-09-17T03:44:13.357171Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:43:45Z`
- `2026-09-17T03:42:21.364757Z` — **MID**: 0 rows; marker `2026-09-17T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T03:42:21.364757Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:41:45Z`
- `2026-09-17T03:40:29.451867Z` — **FUELINST**: 80 rows; marker `2026-09-17T03:40:00Z`
