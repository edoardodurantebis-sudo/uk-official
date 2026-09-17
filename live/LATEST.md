# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T13:54:16.257941Z`  
Current process started UTC: `2026-09-17T13:50:15.215813Z`  
1-second metadata polls in this process: **230**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-128** (n=748, 2026-09-17T13:50:31.660941Z)
- `FUELINST|fuelType=NPSHYD|generation` = **255** (n=748, 2026-09-17T13:50:31.660941Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3305** (n=748, 2026-09-17T13:50:31.660941Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=748, 2026-09-17T13:50:31.660941Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=748, 2026-09-17T13:50:31.660941Z)
- `FUELINST|fuelType=OTHER|generation` = **840** (n=748, 2026-09-17T13:50:31.660941Z)
- `FUELINST|fuelType=PS|generation` = **-442** (n=748, 2026-09-17T13:50:31.660941Z)
- `FUELINST|fuelType=WIND|generation` = **12297** (n=748, 2026-09-17T13:50:31.660941Z)
- `IMBALNGC|TOTAL|imbalance` = **11939** (n=123, 2026-09-17T13:26:12.332279Z)
- `INDDEM|TOTAL|demand` = **-11264** (n=123, 2026-09-17T13:25:39.388031Z)
- `INDGEN|TOTAL|generation` = **28483** (n=123, 2026-09-17T13:25:55.833458Z)
- `MELNGC|TOTAL|margin` = **35870** (n=124, 2026-09-17T13:52:37.774938Z)
- `NDF|TOTAL|demand` = **16043** (n=127, 2026-09-17T13:49:18.118297Z)
- `TSDF|TOTAL|demand` = **16543** (n=127, 2026-09-17T13:49:18.118297Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T13:54:13.169273Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:13.169273Z` — **FREQ**: 5761 rows; marker `2026-09-17T13:53:45Z`
- `2026-09-17T13:54:12.151522Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:11.151393Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:10.151281Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:09.151103Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:08.144522Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:07.144399Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:06.144250Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:05.137354Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:04.137267Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:03.137128Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:02.136976Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:01.136837Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:54:00.136709Z` — **MID**: 0 rows; marker `2026-09-17T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
