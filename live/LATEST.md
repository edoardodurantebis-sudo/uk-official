# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T14:49:02.218903Z`  
Current process started UTC: `2026-09-17T14:45:02.096539Z`  
1-second metadata polls in this process: **192**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.29 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=759, 2026-09-17T14:45:34.490379Z)
- `FUELINST|fuelType=NPSHYD|generation` = **293** (n=759, 2026-09-17T14:45:34.490379Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3305** (n=759, 2026-09-17T14:45:34.490379Z)
- `FUELINST|fuelType=OCGT|generation` = **52** (n=759, 2026-09-17T14:45:34.490379Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=759, 2026-09-17T14:45:34.490379Z)
- `FUELINST|fuelType=OTHER|generation` = **780** (n=759, 2026-09-17T14:45:34.490379Z)
- `FUELINST|fuelType=PS|generation` = **-925** (n=759, 2026-09-17T14:45:34.490379Z)
- `FUELINST|fuelType=WIND|generation` = **13007** (n=759, 2026-09-17T14:45:34.490379Z)
- `IMBALNGC|TOTAL|imbalance` = **11938** (n=125, 2026-09-17T14:26:58.877946Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=125, 2026-09-17T14:26:43.464918Z)
- `INDGEN|TOTAL|generation` = **28481** (n=125, 2026-09-17T14:26:43.464918Z)
- `MELNGC|TOTAL|margin` = **35924** (n=125, 2026-09-17T14:22:51.253441Z)
- `NDF|TOTAL|demand` = **16043** (n=128, 2026-09-17T14:19:23.791920Z)
- `TSDF|TOTAL|demand` = **16543** (n=128, 2026-09-17T14:19:23.791920Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T14:49:01.008561Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:59.777632Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:58.564644Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:57.364965Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:56.138418Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:54.926262Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:53.703711Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:52.510130Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:51.290376Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:50.112217Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:48.846582Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:47.642852Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:46.118288Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:44.908390Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:48:43.714985Z` — **MID**: 0 rows; marker `2026-09-17T14:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
