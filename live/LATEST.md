# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T11:30:53.468920Z`  
Current process started UTC: `2026-09-17T11:26:52.730129Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=3, z=4.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=1, z=4.21 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-622** (n=720, 2026-09-17T11:30:45.447399Z)
- `FUELINST|fuelType=NPSHYD|generation` = **270** (n=720, 2026-09-17T11:30:45.447399Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3311** (n=720, 2026-09-17T11:30:45.447399Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=720, 2026-09-17T11:30:45.447399Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=720, 2026-09-17T11:30:45.447399Z)
- `FUELINST|fuelType=OTHER|generation` = **1055** (n=720, 2026-09-17T11:30:45.447399Z)
- `FUELINST|fuelType=PS|generation` = **-942** (n=720, 2026-09-17T11:30:45.447399Z)
- `FUELINST|fuelType=WIND|generation` = **15096** (n=720, 2026-09-17T11:30:45.447399Z)
- `IMBALNGC|TOTAL|imbalance` = **11977** (n=119, 2026-09-17T11:25:20.550344Z)
- `INDDEM|TOTAL|demand` = **-11265** (n=119, 2026-09-17T11:25:04.042533Z)
- `INDGEN|TOTAL|generation` = **28520** (n=119, 2026-09-17T11:25:04.042533Z)
- `MELNGC|TOTAL|margin` = **37089** (n=119, 2026-09-17T11:21:48.268267Z)
- `NDF|TOTAL|demand` = **16043** (n=122, 2026-09-17T11:19:03.596539Z)
- `TSDF|TOTAL|demand` = **16543** (n=122, 2026-09-17T11:19:03.596539Z)
- `WINDFOR|TOTAL|generation` = **19032** (n=21, 2026-09-17T10:30:44.687451Z)

## Latest publication events

- `2026-09-17T11:30:52.493791Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:51.493704Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:50.490162Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:49.490045Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:48.489964Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:47.489841Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:45.447399Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:45.447399Z` — **FUELHH**: 20 rows; marker `2026-09-17T11:30:00Z`
- `2026-09-17T11:30:45.447399Z` — **FUELINST**: 80 rows; marker `2026-09-17T11:30:00Z`
- `2026-09-17T11:30:44.447320Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:43.447205Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:42.447097Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:41.446976Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:40.446844Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T11:30:39.446765Z` — **MID**: 0 rows; marker `2026-09-17T11:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
