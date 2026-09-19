# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T01:17:31.020880Z`  
Current process started UTC: `2026-09-19T01:13:30.762918Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-604** (n=1129, 2026-09-19T01:15:41.054730Z)
- `FUELINST|fuelType=NPSHYD|generation` = **371** (n=1129, 2026-09-19T01:15:41.054730Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1129, 2026-09-19T01:15:41.054730Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1129, 2026-09-19T01:15:41.054730Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1129, 2026-09-19T01:15:41.054730Z)
- `FUELINST|fuelType=OTHER|generation` = **296** (n=1129, 2026-09-19T01:15:41.054730Z)
- `FUELINST|fuelType=PS|generation` = **-832** (n=1129, 2026-09-19T01:15:41.054730Z)
- `FUELINST|fuelType=WIND|generation` = **16311** (n=1129, 2026-09-19T01:15:41.054730Z)
- `IMBALNGC|TOTAL|imbalance` = **9233** (n=186, 2026-09-19T00:51:26.752169Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=186, 2026-09-19T00:51:26.752169Z)
- `INDGEN|TOTAL|generation` = **26428** (n=186, 2026-09-19T00:51:26.752169Z)
- `MELNGC|TOTAL|margin` = **37127** (n=186, 2026-09-19T00:49:33.266630Z)
- `NDF|TOTAL|demand` = **16550** (n=190, 2026-09-19T00:47:37.549406Z)
- `TSDF|TOTAL|demand` = **17194** (n=190, 2026-09-19T00:47:37.549406Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T01:17:30.067576Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:29.067457Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:27.855911Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:26.651085Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:25.650972Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:24.650892Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:23.650773Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:22.650695Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:21.650571Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:20.650453Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:19.650342Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:18.650233Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:17.650152Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:16.303580Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T01:17:15.303500Z` — **MID**: 0 rows; marker `2026-09-19T01:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
