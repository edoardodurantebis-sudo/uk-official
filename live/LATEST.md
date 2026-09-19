# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T05:42:43.536055Z`  
Current process started UTC: `2026-09-19T05:38:42.159092Z`  
1-second metadata polls in this process: **145**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-454** (n=1182, 2026-09-19T05:40:38.548827Z)
- `FUELINST|fuelType=NPSHYD|generation` = **373** (n=1182, 2026-09-19T05:40:38.548827Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1182, 2026-09-19T05:40:38.548827Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1182, 2026-09-19T05:40:38.548827Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1182, 2026-09-19T05:40:38.548827Z)
- `FUELINST|fuelType=OTHER|generation` = **1002** (n=1182, 2026-09-19T05:40:38.548827Z)
- `FUELINST|fuelType=PS|generation` = **-539** (n=1182, 2026-09-19T05:40:38.548827Z)
- `FUELINST|fuelType=WIND|generation` = **15792** (n=1182, 2026-09-19T05:40:38.548827Z)
- `IMBALNGC|TOTAL|imbalance` = **9712** (n=195, 2026-09-19T05:21:11.032937Z)
- `INDDEM|TOTAL|demand` = **-10865** (n=195, 2026-09-19T05:21:11.032937Z)
- `INDGEN|TOTAL|generation` = **26901** (n=195, 2026-09-19T05:21:11.032937Z)
- `MELNGC|TOTAL|margin` = **38254** (n=195, 2026-09-19T05:19:51.225658Z)
- `NDF|TOTAL|demand` = **16550** (n=199, 2026-09-19T05:17:24.210800Z)
- `TSDF|TOTAL|demand` = **17190** (n=199, 2026-09-19T05:17:24.210800Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T05:42:41.967440Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:40.421707Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:38.840021Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:37.298232Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:35.704283Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:34.139870Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:32.541663Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:30.473029Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:28.911388Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:27.335195Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:25.734176Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:24.210472Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:22.655669Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:21.121427Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:42:19.579273Z` — **MID**: 0 rows; marker `2026-09-19T05:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
