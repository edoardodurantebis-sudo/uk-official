# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T00:52:13.481035Z`  
Current process started UTC: `2026-09-19T00:48:12.346565Z`  
1-second metadata polls in this process: **172**  
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

- `FUELINST|fuelType=INTVKL|generation` = **126** (n=1124, 2026-09-19T00:50:37.533840Z)
- `FUELINST|fuelType=NPSHYD|generation` = **385** (n=1124, 2026-09-19T00:50:37.533840Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1124, 2026-09-19T00:50:37.533840Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1124, 2026-09-19T00:50:37.533840Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1124, 2026-09-19T00:50:37.533840Z)
- `FUELINST|fuelType=OTHER|generation` = **336** (n=1124, 2026-09-19T00:50:37.533840Z)
- `FUELINST|fuelType=PS|generation` = **-829** (n=1124, 2026-09-19T00:50:37.533840Z)
- `FUELINST|fuelType=WIND|generation` = **16366** (n=1124, 2026-09-19T00:50:37.533840Z)
- `IMBALNGC|TOTAL|imbalance` = **9233** (n=186, 2026-09-19T00:51:26.752169Z)
- `INDDEM|TOTAL|demand` = **-10886** (n=186, 2026-09-19T00:51:26.752169Z)
- `INDGEN|TOTAL|generation` = **26428** (n=186, 2026-09-19T00:51:26.752169Z)
- `MELNGC|TOTAL|margin` = **37127** (n=186, 2026-09-19T00:49:33.266630Z)
- `NDF|TOTAL|demand` = **16550** (n=190, 2026-09-19T00:47:37.549406Z)
- `TSDF|TOTAL|demand` = **17194** (n=190, 2026-09-19T00:47:37.549406Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-19T00:52:12.183656Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:52:10.866327Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:52:09.535677Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:52:08.157264Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:52:06.881696Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:52:05.635158Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:52:04.279050Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:52:02.963451Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:52:01.630053Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:51:59.813983Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:51:58.519733Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:51:57.234309Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:51:55.948249Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:51:54.621838Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T00:51:53.313347Z` — **MID**: 0 rows; marker `2026-09-19T00:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
