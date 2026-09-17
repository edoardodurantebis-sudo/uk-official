# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T15:01:41.544748Z`  
Current process started UTC: `2026-09-17T14:57:40.374707Z`  
1-second metadata polls in this process: **132**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=42, delta=42, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.28 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=762, 2026-09-17T15:00:19.630414Z)
- `FUELINST|fuelType=NPSHYD|generation` = **305** (n=762, 2026-09-17T15:00:19.630414Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3302** (n=762, 2026-09-17T15:00:19.630414Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=762, 2026-09-17T15:00:19.630414Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=762, 2026-09-17T15:00:19.630414Z)
- `FUELINST|fuelType=OTHER|generation` = **638** (n=762, 2026-09-17T15:00:19.630414Z)
- `FUELINST|fuelType=PS|generation` = **-649** (n=762, 2026-09-17T15:00:19.630414Z)
- `FUELINST|fuelType=WIND|generation` = **13030** (n=762, 2026-09-17T15:00:19.630414Z)
- `IMBALNGC|TOTAL|imbalance` = **11677** (n=126, 2026-09-17T14:56:26.037019Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=126, 2026-09-17T14:56:09.655477Z)
- `INDGEN|TOTAL|generation` = **28491** (n=126, 2026-09-17T14:56:09.655477Z)
- `MELNGC|TOTAL|margin` = **35653** (n=126, 2026-09-17T14:52:28.971543Z)
- `NDF|TOTAL|demand` = **16314** (n=129, 2026-09-17T14:49:14.579204Z)
- `TSDF|TOTAL|demand` = **16814** (n=129, 2026-09-17T14:49:30.280692Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T15:01:39.791008Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:38.062246Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:36.335816Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:34.389537Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:32.689369Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:30.932166Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:29.207015Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:24.986274Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:23.283441Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:21.453257Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:19.665638Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:17.959687Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:15.475340Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:13.764948Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:01:12.047252Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
