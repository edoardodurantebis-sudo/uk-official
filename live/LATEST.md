# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T15:11:32.340488Z`  
Current process started UTC: `2026-09-19T15:07:31.893233Z`  
1-second metadata polls in this process: **145**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-92, delta=10, z=-8.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-31, delta=73, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.20 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-102, delta=-202, z=-12.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=-15, z=-11.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-89, delta=-179, z=-10.03 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=100, delta=26, z=19.67 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **702** (n=1296, 2026-09-19T15:10:31.904758Z)
- `FUELINST|fuelType=NPSHYD|generation` = **285** (n=1296, 2026-09-19T15:10:31.904758Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1296, 2026-09-19T15:10:31.904758Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1296, 2026-09-19T15:10:31.904758Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1296, 2026-09-19T15:10:31.904758Z)
- `FUELINST|fuelType=OTHER|generation` = **882** (n=1296, 2026-09-19T15:10:31.904758Z)
- `FUELINST|fuelType=PS|generation` = **-633** (n=1296, 2026-09-19T15:10:31.904758Z)
- `FUELINST|fuelType=WIND|generation` = **14183** (n=1296, 2026-09-19T15:10:31.904758Z)
- `IMBALNGC|TOTAL|imbalance` = **-3174** (n=213, 2026-09-19T14:54:40.238983Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=213, 2026-09-19T14:54:23.818315Z)
- `INDGEN|TOTAL|generation` = **16778** (n=213, 2026-09-19T14:54:23.818315Z)
- `MELNGC|TOTAL|margin` = **36925** (n=213, 2026-09-19T14:51:04.797043Z)
- `NDF|TOTAL|demand` = **19452** (n=218, 2026-09-19T14:48:18.199040Z)
- `TSDF|TOTAL|demand` = **19952** (n=218, 2026-09-19T14:48:18.199040Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T15:11:30.759034Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:29.199337Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:27.656167Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:26.129113Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:24.564584Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:23.031663Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:20.958161Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:19.407499Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:17.800338Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:16.238060Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:14.711632Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:13.186518Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:11.613240Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:10.071922Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:11:08.546562Z` — **MID**: 0 rows; marker `2026-09-19T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
