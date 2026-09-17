# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T14:23:52.356705Z`  
Current process started UTC: `2026-09-17T14:19:52.206733Z`  
1-second metadata polls in this process: **232**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=754, 2026-09-17T14:20:27.024427Z)
- `FUELINST|fuelType=NPSHYD|generation` = **273** (n=754, 2026-09-17T14:20:27.024427Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3307** (n=754, 2026-09-17T14:20:27.024427Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=754, 2026-09-17T14:20:27.024427Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=754, 2026-09-17T14:20:27.024427Z)
- `FUELINST|fuelType=OTHER|generation` = **796** (n=754, 2026-09-17T14:20:27.024427Z)
- `FUELINST|fuelType=PS|generation` = **-935** (n=754, 2026-09-17T14:20:27.024427Z)
- `FUELINST|fuelType=WIND|generation` = **12891** (n=754, 2026-09-17T14:20:27.024427Z)
- `IMBALNGC|TOTAL|imbalance` = **11937** (n=124, 2026-09-17T13:56:05.761870Z)
- `INDDEM|TOTAL|demand` = **-11256** (n=124, 2026-09-17T13:55:49.436735Z)
- `INDGEN|TOTAL|generation` = **28480** (n=124, 2026-09-17T13:55:49.436735Z)
- `MELNGC|TOTAL|margin` = **35924** (n=125, 2026-09-17T14:22:51.253441Z)
- `NDF|TOTAL|demand` = **16043** (n=128, 2026-09-17T14:19:23.791920Z)
- `TSDF|TOTAL|demand` = **16543** (n=128, 2026-09-17T14:19:23.791920Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T14:23:51.403222Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:50.403099Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:49.403016Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:48.402937Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:47.402800Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:46.402682Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:45.402561Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:44.402429Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:43.402308Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:42.402194Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:41.402064Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:40.113332Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:39.113212Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:38.113105Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T14:23:37.112975Z` — **MID**: 0 rows; marker `2026-09-17T14:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
