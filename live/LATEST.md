# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T01:15:41.873301Z`  
Current process started UTC: `2026-09-17T01:11:42.080899Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-582, delta=-78, z=-4.09 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-504, delta=-78, z=-3.96 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-338, delta=-52, z=-3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-426, delta=-78, z=-3.82 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-348, delta=-36, z=-3.68 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1448** (n=596, 2026-09-17T01:10:27.905487Z)
- `FUELINST|fuelType=NPSHYD|generation` = **418** (n=596, 2026-09-17T01:10:27.905487Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=596, 2026-09-17T01:10:27.905487Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=596, 2026-09-17T01:10:27.905487Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=596, 2026-09-17T01:10:27.905487Z)
- `FUELINST|fuelType=OTHER|generation` = **155** (n=596, 2026-09-17T01:10:27.905487Z)
- `FUELINST|fuelType=PS|generation` = **-312** (n=596, 2026-09-17T01:10:27.905487Z)
- `FUELINST|fuelType=WIND|generation` = **12662** (n=596, 2026-09-17T01:10:27.905487Z)
- `IMBALNGC|TOTAL|imbalance` = **6515** (n=99, 2026-09-17T00:51:12.288549Z)
- `INDDEM|TOTAL|demand` = **-11747** (n=99, 2026-09-17T00:51:12.288549Z)
- `INDGEN|TOTAL|generation` = **25636** (n=99, 2026-09-17T00:51:12.288549Z)
- `MELNGC|TOTAL|margin` = **34511** (n=99, 2026-09-17T00:49:26.945274Z)
- `NDF|TOTAL|demand` = **18621** (n=101, 2026-09-17T00:47:34.020052Z)
- `TSDF|TOTAL|demand` = **19121** (n=101, 2026-09-17T00:47:34.020052Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T01:14:22.015612Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:13:45Z`
- `2026-09-17T01:12:14.084927Z` — **MID**: 0 rows; marker `2026-09-17T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T01:12:14.084927Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:11:45Z`
- `2026-09-17T01:10:27.905487Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:10:00Z`
- `2026-09-17T01:10:27.905487Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:09:45Z`
- `2026-09-17T01:08:19.716810Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:07:45Z`
- `2026-09-17T01:07:31.618096Z` — **MID**: 0 rows; marker `2026-09-17T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T01:06:21.649739Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:05:45Z`
- `2026-09-17T01:05:33.414884Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:05:00Z`
- `2026-09-17T01:04:13.809667Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:03:45Z`
- `2026-09-17T01:02:20.234850Z` — **FREQ**: 5761 rows; marker `2026-09-17T01:01:45Z`
- `2026-09-17T01:00:27.203745Z` — **FUELHH**: 20 rows; marker `2026-09-17T01:00:00Z`
- `2026-09-17T01:00:27.203745Z` — **FUELINST**: 80 rows; marker `2026-09-17T01:00:00Z`
- `2026-09-17T01:00:11.980706Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:59:45Z`
- `2026-09-17T00:58:22.707594Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:57:45Z`
