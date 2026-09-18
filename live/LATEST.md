# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T10:37:49.784795Z`  
Current process started UTC: `2026-09-18T10:33:49.569175Z`  
1-second metadata polls in this process: **189**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=997, 2026-09-18T10:35:26.440348Z)
- `FUELINST|fuelType=NPSHYD|generation` = **328** (n=997, 2026-09-18T10:35:26.440348Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=997, 2026-09-18T10:35:26.440348Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=997, 2026-09-18T10:35:26.440348Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=997, 2026-09-18T10:35:26.440348Z)
- `FUELINST|fuelType=OTHER|generation` = **818** (n=997, 2026-09-18T10:35:26.440348Z)
- `FUELINST|fuelType=PS|generation` = **-721** (n=997, 2026-09-18T10:35:26.440348Z)
- `FUELINST|fuelType=WIND|generation` = **12212** (n=997, 2026-09-18T10:35:26.440348Z)
- `IMBALNGC|TOTAL|imbalance` = **7078** (n=164, 2026-09-18T10:19:52.073787Z)
- `INDDEM|TOTAL|demand` = **-13796** (n=164, 2026-09-18T10:19:35.912100Z)
- `INDGEN|TOTAL|generation` = **26759** (n=164, 2026-09-18T10:19:35.912100Z)
- `MELNGC|TOTAL|margin` = **36353** (n=164, 2026-09-18T10:19:03.231158Z)
- `NDF|TOTAL|demand` = **16454** (n=168, 2026-09-18T10:17:07.629865Z)
- `TSDF|TOTAL|demand` = **19681** (n=168, 2026-09-18T10:17:07.629865Z)
- `WINDFOR|TOTAL|generation` = **7615** (n=29, 2026-09-18T10:30:46.506872Z)

## Latest publication events

- `2026-09-18T10:37:48.597713Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:47.329273Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:46.142204Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:44.823284Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:43.640925Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:42.463014Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:41.263660Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:40.055289Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:38.865186Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:37.698259Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:36.000732Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:34.805555Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:33.573736Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:32.362215Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:37:31.153645Z` — **MID**: 0 rows; marker `2026-09-18T10:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
