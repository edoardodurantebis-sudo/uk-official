# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T19:27:27.223469Z`  
Current process started UTC: `2026-09-17T19:23:27.020471Z`  
1-second metadata polls in this process: **229**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=-2, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=81, delta=-2, z=4.34 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=82, delta=45, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.58 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1407** (n=815, 2026-09-17T19:25:37.748790Z)
- `FUELINST|fuelType=NPSHYD|generation` = **633** (n=815, 2026-09-17T19:25:37.748790Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=815, 2026-09-17T19:25:37.748790Z)
- `FUELINST|fuelType=OCGT|generation` = **118** (n=815, 2026-09-17T19:25:37.748790Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=815, 2026-09-17T19:25:37.748790Z)
- `FUELINST|fuelType=OTHER|generation` = **679** (n=815, 2026-09-17T19:25:37.748790Z)
- `FUELINST|fuelType=PS|generation` = **426** (n=815, 2026-09-17T19:25:37.748790Z)
- `FUELINST|fuelType=WIND|generation` = **15465** (n=815, 2026-09-17T19:25:37.748790Z)
- `IMBALNGC|TOTAL|imbalance` = **9684** (n=135, 2026-09-17T19:23:43.864314Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=135, 2026-09-17T19:23:43.864314Z)
- `INDGEN|TOTAL|generation` = **26498** (n=135, 2026-09-17T19:23:43.864314Z)
- `MELNGC|TOTAL|margin` = **36493** (n=135, 2026-09-17T19:20:53.732823Z)
- `NDF|TOTAL|demand` = **16314** (n=138, 2026-09-17T19:18:38.940808Z)
- `TSDF|TOTAL|demand` = **16814** (n=138, 2026-09-17T19:18:38.940808Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T19:27:26.275468Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:25.275355Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:24.275241Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:23.275124Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:22.275013Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:21.274895Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:20.274827Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:19.274713Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:18.274596Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:17.274487Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:16.274365Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:15.274250Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:13.976932Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:12.976826Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:27:11.976710Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
