# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T10:17:07.212546Z`  
Current process started UTC: `2026-09-19T10:13:06.203822Z`  
1-second metadata polls in this process: **186**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-10744, delta=3052, z=1.92 -> demand pressure up
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1237, 2026-09-19T10:15:27.753666Z)
- `FUELINST|fuelType=NPSHYD|generation` = **301** (n=1237, 2026-09-19T10:15:27.753666Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1237, 2026-09-19T10:15:27.753666Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1237, 2026-09-19T10:15:27.753666Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1237, 2026-09-19T10:15:27.753666Z)
- `FUELINST|fuelType=OTHER|generation` = **438** (n=1237, 2026-09-19T10:15:27.753666Z)
- `FUELINST|fuelType=PS|generation` = **-690** (n=1237, 2026-09-19T10:15:27.753666Z)
- `FUELINST|fuelType=WIND|generation` = **15781** (n=1237, 2026-09-19T10:15:27.753666Z)
- `IMBALNGC|TOTAL|imbalance` = **7793** (n=203, 2026-09-19T09:50:05.454220Z)
- `INDDEM|TOTAL|demand` = **-13214** (n=203, 2026-09-19T09:49:49.613301Z)
- `INDGEN|TOTAL|generation` = **26724** (n=203, 2026-09-19T09:49:49.613301Z)
- `MELNGC|TOTAL|margin` = **36451** (n=203, 2026-09-19T09:48:44.462675Z)
- `NDF|TOTAL|demand` = **15940** (n=209, 2026-09-19T10:16:50.751867Z)
- `TSDF|TOTAL|demand` = **18932** (n=209, 2026-09-19T10:16:50.751867Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T10:17:06.032664Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:17:04.841411Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:17:03.255337Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:17:01.851776Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:17:00.274857Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:16:58.099459Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:16:56.724167Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:16:55.128341Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:16:53.601129Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:16:50.751867Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:16:50.751867Z` — **TSDF**: 630 rows; marker `2026-09-19T10:16:00Z`
- `2026-09-19T10:16:50.751867Z` — **NDF**: 35 rows; marker `2026-09-19T10:16:00Z`
- `2026-09-19T10:16:49.118829Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:16:47.951758Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:16:46.758144Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
