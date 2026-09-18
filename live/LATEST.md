# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T05:21:11.693642Z`  
Current process started UTC: `2026-09-18T05:17:10.915402Z`  
1-second metadata polls in this process: **224**  
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

- `2026-09-18T05:21:10.726343Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:21:09.362688Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:21:08.362608Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:21:07.308650Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:21:06.308559Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:21:05.308464Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:21:04.308386Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:21:03.261766Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:21:02.261685Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:21:01.261606Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:21:00.261489Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:20:59.261418Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:20:58.261303Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:20:57.261220Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:20:56.261100Z` — **MID**: 0 rows; marker `2026-09-18T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
