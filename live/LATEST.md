# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T12:36:18.384429Z`  
Current process started UTC: `2026-09-19T12:32:17.635395Z`  
1-second metadata polls in this process: **133**  
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

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1265, 2026-09-19T12:35:29.978531Z)
- `FUELINST|fuelType=NPSHYD|generation` = **283** (n=1265, 2026-09-19T12:35:29.978531Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=1265, 2026-09-19T12:35:29.978531Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1265, 2026-09-19T12:35:29.978531Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1265, 2026-09-19T12:35:29.978531Z)
- `FUELINST|fuelType=OTHER|generation` = **402** (n=1265, 2026-09-19T12:35:29.978531Z)
- `FUELINST|fuelType=PS|generation` = **-570** (n=1265, 2026-09-19T12:35:29.978531Z)
- `FUELINST|fuelType=WIND|generation` = **15297** (n=1265, 2026-09-19T12:35:29.978531Z)
- `IMBALNGC|TOTAL|imbalance` = **-3250** (n=208, 2026-09-19T12:24:22.238647Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=208, 2026-09-19T12:24:05.241870Z)
- `INDGEN|TOTAL|generation` = **16759** (n=208, 2026-09-19T12:24:05.241870Z)
- `MELNGC|TOTAL|margin` = **36757** (n=208, 2026-09-19T12:20:45.809462Z)
- `NDF|TOTAL|demand` = **19509** (n=213, 2026-09-19T12:18:29.074439Z)
- `TSDF|TOTAL|demand` = **20009** (n=213, 2026-09-19T12:18:29.074439Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T12:36:16.665747Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:36:14.963196Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:36:13.265906Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:36:11.564265Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:36:09.866053Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:36:08.160044Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:36:06.433241Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:36:04.675059Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:36:02.616633Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:36:00.911716Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:35:58.934891Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:35:57.243336Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:35:55.537939Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:35:53.793499Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:35:52.099180Z` — **MID**: 0 rows; marker `2026-09-19T12:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
