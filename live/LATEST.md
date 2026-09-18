# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T07:35:44.223223Z`  
Current process started UTC: `2026-09-18T07:31:43.065144Z`  
1-second metadata polls in this process: **152**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=NPSHYD|generation` = **377** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=OTHER|generation` = **1492** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=PS|generation` = **599** (n=961, 2026-09-18T07:35:35.258798Z)
- `FUELINST|fuelType=WIND|generation` = **12343** (n=961, 2026-09-18T07:35:35.258798Z)
- `IMBALNGC|TOTAL|imbalance` = **10218** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDDEM|TOTAL|demand` = **-11739** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDGEN|TOTAL|generation` = **27722** (n=159, 2026-09-18T07:19:58.374346Z)
- `MELNGC|TOTAL|margin` = **37765** (n=159, 2026-09-18T07:19:09.419948Z)
- `NDF|TOTAL|demand` = **16314** (n=162, 2026-09-18T07:17:24.178373Z)
- `TSDF|TOTAL|demand` = **17504** (n=162, 2026-09-18T07:17:24.178373Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T07:35:42.742144Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:41.239418Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:39.782565Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:38.310730Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:35.258798Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:35.258798Z` — **FUELINST**: 80 rows; marker `2026-09-18T07:35:00Z`
- `2026-09-18T07:35:33.741380Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:32.308090Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:30.802554Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:29.252578Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:27.762072Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:26.228913Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:24.769165Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:22.844794Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:35:21.399245Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
