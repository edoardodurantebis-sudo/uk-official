# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T10:48:57.538418Z`  
Current process started UTC: `2026-09-17T10:44:56.670057Z`  
1-second metadata polls in this process: **131**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-296** (n=711, 2026-09-17T10:45:44.924198Z)
- `FUELINST|fuelType=NPSHYD|generation` = **270** (n=711, 2026-09-17T10:45:44.924198Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=711, 2026-09-17T10:45:44.924198Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=711, 2026-09-17T10:45:44.924198Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=711, 2026-09-17T10:45:44.924198Z)
- `FUELINST|fuelType=OTHER|generation` = **634** (n=711, 2026-09-17T10:45:44.924198Z)
- `FUELINST|fuelType=PS|generation` = **-950** (n=711, 2026-09-17T10:45:44.924198Z)
- `FUELINST|fuelType=WIND|generation` = **15641** (n=711, 2026-09-17T10:45:44.924198Z)
- `IMBALNGC|TOTAL|imbalance` = **6691** (n=117, 2026-09-17T10:20:07.587303Z)
- `INDDEM|TOTAL|demand` = **-13036** (n=117, 2026-09-17T10:19:50.932861Z)
- `INDGEN|TOTAL|generation` = **26553** (n=117, 2026-09-17T10:19:50.932861Z)
- `MELNGC|TOTAL|margin` = **34438** (n=117, 2026-09-17T10:19:19.197280Z)
- `NDF|TOTAL|demand` = **18256** (n=120, 2026-09-17T10:17:16.694941Z)
- `TSDF|TOTAL|demand` = **19862** (n=120, 2026-09-17T10:17:16.694941Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T10:48:55.841958Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:54.109669Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:52.454509Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:50.711165Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:48.999364Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:47.266131Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:45.535802Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:43.482144Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:41.823507Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:40.083238Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:38.361380Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:36.402105Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:34.633120Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:32.956048Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:48:31.234876Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
