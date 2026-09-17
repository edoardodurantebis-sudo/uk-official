# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T06:02:17.062980Z`  
Current process started UTC: `2026-09-17T05:58:17.141784Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-694** (n=654, 2026-09-17T06:00:30.517210Z)
- `FUELINST|fuelType=NPSHYD|generation` = **445** (n=654, 2026-09-17T06:00:30.517210Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3308** (n=654, 2026-09-17T06:00:30.517210Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=654, 2026-09-17T06:00:30.517210Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=654, 2026-09-17T06:00:30.517210Z)
- `FUELINST|fuelType=OTHER|generation` = **1877** (n=654, 2026-09-17T06:00:30.517210Z)
- `FUELINST|fuelType=PS|generation` = **221** (n=654, 2026-09-17T06:00:30.517210Z)
- `FUELINST|fuelType=WIND|generation` = **13938** (n=654, 2026-09-17T06:00:30.517210Z)
- `IMBALNGC|TOTAL|imbalance` = **7284** (n=109, 2026-09-17T05:50:18.646015Z)
- `INDDEM|TOTAL|demand` = **-11455** (n=109, 2026-09-17T05:50:02.713731Z)
- `INDGEN|TOTAL|generation` = **26405** (n=109, 2026-09-17T05:50:02.713731Z)
- `MELNGC|TOTAL|margin` = **35792** (n=109, 2026-09-17T05:49:14.709133Z)
- `NDF|TOTAL|demand` = **18621** (n=111, 2026-09-17T05:47:07.060151Z)
- `TSDF|TOTAL|demand` = **19121** (n=111, 2026-09-17T05:47:07.060151Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T06:00:30.517210Z` — **FUELHH**: 20 rows; marker `2026-09-17T06:00:00Z`
- `2026-09-17T06:00:30.517210Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:00:00Z`
- `2026-09-17T06:00:14.379537Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:59:45Z`
- `2026-09-17T05:58:22.142313Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:57:45Z`
- `2026-09-17T05:56:14.169447Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:55:45Z`
- `2026-09-17T05:55:26.131800Z` — **FUELINST**: 80 rows; marker `2026-09-17T05:55:00Z`
- `2026-09-17T05:54:06.578157Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:53:45Z`
- `2026-09-17T05:52:11.368103Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:51:45Z`
- `2026-09-17T05:50:34.771519Z` — **FUELINST**: 80 rows; marker `2026-09-17T05:50:00Z`
- `2026-09-17T05:50:18.646015Z` — **IMBALNGC**: 792 rows; marker `2026-09-17T05:46:00Z`
- `2026-09-17T05:50:18.646015Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:49:45Z`
- `2026-09-17T05:50:02.713731Z` — **INDGEN**: 792 rows; marker `2026-09-17T05:46:00Z`
- `2026-09-17T05:50:02.713731Z` — **INDDEM**: 792 rows; marker `2026-09-17T05:46:00Z`
- `2026-09-17T05:49:14.709133Z` — **MELNGC**: 792 rows; marker `2026-09-17T05:46:00Z`
- `2026-09-17T05:48:10.866477Z` — **FREQ**: 5761 rows; marker `2026-09-17T05:47:45Z`
