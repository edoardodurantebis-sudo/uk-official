# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T13:07:43.775042Z`  
Current process started UTC: `2026-09-17T13:03:42.980326Z`  
1-second metadata polls in this process: **233**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-254** (n=739, 2026-09-17T13:05:35.273329Z)
- `FUELINST|fuelType=NPSHYD|generation` = **255** (n=739, 2026-09-17T13:05:35.273329Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3307** (n=739, 2026-09-17T13:05:35.273329Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=739, 2026-09-17T13:05:35.273329Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=739, 2026-09-17T13:05:35.273329Z)
- `FUELINST|fuelType=OTHER|generation` = **875** (n=739, 2026-09-17T13:05:35.273329Z)
- `FUELINST|fuelType=PS|generation` = **-688** (n=739, 2026-09-17T13:05:35.273329Z)
- `FUELINST|fuelType=WIND|generation` = **13522** (n=739, 2026-09-17T13:05:35.273329Z)
- `IMBALNGC|TOTAL|imbalance` = **11936** (n=122, 2026-09-17T12:53:52.857909Z)
- `INDDEM|TOTAL|demand` = **-11262** (n=122, 2026-09-17T12:53:52.857909Z)
- `INDGEN|TOTAL|generation` = **28479** (n=122, 2026-09-17T12:53:52.857909Z)
- `MELNGC|TOTAL|margin` = **36442** (n=122, 2026-09-17T12:51:07.566819Z)
- `NDF|TOTAL|demand` = **16043** (n=125, 2026-09-17T12:48:29.556476Z)
- `TSDF|TOTAL|demand` = **16543** (n=125, 2026-09-17T12:48:29.556476Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T13:07:42.396173Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:41.396049Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:40.395920Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:39.395797Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:38.395708Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:37.395586Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:36.395475Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:35.395345Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:34.395194Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:33.395079Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:32.394999Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:31.394876Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:30.394737Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:29.394640Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:07:28.394505Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
