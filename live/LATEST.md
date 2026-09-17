# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T23:01:51.979896Z`  
Current process started UTC: `2026-09-17T22:57:50.942874Z`  
1-second metadata polls in this process: **132**  
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

- `FUELINST|fuelType=INTVKL|generation` = **402** (n=858, 2026-09-17T23:00:35.757487Z)
- `FUELINST|fuelType=NPSHYD|generation` = **451** (n=858, 2026-09-17T23:00:35.757487Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=858, 2026-09-17T23:00:35.757487Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=858, 2026-09-17T23:00:35.757487Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=858, 2026-09-17T23:00:35.757487Z)
- `FUELINST|fuelType=OTHER|generation` = **611** (n=858, 2026-09-17T23:00:35.757487Z)
- `FUELINST|fuelType=PS|generation` = **52** (n=858, 2026-09-17T23:00:35.757487Z)
- `FUELINST|fuelType=WIND|generation` = **15234** (n=858, 2026-09-17T23:00:35.757487Z)
- `IMBALNGC|TOTAL|imbalance` = **9714** (n=142, 2026-09-17T22:53:01.934421Z)
- `INDDEM|TOTAL|demand` = **-11176** (n=142, 2026-09-17T22:53:01.934421Z)
- `INDGEN|TOTAL|generation` = **26528** (n=142, 2026-09-17T22:52:45.948872Z)
- `MELNGC|TOTAL|margin` = **36504** (n=142, 2026-09-17T22:50:33.469423Z)
- `NDF|TOTAL|demand` = **16314** (n=145, 2026-09-17T22:48:29.814995Z)
- `TSDF|TOTAL|demand` = **16814** (n=145, 2026-09-17T22:48:12.655094Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T23:01:50.362020Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:48.607523Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:46.910028Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:44.407590Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:42.015028Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:40.300954Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:38.626431Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:36.980646Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:35.325291Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:33.631315Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:31.907567Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:29.955558Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:26.053755Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:23.936875Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:01:22.276603Z` — **MID**: 0 rows; marker `2026-09-17T22:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
