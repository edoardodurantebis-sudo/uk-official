# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T10:10:23.115224Z`  
Current process started UTC: `2026-09-17T10:06:22.183689Z`  
1-second metadata polls in this process: **233**  
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

- `FUELINST|fuelType=INTVKL|generation` = **14** (n=703, 2026-09-17T10:05:25.191633Z)
- `FUELINST|fuelType=NPSHYD|generation` = **286** (n=703, 2026-09-17T10:05:25.191633Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=703, 2026-09-17T10:05:25.191633Z)
- `FUELINST|fuelType=OCGT|generation` = **1** (n=703, 2026-09-17T10:05:25.191633Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=703, 2026-09-17T10:05:25.191633Z)
- `FUELINST|fuelType=OTHER|generation` = **1073** (n=703, 2026-09-17T10:05:25.191633Z)
- `FUELINST|fuelType=PS|generation` = **-931** (n=703, 2026-09-17T10:05:25.191633Z)
- `FUELINST|fuelType=WIND|generation` = **15526** (n=703, 2026-09-17T10:05:25.191633Z)
- `IMBALNGC|TOTAL|imbalance` = **6663** (n=116, 2026-09-17T09:49:05.670831Z)
- `INDDEM|TOTAL|demand` = **-13006** (n=116, 2026-09-17T09:49:05.670831Z)
- `INDGEN|TOTAL|generation` = **26525** (n=116, 2026-09-17T09:49:05.670831Z)
- `MELNGC|TOTAL|margin` = **34414** (n=116, 2026-09-17T09:48:18.458078Z)
- `NDF|TOTAL|demand` = **18256** (n=119, 2026-09-17T09:47:00.404161Z)
- `TSDF|TOTAL|demand` = **19862** (n=119, 2026-09-17T09:46:44.222406Z)
- `WINDFOR|TOTAL|generation` = **19255** (n=20, 2026-09-17T08:30:43.563030Z)

## Latest publication events

- `2026-09-17T10:10:22.169794Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:21.169665Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:20.169549Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:19.169433Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:18.169312Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:17.169234Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:16.169110Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:15.168996Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:14.168886Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:13.168822Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:12.168682Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:09.871846Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:09.871846Z` — **FREQ**: 5761 rows; marker `2026-09-17T10:09:45Z`
- `2026-09-17T10:10:08.871734Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:10:07.871650Z` — **MID**: 0 rows; marker `2026-09-17T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
