# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T08:46:11.089009Z`  
Current process started UTC: `2026-09-17T08:42:10.432507Z`  
1-second metadata polls in this process: **228**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16658, delta=-2713, z=-4.41 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16158, delta=-2463, z=-4.57 -> demand pressure easing
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=2, delta=-50, z=-0.16 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=-4, z=3.91 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.42 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=49, delta=49, z=4.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=3, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=1, z=4.21 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=0, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=51, delta=17, z=4.30 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-1134, delta=10, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1114, delta=62, z=-3.54 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1334** (n=687, 2026-09-17T08:45:33.630946Z)
- `FUELINST|fuelType=NPSHYD|generation` = **420** (n=687, 2026-09-17T08:45:33.630946Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=687, 2026-09-17T08:45:33.630946Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=687, 2026-09-17T08:45:33.630946Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=687, 2026-09-17T08:45:33.630946Z)
- `FUELINST|fuelType=OTHER|generation` = **327** (n=687, 2026-09-17T08:45:33.630946Z)
- `FUELINST|fuelType=PS|generation` = **-714** (n=687, 2026-09-17T08:45:33.630946Z)
- `FUELINST|fuelType=WIND|generation` = **15574** (n=687, 2026-09-17T08:45:33.630946Z)
- `IMBALNGC|TOTAL|imbalance` = **7525** (n=113, 2026-09-17T08:19:40.529611Z)
- `INDDEM|TOTAL|demand` = **-12141** (n=113, 2026-09-17T08:19:40.529611Z)
- `INDGEN|TOTAL|generation` = **26531** (n=113, 2026-09-17T08:19:40.529611Z)
- `MELNGC|TOTAL|margin` = **36048** (n=113, 2026-09-17T08:19:07.402525Z)
- `NDF|TOTAL|demand` = **18256** (n=116, 2026-09-17T08:17:16.994479Z)
- `TSDF|TOTAL|demand` = **19006** (n=116, 2026-09-17T08:17:16.994479Z)
- `WINDFOR|TOTAL|generation` = **19255** (n=20, 2026-09-17T08:30:43.563030Z)

## Latest publication events

- `2026-09-17T08:46:10.060154Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:46:09.060085Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:46:08.040264Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:46:06.502267Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:46:05.108125Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:46:03.626849Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:46:02.250233Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:46:01.205538Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:46:00.204364Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:45:59.167376Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:45:58.091658Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:45:57.078868Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:45:55.729266Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:45:54.729190Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:45:53.712661Z` — **MID**: 0 rows; marker `2026-09-17T08:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
