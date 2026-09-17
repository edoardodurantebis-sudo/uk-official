# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T15:31:16.536018Z`  
Current process started UTC: `2026-09-17T15:27:15.789155Z`  
1-second metadata polls in this process: **225**  
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

- `2026-09-17T15:31:15.588119Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:14.146990Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:13.146881Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:12.146805Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:10.523223Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:09.283785Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:08.283701Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:07.283582Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:05.830797Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:04.469228Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:03.469159Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:01.525194Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:31:00.154183Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:30:58.742131Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:30:57.742050Z` — **MID**: 0 rows; marker `2026-09-17T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
