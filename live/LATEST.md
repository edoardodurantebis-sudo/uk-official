# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T19:48:25.627737Z`  
Current process started UTC: `2026-09-17T19:44:25.005412Z`  
1-second metadata polls in this process: **215**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=-2, z=4.17 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1407** (n=819, 2026-09-17T19:45:31.625155Z)
- `FUELINST|fuelType=NPSHYD|generation` = **592** (n=819, 2026-09-17T19:45:31.625155Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=819, 2026-09-17T19:45:31.625155Z)
- `FUELINST|fuelType=OCGT|generation` = **79** (n=819, 2026-09-17T19:45:31.625155Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=819, 2026-09-17T19:45:31.625155Z)
- `FUELINST|fuelType=OTHER|generation` = **352** (n=819, 2026-09-17T19:45:31.625155Z)
- `FUELINST|fuelType=PS|generation` = **501** (n=819, 2026-09-17T19:45:31.625155Z)
- `FUELINST|fuelType=WIND|generation` = **16009** (n=819, 2026-09-17T19:45:31.625155Z)
- `IMBALNGC|TOTAL|imbalance` = **9684** (n=135, 2026-09-17T19:23:43.864314Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=135, 2026-09-17T19:23:43.864314Z)
- `INDGEN|TOTAL|generation` = **26498** (n=135, 2026-09-17T19:23:43.864314Z)
- `MELNGC|TOTAL|margin` = **36493** (n=135, 2026-09-17T19:20:53.732823Z)
- `NDF|TOTAL|demand` = **16314** (n=139, 2026-09-17T19:48:10.710850Z)
- `TSDF|TOTAL|demand` = **16814** (n=139, 2026-09-17T19:48:10.710850Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T19:48:24.674785Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:23.674661Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:22.674566Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:21.674429Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:20.674290Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:19.674192Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:18.657872Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:17.657739Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:16.657603Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:15.657450Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:14.657315Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:13.376361Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:10.710850Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:48:10.710850Z` — **TSDF**: 1152 rows; marker `2026-09-17T19:47:00Z`
- `2026-09-17T19:48:10.710850Z` — **NDF**: 64 rows; marker `2026-09-17T19:47:00Z`
