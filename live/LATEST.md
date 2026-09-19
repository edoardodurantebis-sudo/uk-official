# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T13:47:36.599420Z`  
Current process started UTC: `2026-09-19T13:43:36.368321Z`  
1-second metadata polls in this process: **207**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=14.43 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-18** (n=1279, 2026-09-19T13:45:32.719676Z)
- `FUELINST|fuelType=NPSHYD|generation` = **281** (n=1279, 2026-09-19T13:45:32.719676Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1279, 2026-09-19T13:45:32.719676Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1279, 2026-09-19T13:45:32.719676Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1279, 2026-09-19T13:45:32.719676Z)
- `FUELINST|fuelType=OTHER|generation` = **338** (n=1279, 2026-09-19T13:45:32.719676Z)
- `FUELINST|fuelType=PS|generation` = **-423** (n=1279, 2026-09-19T13:45:32.719676Z)
- `FUELINST|fuelType=WIND|generation` = **14840** (n=1279, 2026-09-19T13:45:32.719676Z)
- `IMBALNGC|TOTAL|imbalance` = **-3234** (n=210, 2026-09-19T13:24:00.524935Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=210, 2026-09-19T13:23:45.180449Z)
- `INDGEN|TOTAL|generation` = **16775** (n=210, 2026-09-19T13:24:00.524935Z)
- `MELNGC|TOTAL|margin` = **36757** (n=210, 2026-09-19T13:20:54.482792Z)
- `NDF|TOTAL|demand` = **19509** (n=215, 2026-09-19T13:18:28.416855Z)
- `TSDF|TOTAL|demand` = **20009** (n=215, 2026-09-19T13:18:28.416855Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T13:47:35.591380Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:34.546771Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:33.519278Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:32.494508Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:31.454080Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:30.415063Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:29.275021Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:28.259148Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:25.623529Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:24.527585Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:23.518452Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:22.452116Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:21.058660Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:20.044778Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T13:47:18.779267Z` — **MID**: 0 rows; marker `2026-09-19T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
