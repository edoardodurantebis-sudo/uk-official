# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T08:37:51.519906Z`  
Current process started UTC: `2026-09-17T08:33:51.311046Z`  
1-second metadata polls in this process: **143**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1334** (n=685, 2026-09-17T08:35:30.552628Z)
- `FUELINST|fuelType=NPSHYD|generation` = **420** (n=685, 2026-09-17T08:35:30.552628Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3319** (n=685, 2026-09-17T08:35:30.552628Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=685, 2026-09-17T08:35:30.552628Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=685, 2026-09-17T08:35:30.552628Z)
- `FUELINST|fuelType=OTHER|generation` = **317** (n=685, 2026-09-17T08:35:30.552628Z)
- `FUELINST|fuelType=PS|generation` = **-563** (n=685, 2026-09-17T08:35:30.552628Z)
- `FUELINST|fuelType=WIND|generation` = **15413** (n=685, 2026-09-17T08:35:30.552628Z)
- `IMBALNGC|TOTAL|imbalance` = **7525** (n=113, 2026-09-17T08:19:40.529611Z)
- `INDDEM|TOTAL|demand` = **-12141** (n=113, 2026-09-17T08:19:40.529611Z)
- `INDGEN|TOTAL|generation` = **26531** (n=113, 2026-09-17T08:19:40.529611Z)
- `MELNGC|TOTAL|margin` = **36048** (n=113, 2026-09-17T08:19:07.402525Z)
- `NDF|TOTAL|demand` = **18256** (n=116, 2026-09-17T08:17:16.994479Z)
- `TSDF|TOTAL|demand` = **19006** (n=116, 2026-09-17T08:17:16.994479Z)
- `WINDFOR|TOTAL|generation` = **19255** (n=20, 2026-09-17T08:30:43.563030Z)

## Latest publication events

- `2026-09-17T08:37:49.918201Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:48.374109Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:46.801621Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:45.199229Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:43.634984Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:41.927160Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:40.021999Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:38.425535Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:36.842029Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:35.250234Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:33.682135Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:32.098413Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:30.497346Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:28.879746Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:37:27.317324Z` — **MID**: 0 rows; marker `2026-09-17T08:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
