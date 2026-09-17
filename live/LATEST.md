# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T07:22:04.090083Z`  
Current process started UTC: `2026-09-17T07:18:03.021458Z`  
1-second metadata polls in this process: **131**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=-4, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.42 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=49, delta=49, z=4.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=3, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=1, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=17, z=4.30 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-1134, delta=10, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1114, delta=62, z=-3.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.73 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.78 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1370** (n=670, 2026-09-17T07:20:27.261050Z)
- `FUELINST|fuelType=NPSHYD|generation` = **418** (n=670, 2026-09-17T07:20:27.261050Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3313** (n=670, 2026-09-17T07:20:27.261050Z)
- `FUELINST|fuelType=OCGT|generation` = **52** (n=670, 2026-09-17T07:20:27.261050Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=670, 2026-09-17T07:20:27.261050Z)
- `FUELINST|fuelType=OTHER|generation` = **545** (n=670, 2026-09-17T07:20:27.261050Z)
- `FUELINST|fuelType=PS|generation` = **223** (n=670, 2026-09-17T07:20:27.261050Z)
- `FUELINST|fuelType=WIND|generation` = **14113** (n=670, 2026-09-17T07:20:27.261050Z)
- `IMBALNGC|TOTAL|imbalance` = **7157** (n=112, 2026-09-17T07:19:39.625704Z)
- `INDDEM|TOTAL|demand` = **-12138** (n=112, 2026-09-17T07:19:39.625704Z)
- `INDGEN|TOTAL|generation` = **26528** (n=112, 2026-09-17T07:19:39.625704Z)
- `MELNGC|TOTAL|margin` = **35577** (n=112, 2026-09-17T07:18:19.457722Z)
- `NDF|TOTAL|demand` = **18621** (n=114, 2026-09-17T07:16:55.100548Z)
- `TSDF|TOTAL|demand` = **19371** (n=114, 2026-09-17T07:17:11.420731Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T07:22:02.387575Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:22:00.623045Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:58.883879Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:57.169395Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:55.453481Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:53.729402Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:51.995030Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:50.273607Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:48.036312Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:46.294334Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:44.579646Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:42.857776Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:41.145443Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:39.402884Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:21:37.668549Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
