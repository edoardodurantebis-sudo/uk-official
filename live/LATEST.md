# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T13:16:11.777052Z`  
Current process started UTC: `2026-09-17T13:12:08.936923Z`  
1-second metadata polls in this process: **134**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.36 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-128** (n=741, 2026-09-17T13:15:35.863720Z)
- `FUELINST|fuelType=NPSHYD|generation` = **255** (n=741, 2026-09-17T13:15:35.863720Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=741, 2026-09-17T13:15:35.863720Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=741, 2026-09-17T13:15:35.863720Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=741, 2026-09-17T13:15:35.863720Z)
- `FUELINST|fuelType=OTHER|generation` = **1029** (n=741, 2026-09-17T13:15:35.863720Z)
- `FUELINST|fuelType=PS|generation` = **-685** (n=741, 2026-09-17T13:15:35.863720Z)
- `FUELINST|fuelType=WIND|generation` = **13491** (n=741, 2026-09-17T13:15:35.863720Z)
- `IMBALNGC|TOTAL|imbalance` = **11936** (n=122, 2026-09-17T12:53:52.857909Z)
- `INDDEM|TOTAL|demand` = **-11262** (n=122, 2026-09-17T12:53:52.857909Z)
- `INDGEN|TOTAL|generation` = **28479** (n=122, 2026-09-17T12:53:52.857909Z)
- `MELNGC|TOTAL|margin` = **36442** (n=122, 2026-09-17T12:51:07.566819Z)
- `NDF|TOTAL|demand` = **16043** (n=125, 2026-09-17T12:48:29.556476Z)
- `TSDF|TOTAL|demand` = **16543** (n=125, 2026-09-17T12:48:29.556476Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T13:16:08.139855Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:16:08.139855Z` — **FREQ**: 5761 rows; marker `2026-09-17T13:15:45Z`
- `2026-09-17T13:16:06.392280Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:16:04.691035Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:16:02.943956Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:16:01.244030Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:15:59.530219Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:15:57.814255Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:15:56.099876Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:15:54.388890Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:15:52.316407Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:15:50.597716Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:15:48.907737Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:15:47.183076Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:15:45.480255Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
