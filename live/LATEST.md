# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T04:43:47.307821Z`  
Current process started UTC: `2026-09-19T04:39:46.228416Z`  
1-second metadata polls in this process: **175**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-578** (n=1170, 2026-09-19T04:40:33.964943Z)
- `FUELINST|fuelType=NPSHYD|generation` = **349** (n=1170, 2026-09-19T04:40:33.964943Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3344** (n=1170, 2026-09-19T04:40:33.964943Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1170, 2026-09-19T04:40:33.964943Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1170, 2026-09-19T04:40:33.964943Z)
- `FUELINST|fuelType=OTHER|generation` = **262** (n=1170, 2026-09-19T04:40:33.964943Z)
- `FUELINST|fuelType=PS|generation` = **-547** (n=1170, 2026-09-19T04:40:33.964943Z)
- `FUELINST|fuelType=WIND|generation` = **16110** (n=1170, 2026-09-19T04:40:33.964943Z)
- `IMBALNGC|TOTAL|imbalance` = **9764** (n=193, 2026-09-19T04:20:34.678100Z)
- `INDDEM|TOTAL|demand` = **-10869** (n=193, 2026-09-19T04:20:34.678100Z)
- `INDGEN|TOTAL|generation` = **26959** (n=193, 2026-09-19T04:20:34.678100Z)
- `MELNGC|TOTAL|margin` = **38315** (n=193, 2026-09-19T04:19:30.729668Z)
- `NDF|TOTAL|demand` = **16550** (n=197, 2026-09-19T04:17:47.536735Z)
- `TSDF|TOTAL|demand` = **17194** (n=197, 2026-09-19T04:17:47.536735Z)
- `WINDFOR|TOTAL|generation` = **6714** (n=33, 2026-09-19T03:30:33.519312Z)

## Latest publication events

- `2026-09-19T04:43:46.050604Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:44.731668Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:43.396388Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:42.158984Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:40.844948Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:39.544066Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:38.278751Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:36.946706Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:35.357316Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:34.047633Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:32.735569Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:31.448030Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:30.111416Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:28.811681Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T04:43:27.514645Z` — **MID**: 0 rows; marker `2026-09-19T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
