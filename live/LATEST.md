# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T16:34:16.302034Z`  
Current process started UTC: `2026-09-17T16:30:15.585816Z`  
1-second metadata polls in this process: **159**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.23 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=42, delta=42, z=3.55 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=780, 2026-09-17T16:30:31.933081Z)
- `FUELINST|fuelType=NPSHYD|generation` = **420** (n=780, 2026-09-17T16:30:31.933081Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=780, 2026-09-17T16:30:31.933081Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=780, 2026-09-17T16:30:31.933081Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=780, 2026-09-17T16:30:31.933081Z)
- `FUELINST|fuelType=OTHER|generation` = **1208** (n=780, 2026-09-17T16:30:31.933081Z)
- `FUELINST|fuelType=PS|generation` = **-254** (n=780, 2026-09-17T16:30:31.933081Z)
- `FUELINST|fuelType=WIND|generation` = **14084** (n=780, 2026-09-17T16:30:31.933081Z)
- `IMBALNGC|TOTAL|imbalance` = **11622** (n=129, 2026-09-17T16:24:37.034205Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=129, 2026-09-17T16:24:05.322902Z)
- `INDGEN|TOTAL|generation` = **28436** (n=129, 2026-09-17T16:24:05.322902Z)
- `MELNGC|TOTAL|margin` = **36692** (n=129, 2026-09-17T16:21:11.558898Z)
- `NDF|TOTAL|demand` = **16314** (n=132, 2026-09-17T16:18:29.666995Z)
- `TSDF|TOTAL|demand` = **16814** (n=132, 2026-09-17T16:18:29.666995Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T16:34:15.007175Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:34:13.658644Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:34:12.345474Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:34:10.997320Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:34:09.669320Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:34:08.349226Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:34:07.040228Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:34:05.705204Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:34:04.246762Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:34:02.495189Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:34:00.955707Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:33:59.586679Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:33:58.215415Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:33:56.901957Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:33:55.580706Z` — **MID**: 0 rows; marker `2026-09-17T16:12:05Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
