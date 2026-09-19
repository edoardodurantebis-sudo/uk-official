# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T12:19:26.897838Z`  
Current process started UTC: `2026-09-19T12:15:26.896161Z`  
1-second metadata polls in this process: **168**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1261, 2026-09-19T12:15:30.852597Z)
- `FUELINST|fuelType=NPSHYD|generation` = **282** (n=1261, 2026-09-19T12:15:30.852597Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=1261, 2026-09-19T12:15:30.852597Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1261, 2026-09-19T12:15:30.852597Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1261, 2026-09-19T12:15:30.852597Z)
- `FUELINST|fuelType=OTHER|generation` = **560** (n=1261, 2026-09-19T12:15:30.852597Z)
- `FUELINST|fuelType=PS|generation` = **-614** (n=1261, 2026-09-19T12:15:30.852597Z)
- `FUELINST|fuelType=WIND|generation` = **15535** (n=1261, 2026-09-19T12:15:30.852597Z)
- `IMBALNGC|TOTAL|imbalance` = **-3260** (n=207, 2026-09-19T11:54:43.988227Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=207, 2026-09-19T11:54:43.988227Z)
- `INDGEN|TOTAL|generation` = **16749** (n=207, 2026-09-19T11:54:43.988227Z)
- `MELNGC|TOTAL|margin` = **36781** (n=207, 2026-09-19T11:51:22.558353Z)
- `NDF|TOTAL|demand` = **19509** (n=213, 2026-09-19T12:18:29.074439Z)
- `TSDF|TOTAL|demand` = **20009** (n=213, 2026-09-19T12:18:29.074439Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T12:19:25.602443Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:24.325828Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:23.005373Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:21.646513Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:20.314291Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:18.630052Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:17.263654Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:15.935708Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:14.685967Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:13.330056Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:12.020568Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:10.725524Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:09.436139Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:07.732084Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:19:06.442826Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
