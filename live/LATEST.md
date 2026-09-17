# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T14:02:42.200228Z`  
Current process started UTC: `2026-09-17T13:58:41.928064Z`  
1-second metadata polls in this process: **211**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-200** (n=750, 2026-09-17T14:00:32.749966Z)
- `FUELINST|fuelType=NPSHYD|generation` = **260** (n=750, 2026-09-17T14:00:32.749966Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3304** (n=750, 2026-09-17T14:00:32.749966Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=750, 2026-09-17T14:00:32.749966Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=750, 2026-09-17T14:00:32.749966Z)
- `FUELINST|fuelType=OTHER|generation` = **710** (n=750, 2026-09-17T14:00:32.749966Z)
- `FUELINST|fuelType=PS|generation` = **-821** (n=750, 2026-09-17T14:00:32.749966Z)
- `FUELINST|fuelType=WIND|generation` = **12683** (n=750, 2026-09-17T14:00:32.749966Z)
- `IMBALNGC|TOTAL|imbalance` = **11937** (n=124, 2026-09-17T13:56:05.761870Z)
- `INDDEM|TOTAL|demand` = **-11256** (n=124, 2026-09-17T13:55:49.436735Z)
- `INDGEN|TOTAL|generation` = **28480** (n=124, 2026-09-17T13:55:49.436735Z)
- `MELNGC|TOTAL|margin` = **35870** (n=124, 2026-09-17T13:52:37.774938Z)
- `NDF|TOTAL|demand` = **16043** (n=127, 2026-09-17T13:49:18.118297Z)
- `TSDF|TOTAL|demand` = **16543** (n=127, 2026-09-17T13:49:18.118297Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T14:02:40.760039Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:39.553399Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:38.116776Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:36.622974Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:35.142225Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:33.626650Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:32.521747Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:31.224084Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:29.426146Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:28.418873Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:26.839705Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:24.269938Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:24.269938Z` — **FREQ**: 5761 rows; marker `2026-09-17T14:01:45Z`
- `2026-09-17T14:02:22.927680Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:02:20.816288Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
