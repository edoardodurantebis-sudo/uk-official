# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T04:55:07.357085Z`  
Current process started UTC: `2026-09-17T04:51:07.733175Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=640, 2026-09-17T04:50:26.228348Z)
- `FUELINST|fuelType=NPSHYD|generation` = **431** (n=640, 2026-09-17T04:50:26.228348Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=640, 2026-09-17T04:50:26.228348Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=640, 2026-09-17T04:50:26.228348Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=640, 2026-09-17T04:50:26.228348Z)
- `FUELINST|fuelType=OTHER|generation` = **496** (n=640, 2026-09-17T04:50:26.228348Z)
- `FUELINST|fuelType=PS|generation` = **-293** (n=640, 2026-09-17T04:50:26.228348Z)
- `FUELINST|fuelType=WIND|generation` = **13983** (n=640, 2026-09-17T04:50:26.228348Z)
- `IMBALNGC|TOTAL|imbalance` = **7267** (n=107, 2026-09-17T04:50:09.965302Z)
- `INDDEM|TOTAL|demand` = **-11454** (n=107, 2026-09-17T04:49:54.263248Z)
- `INDGEN|TOTAL|generation` = **26388** (n=107, 2026-09-17T04:49:54.263248Z)
- `MELNGC|TOTAL|margin` = **35861** (n=107, 2026-09-17T04:49:06.099549Z)
- `NDF|TOTAL|demand` = **18621** (n=109, 2026-09-17T04:46:57.697911Z)
- `TSDF|TOTAL|demand` = **19121** (n=109, 2026-09-17T04:47:13.699898Z)
- `WINDFOR|TOTAL|generation` = **18976** (n=18, 2026-09-17T03:30:42.708765Z)

## Latest publication events

- `2026-09-17T04:54:20.477826Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:53:45Z`
- `2026-09-17T04:52:11.833785Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:51:45Z`
- `2026-09-17T04:50:26.228348Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:50:00Z`
- `2026-09-17T04:50:09.965302Z` — **IMBALNGC**: 828 rows; marker `2026-09-17T04:46:00Z`
- `2026-09-17T04:50:09.965302Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:49:45Z`
- `2026-09-17T04:49:54.263248Z` — **INDGEN**: 828 rows; marker `2026-09-17T04:46:00Z`
- `2026-09-17T04:49:54.263248Z` — **INDDEM**: 828 rows; marker `2026-09-17T04:46:00Z`
- `2026-09-17T04:49:06.099549Z` — **MELNGC**: 828 rows; marker `2026-09-17T04:46:00Z`
- `2026-09-17T04:48:18.621677Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:47:45Z`
- `2026-09-17T04:47:13.699898Z` — **TSDF**: 828 rows; marker `2026-09-17T04:46:00Z`
- `2026-09-17T04:46:57.697911Z` — **NDF**: 46 rows; marker `2026-09-17T04:46:00Z`
- `2026-09-17T04:46:18.180129Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:45:45Z`
- `2026-09-17T04:45:29.660558Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:45:00Z`
- `2026-09-17T04:44:25.757167Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:43:45Z`
- `2026-09-17T04:42:17.845370Z` — **MID**: 0 rows; marker `2026-09-17T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
