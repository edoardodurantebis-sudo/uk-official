# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T05:20:24.190118Z`  
Current process started UTC: `2026-09-17T05:16:23.702578Z`  
1-second metadata polls in this process: **231**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-880** (n=645, 2026-09-17T05:15:34.952951Z)
- `FUELINST|fuelType=NPSHYD|generation` = **425** (n=645, 2026-09-17T05:15:34.952951Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3316** (n=645, 2026-09-17T05:15:34.952951Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=645, 2026-09-17T05:15:34.952951Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=645, 2026-09-17T05:15:34.952951Z)
- `FUELINST|fuelType=OTHER|generation` = **747** (n=645, 2026-09-17T05:15:34.952951Z)
- `FUELINST|fuelType=PS|generation` = **-70** (n=645, 2026-09-17T05:15:34.952951Z)
- `FUELINST|fuelType=WIND|generation` = **13905** (n=645, 2026-09-17T05:15:34.952951Z)
- `IMBALNGC|TOTAL|imbalance` = **7263** (n=108, 2026-09-17T05:19:50.393118Z)
- `INDDEM|TOTAL|demand` = **-11454** (n=108, 2026-09-17T05:19:50.393118Z)
- `INDGEN|TOTAL|generation` = **26384** (n=108, 2026-09-17T05:19:50.393118Z)
- `MELNGC|TOTAL|margin` = **35866** (n=108, 2026-09-17T05:19:02.566048Z)
- `NDF|TOTAL|demand` = **18621** (n=110, 2026-09-17T05:16:56.335729Z)
- `TSDF|TOTAL|demand` = **19121** (n=110, 2026-09-17T05:16:56.335729Z)
- `WINDFOR|TOTAL|generation` = **18976** (n=18, 2026-09-17T03:30:42.708765Z)

## Latest publication events

- `2026-09-17T05:20:22.066992Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:19:45Z`
- `2026-09-17T05:19:50.393118Z` — **INDGEN**: 810 rows; marker `2026-09-17T05:16:00Z`
- `2026-09-17T05:19:50.393118Z` — **INDDEM**: 810 rows; marker `2026-09-17T05:16:00Z`
- `2026-09-17T05:19:50.393118Z` — **IMBALNGC**: 810 rows; marker `2026-09-17T05:16:00Z`
- `2026-09-17T05:19:02.566048Z` — **MELNGC**: 810 rows; marker `2026-09-17T05:16:00Z`
- `2026-09-17T05:18:15.004243Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:17:45Z`
- `2026-09-17T05:16:56.335729Z` — **TSDF**: 810 rows; marker `2026-09-17T05:16:00Z`
- `2026-09-17T05:16:56.335729Z` — **NDF**: 45 rows; marker `2026-09-17T05:16:00Z`
- `2026-09-17T05:16:23.702585Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:15:45Z`
- `2026-09-17T05:15:34.952951Z` — **FUELINST**: 80 rows; marker `2026-09-17T05:15:00Z`
- `2026-09-17T05:14:15.321794Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:13:45Z`
- `2026-09-17T05:12:23.610079Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:11:45Z`
- `2026-09-17T05:12:08.162806Z` — **MID**: 0 rows; marker `2026-09-17T05:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T05:10:25.546342Z` — **FUELINST**: 80 rows; marker `2026-09-17T05:10:00Z`
- `2026-09-17T05:10:09.611803Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:09:45Z`
