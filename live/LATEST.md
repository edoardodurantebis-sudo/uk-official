# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T23:27:01.892651Z`  
Current process started UTC: `2026-09-17T23:23:00.966505Z`  
1-second metadata polls in this process: **226**  
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

- `FUELINST|fuelType=INTVKL|generation` = **608** (n=863, 2026-09-17T23:25:31.319584Z)
- `FUELINST|fuelType=NPSHYD|generation` = **450** (n=863, 2026-09-17T23:25:31.319584Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3319** (n=863, 2026-09-17T23:25:31.319584Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=863, 2026-09-17T23:25:31.319584Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=863, 2026-09-17T23:25:31.319584Z)
- `FUELINST|fuelType=OTHER|generation` = **415** (n=863, 2026-09-17T23:25:31.319584Z)
- `FUELINST|fuelType=PS|generation` = **54** (n=863, 2026-09-17T23:25:31.319584Z)
- `FUELINST|fuelType=WIND|generation` = **14657** (n=863, 2026-09-17T23:25:31.319584Z)
- `IMBALNGC|TOTAL|imbalance` = **9745** (n=143, 2026-09-17T23:22:08.151476Z)
- `INDDEM|TOTAL|demand` = **-11183** (n=143, 2026-09-17T23:22:08.151476Z)
- `INDGEN|TOTAL|generation` = **26559** (n=143, 2026-09-17T23:22:08.151476Z)
- `MELNGC|TOTAL|margin` = **36572** (n=143, 2026-09-17T23:20:11.082648Z)
- `NDF|TOTAL|demand` = **16314** (n=146, 2026-09-17T23:18:11.234096Z)
- `TSDF|TOTAL|demand` = **16814** (n=146, 2026-09-17T23:18:11.234096Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T23:27:00.921526Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:59.921409Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:58.915902Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:57.915794Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:56.915672Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:55.915552Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:54.915442Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:53.915358Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:52.915240Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:51.420727Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:50.420660Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:49.420543Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:48.420468Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:47.420353Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:26:46.420238Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
