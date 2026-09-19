# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T04:39:35.413922Z`  
Current process started UTC: `2026-09-19T04:35:34.591553Z`  
1-second metadata polls in this process: **225**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-578** (n=1169, 2026-09-19T04:35:34.591562Z)
- `FUELINST|fuelType=NPSHYD|generation` = **350** (n=1169, 2026-09-19T04:35:34.591562Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3340** (n=1169, 2026-09-19T04:35:34.591562Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1169, 2026-09-19T04:35:34.591562Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1169, 2026-09-19T04:35:34.591562Z)
- `FUELINST|fuelType=OTHER|generation` = **225** (n=1169, 2026-09-19T04:35:34.591562Z)
- `FUELINST|fuelType=PS|generation` = **-547** (n=1169, 2026-09-19T04:35:34.591562Z)
- `FUELINST|fuelType=WIND|generation` = **16127** (n=1169, 2026-09-19T04:35:34.591562Z)
- `IMBALNGC|TOTAL|imbalance` = **9764** (n=193, 2026-09-19T04:20:34.678100Z)
- `INDDEM|TOTAL|demand` = **-10869** (n=193, 2026-09-19T04:20:34.678100Z)
- `INDGEN|TOTAL|generation` = **26959** (n=193, 2026-09-19T04:20:34.678100Z)
- `MELNGC|TOTAL|margin` = **38315** (n=193, 2026-09-19T04:19:30.729668Z)
- `NDF|TOTAL|demand` = **16550** (n=197, 2026-09-19T04:17:47.536735Z)
- `TSDF|TOTAL|demand` = **17194** (n=197, 2026-09-19T04:17:47.536735Z)
- `WINDFOR|TOTAL|generation` = **6714** (n=33, 2026-09-19T03:30:33.519312Z)

## Latest publication events

- `2026-09-19T04:39:34.474292Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:33.474171Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:32.474056Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:31.473940Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:30.473824Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:29.473748Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:28.473621Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:27.473532Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:26.473431Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:25.070399Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:24.070283Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:23.070173Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:22.070061Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:21.069977Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:39:20.069857Z` — **MID**: 0 rows; marker `2026-09-19T04:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
