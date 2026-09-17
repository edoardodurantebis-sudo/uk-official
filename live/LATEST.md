# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T23:14:27.524173Z`  
Current process started UTC: `2026-09-17T23:10:26.817205Z`  
1-second metadata polls in this process: **133**  
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

- `FUELINST|fuelType=INTVKL|generation` = **608** (n=860, 2026-09-17T23:10:26.817211Z)
- `FUELINST|fuelType=NPSHYD|generation` = **451** (n=860, 2026-09-17T23:10:26.817211Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=860, 2026-09-17T23:10:26.817211Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=860, 2026-09-17T23:10:26.817211Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=860, 2026-09-17T23:10:26.817211Z)
- `FUELINST|fuelType=OTHER|generation` = **637** (n=860, 2026-09-17T23:10:26.817211Z)
- `FUELINST|fuelType=PS|generation` = **55** (n=860, 2026-09-17T23:10:26.817211Z)
- `FUELINST|fuelType=WIND|generation` = **15055** (n=860, 2026-09-17T23:10:26.817211Z)
- `IMBALNGC|TOTAL|imbalance` = **9714** (n=142, 2026-09-17T22:53:01.934421Z)
- `INDDEM|TOTAL|demand` = **-11176** (n=142, 2026-09-17T22:53:01.934421Z)
- `INDGEN|TOTAL|generation` = **26528** (n=142, 2026-09-17T22:52:45.948872Z)
- `MELNGC|TOTAL|margin` = **36504** (n=142, 2026-09-17T22:50:33.469423Z)
- `NDF|TOTAL|demand` = **16314** (n=145, 2026-09-17T22:48:29.814995Z)
- `TSDF|TOTAL|demand` = **16814** (n=145, 2026-09-17T22:48:12.655094Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T23:14:25.861693Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:24.232949Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:22.566248Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:20.884815Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:19.183519Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:15.682871Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:15.682871Z` — **FREQ**: 5761 rows; marker `2026-09-17T23:13:45Z`
- `2026-09-17T23:14:14.031548Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:12.361761Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:10.696603Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:09.014124Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:07.317503Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:05.538535Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:03.890232Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:14:02.244708Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
