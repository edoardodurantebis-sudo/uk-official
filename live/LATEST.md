# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T05:49:47.524332Z`  
Current process started UTC: `2026-09-17T05:45:47.033962Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-880** (n=651, 2026-09-17T05:45:24.695533Z)
- `FUELINST|fuelType=NPSHYD|generation` = **448** (n=651, 2026-09-17T05:45:24.695533Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=651, 2026-09-17T05:45:24.695533Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=651, 2026-09-17T05:45:24.695533Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=651, 2026-09-17T05:45:24.695533Z)
- `FUELINST|fuelType=OTHER|generation` = **1589** (n=651, 2026-09-17T05:45:24.695533Z)
- `FUELINST|fuelType=PS|generation` = **226** (n=651, 2026-09-17T05:45:24.695533Z)
- `FUELINST|fuelType=WIND|generation` = **13893** (n=651, 2026-09-17T05:45:24.695533Z)
- `IMBALNGC|TOTAL|imbalance` = **7263** (n=108, 2026-09-17T05:19:50.393118Z)
- `INDDEM|TOTAL|demand` = **-11454** (n=108, 2026-09-17T05:19:50.393118Z)
- `INDGEN|TOTAL|generation` = **26384** (n=108, 2026-09-17T05:19:50.393118Z)
- `MELNGC|TOTAL|margin` = **35792** (n=109, 2026-09-17T05:49:14.709133Z)
- `NDF|TOTAL|demand` = **18621** (n=111, 2026-09-17T05:47:07.060151Z)
- `TSDF|TOTAL|demand` = **19121** (n=111, 2026-09-17T05:47:07.060151Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T05:49:14.709133Z` — **MELNGC**: 792 rows; marker `2026-09-17T05:46:00Z`
- `2026-09-17T05:48:10.866477Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:47:45Z`
- `2026-09-17T05:47:07.060151Z` — **TSDF**: 792 rows; marker `2026-09-17T05:46:00Z`
- `2026-09-17T05:47:07.060151Z` — **NDF**: 44 rows; marker `2026-09-17T05:46:00Z`
- `2026-09-17T05:46:19.502553Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:45:45Z`
- `2026-09-17T05:45:24.695533Z` — **FUELINST**: 80 rows; marker `2026-09-17T05:45:00Z`
- `2026-09-17T05:44:20.450326Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:43:45Z`
- `2026-09-17T05:42:12.060235Z` — **MID**: 0 rows; marker `2026-09-17T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T05:42:12.060235Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:41:45Z`
- `2026-09-17T05:40:20.459391Z` — **FUELINST**: 80 rows; marker `2026-09-17T05:40:00Z`
- `2026-09-17T05:40:20.459391Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:39:45Z`
- `2026-09-17T05:38:12.845768Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:37:45Z`
- `2026-09-17T05:36:26.376341Z` — **MID**: 0 rows; marker `2026-09-17T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T05:36:10.526733Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:35:45Z`
- `2026-09-17T05:35:38.171328Z` — **FUELINST**: 80 rows; marker `2026-09-17T05:35:00Z`
