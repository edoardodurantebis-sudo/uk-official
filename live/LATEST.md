# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T15:35:30.254154Z`  
Current process started UTC: `2026-09-17T15:31:29.972896Z`  
1-second metadata polls in this process: **137**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=14, z=4.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.03 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=768, 2026-09-17T15:30:44.984543Z)
- `FUELINST|fuelType=NPSHYD|generation` = **353** (n=768, 2026-09-17T15:30:44.984543Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3303** (n=768, 2026-09-17T15:30:44.984543Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=768, 2026-09-17T15:30:44.984543Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=768, 2026-09-17T15:30:44.984543Z)
- `FUELINST|fuelType=OTHER|generation` = **813** (n=768, 2026-09-17T15:30:44.984543Z)
- `FUELINST|fuelType=PS|generation` = **-369** (n=768, 2026-09-17T15:30:44.984543Z)
- `FUELINST|fuelType=WIND|generation` = **13549** (n=768, 2026-09-17T15:30:44.984543Z)
- `IMBALNGC|TOTAL|imbalance` = **11656** (n=127, 2026-09-17T15:25:31.201455Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=127, 2026-09-17T15:25:15.240347Z)
- `INDGEN|TOTAL|generation` = **28470** (n=127, 2026-09-17T15:24:58.748219Z)
- `MELNGC|TOTAL|margin` = **35639** (n=127, 2026-09-17T15:21:53.833624Z)
- `NDF|TOTAL|demand` = **16314** (n=130, 2026-09-17T15:18:51.661313Z)
- `TSDF|TOTAL|demand` = **16814** (n=130, 2026-09-17T15:18:51.661313Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T15:35:28.694991Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:27.101138Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:25.463639Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:23.891997Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:22.332040Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:20.404383Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:18.757536Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:17.189249Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:15.583002Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:14.032069Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:12.455423Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:10.890288Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:09.290529Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:07.694249Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:35:06.106901Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
