# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T04:26:53.313438Z`  
Current process started UTC: `2026-09-19T04:22:53.304485Z`  
1-second metadata polls in this process: **176**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-578** (n=1167, 2026-09-19T04:25:35.731759Z)
- `FUELINST|fuelType=NPSHYD|generation` = **351** (n=1167, 2026-09-19T04:25:35.731759Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3345** (n=1167, 2026-09-19T04:25:35.731759Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1167, 2026-09-19T04:25:35.731759Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1167, 2026-09-19T04:25:35.731759Z)
- `FUELINST|fuelType=OTHER|generation` = **213** (n=1167, 2026-09-19T04:25:35.731759Z)
- `FUELINST|fuelType=PS|generation` = **-545** (n=1167, 2026-09-19T04:25:35.731759Z)
- `FUELINST|fuelType=WIND|generation` = **16019** (n=1167, 2026-09-19T04:25:35.731759Z)
- `IMBALNGC|TOTAL|imbalance` = **9764** (n=193, 2026-09-19T04:20:34.678100Z)
- `INDDEM|TOTAL|demand` = **-10869** (n=193, 2026-09-19T04:20:34.678100Z)
- `INDGEN|TOTAL|generation` = **26959** (n=193, 2026-09-19T04:20:34.678100Z)
- `MELNGC|TOTAL|margin` = **38315** (n=193, 2026-09-19T04:19:30.729668Z)
- `NDF|TOTAL|demand` = **16550** (n=197, 2026-09-19T04:17:47.536735Z)
- `TSDF|TOTAL|demand` = **17194** (n=197, 2026-09-19T04:17:47.536735Z)
- `WINDFOR|TOTAL|generation` = **6714** (n=33, 2026-09-19T03:30:33.519312Z)

## Latest publication events

- `2026-09-19T04:26:52.026964Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:50.745191Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:49.428281Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:48.143377Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:46.875370Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:45.564741Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:44.287628Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:42.947278Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:41.649597Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:40.112165Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:38.796931Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:37.482258Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:36.174528Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:34.905372Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:26:33.635424Z` — **MID**: 0 rows; marker `2026-09-19T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
