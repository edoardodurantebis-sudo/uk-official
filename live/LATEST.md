# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T12:21:21.943532Z`  
Current process started UTC: `2026-09-17T12:17:21.175321Z`  
1-second metadata polls in this process: **156**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-618** (n=730, 2026-09-17T12:20:35.684343Z)
- `FUELINST|fuelType=NPSHYD|generation` = **253** (n=730, 2026-09-17T12:20:35.684343Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3311** (n=730, 2026-09-17T12:20:35.684343Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=730, 2026-09-17T12:20:35.684343Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=730, 2026-09-17T12:20:35.684343Z)
- `FUELINST|fuelType=OTHER|generation` = **450** (n=730, 2026-09-17T12:20:35.684343Z)
- `FUELINST|fuelType=PS|generation` = **-947** (n=730, 2026-09-17T12:20:35.684343Z)
- `FUELINST|fuelType=WIND|generation` = **14160** (n=730, 2026-09-17T12:20:35.684343Z)
- `IMBALNGC|TOTAL|imbalance` = **11963** (n=120, 2026-09-17T11:53:31.798888Z)
- `INDDEM|TOTAL|demand` = **-11265** (n=120, 2026-09-17T11:53:31.798888Z)
- `INDGEN|TOTAL|generation` = **28506** (n=120, 2026-09-17T11:53:31.798888Z)
- `MELNGC|TOTAL|margin` = **36453** (n=121, 2026-09-17T12:20:35.684343Z)
- `NDF|TOTAL|demand` = **16043** (n=124, 2026-09-17T12:18:41.932920Z)
- `TSDF|TOTAL|demand` = **16543** (n=124, 2026-09-17T12:18:41.932920Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T12:21:20.630432Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:19.327347Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:18.027569Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:16.740366Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:15.423617Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:14.137677Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:12.829679Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:11.477519Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:10.137751Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:08.514484Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:07.077606Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:05.751733Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:04.405773Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:03.099664Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:21:01.808291Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
