# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T04:12:31.536977Z`  
Current process started UTC: `2026-09-17T04:08:31.412615Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=632, 2026-09-17T04:10:39.081463Z)
- `FUELINST|fuelType=NPSHYD|generation` = **427** (n=632, 2026-09-17T04:10:39.081463Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=632, 2026-09-17T04:10:39.081463Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=632, 2026-09-17T04:10:39.081463Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=632, 2026-09-17T04:10:39.081463Z)
- `FUELINST|fuelType=OTHER|generation` = **517** (n=632, 2026-09-17T04:10:39.081463Z)
- `FUELINST|fuelType=PS|generation` = **-328** (n=632, 2026-09-17T04:10:39.081463Z)
- `FUELINST|fuelType=WIND|generation` = **13770** (n=632, 2026-09-17T04:10:39.081463Z)
- `IMBALNGC|TOTAL|imbalance` = **7273** (n=105, 2026-09-17T03:50:14.413779Z)
- `INDDEM|TOTAL|demand` = **-11505** (n=105, 2026-09-17T03:49:58.525513Z)
- `INDGEN|TOTAL|generation` = **26394** (n=105, 2026-09-17T03:50:14.413779Z)
- `MELNGC|TOTAL|margin` = **35843** (n=105, 2026-09-17T03:48:53.933230Z)
- `NDF|TOTAL|demand` = **18621** (n=107, 2026-09-17T03:47:34.420298Z)
- `TSDF|TOTAL|demand` = **19121** (n=107, 2026-09-17T03:47:34.420298Z)
- `WINDFOR|TOTAL|generation` = **18976** (n=18, 2026-09-17T03:30:42.708765Z)

## Latest publication events

- `2026-09-17T04:12:15.324694Z` — **MID**: 0 rows; marker `2026-09-17T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T04:12:15.324694Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:11:45Z`
- `2026-09-17T04:10:39.081463Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:10:00Z`
- `2026-09-17T04:10:23.305669Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:09:45Z`
- `2026-09-17T04:08:31.412622Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:07:45Z`
- `2026-09-17T04:06:42.738791Z` — **MID**: 0 rows; marker `2026-09-17T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T04:06:10.612202Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:05:45Z`
- `2026-09-17T04:05:38.841092Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:05:00Z`
- `2026-09-17T04:04:18.673175Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:03:45Z`
- `2026-09-17T04:02:14.498010Z` — **FREQ**: 5761 rows; marker `2026-09-17T04:01:45Z`
- `2026-09-17T04:00:54.621897Z` — **FUELHH**: 20 rows; marker `2026-09-17T04:00:00Z`
- `2026-09-17T04:00:22.927659Z` — **FUELINST**: 80 rows; marker `2026-09-17T04:00:00Z`
- `2026-09-17T04:00:06.777907Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:59:45Z`
- `2026-09-17T03:58:09.021029Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:57:45Z`
- `2026-09-17T03:56:17.522491Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:55:45Z`
