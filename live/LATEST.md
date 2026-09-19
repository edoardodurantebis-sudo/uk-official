# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T13:09:52.998264Z`  
Current process started UTC: `2026-09-19T13:05:52.908767Z`  
1-second metadata polls in this process: **191**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16759, delta=10, z=-3.53 -> state changed
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16749, delta=-28, z=-3.66 -> state changed
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16777, delta=25, z=-3.78 -> state changed
- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16752, delta=-9313, z=-3.94 -> state changed
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **14** (n=1271, 2026-09-19T13:05:29.264422Z)
- `FUELINST|fuelType=NPSHYD|generation` = **282** (n=1271, 2026-09-19T13:05:29.264422Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3321** (n=1271, 2026-09-19T13:05:29.264422Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1271, 2026-09-19T13:05:29.264422Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1271, 2026-09-19T13:05:29.264422Z)
- `FUELINST|fuelType=OTHER|generation` = **364** (n=1271, 2026-09-19T13:05:29.264422Z)
- `FUELINST|fuelType=PS|generation` = **-565** (n=1271, 2026-09-19T13:05:29.264422Z)
- `FUELINST|fuelType=WIND|generation` = **15071** (n=1271, 2026-09-19T13:05:29.264422Z)
- `IMBALNGC|TOTAL|imbalance` = **-3220** (n=209, 2026-09-19T12:54:57.001125Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=209, 2026-09-19T12:54:57.001125Z)
- `INDGEN|TOTAL|generation` = **16789** (n=209, 2026-09-19T12:54:57.001125Z)
- `MELNGC|TOTAL|margin` = **36757** (n=209, 2026-09-19T12:51:51.215184Z)
- `NDF|TOTAL|demand` = **19509** (n=214, 2026-09-19T12:48:45.487251Z)
- `TSDF|TOTAL|demand` = **20009** (n=214, 2026-09-19T12:49:09.277544Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T13:09:51.811029Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:50.621109Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:49.478478Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:48.307470Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:47.134424Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:45.939503Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:44.770363Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:43.574557Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:42.345767Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:41.111173Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:39.587979Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:38.395479Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:37.206865Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:36.059289Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:09:34.879130Z` — **MID**: 0 rows; marker `2026-09-19T13:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
