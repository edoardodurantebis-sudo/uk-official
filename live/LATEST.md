# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T07:09:19.227957Z`  
Current process started UTC: `2026-09-17T07:05:18.013947Z`  
1-second metadata polls in this process: **169**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNSL` `generation` — instantaneous generation mix [fuelType=INTNSL] generation: value=-1176, delta=0, z=-3.87 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **859** (n=667, 2026-09-17T07:05:38.016665Z)
- `FUELINST|fuelType=NPSHYD|generation` = **419** (n=667, 2026-09-17T07:05:38.016665Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=667, 2026-09-17T07:05:38.016665Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=667, 2026-09-17T07:05:38.016665Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=667, 2026-09-17T07:05:38.016665Z)
- `FUELINST|fuelType=OTHER|generation` = **797** (n=667, 2026-09-17T07:05:38.016665Z)
- `FUELINST|fuelType=PS|generation` = **219** (n=667, 2026-09-17T07:05:38.016665Z)
- `FUELINST|fuelType=WIND|generation` = **14004** (n=667, 2026-09-17T07:05:38.016665Z)
- `IMBALNGC|TOTAL|imbalance` = **7338** (n=111, 2026-09-17T06:49:53.327366Z)
- `INDDEM|TOTAL|demand` = **-12129** (n=111, 2026-09-17T06:49:37.422907Z)
- `INDGEN|TOTAL|generation` = **26459** (n=111, 2026-09-17T06:49:37.422907Z)
- `MELNGC|TOTAL|margin` = **35731** (n=111, 2026-09-17T06:48:49.093378Z)
- `NDF|TOTAL|demand` = **18621** (n=113, 2026-09-17T06:46:58.264612Z)
- `TSDF|TOTAL|demand` = **19121** (n=113, 2026-09-17T06:46:58.264612Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T07:09:17.511538Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:09:15.762850Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:09:14.059190Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:09:12.321870Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:09:10.596224Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:09:08.888072Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:09:07.126818Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:09:04.867914Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:09:03.163272Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:09:01.444886Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:08:59.702789Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:08:57.993995Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:08:56.287606Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:08:54.566489Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:08:52.841841Z` — **MID**: 0 rows; marker `2026-09-17T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
