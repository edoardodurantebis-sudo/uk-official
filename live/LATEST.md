# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T12:32:04.460826Z`  
Current process started UTC: `2026-09-19T12:28:03.509503Z`  
1-second metadata polls in this process: **135**  
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

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1264, 2026-09-19T12:30:34.686513Z)
- `FUELINST|fuelType=NPSHYD|generation` = **282** (n=1264, 2026-09-19T12:30:34.686513Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1264, 2026-09-19T12:30:34.686513Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1264, 2026-09-19T12:30:34.686513Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1264, 2026-09-19T12:30:34.686513Z)
- `FUELINST|fuelType=OTHER|generation` = **436** (n=1264, 2026-09-19T12:30:34.686513Z)
- `FUELINST|fuelType=PS|generation` = **-621** (n=1264, 2026-09-19T12:30:34.686513Z)
- `FUELINST|fuelType=WIND|generation` = **15347** (n=1264, 2026-09-19T12:30:34.686513Z)
- `IMBALNGC|TOTAL|imbalance` = **-3250** (n=208, 2026-09-19T12:24:22.238647Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=208, 2026-09-19T12:24:05.241870Z)
- `INDGEN|TOTAL|generation` = **16759** (n=208, 2026-09-19T12:24:05.241870Z)
- `MELNGC|TOTAL|margin` = **36757** (n=208, 2026-09-19T12:20:45.809462Z)
- `NDF|TOTAL|demand` = **19509** (n=213, 2026-09-19T12:18:29.074439Z)
- `TSDF|TOTAL|demand` = **20009** (n=213, 2026-09-19T12:18:29.074439Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T12:32:02.790918Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:32:00.938697Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:59.263582Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:56.333304Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:54.619842Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:52.961963Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:51.330404Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:49.702979Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:47.920098Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:45.714924Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:43.858224Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:42.189048Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:39.832191Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:38.189032Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:31:36.550474Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
