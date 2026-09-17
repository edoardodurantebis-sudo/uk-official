# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T16:25:52.673261Z`  
Current process started UTC: `2026-09-17T16:21:52.058558Z`  
1-second metadata polls in this process: **140**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.23 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=42, delta=42, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=2, z=4.25 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=779, 2026-09-17T16:25:41.800147Z)
- `FUELINST|fuelType=NPSHYD|generation` = **418** (n=779, 2026-09-17T16:25:41.800147Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3313** (n=779, 2026-09-17T16:25:41.800147Z)
- `FUELINST|fuelType=OCGT|generation` = **52** (n=779, 2026-09-17T16:25:41.800147Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=779, 2026-09-17T16:25:41.800147Z)
- `FUELINST|fuelType=OTHER|generation` = **1234** (n=779, 2026-09-17T16:25:41.800147Z)
- `FUELINST|fuelType=PS|generation` = **-255** (n=779, 2026-09-17T16:25:41.800147Z)
- `FUELINST|fuelType=WIND|generation` = **14003** (n=779, 2026-09-17T16:25:41.800147Z)
- `IMBALNGC|TOTAL|imbalance` = **11622** (n=129, 2026-09-17T16:24:37.034205Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=129, 2026-09-17T16:24:05.322902Z)
- `INDGEN|TOTAL|generation` = **28436** (n=129, 2026-09-17T16:24:05.322902Z)
- `MELNGC|TOTAL|margin` = **36692** (n=129, 2026-09-17T16:21:11.558898Z)
- `NDF|TOTAL|demand` = **16314** (n=132, 2026-09-17T16:18:29.666995Z)
- `TSDF|TOTAL|demand` = **16814** (n=132, 2026-09-17T16:18:29.666995Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T16:25:51.055174Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:49.427383Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:47.733916Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:46.159250Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:44.616638Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:41.800147Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:41.800147Z` — **FUELINST**: 80 rows; marker `2026-09-17T16:25:00Z`
- `2026-09-17T16:25:40.221084Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:38.634154Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:37.015606Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:35.294122Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:33.593090Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:32.029720Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:30.401648Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:25:28.845283Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
