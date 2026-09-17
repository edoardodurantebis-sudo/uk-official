# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T22:19:43.336708Z`  
Current process started UTC: `2026-09-17T22:15:41.828817Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **343** (n=849, 2026-09-17T22:15:23.150885Z)
- `FUELINST|fuelType=NPSHYD|generation` = **452** (n=849, 2026-09-17T22:15:23.150885Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3322** (n=849, 2026-09-17T22:15:23.150885Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=849, 2026-09-17T22:15:23.150885Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=849, 2026-09-17T22:15:23.150885Z)
- `FUELINST|fuelType=OTHER|generation` = **1323** (n=849, 2026-09-17T22:15:23.150885Z)
- `FUELINST|fuelType=PS|generation` = **-254** (n=849, 2026-09-17T22:15:23.150885Z)
- `FUELINST|fuelType=WIND|generation` = **15146** (n=849, 2026-09-17T22:15:23.150885Z)
- `IMBALNGC|TOTAL|imbalance` = **9718** (n=140, 2026-09-17T21:53:57.621849Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=140, 2026-09-17T21:53:57.621849Z)
- `INDGEN|TOTAL|generation` = **26532** (n=140, 2026-09-17T21:53:57.621849Z)
- `MELNGC|TOTAL|margin` = **36444** (n=140, 2026-09-17T21:52:01.830500Z)
- `NDF|TOTAL|demand` = **16314** (n=144, 2026-09-17T22:17:57.884209Z)
- `TSDF|TOTAL|demand` = **16814** (n=144, 2026-09-17T22:17:57.884209Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T22:19:41.577939Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:39.952060Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:37.921959Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:36.313659Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:34.716615Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:33.098553Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:31.420375Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:29.739559Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:28.164047Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:26.388525Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:24.745104Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:23.164598Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:21.043266Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:19.318458Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:19:17.587456Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
