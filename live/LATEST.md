# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T15:43:57.486685Z`  
Current process started UTC: `2026-09-17T15:39:57.239020Z`  
1-second metadata polls in this process: **226**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **TSDF** `TOTAL` `demand` — transmission-demand forecast [TOTAL] demand: value=16543, delta=0, z=-3.52 -> demand pressure easing

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-433** (n=770, 2026-09-17T15:40:29.884417Z)
- `FUELINST|fuelType=NPSHYD|generation` = **364** (n=770, 2026-09-17T15:40:29.884417Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3311** (n=770, 2026-09-17T15:40:29.884417Z)
- `FUELINST|fuelType=OCGT|generation` = **58** (n=770, 2026-09-17T15:40:29.884417Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=770, 2026-09-17T15:40:29.884417Z)
- `FUELINST|fuelType=OTHER|generation` = **774** (n=770, 2026-09-17T15:40:29.884417Z)
- `FUELINST|fuelType=PS|generation` = **-275** (n=770, 2026-09-17T15:40:29.884417Z)
- `FUELINST|fuelType=WIND|generation` = **13736** (n=770, 2026-09-17T15:40:29.884417Z)
- `IMBALNGC|TOTAL|imbalance` = **11656** (n=127, 2026-09-17T15:25:31.201455Z)
- `INDDEM|TOTAL|demand` = **-11280** (n=127, 2026-09-17T15:25:15.240347Z)
- `INDGEN|TOTAL|generation` = **28470** (n=127, 2026-09-17T15:24:58.748219Z)
- `MELNGC|TOTAL|margin` = **35639** (n=127, 2026-09-17T15:21:53.833624Z)
- `NDF|TOTAL|demand` = **16314** (n=130, 2026-09-17T15:18:51.661313Z)
- `TSDF|TOTAL|demand` = **16814** (n=130, 2026-09-17T15:18:51.661313Z)
- `WINDFOR|TOTAL|generation` = **18985** (n=22, 2026-09-17T12:30:48.539400Z)

## Latest publication events

- `2026-09-17T15:43:56.496489Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:55.032715Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:54.019803Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:53.017249Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:51.994720Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:50.992153Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:49.959570Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:48.923963Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:47.923895Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:46.888703Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:45.826629Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:44.824066Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:43.811812Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:42.811745Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T15:43:41.804563Z` — **MID**: 0 rows; marker `2026-09-17T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
