# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T23:52:06.401880Z`  
Current process started UTC: `2026-09-17T23:48:05.570308Z`  
1-second metadata polls in this process: **182**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **608** (n=868, 2026-09-17T23:50:34.020814Z)
- `FUELINST|fuelType=NPSHYD|generation` = **452** (n=868, 2026-09-17T23:50:34.020814Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3319** (n=868, 2026-09-17T23:50:34.020814Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=868, 2026-09-17T23:50:34.020814Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=868, 2026-09-17T23:50:34.020814Z)
- `FUELINST|fuelType=OTHER|generation` = **500** (n=868, 2026-09-17T23:50:34.020814Z)
- `FUELINST|fuelType=PS|generation` = **55** (n=868, 2026-09-17T23:50:34.020814Z)
- `FUELINST|fuelType=WIND|generation` = **14365** (n=868, 2026-09-17T23:50:34.020814Z)
- `IMBALNGC|TOTAL|imbalance` = **9745** (n=143, 2026-09-17T23:22:08.151476Z)
- `INDDEM|TOTAL|demand` = **-11183** (n=143, 2026-09-17T23:22:08.151476Z)
- `INDGEN|TOTAL|generation` = **26559** (n=143, 2026-09-17T23:22:08.151476Z)
- `MELNGC|TOTAL|margin` = **36515** (n=144, 2026-09-17T23:50:34.020814Z)
- `NDF|TOTAL|demand` = **16314** (n=147, 2026-09-17T23:48:05.570317Z)
- `TSDF|TOTAL|demand` = **16814** (n=147, 2026-09-17T23:48:22.184365Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-17T23:52:05.140109Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:52:03.934773Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:52:02.741102Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:52:01.546698Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:52:00.363953Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:51:59.168755Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:51:57.962860Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:51:56.265033Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:51:54.996117Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:51:53.787455Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:51:52.567471Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:51:51.368705Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:51:50.151380Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:51:48.854960Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:51:47.671980Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
