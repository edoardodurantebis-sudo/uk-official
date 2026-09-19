# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T02:41:38.151465Z`  
Current process started UTC: `2026-09-19T02:37:38.026325Z`  
1-second metadata polls in this process: **170**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-509** (n=1146, 2026-09-19T02:40:40.458291Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=1146, 2026-09-19T02:40:40.458291Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1146, 2026-09-19T02:40:40.458291Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1146, 2026-09-19T02:40:40.458291Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1146, 2026-09-19T02:40:40.458291Z)
- `FUELINST|fuelType=OTHER|generation` = **561** (n=1146, 2026-09-19T02:40:40.458291Z)
- `FUELINST|fuelType=PS|generation` = **-611** (n=1146, 2026-09-19T02:40:40.458291Z)
- `FUELINST|fuelType=WIND|generation` = **16293** (n=1146, 2026-09-19T02:40:40.458291Z)
- `IMBALNGC|TOTAL|imbalance` = **9256** (n=189, 2026-09-19T02:21:53.930215Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=189, 2026-09-19T02:21:53.930215Z)
- `INDGEN|TOTAL|generation` = **26451** (n=189, 2026-09-19T02:21:53.930215Z)
- `MELNGC|TOTAL|margin` = **38306** (n=189, 2026-09-19T02:19:37.697156Z)
- `NDF|TOTAL|demand` = **16550** (n=193, 2026-09-19T02:17:41.280152Z)
- `TSDF|TOTAL|demand` = **17194** (n=193, 2026-09-19T02:17:41.280152Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T02:41:36.821915Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:35.521244Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:34.188687Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:32.891037Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:31.525089Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:30.206619Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:28.457514Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:27.066909Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:25.776268Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:24.451398Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:23.088103Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:21.782686Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:20.458783Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:19.066038Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:41:17.734226Z` — **MID**: 0 rows; marker `2026-09-19T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
