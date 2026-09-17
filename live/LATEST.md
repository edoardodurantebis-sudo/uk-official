# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T16:38:28.590733Z`  
Current process started UTC: `2026-09-17T16:34:27.342185Z`  
1-second metadata polls in this process: **155**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.23 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=781, 2026-09-17T16:35:32.901727Z)
- `FUELINST|fuelType=NPSHYD|generation` = **419** (n=781, 2026-09-17T16:35:32.901727Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3314** (n=781, 2026-09-17T16:35:32.901727Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=781, 2026-09-17T16:35:32.901727Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=781, 2026-09-17T16:35:32.901727Z)
- `FUELINST|fuelType=OTHER|generation` = **1068** (n=781, 2026-09-17T16:35:32.901727Z)
- `FUELINST|fuelType=PS|generation` = **-30** (n=781, 2026-09-17T16:35:32.901727Z)
- `FUELINST|fuelType=WIND|generation` = **14136** (n=781, 2026-09-17T16:35:32.901727Z)
- `IMBALNGC|TOTAL|imbalance` = **11622** (n=129, 2026-09-17T16:24:37.034205Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=129, 2026-09-17T16:24:05.322902Z)
- `INDGEN|TOTAL|generation` = **28436** (n=129, 2026-09-17T16:24:05.322902Z)
- `MELNGC|TOTAL|margin` = **36692** (n=129, 2026-09-17T16:21:11.558898Z)
- `NDF|TOTAL|demand` = **16314** (n=132, 2026-09-17T16:18:29.666995Z)
- `TSDF|TOTAL|demand` = **16814** (n=132, 2026-09-17T16:18:29.666995Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T16:38:27.073673Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:25.577450Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:24.098271Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:22.577634Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:21.129381Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:17.964457Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:17.964457Z` — **FREQ**: 5761 rows; marker `2026-09-17T16:37:45Z`
- `2026-09-17T16:38:16.463425Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:14.992995Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:13.548804Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:12.050170Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:10.576955Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:09.089306Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:07.608302Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T16:38:05.777397Z` — **MID**: 0 rows; marker `2026-09-17T16:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
