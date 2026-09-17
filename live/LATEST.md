# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T14:57:28.986952Z`  
Current process started UTC: `2026-09-17T14:53:27.680813Z`  
1-second metadata polls in this process: **145**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=2, z=4.25 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=761, 2026-09-17T14:55:36.877831Z)
- `FUELINST|fuelType=NPSHYD|generation` = **296** (n=761, 2026-09-17T14:55:36.877831Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3304** (n=761, 2026-09-17T14:55:36.877831Z)
- `FUELINST|fuelType=OCGT|generation` = **55** (n=761, 2026-09-17T14:55:36.877831Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=761, 2026-09-17T14:55:36.877831Z)
- `FUELINST|fuelType=OTHER|generation` = **666** (n=761, 2026-09-17T14:55:36.877831Z)
- `FUELINST|fuelType=PS|generation` = **-644** (n=761, 2026-09-17T14:55:36.877831Z)
- `FUELINST|fuelType=WIND|generation` = **12908** (n=761, 2026-09-17T14:55:36.877831Z)
- `IMBALNGC|TOTAL|imbalance` = **11677** (n=126, 2026-09-17T14:56:26.037019Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=126, 2026-09-17T14:56:09.655477Z)
- `INDGEN|TOTAL|generation` = **28491** (n=126, 2026-09-17T14:56:09.655477Z)
- `MELNGC|TOTAL|margin` = **35653** (n=126, 2026-09-17T14:52:28.971543Z)
- `NDF|TOTAL|demand` = **16314** (n=129, 2026-09-17T14:49:14.579204Z)
- `TSDF|TOTAL|demand` = **16814** (n=129, 2026-09-17T14:49:30.280692Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T14:57:27.395492Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:25.847462Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:24.292254Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:22.734505Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:21.115782Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:19.508427Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:17.919882Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:16.362309Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:14.494139Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:12.569623Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:11.000487Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:09.428980Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:07.870866Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:06.311956Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:57:04.713096Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
