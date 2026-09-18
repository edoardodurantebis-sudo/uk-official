# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T08:56:14.870694Z`  
Current process started UTC: `2026-09-18T08:52:14.361921Z`  
1-second metadata polls in this process: **225**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=977, 2026-09-18T08:55:39.063777Z)
- `FUELINST|fuelType=NPSHYD|generation` = **360** (n=977, 2026-09-18T08:55:39.063777Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=977, 2026-09-18T08:55:39.063777Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=977, 2026-09-18T08:55:39.063777Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=977, 2026-09-18T08:55:39.063777Z)
- `FUELINST|fuelType=OTHER|generation` = **1028** (n=977, 2026-09-18T08:55:39.063777Z)
- `FUELINST|fuelType=PS|generation` = **227** (n=977, 2026-09-18T08:55:39.063777Z)
- `FUELINST|fuelType=WIND|generation` = **12193** (n=977, 2026-09-18T08:55:39.063777Z)
- `IMBALNGC|TOTAL|imbalance` = **9602** (n=161, 2026-09-18T08:50:11.206473Z)
- `INDDEM|TOTAL|demand` = **-11735** (n=161, 2026-09-18T08:50:26.889076Z)
- `INDGEN|TOTAL|generation` = **27246** (n=161, 2026-09-18T08:50:26.889076Z)
- `MELNGC|TOTAL|margin` = **37681** (n=161, 2026-09-18T08:49:38.558944Z)
- `NDF|TOTAL|demand` = **16454** (n=165, 2026-09-18T08:47:27.012958Z)
- `TSDF|TOTAL|demand` = **17644** (n=165, 2026-09-18T08:47:27.012958Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T08:56:13.862354Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:11.594387Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:11.594387Z` — **FREQ**: 5761 rows; marker `2026-09-18T08:55:45Z`
- `2026-09-18T08:56:10.571781Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:09.571049Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:08.559913Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:07.558232Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:06.544100Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:05.540679Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:04.502947Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:03.502850Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:02.445020Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:01.439135Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:56:00.403638Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:55:59.327303Z` — **MID**: 0 rows; marker `2026-09-18T08:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
