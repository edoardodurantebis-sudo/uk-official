# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T01:09:07.683338Z`  
Current process started UTC: `2026-09-19T01:05:07.544767Z`  
1-second metadata polls in this process: **186**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-416** (n=1127, 2026-09-19T01:05:40.585603Z)
- `FUELINST|fuelType=NPSHYD|generation` = **378** (n=1127, 2026-09-19T01:05:40.585603Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1127, 2026-09-19T01:05:40.585603Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1127, 2026-09-19T01:05:40.585603Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1127, 2026-09-19T01:05:40.585603Z)
- `FUELINST|fuelType=OTHER|generation` = **311** (n=1127, 2026-09-19T01:05:40.585603Z)
- `FUELINST|fuelType=PS|generation` = **-832** (n=1127, 2026-09-19T01:05:40.585603Z)
- `FUELINST|fuelType=WIND|generation` = **16463** (n=1127, 2026-09-19T01:05:40.585603Z)
- `IMBALNGC|TOTAL|imbalance` = **9233** (n=186, 2026-09-19T00:51:26.752169Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=186, 2026-09-19T00:51:26.752169Z)
- `INDGEN|TOTAL|generation` = **26428** (n=186, 2026-09-19T00:51:26.752169Z)
- `MELNGC|TOTAL|margin` = **37127** (n=186, 2026-09-19T00:49:33.266630Z)
- `NDF|TOTAL|demand` = **16550** (n=190, 2026-09-19T00:47:37.549406Z)
- `TSDF|TOTAL|demand` = **17194** (n=190, 2026-09-19T00:47:37.549406Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T01:09:06.684647Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:09:05.446529Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:09:03.825966Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:09:02.825880Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:09:01.819805Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:09:00.819718Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:08:59.819620Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:08:58.051621Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:08:55.450255Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:08:54.450174Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:08:53.450102Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:08:52.450016Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:08:51.079084Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:08:49.732759Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:08:48.682329Z` — **MID**: 0 rows; marker `2026-09-19T01:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
