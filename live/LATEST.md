# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T16:46:58.570007Z`  
Current process started UTC: `2026-09-17T16:42:57.423611Z`  
1-second metadata polls in this process: **143**  
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

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=783, 2026-09-17T16:45:21.380657Z)
- `FUELINST|fuelType=NPSHYD|generation` = **419** (n=783, 2026-09-17T16:45:21.380657Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3323** (n=783, 2026-09-17T16:45:21.380657Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=783, 2026-09-17T16:45:21.380657Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=783, 2026-09-17T16:45:21.380657Z)
- `FUELINST|fuelType=OTHER|generation` = **1098** (n=783, 2026-09-17T16:45:21.380657Z)
- `FUELINST|fuelType=PS|generation` = **164** (n=783, 2026-09-17T16:45:21.380657Z)
- `FUELINST|fuelType=WIND|generation` = **14135** (n=783, 2026-09-17T16:45:21.380657Z)
- `IMBALNGC|TOTAL|imbalance` = **11622** (n=129, 2026-09-17T16:24:37.034205Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=129, 2026-09-17T16:24:05.322902Z)
- `INDGEN|TOTAL|generation` = **28436** (n=129, 2026-09-17T16:24:05.322902Z)
- `MELNGC|TOTAL|margin` = **36692** (n=129, 2026-09-17T16:21:11.558898Z)
- `NDF|TOTAL|demand` = **16314** (n=132, 2026-09-17T16:18:29.666995Z)
- `TSDF|TOTAL|demand` = **16814** (n=132, 2026-09-17T16:18:29.666995Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T16:46:57.005577Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:55.002968Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:53.411013Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:51.781874Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:50.118598Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:48.165011Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:46.610868Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:43.663191Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:41.802824Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:39.956432Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:38.254738Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:36.475745Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:34.582940Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:32.821037Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:46:31.181786Z` — **MID**: 0 rows; marker `2026-09-17T16:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
