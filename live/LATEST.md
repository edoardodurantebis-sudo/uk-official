# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T13:35:03.331912Z`  
Current process started UTC: `2026-09-19T13:31:01.951615Z`  
1-second metadata polls in this process: **176**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-18** (n=1276, 2026-09-19T13:30:39.533266Z)
- `FUELINST|fuelType=NPSHYD|generation` = **281** (n=1276, 2026-09-19T13:30:39.533266Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1276, 2026-09-19T13:30:39.533266Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1276, 2026-09-19T13:30:39.533266Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1276, 2026-09-19T13:30:39.533266Z)
- `FUELINST|fuelType=OTHER|generation` = **310** (n=1276, 2026-09-19T13:30:39.533266Z)
- `FUELINST|fuelType=PS|generation` = **-576** (n=1276, 2026-09-19T13:30:39.533266Z)
- `FUELINST|fuelType=WIND|generation` = **14974** (n=1276, 2026-09-19T13:30:39.533266Z)
- `IMBALNGC|TOTAL|imbalance` = **-3234** (n=210, 2026-09-19T13:24:00.524935Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=210, 2026-09-19T13:23:45.180449Z)
- `INDGEN|TOTAL|generation` = **16775** (n=210, 2026-09-19T13:24:00.524935Z)
- `MELNGC|TOTAL|margin` = **36757** (n=210, 2026-09-19T13:20:54.482792Z)
- `NDF|TOTAL|demand` = **19509** (n=215, 2026-09-19T13:18:28.416855Z)
- `TSDF|TOTAL|demand` = **20009** (n=215, 2026-09-19T13:18:28.416855Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T13:35:01.772361Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:35:00.600469Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:59.380632Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:58.171885Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:56.994207Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:55.808801Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:54.626508Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:53.418085Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:52.180144Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:50.962902Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:49.761339Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:48.531307Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:47.342206Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:45.665482Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:34:44.442233Z` — **MID**: 0 rows; marker `2026-09-19T13:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
