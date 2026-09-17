# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T00:46:15.773995Z`  
Current process started UTC: `2026-09-17T00:42:14.556108Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.63 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1221** (n=591, 2026-09-17T00:45:42.197976Z)
- `FUELINST|fuelType=NPSHYD|generation` = **423** (n=591, 2026-09-17T00:45:42.197976Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=591, 2026-09-17T00:45:42.197976Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=591, 2026-09-17T00:45:42.197976Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=591, 2026-09-17T00:45:42.197976Z)
- `FUELINST|fuelType=OTHER|generation` = **445** (n=591, 2026-09-17T00:45:42.197976Z)
- `FUELINST|fuelType=PS|generation` = **-244** (n=591, 2026-09-17T00:45:42.197976Z)
- `FUELINST|fuelType=WIND|generation` = **12322** (n=591, 2026-09-17T00:45:42.197976Z)
- `IMBALNGC|TOTAL|imbalance` = **6558** (n=98, 2026-09-17T00:21:19.678881Z)
- `INDDEM|TOTAL|demand` = **-11763** (n=98, 2026-09-17T00:21:19.678881Z)
- `INDGEN|TOTAL|generation` = **25617** (n=98, 2026-09-17T00:21:19.678881Z)
- `MELNGC|TOTAL|margin` = **34508** (n=98, 2026-09-17T00:19:18.077385Z)
- `NDF|TOTAL|demand` = **18621** (n=100, 2026-09-17T00:17:58.523543Z)
- `TSDF|TOTAL|demand` = **19121** (n=100, 2026-09-17T00:17:58.523543Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T00:46:14.251340Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:45:45Z`
- `2026-09-17T00:45:42.197976Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:45:00Z`
- `2026-09-17T00:44:06.730896Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:43:45Z`
- `2026-09-17T00:42:14.556117Z` — **MID**: 0 rows; marker `2026-09-17T00:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T00:42:14.556117Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:41:45Z`
- `2026-09-17T00:40:32.787292Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:40:00Z`
- `2026-09-17T00:40:16.997528Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:39:45Z`
- `2026-09-17T00:38:25.182068Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:37:45Z`
- `2026-09-17T00:37:21.597543Z` — **MID**: 0 rows; marker `2026-09-17T00:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T00:36:17.976831Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:35:45Z`
- `2026-09-17T00:35:29.501746Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:35:00Z`
- `2026-09-17T00:34:26.068292Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:33:45Z`
- `2026-09-17T00:32:24.382740Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:31:45Z`
- `2026-09-17T00:30:30.180271Z` — **FUELHH**: 20 rows; marker `2026-09-17T00:30:00Z`
- `2026-09-17T00:30:30.180271Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:30:00Z`
