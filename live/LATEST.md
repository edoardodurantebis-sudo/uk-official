# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T18:29:14.867268Z`  
Current process started UTC: `2026-09-18T18:25:14.035912Z`  
1-second metadata polls in this process: **192**  
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

- `FUELINST|fuelType=INTVKL|generation` = **939** (n=1068, 2026-09-18T18:25:29.983428Z)
- `FUELINST|fuelType=NPSHYD|generation` = **494** (n=1068, 2026-09-18T18:25:29.983428Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1068, 2026-09-18T18:25:29.983428Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=1068, 2026-09-18T18:25:29.983428Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1068, 2026-09-18T18:25:29.983428Z)
- `FUELINST|fuelType=OTHER|generation` = **1481** (n=1068, 2026-09-18T18:25:29.983428Z)
- `FUELINST|fuelType=PS|generation` = **523** (n=1068, 2026-09-18T18:25:29.983428Z)
- `FUELINST|fuelType=WIND|generation` = **16909** (n=1068, 2026-09-18T18:25:29.983428Z)
- `IMBALNGC|TOTAL|imbalance` = **9176** (n=176, 2026-09-18T18:24:19.444583Z)
- `INDDEM|TOTAL|demand` = **-10736** (n=176, 2026-09-18T18:24:03.813466Z)
- `INDGEN|TOTAL|generation` = **26226** (n=176, 2026-09-18T18:24:03.813466Z)
- `MELNGC|TOTAL|margin` = **37767** (n=176, 2026-09-18T18:21:20.209125Z)
- `NDF|TOTAL|demand` = **16550** (n=180, 2026-09-18T18:18:44.073570Z)
- `TSDF|TOTAL|demand` = **17050** (n=180, 2026-09-18T18:18:44.073570Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T18:29:13.664655Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:29:12.457369Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:29:11.270729Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:29:10.047591Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:29:08.830684Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:29:07.617581Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:29:06.425206Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:29:05.206425Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:29:04.015690Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:29:02.762053Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:29:01.559714Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:28:58.208191Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:28:56.995089Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:28:55.817360Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:28:54.625170Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
