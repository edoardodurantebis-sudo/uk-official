# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T15:22:53.053169Z`  
Current process started UTC: `2026-09-17T15:18:51.661305Z`  
1-second metadata polls in this process: **141**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.13 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.23 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=42, delta=42, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=1, z=4.28 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=2, z=4.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=1, z=4.14 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=52, delta=18, z=4.10 -> generation-mix component moved
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=0, z=-3.52 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16043, delta=0, z=-3.54 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16043, delta=0, z=-3.76 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=0, z=-3.73 -> demand pressure easing
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=-54, z=-3.99 -> demand pressure easing
- **NDF** `TOTAL` `demand` — national-demand forecast [TOTAL] demand: value=16043, delta=-54, z=-4.02 -> demand pressure easing

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=766, 2026-09-17T15:20:30.950790Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=766, 2026-09-17T15:20:30.950790Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3304** (n=766, 2026-09-17T15:20:30.950790Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=766, 2026-09-17T15:20:30.950790Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=766, 2026-09-17T15:20:30.950790Z)
- `FUELINST|fuelType=OTHER|generation` = **653** (n=766, 2026-09-17T15:20:30.950790Z)
- `FUELINST|fuelType=PS|generation` = **-465** (n=766, 2026-09-17T15:20:30.950790Z)
- `FUELINST|fuelType=WIND|generation` = **13118** (n=766, 2026-09-17T15:20:30.950790Z)
- `IMBALNGC|TOTAL|imbalance` = **11677** (n=126, 2026-09-17T14:56:26.037019Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=126, 2026-09-17T14:56:09.655477Z)
- `INDGEN|TOTAL|generation` = **28491** (n=126, 2026-09-17T14:56:09.655477Z)
- `MELNGC|TOTAL|margin` = **35639** (n=127, 2026-09-17T15:21:53.833624Z)
- `NDF|TOTAL|demand` = **16314** (n=130, 2026-09-17T15:18:51.661313Z)
- `TSDF|TOTAL|demand` = **16814** (n=130, 2026-09-17T15:18:51.661313Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T15:22:51.470524Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:49.853583Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:48.224421Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:46.652663Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:45.014798Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:42.924740Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:41.357753Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:39.715659Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:38.065908Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:36.470586Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:34.903391Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:33.238026Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:31.600377Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:29.942874Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:22:28.370525Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
