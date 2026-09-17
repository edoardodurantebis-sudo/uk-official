# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T13:37:16.894514Z`  
Current process started UTC: `2026-09-17T13:33:15.371278Z`  
1-second metadata polls in this process: **134**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-128** (n=745, 2026-09-17T13:35:37.143672Z)
- `FUELINST|fuelType=NPSHYD|generation` = **254** (n=745, 2026-09-17T13:35:37.143672Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3308** (n=745, 2026-09-17T13:35:37.143672Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=745, 2026-09-17T13:35:37.143672Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=745, 2026-09-17T13:35:37.143672Z)
- `FUELINST|fuelType=OTHER|generation` = **652** (n=745, 2026-09-17T13:35:37.143672Z)
- `FUELINST|fuelType=PS|generation` = **-697** (n=745, 2026-09-17T13:35:37.143672Z)
- `FUELINST|fuelType=WIND|generation` = **12835** (n=745, 2026-09-17T13:35:37.143672Z)
- `IMBALNGC|TOTAL|imbalance` = **11939** (n=123, 2026-09-17T13:26:12.332279Z)
- `INDDEM|TOTAL|demand` = **-11264** (n=123, 2026-09-17T13:25:39.388031Z)
- `INDGEN|TOTAL|generation` = **28483** (n=123, 2026-09-17T13:25:55.833458Z)
- `MELNGC|TOTAL|margin` = **36448** (n=123, 2026-09-17T13:22:51.041915Z)
- `NDF|TOTAL|demand` = **16043** (n=126, 2026-09-17T13:19:32.791265Z)
- `TSDF|TOTAL|demand` = **16543** (n=126, 2026-09-17T13:19:32.791265Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T13:37:14.813634Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:37:13.110540Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:37:11.348224Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:37:09.370651Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:37:07.660196Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:37:05.959513Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:37:04.210899Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:37:02.508410Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:37:00.790274Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:36:58.594913Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:36:56.844738Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:36:55.098906Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:36:53.361321Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:36:51.663158Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T13:36:49.933298Z` — **MID**: 0 rows; marker `2026-09-17T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
