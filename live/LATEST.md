# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T18:08:04.610037Z`  
Current process started UTC: `2026-09-18T18:04:04.542495Z`  
1-second metadata polls in this process: **229**  
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

- `FUELINST|fuelType=INTVKL|generation` = **894** (n=1064, 2026-09-18T18:05:23.622475Z)
- `FUELINST|fuelType=NPSHYD|generation` = **490** (n=1064, 2026-09-18T18:05:23.622475Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1064, 2026-09-18T18:05:23.622475Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=1064, 2026-09-18T18:05:23.622475Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1064, 2026-09-18T18:05:23.622475Z)
- `FUELINST|fuelType=OTHER|generation` = **1751** (n=1064, 2026-09-18T18:05:23.622475Z)
- `FUELINST|fuelType=PS|generation` = **579** (n=1064, 2026-09-18T18:05:23.622475Z)
- `FUELINST|fuelType=WIND|generation` = **16773** (n=1064, 2026-09-18T18:05:23.622475Z)
- `IMBALNGC|TOTAL|imbalance` = **9111** (n=175, 2026-09-18T17:53:01.127856Z)
- `INDDEM|TOTAL|demand` = **-10766** (n=175, 2026-09-18T17:53:01.127856Z)
- `INDGEN|TOTAL|generation` = **26161** (n=175, 2026-09-18T17:53:01.127856Z)
- `MELNGC|TOTAL|margin` = **37647** (n=175, 2026-09-18T17:50:25.863831Z)
- `NDF|TOTAL|demand` = **16550** (n=179, 2026-09-18T17:48:14.663667Z)
- `TSDF|TOTAL|demand` = **17050** (n=179, 2026-09-18T17:48:30.574499Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T18:08:03.609400Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:08:02.609323Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:08:01.609206Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:08:00.609094Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:07:59.609012Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:07:58.608913Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:07:57.608790Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:07:56.608666Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:07:55.608546Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:07:54.608478Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:07:53.608356Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:07:52.608278Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:07:51.608155Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:07:50.608075Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:07:49.022030Z` — **MID**: 0 rows; marker `2026-09-18T17:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
