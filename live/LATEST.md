# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T05:25:22.973436Z`  
Current process started UTC: `2026-09-18T05:21:21.682123Z`  
1-second metadata polls in this process: **145**  
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

- `FUELINST|fuelType=INTVKL|generation` = **954** (n=934, 2026-09-18T05:20:37.336134Z)
- `FUELINST|fuelType=NPSHYD|generation` = **475** (n=934, 2026-09-18T05:20:37.336134Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=934, 2026-09-18T05:20:37.336134Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=934, 2026-09-18T05:20:37.336134Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=934, 2026-09-18T05:20:37.336134Z)
- `FUELINST|fuelType=OTHER|generation` = **374** (n=934, 2026-09-18T05:20:37.336134Z)
- `FUELINST|fuelType=PS|generation` = **528** (n=934, 2026-09-18T05:20:37.336134Z)
- `FUELINST|fuelType=WIND|generation` = **13589** (n=934, 2026-09-18T05:20:37.336134Z)
- `IMBALNGC|TOTAL|imbalance` = **10704** (n=155, 2026-09-18T05:20:21.081324Z)
- `INDDEM|TOTAL|demand` = **-11169** (n=155, 2026-09-18T05:20:21.081324Z)
- `INDGEN|TOTAL|generation` = **27518** (n=155, 2026-09-18T05:20:21.081324Z)
- `MELNGC|TOTAL|margin` = **38019** (n=155, 2026-09-18T05:19:16.747972Z)
- `NDF|TOTAL|demand` = **16314** (n=158, 2026-09-18T05:17:26.772425Z)
- `TSDF|TOTAL|demand` = **16814** (n=158, 2026-09-18T05:17:26.772425Z)
- `WINDFOR|TOTAL|generation` = **7845** (n=26, 2026-09-18T03:30:37.036559Z)

## Latest publication events

- `2026-09-18T05:25:21.374215Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:19.824695Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:18.263865Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:16.695600Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:14.624624Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:13.053311Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:11.444740Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:09.817903Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:08.240488Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:06.704961Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:05.123603Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:03.589543Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:02.014441Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:25:00.389303Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:24:58.174849Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
