# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T19:49:47.344647Z`  
Current process started UTC: `2026-09-18T19:45:47.341940Z`  
1-second metadata polls in this process: **220**  
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

- `FUELINST|fuelType=INTVKL|generation` = **943** (n=1084, 2026-09-18T19:45:47.341948Z)
- `FUELINST|fuelType=NPSHYD|generation` = **486** (n=1084, 2026-09-18T19:45:47.341948Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1084, 2026-09-18T19:45:47.341948Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1084, 2026-09-18T19:45:47.341948Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1084, 2026-09-18T19:45:47.341948Z)
- `FUELINST|fuelType=OTHER|generation` = **937** (n=1084, 2026-09-18T19:45:47.341948Z)
- `FUELINST|fuelType=PS|generation` = **411** (n=1084, 2026-09-18T19:45:47.341948Z)
- `FUELINST|fuelType=WIND|generation` = **16790** (n=1084, 2026-09-18T19:45:47.341948Z)
- `IMBALNGC|TOTAL|imbalance` = **9032** (n=178, 2026-09-18T19:22:27.550765Z)
- `INDDEM|TOTAL|demand` = **-10891** (n=178, 2026-09-18T19:22:12.034913Z)
- `INDGEN|TOTAL|generation` = **26226** (n=178, 2026-09-18T19:22:12.034913Z)
- `MELNGC|TOTAL|margin` = **37505** (n=178, 2026-09-18T19:20:16.544424Z)
- `NDF|TOTAL|demand` = **16550** (n=183, 2026-09-18T19:47:55.702271Z)
- `TSDF|TOTAL|demand` = **17194** (n=183, 2026-09-18T19:47:55.702271Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T19:49:46.382220Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:45.382106Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:44.381992Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:43.381910Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:42.381804Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:41.381685Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:40.381569Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:39.381449Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:38.381327Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:37.381203Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:36.381086Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:35.106584Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:31.651173Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:30.651061Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:49:29.650952Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
