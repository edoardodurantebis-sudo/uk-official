# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T13:47:17.096348Z`  
Current process started UTC: `2026-09-18T13:43:16.703327Z`  
1-second metadata polls in this process: **219**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1389** (n=1035, 2026-09-18T13:45:26.886767Z)
- `FUELINST|fuelType=NPSHYD|generation` = **318** (n=1035, 2026-09-18T13:45:26.886767Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1035, 2026-09-18T13:45:26.886767Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1035, 2026-09-18T13:45:26.886767Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1035, 2026-09-18T13:45:26.886767Z)
- `FUELINST|fuelType=OTHER|generation` = **454** (n=1035, 2026-09-18T13:45:26.886767Z)
- `FUELINST|fuelType=PS|generation` = **-707** (n=1035, 2026-09-18T13:45:26.886767Z)
- `FUELINST|fuelType=WIND|generation` = **15566** (n=1035, 2026-09-18T13:45:26.886767Z)
- `IMBALNGC|TOTAL|imbalance` = **8935** (n=170, 2026-09-18T13:25:04.803083Z)
- `INDDEM|TOTAL|demand` = **-10745** (n=170, 2026-09-18T13:25:04.803083Z)
- `INDGEN|TOTAL|generation` = **25605** (n=170, 2026-09-18T13:25:04.803083Z)
- `MELNGC|TOTAL|margin` = **38174** (n=170, 2026-09-18T13:21:37.459648Z)
- `NDF|TOTAL|demand` = **16170** (n=174, 2026-09-18T13:18:55.653418Z)
- `TSDF|TOTAL|demand` = **16670** (n=174, 2026-09-18T13:18:55.653418Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T13:47:16.115942Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:15.115857Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:13.894554Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:12.894442Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:11.894359Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:10.621796Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:09.613846Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:08.613736Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:06.960931Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:05.619007Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:04.618938Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:03.080983Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:02.080904Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:01.014216Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T13:47:00.014107Z` — **MID**: 0 rows; marker `2026-09-18T13:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
