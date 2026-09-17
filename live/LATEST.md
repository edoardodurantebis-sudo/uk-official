# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T12:38:10.124299Z`  
Current process started UTC: `2026-09-17T12:34:10.142451Z`  
1-second metadata polls in this process: **229**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-618** (n=733, 2026-09-17T12:35:29.369442Z)
- `FUELINST|fuelType=NPSHYD|generation` = **256** (n=733, 2026-09-17T12:35:29.369442Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3304** (n=733, 2026-09-17T12:35:29.369442Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=733, 2026-09-17T12:35:29.369442Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=733, 2026-09-17T12:35:29.369442Z)
- `FUELINST|fuelType=OTHER|generation` = **1176** (n=733, 2026-09-17T12:35:29.369442Z)
- `FUELINST|fuelType=PS|generation` = **-915** (n=733, 2026-09-17T12:35:29.369442Z)
- `FUELINST|fuelType=WIND|generation` = **14211** (n=733, 2026-09-17T12:35:29.369442Z)
- `IMBALNGC|TOTAL|imbalance` = **11939** (n=121, 2026-09-17T12:24:37.200930Z)
- `INDDEM|TOTAL|demand` = **-11262** (n=121, 2026-09-17T12:24:37.200930Z)
- `INDGEN|TOTAL|generation` = **28482** (n=121, 2026-09-17T12:24:37.200930Z)
- `MELNGC|TOTAL|margin` = **36453** (n=121, 2026-09-17T12:20:35.684343Z)
- `NDF|TOTAL|demand` = **16043** (n=124, 2026-09-17T12:18:41.932920Z)
- `TSDF|TOTAL|demand` = **16543** (n=124, 2026-09-17T12:18:41.932920Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T12:38:09.159386Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:38:08.159264Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:38:07.159139Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:38:06.159007Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:38:05.158884Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:38:04.158747Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:38:03.137920Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:38:02.137798Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:38:01.137693Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:38:00.137630Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:37:59.137500Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:37:58.137367Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:37:57.137243Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:37:56.137150Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:37:54.781193Z` — **MID**: 0 rows; marker `2026-09-17T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
