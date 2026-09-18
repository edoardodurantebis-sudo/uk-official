# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T08:22:03.401686Z`  
Current process started UTC: `2026-09-18T08:18:02.594029Z`  
1-second metadata polls in this process: **136**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=970, 2026-09-18T08:20:46.536994Z)
- `FUELINST|fuelType=NPSHYD|generation` = **377** (n=970, 2026-09-18T08:20:46.536994Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=970, 2026-09-18T08:20:46.536994Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=970, 2026-09-18T08:20:46.536994Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=970, 2026-09-18T08:20:46.536994Z)
- `FUELINST|fuelType=OTHER|generation` = **1655** (n=970, 2026-09-18T08:20:46.536994Z)
- `FUELINST|fuelType=PS|generation` = **544** (n=970, 2026-09-18T08:20:46.536994Z)
- `FUELINST|fuelType=WIND|generation` = **12305** (n=970, 2026-09-18T08:20:46.536994Z)
- `IMBALNGC|TOTAL|imbalance` = **9625** (n=160, 2026-09-18T08:20:46.536994Z)
- `INDDEM|TOTAL|demand` = **-11736** (n=160, 2026-09-18T08:20:29.773738Z)
- `INDGEN|TOTAL|generation` = **27269** (n=160, 2026-09-18T08:20:29.773738Z)
- `MELNGC|TOTAL|margin` = **37653** (n=160, 2026-09-18T08:19:40.681819Z)
- `NDF|TOTAL|demand` = **16454** (n=164, 2026-09-18T08:17:38.545846Z)
- `TSDF|TOTAL|demand` = **17644** (n=164, 2026-09-18T08:17:38.545846Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T08:22:01.786479Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:22:00.146404Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:58.503235Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:56.905072Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:55.354491Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:53.413544Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:51.806743Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:50.260281Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:48.736873Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:47.190903Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:45.559946Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:43.733336Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:42.122061Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:40.546637Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:21:38.958518Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
