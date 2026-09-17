# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T14:53:15.569580Z`  
Current process started UTC: `2026-09-17T14:49:14.579197Z`  
1-second metadata polls in this process: **154**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=1, z=4.14 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=18, z=4.10 -> generation-mix component moved
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=0, z=-3.52 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16043, delta=0, z=-3.54 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16043, delta=0, z=-3.76 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=0, z=-3.73 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=-54, z=-3.99 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16043, delta=-54, z=-4.02 -> demand pressure easing
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11265, delta=1771, z=1.70 -> demand pressure up
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16597, delta=-3265, z=-4.21 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16097, delta=-2159, z=-4.24 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16658, delta=-2713, z=-4.41 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16158, delta=-2463, z=-4.57 -> demand pressure easing
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=2, delta=-50, z=-0.16 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=-4, z=3.91 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=760, 2026-09-17T14:50:35.236948Z)
- `FUELINST|fuelType=NPSHYD|generation` = **294** (n=760, 2026-09-17T14:50:35.236948Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3305** (n=760, 2026-09-17T14:50:35.236948Z)
- `FUELINST|fuelType=OCGT|generation` = **53** (n=760, 2026-09-17T14:50:35.236948Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=760, 2026-09-17T14:50:35.236948Z)
- `FUELINST|fuelType=OTHER|generation` = **796** (n=760, 2026-09-17T14:50:35.236948Z)
- `FUELINST|fuelType=PS|generation` = **-746** (n=760, 2026-09-17T14:50:35.236948Z)
- `FUELINST|fuelType=WIND|generation` = **12960** (n=760, 2026-09-17T14:50:35.236948Z)
- `IMBALNGC|TOTAL|imbalance` = **11938** (n=125, 2026-09-17T14:26:58.877946Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=125, 2026-09-17T14:26:43.464918Z)
- `INDGEN|TOTAL|generation` = **28481** (n=125, 2026-09-17T14:26:43.464918Z)
- `MELNGC|TOTAL|margin` = **35653** (n=126, 2026-09-17T14:52:28.971543Z)
- `NDF|TOTAL|demand` = **16314** (n=129, 2026-09-17T14:49:14.579204Z)
- `TSDF|TOTAL|demand` = **16814** (n=129, 2026-09-17T14:49:30.280692Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T14:53:14.093524Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:53:12.612626Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:53:11.120544Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:53:09.608331Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:53:08.146018Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:53:06.650727Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:53:05.080962Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:53:03.611713Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:53:01.829049Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:53:00.398394Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:52:58.860943Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:52:57.429482Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:52:55.962763Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:52:54.473431Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:52:52.953127Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
