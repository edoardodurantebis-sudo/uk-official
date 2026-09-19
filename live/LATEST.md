# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T13:43:26.061910Z`  
Current process started UTC: `2026-09-19T13:39:24.804420Z`  
1-second metadata polls in this process: **149**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=15.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=1, z=17.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=74, delta=74, z=126.77 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=102, delta=0, z=19.98 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-18** (n=1278, 2026-09-19T13:40:45.414294Z)
- `FUELINST|fuelType=NPSHYD|generation` = **282** (n=1278, 2026-09-19T13:40:45.414294Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1278, 2026-09-19T13:40:45.414294Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1278, 2026-09-19T13:40:45.414294Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1278, 2026-09-19T13:40:45.414294Z)
- `FUELINST|fuelType=OTHER|generation` = **393** (n=1278, 2026-09-19T13:40:45.414294Z)
- `FUELINST|fuelType=PS|generation` = **-554** (n=1278, 2026-09-19T13:40:45.414294Z)
- `FUELINST|fuelType=WIND|generation` = **14836** (n=1278, 2026-09-19T13:40:45.414294Z)
- `IMBALNGC|TOTAL|imbalance` = **-3234** (n=210, 2026-09-19T13:24:00.524935Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=210, 2026-09-19T13:23:45.180449Z)
- `INDGEN|TOTAL|generation` = **16775** (n=210, 2026-09-19T13:24:00.524935Z)
- `MELNGC|TOTAL|margin` = **36757** (n=210, 2026-09-19T13:20:54.482792Z)
- `NDF|TOTAL|demand` = **19509** (n=215, 2026-09-19T13:18:28.416855Z)
- `TSDF|TOTAL|demand` = **20009** (n=215, 2026-09-19T13:18:28.416855Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T13:43:24.225435Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:22.700600Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:21.181903Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:19.651564Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:18.092888Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:16.566136Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:15.036429Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:13.494364Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:11.958521Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:10.426039Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:08.479903Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:06.957374Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:05.408689Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:03.884018Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:43:02.370898Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
