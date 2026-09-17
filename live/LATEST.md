# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T06:19:02.466959Z`  
Current process started UTC: `2026-09-17T06:15:01.517317Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-113** (n=657, 2026-09-17T06:15:34.252894Z)
- `FUELINST|fuelType=NPSHYD|generation` = **441** (n=657, 2026-09-17T06:15:34.252894Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3313** (n=657, 2026-09-17T06:15:34.252894Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=657, 2026-09-17T06:15:34.252894Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=657, 2026-09-17T06:15:34.252894Z)
- `FUELINST|fuelType=OTHER|generation` = **2022** (n=657, 2026-09-17T06:15:34.252894Z)
- `FUELINST|fuelType=PS|generation` = **455** (n=657, 2026-09-17T06:15:34.252894Z)
- `FUELINST|fuelType=WIND|generation` = **13855** (n=657, 2026-09-17T06:15:34.252894Z)
- `IMBALNGC|TOTAL|imbalance` = **7284** (n=109, 2026-09-17T05:50:18.646015Z)
- `INDDEM|TOTAL|demand` = **-11455** (n=109, 2026-09-17T05:50:02.713731Z)
- `INDGEN|TOTAL|generation` = **26405** (n=109, 2026-09-17T05:50:02.713731Z)
- `MELNGC|TOTAL|margin` = **35773** (n=110, 2026-09-17T06:19:01.245120Z)
- `NDF|TOTAL|demand` = **18621** (n=112, 2026-09-17T06:17:10.019795Z)
- `TSDF|TOTAL|demand` = **19121** (n=112, 2026-09-17T06:17:10.019795Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T06:19:01.245120Z` — **MELNGC**: 774 rows; marker `2026-09-17T06:16:00Z`
- `2026-09-17T06:18:29.805530Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:17:45Z`
- `2026-09-17T06:17:10.019795Z` — **TSDF**: 774 rows; marker `2026-09-17T06:16:00Z`
- `2026-09-17T06:17:10.019795Z` — **NDF**: 43 rows; marker `2026-09-17T06:16:00Z`
- `2026-09-17T06:16:22.330486Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:15:45Z`
- `2026-09-17T06:15:34.252894Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:15:00Z`
- `2026-09-17T06:14:24.524429Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:13:45Z`
- `2026-09-17T06:12:15.976665Z` — **MID**: 0 rows; marker `2026-09-17T06:12:06Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T06:12:15.976665Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:11:45Z`
- `2026-09-17T06:10:39.700652Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:10:00Z`
- `2026-09-17T06:10:23.877655Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:09:45Z`
- `2026-09-17T06:08:16.026242Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:07:45Z`
- `2026-09-17T06:06:13.231461Z` — **MID**: 0 rows; marker `2026-09-17T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T06:06:13.231461Z` — **FREQ**: 5761 rows; marker `2026-09-17T06:05:45Z`
- `2026-09-17T06:05:41.175499Z` — **FUELINST**: 80 rows; marker `2026-09-17T06:05:00Z`
