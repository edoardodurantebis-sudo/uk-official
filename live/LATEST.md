# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T04:05:47.152229Z`  
Current process started UTC: `2026-09-19T04:01:45.616245Z`  
1-second metadata polls in this process: **127**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-553** (n=1163, 2026-09-19T04:05:39.175896Z)
- `FUELINST|fuelType=NPSHYD|generation` = **351** (n=1163, 2026-09-19T04:05:39.175896Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1163, 2026-09-19T04:05:39.175896Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1163, 2026-09-19T04:05:39.175896Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1163, 2026-09-19T04:05:39.175896Z)
- `FUELINST|fuelType=OTHER|generation` = **234** (n=1163, 2026-09-19T04:05:39.175896Z)
- `FUELINST|fuelType=PS|generation` = **-539** (n=1163, 2026-09-19T04:05:39.175896Z)
- `FUELINST|fuelType=WIND|generation` = **15785** (n=1163, 2026-09-19T04:05:39.175896Z)
- `IMBALNGC|TOTAL|imbalance` = **9802** (n=192, 2026-09-19T03:50:47.229270Z)
- `INDDEM|TOTAL|demand` = **-10879** (n=192, 2026-09-19T03:50:47.229270Z)
- `INDGEN|TOTAL|generation` = **26996** (n=192, 2026-09-19T03:50:47.229270Z)
- `MELNGC|TOTAL|margin` = **38309** (n=192, 2026-09-19T03:49:25.726375Z)
- `NDF|TOTAL|demand` = **16550** (n=196, 2026-09-19T03:47:06.305878Z)
- `TSDF|TOTAL|demand` = **17194** (n=196, 2026-09-19T03:47:40.778261Z)
- `WINDFOR|TOTAL|generation` = **6714** (n=33, 2026-09-19T03:30:33.519312Z)

## Latest publication events

- `2026-09-19T04:05:45.443318Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:43.716451Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:42.011012Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:39.175896Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:39.175896Z` — **FUELINST**: 80 rows; marker `2026-09-19T04:05:00Z`
- `2026-09-19T04:05:37.492220Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:35.822598Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:34.140055Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:32.403501Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:30.618094Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:28.936683Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:27.272729Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:25.564353Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:23.591685Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:05:21.921159Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
