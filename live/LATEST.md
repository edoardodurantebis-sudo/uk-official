# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T11:01:31.276968Z`  
Current process started UTC: `2026-09-17T10:57:31.199565Z`  
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

- `FUELINST|fuelType=INTVKL|generation` = **-372** (n=714, 2026-09-17T11:00:29.376858Z)
- `FUELINST|fuelType=NPSHYD|generation` = **272** (n=714, 2026-09-17T11:00:29.376858Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3306** (n=714, 2026-09-17T11:00:29.376858Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=714, 2026-09-17T11:00:29.376858Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=714, 2026-09-17T11:00:29.376858Z)
- `FUELINST|fuelType=OTHER|generation` = **755** (n=714, 2026-09-17T11:00:29.376858Z)
- `FUELINST|fuelType=PS|generation` = **-933** (n=714, 2026-09-17T11:00:29.376858Z)
- `FUELINST|fuelType=WIND|generation` = **15483** (n=714, 2026-09-17T11:00:29.376858Z)
- `IMBALNGC|TOTAL|imbalance` = **11942** (n=118, 2026-09-17T10:55:58.735722Z)
- `INDDEM|TOTAL|demand` = **-11265** (n=118, 2026-09-17T10:55:27.413700Z)
- `INDGEN|TOTAL|generation` = **28539** (n=118, 2026-09-17T10:55:42.964470Z)
- `MELNGC|TOTAL|margin` = **36813** (n=118, 2026-09-17T10:51:20.211901Z)
- `NDF|TOTAL|demand` = **16097** (n=121, 2026-09-17T10:49:09.296610Z)
- `TSDF|TOTAL|demand` = **16597** (n=121, 2026-09-17T10:49:09.296610Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T11:01:29.736138Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:28.175319Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:26.626958Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:25.058102Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:23.509841Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:21.934416Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:20.027341Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:18.458555Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:16.885741Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:15.295984Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:13.740212Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:12.156398Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:10.599780Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:09.038482Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:01:07.479284Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
