# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T06:07:55.133037Z`  
Current process started UTC: `2026-09-19T06:03:54.933052Z`  
1-second metadata polls in this process: **173**  
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

- `FUELINST|fuelType=INTVKL|generation` = **150** (n=1187, 2026-09-19T06:05:31.955725Z)
- `FUELINST|fuelType=NPSHYD|generation` = **351** (n=1187, 2026-09-19T06:05:31.955725Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1187, 2026-09-19T06:05:31.955725Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1187, 2026-09-19T06:05:31.955725Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1187, 2026-09-19T06:05:31.955725Z)
- `FUELINST|fuelType=OTHER|generation` = **429** (n=1187, 2026-09-19T06:05:31.955725Z)
- `FUELINST|fuelType=PS|generation` = **-543** (n=1187, 2026-09-19T06:05:31.955725Z)
- `FUELINST|fuelType=WIND|generation` = **15830** (n=1187, 2026-09-19T06:05:31.955725Z)
- `IMBALNGC|TOTAL|imbalance` = **9697** (n=196, 2026-09-19T05:50:34.942583Z)
- `INDDEM|TOTAL|demand` = **-10865** (n=196, 2026-09-19T05:50:34.942583Z)
- `INDGEN|TOTAL|generation` = **26887** (n=196, 2026-09-19T05:50:50.449260Z)
- `MELNGC|TOTAL|margin` = **38235** (n=196, 2026-09-19T05:49:46.009897Z)
- `NDF|TOTAL|demand` = **16550** (n=200, 2026-09-19T05:47:37.564895Z)
- `TSDF|TOTAL|demand` = **17190** (n=200, 2026-09-19T05:47:37.564895Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T06:07:53.830086Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:52.518747Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:51.198171Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:49.886752Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:48.551297Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:47.267355Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:45.415743Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:44.102765Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:42.814128Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:41.496206Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:40.197223Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:38.887463Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:37.544905Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:36.211343Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:07:34.882117Z` — **MID**: 0 rows; marker `2026-09-19T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
