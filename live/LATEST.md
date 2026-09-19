# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T11:03:39.864025Z`  
Current process started UTC: `2026-09-19T10:59:39.832125Z`  
1-second metadata polls in this process: **162**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **66** (n=1246, 2026-09-19T11:00:45.292805Z)
- `FUELINST|fuelType=NPSHYD|generation` = **304** (n=1246, 2026-09-19T11:00:45.292805Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=1246, 2026-09-19T11:00:45.292805Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1246, 2026-09-19T11:00:45.292805Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1246, 2026-09-19T11:00:45.292805Z)
- `FUELINST|fuelType=OTHER|generation` = **313** (n=1246, 2026-09-19T11:00:45.292805Z)
- `FUELINST|fuelType=PS|generation` = **-702** (n=1246, 2026-09-19T11:00:45.292805Z)
- `FUELINST|fuelType=WIND|generation` = **15813** (n=1246, 2026-09-19T11:00:45.292805Z)
- `IMBALNGC|TOTAL|imbalance` = **-3378** (n=205, 2026-09-19T10:55:05.891910Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=205, 2026-09-19T10:55:05.891910Z)
- `INDGEN|TOTAL|generation` = **16752** (n=205, 2026-09-19T10:55:05.891910Z)
- `MELNGC|TOTAL|margin` = **35551** (n=205, 2026-09-19T10:51:23.218211Z)
- `NDF|TOTAL|demand` = **19631** (n=210, 2026-09-19T10:48:46.270828Z)
- `TSDF|TOTAL|demand` = **20131** (n=210, 2026-09-19T10:49:02.446019Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T11:03:38.559543Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:37.255304Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:35.882750Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:34.588764Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:33.174748Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:31.853281Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:30.486153Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:27.517955Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:25.655751Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:24.337771Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:22.988748Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:21.690661Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:20.372630Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:19.035852Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:03:17.477708Z` — **MID**: 0 rows; marker `2026-09-19T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
