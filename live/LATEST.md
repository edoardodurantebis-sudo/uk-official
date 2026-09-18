# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T12:36:05.965243Z`  
Current process started UTC: `2026-09-18T12:32:05.583909Z`  
1-second metadata polls in this process: **137**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-10744, delta=3052, z=1.92 -> demand pressure up
- **WINDFOR** `TOTAL` `generation` — wind forecast [TOTAL] generation: value=7845, delta=-11023, z=-4.38 -> renewable cushion down / residual-load pressure up
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=80, delta=-38, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=118, delta=27, z=6.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1021, 2026-09-18T12:35:23.862073Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1021, 2026-09-18T12:35:23.862073Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1021, 2026-09-18T12:35:23.862073Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1021, 2026-09-18T12:35:23.862073Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1021, 2026-09-18T12:35:23.862073Z)
- `FUELINST|fuelType=OTHER|generation` = **448** (n=1021, 2026-09-18T12:35:23.862073Z)
- `FUELINST|fuelType=PS|generation` = **-480** (n=1021, 2026-09-18T12:35:23.862073Z)
- `FUELINST|fuelType=WIND|generation` = **14602** (n=1021, 2026-09-18T12:35:23.862073Z)
- `IMBALNGC|TOTAL|imbalance` = **8916** (n=168, 2026-09-18T12:25:23.211398Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=168, 2026-09-18T12:25:06.499475Z)
- `INDGEN|TOTAL|generation` = **25586** (n=168, 2026-09-18T12:25:06.499475Z)
- `MELNGC|TOTAL|margin` = **38104** (n=168, 2026-09-18T12:21:55.537431Z)
- `NDF|TOTAL|demand` = **16170** (n=172, 2026-09-18T12:19:30.897632Z)
- `TSDF|TOTAL|demand` = **16670** (n=172, 2026-09-18T12:19:30.897632Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T12:36:04.334108Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:36:02.687809Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:36:01.028528Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:59.348703Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:57.807592Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:55.832920Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:54.176893Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:52.520394Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:50.944179Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:49.375179Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:47.682215Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:46.097444Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:44.512419Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:42.935372Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:35:41.319672Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
