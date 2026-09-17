# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T19:10:36.602403Z`  
Current process started UTC: `2026-09-17T19:06:36.437868Z`  
1-second metadata polls in this process: **230**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=-2, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=81, delta=-2, z=4.34 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=82, delta=45, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=-1, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=84, delta=7, z=4.84 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1407** (n=812, 2026-09-17T19:10:33.566035Z)
- `FUELINST|fuelType=NPSHYD|generation` = **635** (n=812, 2026-09-17T19:10:33.566035Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3325** (n=812, 2026-09-17T19:10:33.566035Z)
- `FUELINST|fuelType=OCGT|generation` = **118** (n=812, 2026-09-17T19:10:33.566035Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=812, 2026-09-17T19:10:33.566035Z)
- `FUELINST|fuelType=OTHER|generation` = **912** (n=812, 2026-09-17T19:10:33.566035Z)
- `FUELINST|fuelType=PS|generation` = **278** (n=812, 2026-09-17T19:10:33.566035Z)
- `FUELINST|fuelType=WIND|generation` = **15233** (n=812, 2026-09-17T19:10:33.566035Z)
- `IMBALNGC|TOTAL|imbalance` = **9701** (n=134, 2026-09-17T18:53:56.215839Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=134, 2026-09-17T18:53:56.215839Z)
- `INDGEN|TOTAL|generation` = **26515** (n=134, 2026-09-17T18:53:56.215839Z)
- `MELNGC|TOTAL|margin` = **36584** (n=134, 2026-09-17T18:51:06.144242Z)
- `NDF|TOTAL|demand` = **16314** (n=137, 2026-09-17T18:48:33.698047Z)
- `TSDF|TOTAL|demand` = **16814** (n=137, 2026-09-17T18:48:33.698047Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T19:10:35.654729Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:33.566035Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:33.566035Z` — **FUELINST**: 80 rows; marker `2026-09-17T19:10:00Z`
- `2026-09-17T19:10:32.548726Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:31.548568Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:30.532842Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:29.532686Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:28.532617Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:27.528666Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:26.528571Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:25.528483Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:24.499355Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:23.499274Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:22.499186Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:10:21.499022Z` — **MID**: 0 rows; marker `2026-09-17T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
