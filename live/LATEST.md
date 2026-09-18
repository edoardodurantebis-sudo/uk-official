# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T10:12:40.576735Z`  
Current process started UTC: `2026-09-18T10:08:39.471811Z`  
1-second metadata polls in this process: **171**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=992, 2026-09-18T10:10:36.069743Z)
- `FUELINST|fuelType=NPSHYD|generation` = **316** (n=992, 2026-09-18T10:10:36.069743Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=992, 2026-09-18T10:10:36.069743Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=992, 2026-09-18T10:10:36.069743Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=992, 2026-09-18T10:10:36.069743Z)
- `FUELINST|fuelType=OTHER|generation` = **793** (n=992, 2026-09-18T10:10:36.069743Z)
- `FUELINST|fuelType=PS|generation` = **-718** (n=992, 2026-09-18T10:10:36.069743Z)
- `FUELINST|fuelType=WIND|generation` = **11704** (n=992, 2026-09-18T10:10:36.069743Z)
- `IMBALNGC|TOTAL|imbalance` = **7801** (n=163, 2026-09-18T09:49:53.694216Z)
- `INDDEM|TOTAL|demand` = **-13189** (n=163, 2026-09-18T09:49:53.694216Z)
- `INDGEN|TOTAL|generation` = **26894** (n=163, 2026-09-18T09:49:53.694216Z)
- `MELNGC|TOTAL|margin` = **36164** (n=163, 2026-09-18T09:49:19.963149Z)
- `NDF|TOTAL|demand` = **16454** (n=167, 2026-09-18T09:47:20.937653Z)
- `TSDF|TOTAL|demand` = **19093** (n=167, 2026-09-18T09:47:20.937653Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T10:12:39.235988Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:37.919980Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:36.595350Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:35.247423Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:33.928101Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:32.558571Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:30.709696Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:29.330190Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:27.983697Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:26.598458Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:25.299416Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:23.923923Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:22.554837Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:21.237536Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:12:19.850301Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
