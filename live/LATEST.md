# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T00:54:40.716386Z`  
Current process started UTC: `2026-09-17T00:50:40.388400Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.68 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.72 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.77 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-286, delta=-258, z=-4.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.82 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=-40, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-272, delta=-77, z=-3.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-195, delta=-78, z=-3.76 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-28, delta=-68, z=-3.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-117, delta=-77, z=-3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=3, delta=-50, z=-0.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=-3, z=4.28 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1221** (n=592, 2026-09-17T00:50:40.388409Z)
- `FUELINST|fuelType=NPSHYD|generation` = **422** (n=592, 2026-09-17T00:50:40.388409Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3311** (n=592, 2026-09-17T00:50:40.388409Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=592, 2026-09-17T00:50:40.388409Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=592, 2026-09-17T00:50:40.388409Z)
- `FUELINST|fuelType=OTHER|generation` = **516** (n=592, 2026-09-17T00:50:40.388409Z)
- `FUELINST|fuelType=PS|generation` = **-288** (n=592, 2026-09-17T00:50:40.388409Z)
- `FUELINST|fuelType=WIND|generation` = **12227** (n=592, 2026-09-17T00:50:40.388409Z)
- `IMBALNGC|TOTAL|imbalance` = **6515** (n=99, 2026-09-17T00:51:12.288549Z)
- `INDDEM|TOTAL|demand` = **-11747** (n=99, 2026-09-17T00:51:12.288549Z)
- `INDGEN|TOTAL|generation` = **25636** (n=99, 2026-09-17T00:51:12.288549Z)
- `MELNGC|TOTAL|margin` = **34511** (n=99, 2026-09-17T00:49:26.945274Z)
- `NDF|TOTAL|demand` = **18621** (n=101, 2026-09-17T00:47:34.020052Z)
- `TSDF|TOTAL|demand` = **19121** (n=101, 2026-09-17T00:47:34.020052Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T00:54:08.460033Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:53:45Z`
- `2026-09-17T00:52:16.369822Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:51:45Z`
- `2026-09-17T00:51:12.288549Z` — **INDGEN**: 972 rows; marker `2026-09-17T00:47:00Z`
- `2026-09-17T00:51:12.288549Z` — **INDDEM**: 972 rows; marker `2026-09-17T00:47:00Z`
- `2026-09-17T00:51:12.288549Z` — **IMBALNGC**: 972 rows; marker `2026-09-17T00:47:00Z`
- `2026-09-17T00:50:40.388409Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:50:00Z`
- `2026-09-17T00:50:40.388409Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:49:45Z`
- `2026-09-17T00:49:26.945274Z` — **MELNGC**: 972 rows; marker `2026-09-17T00:47:00Z`
- `2026-09-17T00:48:06.729830Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:47:45Z`
- `2026-09-17T00:47:34.020052Z` — **TSDF**: 972 rows; marker `2026-09-17T00:47:00Z`
- `2026-09-17T00:47:34.020052Z` — **NDF**: 54 rows; marker `2026-09-17T00:47:00Z`
- `2026-09-17T00:46:14.251340Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:45:45Z`
- `2026-09-17T00:45:42.197976Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:45:00Z`
- `2026-09-17T00:44:06.730896Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:43:45Z`
- `2026-09-17T00:42:14.556117Z` — **MID**: 0 rows; marker `2026-09-17T00:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
