# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T16:42:42.914572Z`  
Current process started UTC: `2026-09-17T16:38:41.343713Z`  
1-second metadata polls in this process: **135**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=52, delta=-3, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.58 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=-2, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=0, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=57, delta=1, z=4.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=14, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.03 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.13 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.18 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=782, 2026-09-17T16:40:31.297470Z)
- `FUELINST|fuelType=NPSHYD|generation` = **418** (n=782, 2026-09-17T16:40:31.297470Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=782, 2026-09-17T16:40:31.297470Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=782, 2026-09-17T16:40:31.297470Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=782, 2026-09-17T16:40:31.297470Z)
- `FUELINST|fuelType=OTHER|generation` = **1073** (n=782, 2026-09-17T16:40:31.297470Z)
- `FUELINST|fuelType=PS|generation` = **64** (n=782, 2026-09-17T16:40:31.297470Z)
- `FUELINST|fuelType=WIND|generation` = **14134** (n=782, 2026-09-17T16:40:31.297470Z)
- `IMBALNGC|TOTAL|imbalance` = **11622** (n=129, 2026-09-17T16:24:37.034205Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=129, 2026-09-17T16:24:05.322902Z)
- `INDGEN|TOTAL|generation` = **28436** (n=129, 2026-09-17T16:24:05.322902Z)
- `MELNGC|TOTAL|margin` = **36692** (n=129, 2026-09-17T16:21:11.558898Z)
- `NDF|TOTAL|demand` = **16314** (n=132, 2026-09-17T16:18:29.666995Z)
- `TSDF|TOTAL|demand` = **16814** (n=132, 2026-09-17T16:18:29.666995Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T16:42:41.209404Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:39.244768Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:37.510224Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:35.807609Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:34.105400Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:32.409245Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:30.700395Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:28.985561Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:27.278825Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:25.573222Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:23.488200Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:21.744561Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:20.037413Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:18.337159Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:42:16.607370Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
