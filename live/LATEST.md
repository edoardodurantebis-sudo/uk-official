# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T11:28:55.220534Z`  
Current process started UTC: `2026-09-19T11:24:54.717954Z`  
1-second metadata polls in this process: **174**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16777, delta=25, z=-3.78 -> state changed
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **333** (n=1251, 2026-09-19T11:25:26.544383Z)
- `FUELINST|fuelType=NPSHYD|generation` = **307** (n=1251, 2026-09-19T11:25:26.544383Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1251, 2026-09-19T11:25:26.544383Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1251, 2026-09-19T11:25:26.544383Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1251, 2026-09-19T11:25:26.544383Z)
- `FUELINST|fuelType=OTHER|generation` = **510** (n=1251, 2026-09-19T11:25:26.544383Z)
- `FUELINST|fuelType=PS|generation` = **-935** (n=1251, 2026-09-19T11:25:26.544383Z)
- `FUELINST|fuelType=WIND|generation` = **15675** (n=1251, 2026-09-19T11:25:26.544383Z)
- `IMBALNGC|TOTAL|imbalance` = **-3354** (n=206, 2026-09-19T11:25:26.544383Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=206, 2026-09-19T11:25:10.722520Z)
- `INDGEN|TOTAL|generation` = **16777** (n=206, 2026-09-19T11:24:54.717962Z)
- `MELNGC|TOTAL|margin` = **36659** (n=206, 2026-09-19T11:21:14.136124Z)
- `NDF|TOTAL|demand` = **19631** (n=211, 2026-09-19T11:18:50.597516Z)
- `TSDF|TOTAL|demand` = **20131** (n=211, 2026-09-19T11:18:50.597516Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T11:28:53.747504Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:52.457033Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:51.129572Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:49.819690Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:48.495003Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:47.198220Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:45.907387Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:44.626709Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:43.247798Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:41.958484Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:40.399616Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:39.120695Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:37.828488Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:36.551879Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:28:35.268272Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
