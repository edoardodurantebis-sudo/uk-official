# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T12:48:39.475090Z`  
Current process started UTC: `2026-09-18T12:44:38.999773Z`  
1-second metadata polls in this process: **124**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1023, 2026-09-18T12:45:28.322302Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1023, 2026-09-18T12:45:28.322302Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3342** (n=1023, 2026-09-18T12:45:28.322302Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1023, 2026-09-18T12:45:28.322302Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1023, 2026-09-18T12:45:28.322302Z)
- `FUELINST|fuelType=OTHER|generation` = **559** (n=1023, 2026-09-18T12:45:28.322302Z)
- `FUELINST|fuelType=PS|generation` = **-717** (n=1023, 2026-09-18T12:45:28.322302Z)
- `FUELINST|fuelType=WIND|generation` = **15017** (n=1023, 2026-09-18T12:45:28.322302Z)
- `IMBALNGC|TOTAL|imbalance` = **8916** (n=168, 2026-09-18T12:25:23.211398Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=168, 2026-09-18T12:25:06.499475Z)
- `INDGEN|TOTAL|generation` = **25586** (n=168, 2026-09-18T12:25:06.499475Z)
- `MELNGC|TOTAL|margin` = **38104** (n=168, 2026-09-18T12:21:55.537431Z)
- `NDF|TOTAL|demand` = **16170** (n=173, 2026-09-18T12:48:33.598652Z)
- `TSDF|TOTAL|demand` = **16670** (n=173, 2026-09-18T12:48:33.598652Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T12:48:33.598652Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:48:33.598652Z` — **TSDF**: 1404 rows; marker `2026-09-18T12:48:00Z`
- `2026-09-18T12:48:33.598652Z` — **NDF**: 78 rows; marker `2026-09-18T12:48:00Z`
- `2026-09-18T12:48:31.754624Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:48:29.914551Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:48:27.844466Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:48:26.030739Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:48:24.236401Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:48:22.487939Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:48:20.755306Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:48:16.907281Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:48:16.907281Z` — **FREQ**: 5761 rows; marker `2026-09-18T12:47:45Z`
- `2026-09-18T12:48:15.125295Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:48:13.382604Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:48:11.567500Z` — **MID**: 0 rows; marker `2026-09-18T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
