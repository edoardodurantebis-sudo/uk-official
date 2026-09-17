# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T13:45:48.717840Z`  
Current process started UTC: `2026-09-17T13:41:48.129487Z`  
1-second metadata polls in this process: **174**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-128** (n=747, 2026-09-17T13:45:37.448626Z)
- `FUELINST|fuelType=NPSHYD|generation` = **255** (n=747, 2026-09-17T13:45:37.448626Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=747, 2026-09-17T13:45:37.448626Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=747, 2026-09-17T13:45:37.448626Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=747, 2026-09-17T13:45:37.448626Z)
- `FUELINST|fuelType=OTHER|generation` = **715** (n=747, 2026-09-17T13:45:37.448626Z)
- `FUELINST|fuelType=PS|generation` = **-686** (n=747, 2026-09-17T13:45:37.448626Z)
- `FUELINST|fuelType=WIND|generation` = **12417** (n=747, 2026-09-17T13:45:37.448626Z)
- `IMBALNGC|TOTAL|imbalance` = **11939** (n=123, 2026-09-17T13:26:12.332279Z)
- `INDDEM|TOTAL|demand` = **-11264** (n=123, 2026-09-17T13:25:39.388031Z)
- `INDGEN|TOTAL|generation` = **28483** (n=123, 2026-09-17T13:25:55.833458Z)
- `MELNGC|TOTAL|margin` = **36448** (n=123, 2026-09-17T13:22:51.041915Z)
- `NDF|TOTAL|demand` = **16043** (n=126, 2026-09-17T13:19:32.791265Z)
- `TSDF|TOTAL|demand` = **16543** (n=126, 2026-09-17T13:19:32.791265Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T13:45:47.429387Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:46.132651Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:44.804361Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:43.502007Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:42.189022Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:40.901291Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:39.615414Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:37.448626Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:37.448626Z` — **FUELINST**: 80 rows; marker `2026-09-17T13:45:00Z`
- `2026-09-17T13:45:36.137745Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:34.827229Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:33.549323Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:32.254801Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:30.948030Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:45:29.593837Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
