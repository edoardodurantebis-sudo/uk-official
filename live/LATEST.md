# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T04:46:47.652927Z`  
Current process started UTC: `2026-09-17T04:42:47.638834Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=639, 2026-09-17T04:45:29.660558Z)
- `FUELINST|fuelType=NPSHYD|generation` = **440** (n=639, 2026-09-17T04:45:29.660558Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=639, 2026-09-17T04:45:29.660558Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=639, 2026-09-17T04:45:29.660558Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=639, 2026-09-17T04:45:29.660558Z)
- `FUELINST|fuelType=OTHER|generation` = **377** (n=639, 2026-09-17T04:45:29.660558Z)
- `FUELINST|fuelType=PS|generation` = **-286** (n=639, 2026-09-17T04:45:29.660558Z)
- `FUELINST|fuelType=WIND|generation` = **14063** (n=639, 2026-09-17T04:45:29.660558Z)
- `IMBALNGC|TOTAL|imbalance` = **7239** (n=106, 2026-09-17T04:20:39.839492Z)
- `INDDEM|TOTAL|demand` = **-11454** (n=106, 2026-09-17T04:20:23.631444Z)
- `INDGEN|TOTAL|generation` = **26360** (n=106, 2026-09-17T04:20:23.631444Z)
- `MELNGC|TOTAL|margin` = **35848** (n=106, 2026-09-17T04:19:02.911009Z)
- `NDF|TOTAL|demand` = **18621** (n=108, 2026-09-17T04:17:26.094802Z)
- `TSDF|TOTAL|demand` = **19121** (n=108, 2026-09-17T04:17:26.094802Z)
- `WINDFOR|TOTAL|generation` = **18976** (n=18, 2026-09-17T03:30:42.708765Z)

## Latest publication events

- `2026-09-17T04:46:18.180129Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:45:45Z`
- `2026-09-17T04:45:29.660558Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:45:00Z`
- `2026-09-17T04:44:25.757167Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:43:45Z`
- `2026-09-17T04:42:17.845370Z` — **MID**: 0 rows; marker `2026-09-17T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T04:42:17.845370Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:41:45Z`
- `2026-09-17T04:40:25.302279Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:40:00Z`
- `2026-09-17T04:40:09.861028Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:39:45Z`
- `2026-09-17T04:38:13.960027Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:37:45Z`
- `2026-09-17T04:36:37.727785Z` — **MID**: 0 rows; marker `2026-09-17T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T04:36:06.328080Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:35:45Z`
- `2026-09-17T04:35:34.665922Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:35:00Z`
- `2026-09-17T04:34:15.070106Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:33:45Z`
- `2026-09-17T04:32:14.130721Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:31:45Z`
- `2026-09-17T04:30:36.381746Z` — **FUELHH**: 20 rows; marker `2026-09-17T04:30:00Z`
- `2026-09-17T04:30:36.381746Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:30:00Z`
