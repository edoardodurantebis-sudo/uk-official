# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T09:53:34.921861Z`  
Current process started UTC: `2026-09-17T09:49:33.958923Z`  
1-second metadata polls in this process: **177**  
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

- `FUELINST|fuelType=INTVKL|generation` = **741** (n=700, 2026-09-17T09:50:41.477434Z)
- `FUELINST|fuelType=NPSHYD|generation` = **320** (n=700, 2026-09-17T09:50:41.477434Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3316** (n=700, 2026-09-17T09:50:41.477434Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=700, 2026-09-17T09:50:41.477434Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=700, 2026-09-17T09:50:41.477434Z)
- `FUELINST|fuelType=OTHER|generation` = **669** (n=700, 2026-09-17T09:50:41.477434Z)
- `FUELINST|fuelType=PS|generation` = **-954** (n=700, 2026-09-17T09:50:41.477434Z)
- `FUELINST|fuelType=WIND|generation` = **15665** (n=700, 2026-09-17T09:50:41.477434Z)
- `IMBALNGC|TOTAL|imbalance` = **6663** (n=116, 2026-09-17T09:49:05.670831Z)
- `INDDEM|TOTAL|demand` = **-13006** (n=116, 2026-09-17T09:49:05.670831Z)
- `INDGEN|TOTAL|generation` = **26525** (n=116, 2026-09-17T09:49:05.670831Z)
- `MELNGC|TOTAL|margin` = **34414** (n=116, 2026-09-17T09:48:18.458078Z)
- `NDF|TOTAL|demand` = **18256** (n=119, 2026-09-17T09:47:00.404161Z)
- `TSDF|TOTAL|demand` = **19862** (n=119, 2026-09-17T09:46:44.222406Z)
- `WINDFOR|TOTAL|generation` = **19255** (n=20, 2026-09-17T08:30:43.563030Z)

## Latest publication events

- `2026-09-17T09:53:33.603323Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:32.306928Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:31.020517Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:29.732285Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:28.429166Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:27.154116Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:25.856806Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:24.549381Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:22.944587Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:21.649863Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:20.371267Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:19.051732Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:17.788192Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:16.489830Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T09:53:15.187824Z` — **MID**: 0 rows; marker `2026-09-17T09:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
