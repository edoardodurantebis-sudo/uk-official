# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T19:40:05.246865Z`  
Current process started UTC: `2026-09-17T19:36:05.186345Z`  
1-second metadata polls in this process: **228**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=81, delta=-2, z=4.34 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1407** (n=817, 2026-09-17T19:35:25.100077Z)
- `FUELINST|fuelType=NPSHYD|generation` = **613** (n=817, 2026-09-17T19:35:25.100077Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=817, 2026-09-17T19:35:25.100077Z)
- `FUELINST|fuelType=OCGT|generation` = **118** (n=817, 2026-09-17T19:35:25.100077Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=817, 2026-09-17T19:35:25.100077Z)
- `FUELINST|fuelType=OTHER|generation` = **389** (n=817, 2026-09-17T19:35:25.100077Z)
- `FUELINST|fuelType=PS|generation` = **480** (n=817, 2026-09-17T19:35:25.100077Z)
- `FUELINST|fuelType=WIND|generation` = **15755** (n=817, 2026-09-17T19:35:25.100077Z)
- `IMBALNGC|TOTAL|imbalance` = **9684** (n=135, 2026-09-17T19:23:43.864314Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=135, 2026-09-17T19:23:43.864314Z)
- `INDGEN|TOTAL|generation` = **26498** (n=135, 2026-09-17T19:23:43.864314Z)
- `MELNGC|TOTAL|margin` = **36493** (n=135, 2026-09-17T19:20:53.732823Z)
- `NDF|TOTAL|demand` = **16314** (n=138, 2026-09-17T19:18:38.940808Z)
- `TSDF|TOTAL|demand` = **16814** (n=138, 2026-09-17T19:18:38.940808Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T19:40:04.201609Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:40:03.191380Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:40:02.187455Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:40:01.144009Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:39:59.693180Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:39:58.678329Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:39:57.657718Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:39:56.657648Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:39:55.657574Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:39:54.654877Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:39:53.628446Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:39:52.628357Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:39:51.596268Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:39:50.569497Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:39:49.525161Z` — **MID**: 0 rows; marker `2026-09-17T19:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
