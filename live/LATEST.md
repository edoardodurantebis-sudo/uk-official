# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T05:33:49.244427Z`  
Current process started UTC: `2026-09-18T05:29:48.407712Z`  
1-second metadata polls in this process: **130**  
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

- `FUELINST|fuelType=INTVKL|generation` = **954** (n=936, 2026-09-18T05:30:21.577972Z)
- `FUELINST|fuelType=NPSHYD|generation` = **478** (n=936, 2026-09-18T05:30:21.577972Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=936, 2026-09-18T05:30:21.577972Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=936, 2026-09-18T05:30:21.577972Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=936, 2026-09-18T05:30:21.577972Z)
- `FUELINST|fuelType=OTHER|generation` = **332** (n=936, 2026-09-18T05:30:21.577972Z)
- `FUELINST|fuelType=PS|generation` = **490** (n=936, 2026-09-18T05:30:21.577972Z)
- `FUELINST|fuelType=WIND|generation` = **13707** (n=936, 2026-09-18T05:30:21.577972Z)
- `IMBALNGC|TOTAL|imbalance` = **10704** (n=155, 2026-09-18T05:20:21.081324Z)
- `INDDEM|TOTAL|demand` = **-11169** (n=155, 2026-09-18T05:20:21.081324Z)
- `INDGEN|TOTAL|generation` = **27518** (n=155, 2026-09-18T05:20:21.081324Z)
- `MELNGC|TOTAL|margin` = **38019** (n=155, 2026-09-18T05:19:16.747972Z)
- `NDF|TOTAL|demand` = **16314** (n=158, 2026-09-18T05:17:26.772425Z)
- `TSDF|TOTAL|demand` = **16814** (n=158, 2026-09-18T05:17:26.772425Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T05:33:47.540598Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:45.830833Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:44.112265Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:42.382937Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:40.671460Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:38.960448Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:36.881056Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:35.169011Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:33.421038Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:31.681402Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:29.972485Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:28.244044Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:26.529850Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:24.823663Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:33:23.125091Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
