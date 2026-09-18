# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T10:25:17.081263Z`  
Current process started UTC: `2026-09-18T10:21:15.880456Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=994, 2026-09-18T10:20:40.595659Z)
- `FUELINST|fuelType=NPSHYD|generation` = **316** (n=994, 2026-09-18T10:20:40.595659Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=994, 2026-09-18T10:20:40.595659Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=994, 2026-09-18T10:20:40.595659Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=994, 2026-09-18T10:20:40.595659Z)
- `FUELINST|fuelType=OTHER|generation` = **613** (n=994, 2026-09-18T10:20:40.595659Z)
- `FUELINST|fuelType=PS|generation` = **-721** (n=994, 2026-09-18T10:20:40.595659Z)
- `FUELINST|fuelType=WIND|generation` = **11996** (n=994, 2026-09-18T10:20:40.595659Z)
- `IMBALNGC|TOTAL|imbalance` = **7078** (n=164, 2026-09-18T10:19:52.073787Z)
- `INDDEM|TOTAL|demand` = **-13796** (n=164, 2026-09-18T10:19:35.912100Z)
- `INDGEN|TOTAL|generation` = **26759** (n=164, 2026-09-18T10:19:35.912100Z)
- `MELNGC|TOTAL|margin` = **36353** (n=164, 2026-09-18T10:19:03.231158Z)
- `NDF|TOTAL|demand` = **16454** (n=168, 2026-09-18T10:17:07.629865Z)
- `TSDF|TOTAL|demand` = **19681** (n=168, 2026-09-18T10:17:07.629865Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T10:25:15.868558Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:14.632121Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:13.430414Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:12.250687Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:11.045700Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:09.837717Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:08.627526Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:07.415883Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:05.344979Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:04.135346Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:02.946873Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:01.711829Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:25:00.486019Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:24:59.303957Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:24:58.079883Z` — **MID**: 0 rows; marker `2026-09-18T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
