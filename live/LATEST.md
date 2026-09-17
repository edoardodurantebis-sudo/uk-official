# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T23:18:39.170518Z`  
Current process started UTC: `2026-09-17T23:14:38.184152Z`  
1-second metadata polls in this process: **169**  
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

- `FUELINST|fuelType=INTVKL|generation` = **608** (n=861, 2026-09-17T23:15:43.980491Z)
- `FUELINST|fuelType=NPSHYD|generation` = **451** (n=861, 2026-09-17T23:15:43.980491Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3319** (n=861, 2026-09-17T23:15:43.980491Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=861, 2026-09-17T23:15:43.980491Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=861, 2026-09-17T23:15:43.980491Z)
- `FUELINST|fuelType=OTHER|generation` = **635** (n=861, 2026-09-17T23:15:43.980491Z)
- `FUELINST|fuelType=PS|generation` = **55** (n=861, 2026-09-17T23:15:43.980491Z)
- `FUELINST|fuelType=WIND|generation` = **14945** (n=861, 2026-09-17T23:15:43.980491Z)
- `IMBALNGC|TOTAL|imbalance` = **9714** (n=142, 2026-09-17T22:53:01.934421Z)
- `INDDEM|TOTAL|demand` = **-11176** (n=142, 2026-09-17T22:53:01.934421Z)
- `INDGEN|TOTAL|generation` = **26528** (n=142, 2026-09-17T22:52:45.948872Z)
- `MELNGC|TOTAL|margin` = **36504** (n=142, 2026-09-17T22:50:33.469423Z)
- `NDF|TOTAL|demand` = **16314** (n=146, 2026-09-17T23:18:11.234096Z)
- `TSDF|TOTAL|demand` = **16814** (n=146, 2026-09-17T23:18:11.234096Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T23:18:37.975983Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:36.383288Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:34.840621Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:33.313923Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:32.101230Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:30.919019Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:27.854795Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:27.854795Z` — **FREQ**: 5761 rows; marker `2026-09-17T23:17:45Z`
- `2026-09-17T23:18:26.687641Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:25.278859Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:23.730822Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:22.508675Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:21.167747Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:19.967104Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:18:18.370750Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
