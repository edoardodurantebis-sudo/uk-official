# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T12:55:08.917463Z`  
Current process started UTC: `2026-09-17T12:51:07.566808Z`  
1-second metadata polls in this process: **154**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-618** (n=736, 2026-09-17T12:50:23.570470Z)
- `FUELINST|fuelType=NPSHYD|generation` = **255** (n=736, 2026-09-17T12:50:23.570470Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3300** (n=736, 2026-09-17T12:50:23.570470Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=736, 2026-09-17T12:50:23.570470Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=736, 2026-09-17T12:50:23.570470Z)
- `FUELINST|fuelType=OTHER|generation` = **1131** (n=736, 2026-09-17T12:50:23.570470Z)
- `FUELINST|fuelType=PS|generation` = **-928** (n=736, 2026-09-17T12:50:23.570470Z)
- `FUELINST|fuelType=WIND|generation` = **14246** (n=736, 2026-09-17T12:50:23.570470Z)
- `IMBALNGC|TOTAL|imbalance` = **11936** (n=122, 2026-09-17T12:53:52.857909Z)
- `INDDEM|TOTAL|demand` = **-11262** (n=122, 2026-09-17T12:53:52.857909Z)
- `INDGEN|TOTAL|generation` = **28479** (n=122, 2026-09-17T12:53:52.857909Z)
- `MELNGC|TOTAL|margin` = **36442** (n=122, 2026-09-17T12:51:07.566819Z)
- `NDF|TOTAL|demand` = **16043** (n=125, 2026-09-17T12:48:29.556476Z)
- `TSDF|TOTAL|demand` = **16543** (n=125, 2026-09-17T12:48:29.556476Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T12:55:07.430675Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:55:05.971787Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:55:04.522290Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:55:03.033029Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:55:01.556241Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:54:59.635575Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:54:58.149934Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:54:56.692978Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:54:55.203760Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:54:53.747018Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:54:52.280218Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:54:50.801178Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:54:49.332766Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:54:47.848194Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:54:46.380365Z` — **MID**: 0 rows; marker `2026-09-17T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
