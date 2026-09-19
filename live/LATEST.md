# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T02:29:01.648906Z`  
Current process started UTC: `2026-09-19T02:25:00.960075Z`  
1-second metadata polls in this process: **229**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-509** (n=1143, 2026-09-19T02:25:36.768944Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=1143, 2026-09-19T02:25:36.768944Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1143, 2026-09-19T02:25:36.768944Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1143, 2026-09-19T02:25:36.768944Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1143, 2026-09-19T02:25:36.768944Z)
- `FUELINST|fuelType=OTHER|generation` = **375** (n=1143, 2026-09-19T02:25:36.768944Z)
- `FUELINST|fuelType=PS|generation` = **-669** (n=1143, 2026-09-19T02:25:36.768944Z)
- `FUELINST|fuelType=WIND|generation` = **16098** (n=1143, 2026-09-19T02:25:36.768944Z)
- `IMBALNGC|TOTAL|imbalance` = **9256** (n=189, 2026-09-19T02:21:53.930215Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=189, 2026-09-19T02:21:53.930215Z)
- `INDGEN|TOTAL|generation` = **26451** (n=189, 2026-09-19T02:21:53.930215Z)
- `MELNGC|TOTAL|margin` = **38306** (n=189, 2026-09-19T02:19:37.697156Z)
- `NDF|TOTAL|demand` = **16550** (n=193, 2026-09-19T02:17:41.280152Z)
- `TSDF|TOTAL|demand` = **17194** (n=193, 2026-09-19T02:17:41.280152Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T02:29:00.702893Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:59.702796Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:58.702678Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:57.702578Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:56.702469Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:55.702402Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:52.778029Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:51.777905Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:50.777789Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:49.777687Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:48.777587Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:47.777519Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:46.777426Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:45.777329Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:28:44.777216Z` — **MID**: 0 rows; marker `2026-09-19T02:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
