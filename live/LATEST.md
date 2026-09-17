# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T12:25:34.605392Z`  
Current process started UTC: `2026-09-17T12:21:33.948794Z`  
1-second metadata polls in this process: **169**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-618** (n=731, 2026-09-17T12:25:25.768794Z)
- `FUELINST|fuelType=NPSHYD|generation` = **254** (n=731, 2026-09-17T12:25:25.768794Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3308** (n=731, 2026-09-17T12:25:25.768794Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=731, 2026-09-17T12:25:25.768794Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=731, 2026-09-17T12:25:25.768794Z)
- `FUELINST|fuelType=OTHER|generation` = **570** (n=731, 2026-09-17T12:25:25.768794Z)
- `FUELINST|fuelType=PS|generation` = **-953** (n=731, 2026-09-17T12:25:25.768794Z)
- `FUELINST|fuelType=WIND|generation` = **14147** (n=731, 2026-09-17T12:25:25.768794Z)
- `IMBALNGC|TOTAL|imbalance` = **11939** (n=121, 2026-09-17T12:24:37.200930Z)
- `INDDEM|TOTAL|demand` = **-11262** (n=121, 2026-09-17T12:24:37.200930Z)
- `INDGEN|TOTAL|generation` = **28482** (n=121, 2026-09-17T12:24:37.200930Z)
- `MELNGC|TOTAL|margin` = **36453** (n=121, 2026-09-17T12:20:35.684343Z)
- `NDF|TOTAL|demand` = **16043** (n=124, 2026-09-17T12:18:41.932920Z)
- `TSDF|TOTAL|demand` = **16543** (n=124, 2026-09-17T12:18:41.932920Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T12:25:33.292481Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:31.989168Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:30.599457Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:29.278886Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:25.768794Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:25.768794Z` — **FUELINST**: 80 rows; marker `2026-09-17T12:25:00Z`
- `2026-09-17T12:25:24.436650Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:23.119280Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:21.827356Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:20.527434Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:19.187118Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:17.876119Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:16.567580Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:15.262888Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:25:13.945961Z` — **MID**: 0 rows; marker `2026-09-17T12:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
