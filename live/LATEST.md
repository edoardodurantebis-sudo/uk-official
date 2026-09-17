# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T07:13:31.885593Z`  
Current process started UTC: `2026-09-17T07:09:31.073126Z`  
1-second metadata polls in this process: **177**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.73 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.82 -> generation-mix component moved
- **FUELHH** `fuelType=INTNSL` `generation` — half-hour generation mix [fuelType=INTNSL] generation: value=-1144, delta=-306, z=-4.09 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1273** (n=668, 2026-09-17T07:10:35.800860Z)
- `FUELINST|fuelType=NPSHYD|generation` = **414** (n=668, 2026-09-17T07:10:35.800860Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3314** (n=668, 2026-09-17T07:10:35.800860Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=668, 2026-09-17T07:10:35.800860Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=668, 2026-09-17T07:10:35.800860Z)
- `FUELINST|fuelType=OTHER|generation` = **461** (n=668, 2026-09-17T07:10:35.800860Z)
- `FUELINST|fuelType=PS|generation` = **223** (n=668, 2026-09-17T07:10:35.800860Z)
- `FUELINST|fuelType=WIND|generation` = **14111** (n=668, 2026-09-17T07:10:35.800860Z)
- `IMBALNGC|TOTAL|imbalance` = **7338** (n=111, 2026-09-17T06:49:53.327366Z)
- `INDDEM|TOTAL|demand` = **-12129** (n=111, 2026-09-17T06:49:37.422907Z)
- `INDGEN|TOTAL|generation` = **26459** (n=111, 2026-09-17T06:49:37.422907Z)
- `MELNGC|TOTAL|margin` = **35731** (n=111, 2026-09-17T06:48:49.093378Z)
- `NDF|TOTAL|demand` = **18621** (n=113, 2026-09-17T06:46:58.264612Z)
- `TSDF|TOTAL|demand` = **19121** (n=113, 2026-09-17T06:46:58.264612Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T07:13:30.579047Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:29.270343Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:27.963728Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:26.649881Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:25.373588Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:24.033248Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:22.761943Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:21.436044Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:20.121065Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:18.834428Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:17.500054Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:15.906135Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:14.573365Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:13.260435Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:13:11.992720Z` — **MID**: 0 rows; marker `2026-09-17T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
