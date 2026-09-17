# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T11:14:08.994466Z`  
Current process started UTC: `2026-09-17T11:10:07.939015Z`  
1-second metadata polls in this process: **147**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11265, delta=1771, z=1.70 -> demand pressure up
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16597, delta=-3265, z=-4.21 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16097, delta=-2159, z=-4.24 -> demand pressure easing
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-622** (n=716, 2026-09-17T11:10:39.850481Z)
- `FUELINST|fuelType=NPSHYD|generation` = **269** (n=716, 2026-09-17T11:10:39.850481Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3306** (n=716, 2026-09-17T11:10:39.850481Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=716, 2026-09-17T11:10:39.850481Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=716, 2026-09-17T11:10:39.850481Z)
- `FUELINST|fuelType=OTHER|generation` = **1127** (n=716, 2026-09-17T11:10:39.850481Z)
- `FUELINST|fuelType=PS|generation` = **-935** (n=716, 2026-09-17T11:10:39.850481Z)
- `FUELINST|fuelType=WIND|generation` = **15206** (n=716, 2026-09-17T11:10:39.850481Z)
- `IMBALNGC|TOTAL|imbalance` = **11942** (n=118, 2026-09-17T10:55:58.735722Z)
- `INDDEM|TOTAL|demand` = **-11265** (n=118, 2026-09-17T10:55:27.413700Z)
- `INDGEN|TOTAL|generation` = **28539** (n=118, 2026-09-17T10:55:42.964470Z)
- `MELNGC|TOTAL|margin` = **36813** (n=118, 2026-09-17T10:51:20.211901Z)
- `NDF|TOTAL|demand` = **16097** (n=121, 2026-09-17T10:49:09.296610Z)
- `TSDF|TOTAL|demand` = **16597** (n=121, 2026-09-17T10:49:09.296610Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T11:14:07.454873Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:14:05.878226Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:14:04.317348Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:14:02.757106Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:14:01.169929Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:13:59.617527Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:13:58.053674Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:13:56.494353Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:13:54.588543Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:13:53.045591Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:13:51.501449Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:13:49.959054Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:13:48.408082Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:13:46.840201Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:13:45.308168Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
