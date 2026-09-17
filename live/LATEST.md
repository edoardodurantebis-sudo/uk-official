# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T07:51:34.065533Z`  
Current process started UTC: `2026-09-17T07:47:33.135441Z`  
1-second metadata polls in this process: **230**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1370** (n=676, 2026-09-17T07:50:32.780810Z)
- `FUELINST|fuelType=NPSHYD|generation` = **417** (n=676, 2026-09-17T07:50:32.780810Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3310** (n=676, 2026-09-17T07:50:32.780810Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=676, 2026-09-17T07:50:32.780810Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=676, 2026-09-17T07:50:32.780810Z)
- `FUELINST|fuelType=OTHER|generation` = **366** (n=676, 2026-09-17T07:50:32.780810Z)
- `FUELINST|fuelType=PS|generation` = **226** (n=676, 2026-09-17T07:50:32.780810Z)
- `FUELINST|fuelType=WIND|generation` = **15508** (n=676, 2026-09-17T07:50:32.780810Z)
- `IMBALNGC|TOTAL|imbalance` = **7157** (n=112, 2026-09-17T07:19:39.625704Z)
- `INDDEM|TOTAL|demand` = **-12138** (n=112, 2026-09-17T07:19:39.625704Z)
- `INDGEN|TOTAL|generation` = **26528** (n=112, 2026-09-17T07:19:39.625704Z)
- `MELNGC|TOTAL|margin` = **35577** (n=112, 2026-09-17T07:18:19.457722Z)
- `NDF|TOTAL|demand` = **16158** (n=115, 2026-09-17T07:45:46.989663Z)
- `TSDF|TOTAL|demand` = **16658** (n=115, 2026-09-17T07:45:46.989663Z)
- `WINDFOR|TOTAL|generation` = **19265** (n=19, 2026-09-17T05:30:37.912884Z)

## Latest publication events

- `2026-09-17T07:51:33.126573Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:32.126452Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:31.126331Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:30.126250Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:29.126131Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:28.126033Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:27.125913Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:26.125799Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:25.125679Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:24.125571Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:23.125451Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:22.125335Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:20.629406Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:19.629319Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T07:51:18.629237Z` — **MID**: 0 rows; marker `2026-09-17T07:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
