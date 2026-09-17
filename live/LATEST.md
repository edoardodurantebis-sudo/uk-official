# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T03:08:48.750239Z`  
Current process started UTC: `2026-09-17T03:04:49.078676Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1036, delta=-93, z=-3.88 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-838, delta=-46, z=-3.77 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-943, delta=-91, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-852, delta=-43, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-809, delta=0, z=-3.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-809, delta=0, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-809, delta=-1, z=-3.66 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-808, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-792, delta=-154, z=-3.97 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=0, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=0, z=-3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=0, z=-3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-807, delta=-24, z=-3.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-783, delta=-46, z=-3.90 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=619, 2026-09-17T03:05:37.626315Z)
- `FUELINST|fuelType=NPSHYD|generation` = **428** (n=619, 2026-09-17T03:05:37.626315Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=619, 2026-09-17T03:05:37.626315Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=619, 2026-09-17T03:05:37.626315Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=619, 2026-09-17T03:05:37.626315Z)
- `FUELINST|fuelType=OTHER|generation` = **699** (n=619, 2026-09-17T03:05:37.626315Z)
- `FUELINST|fuelType=PS|generation` = **-541** (n=619, 2026-09-17T03:05:37.626315Z)
- `FUELINST|fuelType=WIND|generation` = **13276** (n=619, 2026-09-17T03:05:37.626315Z)
- `IMBALNGC|TOTAL|imbalance` = **6513** (n=103, 2026-09-17T02:50:27.023315Z)
- `INDDEM|TOTAL|demand` = **-11516** (n=103, 2026-09-17T02:50:27.023315Z)
- `INDGEN|TOTAL|generation` = **25634** (n=103, 2026-09-17T02:50:27.023315Z)
- `MELNGC|TOTAL|margin` = **35862** (n=103, 2026-09-17T02:49:22.934688Z)
- `NDF|TOTAL|demand` = **18621** (n=105, 2026-09-17T02:47:22.060499Z)
- `TSDF|TOTAL|demand` = **19121** (n=105, 2026-09-17T02:47:22.060499Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T03:08:18.166346Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:07:45Z`
- `2026-09-17T03:06:25.795918Z` — **MID**: 0 rows; marker `2026-09-17T03:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T03:06:09.929434Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:05:45Z`
- `2026-09-17T03:05:37.626315Z` — **FUELINST**: 80 rows; marker `2026-09-17T03:05:00Z`
- `2026-09-17T03:04:24.648203Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:03:45Z`
- `2026-09-17T03:02:16.533804Z` — **FREQ**: 5761 rows; marker `2026-09-17T03:01:45Z`
- `2026-09-17T03:00:54.875566Z` — **FUELHH**: 20 rows; marker `2026-09-17T03:00:00Z`
- `2026-09-17T03:00:39.473274Z` — **FUELINST**: 80 rows; marker `2026-09-17T03:00:00Z`
- `2026-09-17T03:00:10.474452Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:59:45Z`
- `2026-09-17T02:58:18.372492Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:57:45Z`
- `2026-09-17T02:56:25.972214Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:55:45Z`
- `2026-09-17T02:55:43.277417Z` — **FUELINST**: 80 rows; marker `2026-09-17T02:55:00Z`
- `2026-09-17T02:54:23.219211Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:53:45Z`
- `2026-09-17T02:52:30.874141Z` — **FREQ**: 5761 rows; marker `2026-09-17T02:51:45Z`
- `2026-09-17T02:50:42.358394Z` — **FUELINST**: 80 rows; marker `2026-09-17T02:50:00Z`
