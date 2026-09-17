# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T13:20:25.384210Z`  
Current process started UTC: `2026-09-17T13:16:24.625211Z`  
1-second metadata polls in this process: **226**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-128** (n=742, 2026-09-17T13:20:20.570100Z)
- `FUELINST|fuelType=NPSHYD|generation` = **254** (n=742, 2026-09-17T13:20:20.570100Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3306** (n=742, 2026-09-17T13:20:20.570100Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=742, 2026-09-17T13:20:20.570100Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=742, 2026-09-17T13:20:20.570100Z)
- `FUELINST|fuelType=OTHER|generation` = **794** (n=742, 2026-09-17T13:20:20.570100Z)
- `FUELINST|fuelType=PS|generation` = **-690** (n=742, 2026-09-17T13:20:20.570100Z)
- `FUELINST|fuelType=WIND|generation` = **13387** (n=742, 2026-09-17T13:20:20.570100Z)
- `IMBALNGC|TOTAL|imbalance` = **11936** (n=122, 2026-09-17T12:53:52.857909Z)
- `INDDEM|TOTAL|demand` = **-11262** (n=122, 2026-09-17T12:53:52.857909Z)
- `INDGEN|TOTAL|generation` = **28479** (n=122, 2026-09-17T12:53:52.857909Z)
- `MELNGC|TOTAL|margin` = **36442** (n=122, 2026-09-17T12:51:07.566819Z)
- `NDF|TOTAL|demand` = **16043** (n=126, 2026-09-17T13:19:32.791265Z)
- `TSDF|TOTAL|demand` = **16543** (n=126, 2026-09-17T13:19:32.791265Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T13:20:24.389625Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:23.389552Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:20.570100Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:20.570100Z` — **FUELINST**: 80 rows; marker `2026-09-17T13:20:00Z`
- `2026-09-17T13:20:20.570100Z` — **FREQ**: 5761 rows; marker `2026-09-17T13:19:45Z`
- `2026-09-17T13:20:19.539619Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:18.539540Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:17.521930Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:16.521859Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:15.510430Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:14.477029Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:13.404484Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:12.360060Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:11.349240Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:20:10.347335Z` — **MID**: 0 rows; marker `2026-09-17T13:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
