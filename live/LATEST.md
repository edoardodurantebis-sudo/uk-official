# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T11:18:19.777127Z`  
Current process started UTC: `2026-09-17T11:14:19.453087Z`  
1-second metadata polls in this process: **226**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-622** (n=717, 2026-09-17T11:15:41.077987Z)
- `FUELINST|fuelType=NPSHYD|generation` = **271** (n=717, 2026-09-17T11:15:41.077987Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3308** (n=717, 2026-09-17T11:15:41.077987Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=717, 2026-09-17T11:15:41.077987Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=717, 2026-09-17T11:15:41.077987Z)
- `FUELINST|fuelType=OTHER|generation` = **994** (n=717, 2026-09-17T11:15:41.077987Z)
- `FUELINST|fuelType=PS|generation` = **-751** (n=717, 2026-09-17T11:15:41.077987Z)
- `FUELINST|fuelType=WIND|generation` = **15084** (n=717, 2026-09-17T11:15:41.077987Z)
- `IMBALNGC|TOTAL|imbalance` = **11942** (n=118, 2026-09-17T10:55:58.735722Z)
- `INDDEM|TOTAL|demand` = **-11265** (n=118, 2026-09-17T10:55:27.413700Z)
- `INDGEN|TOTAL|generation` = **28539** (n=118, 2026-09-17T10:55:42.964470Z)
- `MELNGC|TOTAL|margin` = **36813** (n=118, 2026-09-17T10:51:20.211901Z)
- `NDF|TOTAL|demand` = **16097** (n=121, 2026-09-17T10:49:09.296610Z)
- `TSDF|TOTAL|demand` = **16597** (n=121, 2026-09-17T10:49:09.296610Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T11:18:18.821745Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:17.821648Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:16.821556Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:15.821414Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:14.821345Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:13.821207Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:12.821069Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:11.820960Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:10.703037Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:09.702943Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:08.702865Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:07.528494Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:06.528369Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:05.528274Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:18:04.068148Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
