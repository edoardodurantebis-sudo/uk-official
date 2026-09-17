# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T15:48:07.640939Z`  
Current process started UTC: `2026-09-17T15:44:07.123365Z`  
1-second metadata polls in this process: **223**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=0, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=57, delta=1, z=4.02 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=771, 2026-09-17T15:45:47.808989Z)
- `FUELINST|fuelType=NPSHYD|generation` = **362** (n=771, 2026-09-17T15:45:47.808989Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3309** (n=771, 2026-09-17T15:45:47.808989Z)
- `FUELINST|fuelType=OCGT|generation` = **58** (n=771, 2026-09-17T15:45:47.808989Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=771, 2026-09-17T15:45:47.808989Z)
- `FUELINST|fuelType=OTHER|generation` = **750** (n=771, 2026-09-17T15:45:47.808989Z)
- `FUELINST|fuelType=PS|generation` = **-259** (n=771, 2026-09-17T15:45:47.808989Z)
- `FUELINST|fuelType=WIND|generation` = **13821** (n=771, 2026-09-17T15:45:47.808989Z)
- `IMBALNGC|TOTAL|imbalance` = **11656** (n=127, 2026-09-17T15:25:31.201455Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=127, 2026-09-17T15:25:15.240347Z)
- `INDGEN|TOTAL|generation` = **28470** (n=127, 2026-09-17T15:24:58.748219Z)
- `MELNGC|TOTAL|margin` = **35639** (n=127, 2026-09-17T15:21:53.833624Z)
- `NDF|TOTAL|demand` = **16314** (n=130, 2026-09-17T15:18:51.661313Z)
- `TSDF|TOTAL|demand` = **16814** (n=130, 2026-09-17T15:18:51.661313Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T15:48:06.595960Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:48:05.595862Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:48:04.013713Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:48:03.013634Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:48:01.793003Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:48:00.770812Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:47:59.770736Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:47:58.770654Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:47:57.414916Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:47:55.893407Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:47:54.893340Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:47:53.893218Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:47:52.893126Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:47:51.893009Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:47:50.892871Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
