# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T11:45:02.677538Z`  
Current process started UTC: `2026-09-18T11:41:02.290886Z`  
1-second metadata polls in this process: **169**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=1010, 2026-09-18T11:40:33.544489Z)
- `FUELINST|fuelType=NPSHYD|generation` = **332** (n=1010, 2026-09-18T11:40:33.544489Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3342** (n=1010, 2026-09-18T11:40:33.544489Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1010, 2026-09-18T11:40:33.544489Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1010, 2026-09-18T11:40:33.544489Z)
- `FUELINST|fuelType=OTHER|generation` = **1006** (n=1010, 2026-09-18T11:40:33.544489Z)
- `FUELINST|fuelType=PS|generation` = **-714** (n=1010, 2026-09-18T11:40:33.544489Z)
- `FUELINST|fuelType=WIND|generation` = **12755** (n=1010, 2026-09-18T11:40:33.544489Z)
- `IMBALNGC|TOTAL|imbalance` = **8997** (n=166, 2026-09-18T11:27:14.159590Z)
- `INDDEM|TOTAL|demand` = **-10744** (n=166, 2026-09-18T11:26:58.717077Z)
- `INDGEN|TOTAL|generation` = **25667** (n=166, 2026-09-18T11:26:58.717077Z)
- `MELNGC|TOTAL|margin` = **38124** (n=166, 2026-09-18T11:22:30.597764Z)
- `NDF|TOTAL|demand` = **16170** (n=170, 2026-09-18T11:19:42.804217Z)
- `TSDF|TOTAL|demand` = **16670** (n=170, 2026-09-18T11:20:04.075631Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T11:45:01.258357Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:59.735230Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:58.377764Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:57.036425Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:55.680623Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:54.329456Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:52.581609Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:51.237876Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:49.899913Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:48.607144Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:47.267284Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:45.931479Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:44.543421Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:43.190115Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T11:44:41.850310Z` — **MID**: 0 rows; marker `2026-09-18T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
