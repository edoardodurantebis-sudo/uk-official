# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T03:57:21.989482Z`  
Current process started UTC: `2026-09-19T03:53:21.908831Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-487** (n=1161, 2026-09-19T03:55:33.750114Z)
- `FUELINST|fuelType=NPSHYD|generation` = **337** (n=1161, 2026-09-19T03:55:33.750114Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1161, 2026-09-19T03:55:33.750114Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1161, 2026-09-19T03:55:33.750114Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1161, 2026-09-19T03:55:33.750114Z)
- `FUELINST|fuelType=OTHER|generation` = **384** (n=1161, 2026-09-19T03:55:33.750114Z)
- `FUELINST|fuelType=PS|generation` = **-540** (n=1161, 2026-09-19T03:55:33.750114Z)
- `FUELINST|fuelType=WIND|generation` = **15718** (n=1161, 2026-09-19T03:55:33.750114Z)
- `IMBALNGC|TOTAL|imbalance` = **9802** (n=192, 2026-09-19T03:50:47.229270Z)
- `INDDEM|TOTAL|demand` = **-10879** (n=192, 2026-09-19T03:50:47.229270Z)
- `INDGEN|TOTAL|generation` = **26996** (n=192, 2026-09-19T03:50:47.229270Z)
- `MELNGC|TOTAL|margin` = **38309** (n=192, 2026-09-19T03:49:25.726375Z)
- `NDF|TOTAL|demand` = **16550** (n=196, 2026-09-19T03:47:06.305878Z)
- `TSDF|TOTAL|demand` = **17194** (n=196, 2026-09-19T03:47:40.778261Z)
- `WINDFOR|TOTAL|generation` = **6714** (n=33, 2026-09-19T03:30:33.519312Z)

## Latest publication events

- `2026-09-19T03:57:20.659371Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:19.356302Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:18.044583Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:16.699897Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:15.309064Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:14.005824Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:12.712592Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:11.069912Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:09.739999Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:08.379241Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:07.044299Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:05.729266Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:04.363309Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:03.000916Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:57:01.692919Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
