# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T18:41:13.123758Z`  
Current process started UTC: `2026-09-17T18:37:12.595884Z`  
1-second metadata polls in this process: **145**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=-2, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=81, delta=-2, z=4.34 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=82, delta=45, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=-1, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=84, delta=7, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=77, delta=66, z=4.46 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=58, delta=2, z=3.72 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=52, delta=-3, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.58 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=806, 2026-09-17T18:40:28.619279Z)
- `FUELINST|fuelType=NPSHYD|generation` = **627** (n=806, 2026-09-17T18:40:28.619279Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3324** (n=806, 2026-09-17T18:40:28.619279Z)
- `FUELINST|fuelType=OCGT|generation` = **79** (n=806, 2026-09-17T18:40:28.619279Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=806, 2026-09-17T18:40:28.619279Z)
- `FUELINST|fuelType=OTHER|generation` = **1787** (n=806, 2026-09-17T18:40:28.619279Z)
- `FUELINST|fuelType=PS|generation` = **282** (n=806, 2026-09-17T18:40:28.619279Z)
- `FUELINST|fuelType=WIND|generation` = **15045** (n=806, 2026-09-17T18:40:28.619279Z)
- `IMBALNGC|TOTAL|imbalance` = **9682** (n=133, 2026-09-17T18:24:32.722523Z)
- `INDDEM|TOTAL|demand` = **-11254** (n=133, 2026-09-17T18:24:12.670545Z)
- `INDGEN|TOTAL|generation` = **26496** (n=133, 2026-09-17T18:24:12.670545Z)
- `MELNGC|TOTAL|margin` = **36584** (n=133, 2026-09-17T18:21:20.240550Z)
- `NDF|TOTAL|demand` = **16314** (n=136, 2026-09-17T18:18:46.937615Z)
- `TSDF|TOTAL|demand` = **16814** (n=136, 2026-09-17T18:18:46.937615Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T18:41:11.565227Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:41:09.984422Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:41:08.447803Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:41:06.862250Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:41:05.279072Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:41:03.663637Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:41:01.713263Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:41:00.135165Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:40:58.556420Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:40:56.960162Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:40:55.388615Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:40:53.842401Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:40:52.266756Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:40:50.679494Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:40:49.079559Z` — **MID**: 0 rows; marker `2026-09-17T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
