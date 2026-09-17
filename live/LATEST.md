# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T10:57:20.880184Z`  
Current process started UTC: `2026-09-17T10:53:20.182679Z`  
1-second metadata polls in this process: **193**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-296** (n=713, 2026-09-17T10:55:42.964470Z)
- `FUELINST|fuelType=NPSHYD|generation` = **271** (n=713, 2026-09-17T10:55:42.964470Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3308** (n=713, 2026-09-17T10:55:42.964470Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=713, 2026-09-17T10:55:42.964470Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=713, 2026-09-17T10:55:42.964470Z)
- `FUELINST|fuelType=OTHER|generation` = **699** (n=713, 2026-09-17T10:55:42.964470Z)
- `FUELINST|fuelType=PS|generation` = **-937** (n=713, 2026-09-17T10:55:42.964470Z)
- `FUELINST|fuelType=WIND|generation` = **15569** (n=713, 2026-09-17T10:55:42.964470Z)
- `IMBALNGC|TOTAL|imbalance` = **11942** (n=118, 2026-09-17T10:55:58.735722Z)
- `INDDEM|TOTAL|demand` = **-11265** (n=118, 2026-09-17T10:55:27.413700Z)
- `INDGEN|TOTAL|generation` = **28539** (n=118, 2026-09-17T10:55:42.964470Z)
- `MELNGC|TOTAL|margin` = **36813** (n=118, 2026-09-17T10:51:20.211901Z)
- `NDF|TOTAL|demand` = **16097** (n=121, 2026-09-17T10:49:09.296610Z)
- `TSDF|TOTAL|demand` = **16597** (n=121, 2026-09-17T10:49:09.296610Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T10:57:19.718110Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:18.277794Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:17.100015Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:15.929115Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:14.759826Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:13.592996Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:12.379010Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:11.152774Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:09.960200Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:08.773361Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:07.588082Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:06.426471Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:05.191756Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:04.008495Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T10:57:02.470462Z` — **MID**: 0 rows; marker `2026-09-17T10:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
