# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T12:53:10.004522Z`  
Current process started UTC: `2026-09-19T12:49:09.277537Z`  
1-second metadata polls in this process: **189**  
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

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1268, 2026-09-19T12:50:45.422876Z)
- `FUELINST|fuelType=NPSHYD|generation` = **283** (n=1268, 2026-09-19T12:50:45.422876Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1268, 2026-09-19T12:50:45.422876Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1268, 2026-09-19T12:50:45.422876Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1268, 2026-09-19T12:50:45.422876Z)
- `FUELINST|fuelType=OTHER|generation` = **373** (n=1268, 2026-09-19T12:50:45.422876Z)
- `FUELINST|fuelType=PS|generation` = **-564** (n=1268, 2026-09-19T12:50:45.422876Z)
- `FUELINST|fuelType=WIND|generation` = **15233** (n=1268, 2026-09-19T12:50:45.422876Z)
- `IMBALNGC|TOTAL|imbalance` = **-3250** (n=208, 2026-09-19T12:24:22.238647Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=208, 2026-09-19T12:24:05.241870Z)
- `INDGEN|TOTAL|generation` = **16759** (n=208, 2026-09-19T12:24:05.241870Z)
- `MELNGC|TOTAL|margin` = **36757** (n=209, 2026-09-19T12:51:51.215184Z)
- `NDF|TOTAL|demand` = **19509** (n=214, 2026-09-19T12:48:45.487251Z)
- `TSDF|TOTAL|demand` = **20009** (n=214, 2026-09-19T12:49:09.277544Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T12:53:08.785567Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:53:07.596163Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:53:06.407374Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:53:05.218336Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:53:04.020039Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:53:02.830428Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:53:01.605399Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:53:00.408702Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:52:59.217219Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:52:58.031834Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:52:56.198858Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:52:54.992793Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:52:53.817190Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:52:52.595052Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T12:52:51.394932Z` — **MID**: 0 rows; marker `2026-09-19T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
