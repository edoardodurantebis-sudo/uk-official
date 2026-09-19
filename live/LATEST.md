# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T13:22:29.549245Z`  
Current process started UTC: `2026-09-19T13:18:28.416847Z`  
1-second metadata polls in this process: **186**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-18** (n=1274, 2026-09-19T13:20:37.882833Z)
- `FUELINST|fuelType=NPSHYD|generation` = **281** (n=1274, 2026-09-19T13:20:37.882833Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1274, 2026-09-19T13:20:37.882833Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1274, 2026-09-19T13:20:37.882833Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1274, 2026-09-19T13:20:37.882833Z)
- `FUELINST|fuelType=OTHER|generation` = **368** (n=1274, 2026-09-19T13:20:37.882833Z)
- `FUELINST|fuelType=PS|generation` = **-569** (n=1274, 2026-09-19T13:20:37.882833Z)
- `FUELINST|fuelType=WIND|generation` = **15011** (n=1274, 2026-09-19T13:20:37.882833Z)
- `IMBALNGC|TOTAL|imbalance` = **-3220** (n=209, 2026-09-19T12:54:57.001125Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=209, 2026-09-19T12:54:57.001125Z)
- `INDGEN|TOTAL|generation` = **16789** (n=209, 2026-09-19T12:54:57.001125Z)
- `MELNGC|TOTAL|margin` = **36757** (n=210, 2026-09-19T13:20:54.482792Z)
- `NDF|TOTAL|demand` = **19509** (n=215, 2026-09-19T13:18:28.416855Z)
- `TSDF|TOTAL|demand` = **20009** (n=215, 2026-09-19T13:18:28.416855Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T13:22:28.355386Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:27.169060Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:25.948226Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:24.765063Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:23.376071Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:21.980693Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:20.813152Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:19.153893Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:17.975429Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:14.970700Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:14.970700Z` — **FREQ**: 5761 rows; marker `2026-09-19T13:21:45Z`
- `2026-09-19T13:22:13.728346Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:12.497031Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:11.288190Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:22:09.925511Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
