# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T10:08:28.607726Z`  
Current process started UTC: `2026-09-18T10:04:26.693289Z`  
1-second metadata polls in this process: **218**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=991, 2026-09-18T10:05:30.219164Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=991, 2026-09-18T10:05:30.219164Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=991, 2026-09-18T10:05:30.219164Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=991, 2026-09-18T10:05:30.219164Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=991, 2026-09-18T10:05:30.219164Z)
- `FUELINST|fuelType=OTHER|generation` = **880** (n=991, 2026-09-18T10:05:30.219164Z)
- `FUELINST|fuelType=PS|generation` = **-702** (n=991, 2026-09-18T10:05:30.219164Z)
- `FUELINST|fuelType=WIND|generation` = **11701** (n=991, 2026-09-18T10:05:30.219164Z)
- `IMBALNGC|TOTAL|imbalance` = **7801** (n=163, 2026-09-18T09:49:53.694216Z)
- `INDDEM|TOTAL|demand` = **-13189** (n=163, 2026-09-18T09:49:53.694216Z)
- `INDGEN|TOTAL|generation` = **26894** (n=163, 2026-09-18T09:49:53.694216Z)
- `MELNGC|TOTAL|margin` = **36164** (n=163, 2026-09-18T09:49:19.963149Z)
- `NDF|TOTAL|demand` = **16454** (n=167, 2026-09-18T09:47:20.937653Z)
- `TSDF|TOTAL|demand` = **19093** (n=167, 2026-09-18T09:47:20.937653Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T10:08:26.397390Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:25.326309Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:24.048820Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:22.976142Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:21.914885Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:20.744407Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:19.738695Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:18.703063Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:17.660828Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:16.643691Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:15.643597Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:14.550751Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:13.146127Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:10.544268Z` — **MID**: 0 rows; marker `2026-09-18T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:08:10.544268Z` — **FREQ**: 5761 rows; marker `2026-09-18T10:07:45Z`
