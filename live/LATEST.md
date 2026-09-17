# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T22:11:14.460766Z`  
Current process started UTC: `2026-09-17T22:07:14.449805Z`  
1-second metadata polls in this process: **131**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **343** (n=848, 2026-09-17T22:10:26.263364Z)
- `FUELINST|fuelType=NPSHYD|generation` = **453** (n=848, 2026-09-17T22:10:26.263364Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=848, 2026-09-17T22:10:26.263364Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=848, 2026-09-17T22:10:26.263364Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=848, 2026-09-17T22:10:26.263364Z)
- `FUELINST|fuelType=OTHER|generation` = **1429** (n=848, 2026-09-17T22:10:26.263364Z)
- `FUELINST|fuelType=PS|generation` = **-254** (n=848, 2026-09-17T22:10:26.263364Z)
- `FUELINST|fuelType=WIND|generation` = **14932** (n=848, 2026-09-17T22:10:26.263364Z)
- `IMBALNGC|TOTAL|imbalance` = **9718** (n=140, 2026-09-17T21:53:57.621849Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=140, 2026-09-17T21:53:57.621849Z)
- `INDGEN|TOTAL|generation` = **26532** (n=140, 2026-09-17T21:53:57.621849Z)
- `MELNGC|TOTAL|margin` = **36444** (n=140, 2026-09-17T21:52:01.830500Z)
- `NDF|TOTAL|demand` = **16314** (n=143, 2026-09-17T21:48:44.127229Z)
- `TSDF|TOTAL|demand` = **16814** (n=143, 2026-09-17T21:48:44.127229Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T22:11:12.758958Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:11:11.043354Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:11:09.328323Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:11:07.606577Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:11:05.895370Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:11:04.197695Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:11:00.418617Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:10:58.713310Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:10:57.013129Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:10:55.283770Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:10:53.575788Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:10:51.849412Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:10:49.980636Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:10:48.229313Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:10:46.528289Z` — **MID**: 0 rows; marker `2026-09-17T22:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
