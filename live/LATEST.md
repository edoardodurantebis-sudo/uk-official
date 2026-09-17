# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T05:33:01.985417Z`  
Current process started UTC: `2026-09-17T05:29:01.825123Z`  
1-second metadata polls in this process: **236**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-880** (n=648, 2026-09-17T05:30:37.912884Z)
- `FUELINST|fuelType=NPSHYD|generation` = **427** (n=648, 2026-09-17T05:30:37.912884Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=648, 2026-09-17T05:30:37.912884Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=648, 2026-09-17T05:30:37.912884Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=648, 2026-09-17T05:30:37.912884Z)
- `FUELINST|fuelType=OTHER|generation` = **1240** (n=648, 2026-09-17T05:30:37.912884Z)
- `FUELINST|fuelType=PS|generation` = **221** (n=648, 2026-09-17T05:30:37.912884Z)
- `FUELINST|fuelType=WIND|generation` = **13892** (n=648, 2026-09-17T05:30:37.912884Z)
- `IMBALNGC|TOTAL|imbalance` = **7263** (n=108, 2026-09-17T05:19:50.393118Z)
- `INDDEM|TOTAL|demand` = **-11454** (n=108, 2026-09-17T05:19:50.393118Z)
- `INDGEN|TOTAL|generation` = **26384** (n=108, 2026-09-17T05:19:50.393118Z)
- `MELNGC|TOTAL|margin` = **35866** (n=108, 2026-09-17T05:19:02.566048Z)
- `NDF|TOTAL|demand` = **18621** (n=110, 2026-09-17T05:16:56.335729Z)
- `TSDF|TOTAL|demand` = **19121** (n=110, 2026-09-17T05:16:56.335729Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T05:32:29.529525Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:31:45Z`
- `2026-09-17T05:30:37.912884Z` — **WINDFOR**: 73 rows; marker `2026-09-17T05:30:00Z`
- `2026-09-17T05:30:37.912884Z` — **FUELHH**: 20 rows; marker `2026-09-17T05:30:00Z`
- `2026-09-17T05:30:37.912884Z` — **FUELINST**: 80 rows; marker `2026-09-17T05:30:00Z`
- `2026-09-17T05:30:21.834798Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:29:45Z`
- `2026-09-17T05:28:18.716952Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:27:45Z`
- `2026-09-17T05:26:26.919328Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:25:45Z`
- `2026-09-17T05:25:38.577652Z` — **FUELINST**: 80 rows; marker `2026-09-17T05:25:00Z`
- `2026-09-17T05:24:25.484644Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:23:45Z`
- `2026-09-17T05:22:14.858764Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:21:45Z`
- `2026-09-17T05:20:37.710872Z` — **FUELINST**: 80 rows; marker `2026-09-17T05:20:00Z`
- `2026-09-17T05:20:22.066992Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:19:45Z`
- `2026-09-17T05:19:50.393118Z` — **INDGEN**: 810 rows; marker `2026-09-17T05:16:00Z`
- `2026-09-17T05:19:50.393118Z` — **INDDEM**: 810 rows; marker `2026-09-17T05:16:00Z`
- `2026-09-17T05:19:50.393118Z` — **IMBALNGC**: 810 rows; marker `2026-09-17T05:16:00Z`
