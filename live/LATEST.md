# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T13:26:42.519879Z`  
Current process started UTC: `2026-09-19T13:22:42.055200Z`  
1-second metadata polls in this process: **223**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=102, delta=0, z=24.13 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=102, delta=0, z=32.77 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=102, delta=61, z=83.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=41, delta=41, z=94.66 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-18** (n=1275, 2026-09-19T13:25:35.569232Z)
- `FUELINST|fuelType=NPSHYD|generation` = **280** (n=1275, 2026-09-19T13:25:35.569232Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1275, 2026-09-19T13:25:35.569232Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1275, 2026-09-19T13:25:35.569232Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1275, 2026-09-19T13:25:35.569232Z)
- `FUELINST|fuelType=OTHER|generation` = **350** (n=1275, 2026-09-19T13:25:35.569232Z)
- `FUELINST|fuelType=PS|generation` = **-574** (n=1275, 2026-09-19T13:25:35.569232Z)
- `FUELINST|fuelType=WIND|generation` = **14970** (n=1275, 2026-09-19T13:25:35.569232Z)
- `IMBALNGC|TOTAL|imbalance` = **-3234** (n=210, 2026-09-19T13:24:00.524935Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=210, 2026-09-19T13:23:45.180449Z)
- `INDGEN|TOTAL|generation` = **16775** (n=210, 2026-09-19T13:24:00.524935Z)
- `MELNGC|TOTAL|margin` = **36757** (n=210, 2026-09-19T13:20:54.482792Z)
- `NDF|TOTAL|demand` = **19509** (n=215, 2026-09-19T13:18:28.416855Z)
- `TSDF|TOTAL|demand` = **20009** (n=215, 2026-09-19T13:18:28.416855Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T13:26:41.468176Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:40.406418Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:38.962960Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:37.883749Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:36.844726Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:35.842986Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:34.821713Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:33.801854Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:32.786737Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:31.762868Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:30.760262Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:29.719951Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:28.696760Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:27.685851Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:26:26.665425Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
