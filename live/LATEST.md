# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T02:33:15.622081Z`  
Current process started UTC: `2026-09-19T02:29:14.781430Z`  
1-second metadata polls in this process: **129**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-509** (n=1144, 2026-09-19T02:30:36.397418Z)
- `FUELINST|fuelType=NPSHYD|generation` = **345** (n=1144, 2026-09-19T02:30:36.397418Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3348** (n=1144, 2026-09-19T02:30:36.397418Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1144, 2026-09-19T02:30:36.397418Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1144, 2026-09-19T02:30:36.397418Z)
- `FUELINST|fuelType=OTHER|generation` = **422** (n=1144, 2026-09-19T02:30:36.397418Z)
- `FUELINST|fuelType=PS|generation` = **-672** (n=1144, 2026-09-19T02:30:36.397418Z)
- `FUELINST|fuelType=WIND|generation` = **16151** (n=1144, 2026-09-19T02:30:36.397418Z)
- `IMBALNGC|TOTAL|imbalance` = **9256** (n=189, 2026-09-19T02:21:53.930215Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=189, 2026-09-19T02:21:53.930215Z)
- `INDGEN|TOTAL|generation` = **26451** (n=189, 2026-09-19T02:21:53.930215Z)
- `MELNGC|TOTAL|margin` = **38306** (n=189, 2026-09-19T02:19:37.697156Z)
- `NDF|TOTAL|demand` = **16550** (n=193, 2026-09-19T02:17:41.280152Z)
- `TSDF|TOTAL|demand` = **17194** (n=193, 2026-09-19T02:17:41.280152Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T02:33:13.917852Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:33:12.067956Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:33:10.378046Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:33:08.664583Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:33:06.957365Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:33:05.229432Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:33:02.850564Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:33:01.116892Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:32:59.364151Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:32:57.670253Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:32:55.961555Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:32:54.259610Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:32:52.560157Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:32:50.864683Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:32:49.156740Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
