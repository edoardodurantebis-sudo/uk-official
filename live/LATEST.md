# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T11:16:16.678454Z`  
Current process started UTC: `2026-09-19T11:12:15.968695Z`  
1-second metadata polls in this process: **228**  
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

- `FUELINST|fuelType=INTVKL|generation` = **333** (n=1249, 2026-09-19T11:15:29.962854Z)
- `FUELINST|fuelType=NPSHYD|generation` = **306** (n=1249, 2026-09-19T11:15:29.962854Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1249, 2026-09-19T11:15:29.962854Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1249, 2026-09-19T11:15:29.962854Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1249, 2026-09-19T11:15:29.962854Z)
- `FUELINST|fuelType=OTHER|generation` = **516** (n=1249, 2026-09-19T11:15:29.962854Z)
- `FUELINST|fuelType=PS|generation` = **-822** (n=1249, 2026-09-19T11:15:29.962854Z)
- `FUELINST|fuelType=WIND|generation` = **15766** (n=1249, 2026-09-19T11:15:29.962854Z)
- `IMBALNGC|TOTAL|imbalance` = **-3378** (n=205, 2026-09-19T10:55:05.891910Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=205, 2026-09-19T10:55:05.891910Z)
- `INDGEN|TOTAL|generation` = **16752** (n=205, 2026-09-19T10:55:05.891910Z)
- `MELNGC|TOTAL|margin` = **35551** (n=205, 2026-09-19T10:51:23.218211Z)
- `NDF|TOTAL|demand` = **19631** (n=210, 2026-09-19T10:48:46.270828Z)
- `TSDF|TOTAL|demand` = **20131** (n=210, 2026-09-19T10:49:02.446019Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T11:16:15.719393Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:14.719277Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:13.719162Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:12.719041Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:11.718910Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:10.718787Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:09.588850Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:07.957545Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:06.957426Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:05.723701Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:04.530435Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:03.420931Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:01.703674Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:16:00.703603Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:15:59.583816Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
