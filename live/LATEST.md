# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T23:10:15.205490Z`  
Current process started UTC: `2026-09-17T23:06:13.932308Z`  
1-second metadata polls in this process: **176**  
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

- `FUELINST|fuelType=INTVKL|generation` = **537** (n=859, 2026-09-17T23:05:37.348507Z)
- `FUELINST|fuelType=NPSHYD|generation` = **452** (n=859, 2026-09-17T23:05:37.348507Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=859, 2026-09-17T23:05:37.348507Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=859, 2026-09-17T23:05:37.348507Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=859, 2026-09-17T23:05:37.348507Z)
- `FUELINST|fuelType=OTHER|generation` = **639** (n=859, 2026-09-17T23:05:37.348507Z)
- `FUELINST|fuelType=PS|generation` = **55** (n=859, 2026-09-17T23:05:37.348507Z)
- `FUELINST|fuelType=WIND|generation` = **15119** (n=859, 2026-09-17T23:05:37.348507Z)
- `IMBALNGC|TOTAL|imbalance` = **9714** (n=142, 2026-09-17T22:53:01.934421Z)
- `INDDEM|TOTAL|demand` = **-11176** (n=142, 2026-09-17T22:53:01.934421Z)
- `INDGEN|TOTAL|generation` = **26528** (n=142, 2026-09-17T22:52:45.948872Z)
- `MELNGC|TOTAL|margin` = **36504** (n=142, 2026-09-17T22:50:33.469423Z)
- `NDF|TOTAL|demand` = **16314** (n=145, 2026-09-17T22:48:29.814995Z)
- `TSDF|TOTAL|demand` = **16814** (n=145, 2026-09-17T22:48:12.655094Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T23:10:13.924943Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:10:12.538945Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:10:11.234193Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:10:09.906934Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:10:08.598785Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:10:07.311345Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:10:05.995840Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:10:04.674173Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:10:03.320813Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:10:01.422040Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:10:00.141442Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:09:58.825214Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:09:57.506793Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:09:56.202597Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:09:54.905002Z` — **MID**: 0 rows; marker `2026-09-17T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
