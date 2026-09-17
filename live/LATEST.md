# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T00:25:19.333981Z`  
Current process started UTC: `2026-09-17T00:21:19.678872Z`  
1-second metadata polls in this process: **233**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=0, z=-3.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-312, delta=-40, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-272, delta=-77, z=-3.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-195, delta=-78, z=-3.76 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-28, delta=-68, z=-3.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-117, delta=-77, z=-3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=3, delta=-50, z=-0.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=-3, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.72 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.82 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=50, delta=50, z=5.13 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=40, delta=-418, z=-3.53 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.03 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-1221** (n=586, 2026-09-17T00:20:21.841120Z)
- `FUELINST|fuelType=NPSHYD|generation` = **421** (n=586, 2026-09-17T00:20:21.841120Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=586, 2026-09-17T00:20:21.841120Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=586, 2026-09-17T00:20:21.841120Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=586, 2026-09-17T00:20:21.841120Z)
- `FUELINST|fuelType=OTHER|generation` = **454** (n=586, 2026-09-17T00:20:21.841120Z)
- `FUELINST|fuelType=PS|generation` = **-246** (n=586, 2026-09-17T00:20:21.841120Z)
- `FUELINST|fuelType=WIND|generation` = **11814** (n=586, 2026-09-17T00:20:21.841120Z)
- `IMBALNGC|TOTAL|imbalance` = **6558** (n=98, 2026-09-17T00:21:19.678881Z)
- `INDDEM|TOTAL|demand` = **-11763** (n=98, 2026-09-17T00:21:19.678881Z)
- `INDGEN|TOTAL|generation` = **25617** (n=98, 2026-09-17T00:21:19.678881Z)
- `MELNGC|TOTAL|margin` = **34508** (n=98, 2026-09-17T00:19:18.077385Z)
- `NDF|TOTAL|demand` = **18621** (n=100, 2026-09-17T00:17:58.523543Z)
- `TSDF|TOTAL|demand` = **19121** (n=100, 2026-09-17T00:17:58.523543Z)
- `WINDFOR|TOTAL|generation` = **20102** (n=17, 2026-09-16T23:30:41.101363Z)

## Latest publication events

- `2026-09-17T00:24:17.620784Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:23:45Z`
- `2026-09-17T00:22:24.575229Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:21:45Z`
- `2026-09-17T00:21:19.678881Z` — **INDGEN**: 990 rows; marker `2026-09-17T00:17:00Z`
- `2026-09-17T00:21:19.678881Z` — **INDDEM**: 990 rows; marker `2026-09-17T00:17:00Z`
- `2026-09-17T00:21:19.678881Z` — **IMBALNGC**: 990 rows; marker `2026-09-17T00:17:00Z`
- `2026-09-17T00:20:21.841120Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:20:00Z`
- `2026-09-17T00:20:21.841120Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:19:45Z`
- `2026-09-17T00:19:18.077385Z` — **MELNGC**: 990 rows; marker `2026-09-17T00:17:00Z`
- `2026-09-17T00:18:13.887957Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:17:45Z`
- `2026-09-17T00:17:58.523543Z` — **TSDF**: 990 rows; marker `2026-09-17T00:17:00Z`
- `2026-09-17T00:17:58.523543Z` — **NDF**: 55 rows; marker `2026-09-17T00:17:00Z`
- `2026-09-17T00:16:06.804222Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:15:45Z`
- `2026-09-17T00:15:34.629703Z` — **FUELINST**: 80 rows; marker `2026-09-17T00:15:00Z`
- `2026-09-17T00:14:15.075618Z` — **FREQ**: 5761 rows; marker `2026-09-17T00:13:45Z`
- `2026-09-17T00:12:54.447850Z` — **MID**: 0 rows; marker `2026-09-17T00:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
