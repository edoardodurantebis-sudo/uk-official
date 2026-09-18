# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T09:04:44.859396Z`  
Current process started UTC: `2026-09-18T09:00:44.030944Z`  
1-second metadata polls in this process: **221**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=978, 2026-09-18T09:00:44.030953Z)
- `FUELINST|fuelType=NPSHYD|generation` = **357** (n=978, 2026-09-18T09:00:44.030953Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=978, 2026-09-18T09:00:44.030953Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=978, 2026-09-18T09:00:44.030953Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=978, 2026-09-18T09:00:44.030953Z)
- `FUELINST|fuelType=OTHER|generation` = **960** (n=978, 2026-09-18T09:00:44.030953Z)
- `FUELINST|fuelType=PS|generation` = **224** (n=978, 2026-09-18T09:00:44.030953Z)
- `FUELINST|fuelType=WIND|generation` = **12028** (n=978, 2026-09-18T09:00:44.030953Z)
- `IMBALNGC|TOTAL|imbalance` = **9602** (n=161, 2026-09-18T08:50:11.206473Z)
- `INDDEM|TOTAL|demand` = **-11735** (n=161, 2026-09-18T08:50:26.889076Z)
- `INDGEN|TOTAL|generation` = **27246** (n=161, 2026-09-18T08:50:26.889076Z)
- `MELNGC|TOTAL|margin` = **37681** (n=161, 2026-09-18T08:49:38.558944Z)
- `NDF|TOTAL|demand` = **16454** (n=165, 2026-09-18T08:47:27.012958Z)
- `TSDF|TOTAL|demand` = **17644** (n=165, 2026-09-18T08:47:27.012958Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T09:04:43.861485Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:42.861407Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:41.861311Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:40.861244Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:39.861128Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:38.861041Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:37.796735Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:36.796668Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:35.796586Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:34.796507Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:33.796439Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:30.917341Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:29.917256Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:28.917187Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:04:27.917104Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
