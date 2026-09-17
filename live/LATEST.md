# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T12:08:43.973994Z`  
Current process started UTC: `2026-09-17T12:04:43.765342Z`  
1-second metadata polls in this process: **228**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.42 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=49, delta=49, z=4.48 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-620** (n=727, 2026-09-17T12:05:32.046180Z)
- `FUELINST|fuelType=NPSHYD|generation` = **267** (n=727, 2026-09-17T12:05:32.046180Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3304** (n=727, 2026-09-17T12:05:32.046180Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=727, 2026-09-17T12:05:32.046180Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=727, 2026-09-17T12:05:32.046180Z)
- `FUELINST|fuelType=OTHER|generation` = **747** (n=727, 2026-09-17T12:05:32.046180Z)
- `FUELINST|fuelType=PS|generation` = **-944** (n=727, 2026-09-17T12:05:32.046180Z)
- `FUELINST|fuelType=WIND|generation` = **14722** (n=727, 2026-09-17T12:05:32.046180Z)
- `IMBALNGC|TOTAL|imbalance` = **11963** (n=120, 2026-09-17T11:53:31.798888Z)
- `INDDEM|TOTAL|demand` = **-11265** (n=120, 2026-09-17T11:53:31.798888Z)
- `INDGEN|TOTAL|generation` = **28506** (n=120, 2026-09-17T11:53:31.798888Z)
- `MELNGC|TOTAL|margin` = **36723** (n=120, 2026-09-17T11:50:23.103050Z)
- `NDF|TOTAL|demand` = **16043** (n=123, 2026-09-17T11:48:45.810334Z)
- `TSDF|TOTAL|demand` = **16543** (n=123, 2026-09-17T11:48:29.902929Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T12:08:42.950307Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:41.950233Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:40.950163Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:39.950063Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:38.949956Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:37.949821Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:36.944057Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:35.943937Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:34.943828Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:33.943725Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:32.943610Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:31.943505Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:30.666336Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:29.666256Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T12:08:28.666148Z` — **MID**: 0 rows; marker `2026-09-17T12:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
