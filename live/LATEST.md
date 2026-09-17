# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T11:05:43.398238Z`  
Current process started UTC: `2026-09-17T11:01:42.132328Z`  
1-second metadata polls in this process: **145**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-535** (n=715, 2026-09-17T11:05:29.732845Z)
- `FUELINST|fuelType=NPSHYD|generation` = **271** (n=715, 2026-09-17T11:05:29.732845Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=715, 2026-09-17T11:05:29.732845Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=715, 2026-09-17T11:05:29.732845Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=715, 2026-09-17T11:05:29.732845Z)
- `FUELINST|fuelType=OTHER|generation` = **996** (n=715, 2026-09-17T11:05:29.732845Z)
- `FUELINST|fuelType=PS|generation` = **-938** (n=715, 2026-09-17T11:05:29.732845Z)
- `FUELINST|fuelType=WIND|generation` = **15391** (n=715, 2026-09-17T11:05:29.732845Z)
- `IMBALNGC|TOTAL|imbalance` = **11942** (n=118, 2026-09-17T10:55:58.735722Z)
- `INDDEM|TOTAL|demand` = **-11265** (n=118, 2026-09-17T10:55:27.413700Z)
- `INDGEN|TOTAL|generation` = **28539** (n=118, 2026-09-17T10:55:42.964470Z)
- `MELNGC|TOTAL|margin` = **36813** (n=118, 2026-09-17T10:51:20.211901Z)
- `NDF|TOTAL|demand` = **16097** (n=121, 2026-09-17T10:49:09.296610Z)
- `TSDF|TOTAL|demand` = **16597** (n=121, 2026-09-17T10:49:09.296610Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T11:05:41.855567Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:40.299044Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:38.736111Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:37.186091Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:35.647055Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:34.026654Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:32.482433Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:29.732845Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:29.732845Z` — **FUELINST**: 80 rows; marker `2026-09-17T11:05:00Z`
- `2026-09-17T11:05:28.188411Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:26.563386Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:25.011452Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:23.461467Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:21.653867Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:05:19.963885Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
