# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T07:02:41.683465Z`  
Current process started UTC: `2026-09-19T06:58:40.364560Z`  
1-second metadata polls in this process: **129**  
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

- `FUELINST|fuelType=INTVKL|generation` = **666** (n=1198, 2026-09-19T07:00:32.449340Z)
- `FUELINST|fuelType=NPSHYD|generation` = **368** (n=1198, 2026-09-19T07:00:32.449340Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1198, 2026-09-19T07:00:32.449340Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1198, 2026-09-19T07:00:32.449340Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1198, 2026-09-19T07:00:32.449340Z)
- `FUELINST|fuelType=OTHER|generation` = **815** (n=1198, 2026-09-19T07:00:32.449340Z)
- `FUELINST|fuelType=PS|generation` = **-374** (n=1198, 2026-09-19T07:00:32.449340Z)
- `FUELINST|fuelType=WIND|generation` = **15808** (n=1198, 2026-09-19T07:00:32.449340Z)
- `IMBALNGC|TOTAL|imbalance` = **9478** (n=198, 2026-09-19T06:50:13.925182Z)
- `INDDEM|TOTAL|demand` = **-11352** (n=198, 2026-09-19T06:50:13.925182Z)
- `INDGEN|TOTAL|generation` = **26907** (n=198, 2026-09-19T06:50:13.925182Z)
- `MELNGC|TOTAL|margin` = **38030** (n=198, 2026-09-19T06:49:00.398728Z)
- `NDF|TOTAL|demand` = **16550** (n=202, 2026-09-19T06:47:06.856404Z)
- `TSDF|TOTAL|demand` = **17429** (n=202, 2026-09-19T06:47:06.856404Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T07:02:39.909446Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:38.178408Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:36.440623Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:34.355362Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:32.633946Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:30.293039Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:28.588496Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:26.729502Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:25.005084Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:23.300026Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:21.398462Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:19.521920Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:17.804899Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:13.246890Z` — **MID**: 0 rows; marker `2026-09-19T06:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T07:02:13.246890Z` — **FREQ**: 5761 rows; marker `2026-09-19T07:01:45Z`
