# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T08:29:24.433816Z`  
Current process started UTC: `2026-09-17T08:25:24.394431Z`  
1-second metadata polls in this process: **157**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1334** (n=683, 2026-09-17T08:25:24.394439Z)
- `FUELINST|fuelType=NPSHYD|generation` = **418** (n=683, 2026-09-17T08:25:24.394439Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=683, 2026-09-17T08:25:24.394439Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=683, 2026-09-17T08:25:24.394439Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=683, 2026-09-17T08:25:24.394439Z)
- `FUELINST|fuelType=OTHER|generation` = **528** (n=683, 2026-09-17T08:25:24.394439Z)
- `FUELINST|fuelType=PS|generation` = **-425** (n=683, 2026-09-17T08:25:24.394439Z)
- `FUELINST|fuelType=WIND|generation` = **15647** (n=683, 2026-09-17T08:25:24.394439Z)
- `IMBALNGC|TOTAL|imbalance` = **7525** (n=113, 2026-09-17T08:19:40.529611Z)
- `INDDEM|TOTAL|demand` = **-12141** (n=113, 2026-09-17T08:19:40.529611Z)
- `INDGEN|TOTAL|generation` = **26531** (n=113, 2026-09-17T08:19:40.529611Z)
- `MELNGC|TOTAL|margin` = **36048** (n=113, 2026-09-17T08:19:07.402525Z)
- `NDF|TOTAL|demand` = **18256** (n=116, 2026-09-17T08:17:16.994479Z)
- `TSDF|TOTAL|demand` = **19006** (n=116, 2026-09-17T08:17:16.994479Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T08:29:22.964357Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:21.513654Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:20.029171Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:18.564221Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:17.112521Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:15.415483Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:13.964369Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:12.519445Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:11.070138Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:09.615252Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:08.168490Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:06.706980Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:05.246967Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:03.773505Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T08:29:02.338835Z` — **MID**: 0 rows; marker `2026-09-17T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
