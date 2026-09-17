# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T15:18:39.104623Z`  
Current process started UTC: `2026-09-17T15:14:38.283276Z`  
1-second metadata polls in this process: **167**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-11265, delta=1771, z=1.70 -> demand pressure up

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=765, 2026-09-17T15:15:27.338861Z)
- `FUELINST|fuelType=NPSHYD|generation` = **339** (n=765, 2026-09-17T15:15:27.338861Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3308** (n=765, 2026-09-17T15:15:27.338861Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=765, 2026-09-17T15:15:27.338861Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=765, 2026-09-17T15:15:27.338861Z)
- `FUELINST|fuelType=OTHER|generation` = **642** (n=765, 2026-09-17T15:15:27.338861Z)
- `FUELINST|fuelType=PS|generation` = **-645** (n=765, 2026-09-17T15:15:27.338861Z)
- `FUELINST|fuelType=WIND|generation` = **13098** (n=765, 2026-09-17T15:15:27.338861Z)
- `IMBALNGC|TOTAL|imbalance` = **11677** (n=126, 2026-09-17T14:56:26.037019Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=126, 2026-09-17T14:56:09.655477Z)
- `INDGEN|TOTAL|generation` = **28491** (n=126, 2026-09-17T14:56:09.655477Z)
- `MELNGC|TOTAL|margin` = **35653** (n=126, 2026-09-17T14:52:28.971543Z)
- `NDF|TOTAL|demand` = **16314** (n=129, 2026-09-17T14:49:14.579204Z)
- `TSDF|TOTAL|demand` = **16814** (n=129, 2026-09-17T14:49:30.280692Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T15:18:37.786423Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:36.442522Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:35.102500Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:33.533761Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:32.102075Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:30.749149Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:29.374927Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:28.020905Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:24.811591Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:24.811591Z` — **FREQ**: 5761 rows; marker `2026-09-17T15:17:45Z`
- `2026-09-17T15:18:23.458125Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:22.080410Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:20.728428Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:19.393650Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:18:18.029840Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
