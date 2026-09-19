# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T02:07:57.986382Z`  
Current process started UTC: `2026-09-19T02:03:57.740201Z`  
1-second metadata polls in this process: **139**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-534** (n=1139, 2026-09-19T02:05:39.449255Z)
- `FUELINST|fuelType=NPSHYD|generation` = **354** (n=1139, 2026-09-19T02:05:39.449255Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1139, 2026-09-19T02:05:39.449255Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1139, 2026-09-19T02:05:39.449255Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1139, 2026-09-19T02:05:39.449255Z)
- `FUELINST|fuelType=OTHER|generation` = **406** (n=1139, 2026-09-19T02:05:39.449255Z)
- `FUELINST|fuelType=PS|generation` = **-753** (n=1139, 2026-09-19T02:05:39.449255Z)
- `FUELINST|fuelType=WIND|generation` = **16334** (n=1139, 2026-09-19T02:05:39.449255Z)
- `IMBALNGC|TOTAL|imbalance` = **9241** (n=188, 2026-09-19T01:51:39.036034Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=188, 2026-09-19T01:51:39.036034Z)
- `INDGEN|TOTAL|generation` = **26435** (n=188, 2026-09-19T01:51:39.036034Z)
- `MELNGC|TOTAL|margin` = **37111** (n=188, 2026-09-19T01:49:54.147817Z)
- `NDF|TOTAL|demand` = **16550** (n=192, 2026-09-19T01:47:41.604873Z)
- `TSDF|TOTAL|demand` = **17194** (n=192, 2026-09-19T01:47:41.604873Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T02:07:56.391609Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:54.809971Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:52.549528Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:50.978113Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:49.357593Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:47.811262Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:46.106656Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:44.539323Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:42.978015Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:41.294477Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:39.709604Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:38.158423Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:36.241216Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:34.676124Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T02:07:33.083771Z` — **MID**: 0 rows; marker `2026-09-19T02:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
