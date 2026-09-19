# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T03:36:20.103030Z`  
Current process started UTC: `2026-09-19T03:32:19.890561Z`  
1-second metadata polls in this process: **178**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-487** (n=1157, 2026-09-19T03:35:32.121866Z)
- `FUELINST|fuelType=NPSHYD|generation` = **335** (n=1157, 2026-09-19T03:35:32.121866Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3344** (n=1157, 2026-09-19T03:35:32.121866Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1157, 2026-09-19T03:35:32.121866Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1157, 2026-09-19T03:35:32.121866Z)
- `FUELINST|fuelType=OTHER|generation` = **491** (n=1157, 2026-09-19T03:35:32.121866Z)
- `FUELINST|fuelType=PS|generation` = **-544** (n=1157, 2026-09-19T03:35:32.121866Z)
- `FUELINST|fuelType=WIND|generation` = **15743** (n=1157, 2026-09-19T03:35:32.121866Z)
- `IMBALNGC|TOTAL|imbalance` = **9422** (n=191, 2026-09-19T03:21:05.977521Z)
- `INDDEM|TOTAL|demand` = **-10881** (n=191, 2026-09-19T03:21:05.977521Z)
- `INDGEN|TOTAL|generation` = **26617** (n=191, 2026-09-19T03:21:05.977521Z)
- `MELNGC|TOTAL|margin` = **38308** (n=191, 2026-09-19T03:19:22.215712Z)
- `NDF|TOTAL|demand` = **16550** (n=195, 2026-09-19T03:17:29.129773Z)
- `TSDF|TOTAL|demand` = **17194** (n=195, 2026-09-19T03:17:29.129773Z)
- `WINDFOR|TOTAL|generation` = **6714** (n=33, 2026-09-19T03:30:33.519312Z)

## Latest publication events

- `2026-09-19T03:36:18.793771Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:17.545700Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:16.231566Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:14.881877Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:13.577720Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:12.257397Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:10.994346Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:09.697170Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:08.468073Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:07.179118Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:05.869588Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:04.260840Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:02.979016Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:01.651015Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:36:00.363382Z` — **MID**: 0 rows; marker `2026-09-19T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
