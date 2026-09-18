# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T09:17:23.455550Z`  
Current process started UTC: `2026-09-18T09:13:21.406422Z`  
1-second metadata polls in this process: **223**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=981, 2026-09-18T09:15:29.362805Z)
- `FUELINST|fuelType=NPSHYD|generation` = **347** (n=981, 2026-09-18T09:15:29.362805Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=981, 2026-09-18T09:15:29.362805Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=981, 2026-09-18T09:15:29.362805Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=981, 2026-09-18T09:15:29.362805Z)
- `FUELINST|fuelType=OTHER|generation` = **810** (n=981, 2026-09-18T09:15:29.362805Z)
- `FUELINST|fuelType=PS|generation` = **-244** (n=981, 2026-09-18T09:15:29.362805Z)
- `FUELINST|fuelType=WIND|generation` = **11669** (n=981, 2026-09-18T09:15:29.362805Z)
- `IMBALNGC|TOTAL|imbalance` = **9602** (n=161, 2026-09-18T08:50:11.206473Z)
- `INDDEM|TOTAL|demand` = **-11735** (n=161, 2026-09-18T08:50:26.889076Z)
- `INDGEN|TOTAL|generation` = **27246** (n=161, 2026-09-18T08:50:26.889076Z)
- `MELNGC|TOTAL|margin` = **37681** (n=161, 2026-09-18T08:49:38.558944Z)
- `NDF|TOTAL|demand` = **16454** (n=166, 2026-09-18T09:17:04.819417Z)
- `TSDF|TOTAL|demand` = **19093** (n=166, 2026-09-18T09:17:21.227303Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T09:17:21.227303Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:21.227303Z` — **TSDF**: 666 rows; marker `2026-09-18T09:16:00Z`
- `2026-09-18T09:17:19.975390Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:18.719954Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:17.643327Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:16.643220Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:15.643102Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:14.643001Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:13.550698Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:12.419371Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:11.419257Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:10.386801Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:09.386684Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:08.128145Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:17:06.940174Z` — **MID**: 0 rows; marker `2026-09-18T09:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
