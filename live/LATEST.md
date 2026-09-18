# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T12:31:54.166789Z`  
Current process started UTC: `2026-09-18T12:27:54.124084Z`  
1-second metadata polls in this process: **147**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1020, 2026-09-18T12:30:39.444684Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1020, 2026-09-18T12:30:39.444684Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1020, 2026-09-18T12:30:39.444684Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1020, 2026-09-18T12:30:39.444684Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1020, 2026-09-18T12:30:39.444684Z)
- `FUELINST|fuelType=OTHER|generation` = **666** (n=1020, 2026-09-18T12:30:39.444684Z)
- `FUELINST|fuelType=PS|generation` = **-652** (n=1020, 2026-09-18T12:30:39.444684Z)
- `FUELINST|fuelType=WIND|generation` = **14483** (n=1020, 2026-09-18T12:30:39.444684Z)
- `IMBALNGC|TOTAL|imbalance` = **8916** (n=168, 2026-09-18T12:25:23.211398Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=168, 2026-09-18T12:25:06.499475Z)
- `INDGEN|TOTAL|generation` = **25586** (n=168, 2026-09-18T12:25:06.499475Z)
- `MELNGC|TOTAL|margin` = **38104** (n=168, 2026-09-18T12:21:55.537431Z)
- `NDF|TOTAL|demand` = **16170** (n=172, 2026-09-18T12:19:30.897632Z)
- `TSDF|TOTAL|demand` = **16670** (n=172, 2026-09-18T12:19:30.897632Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T12:31:52.374662Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:50.740631Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:49.062213Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:47.611433Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:45.794905Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:44.321028Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:42.872465Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:40.527055Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:38.892304Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:36.955741Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:35.151068Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:33.415531Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:31.521347Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:29.257130Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T12:31:27.490517Z` — **MID**: 0 rows; marker `2026-09-18T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
