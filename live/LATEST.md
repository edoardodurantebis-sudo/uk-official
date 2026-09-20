# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T02:41:53.581510Z`  
Current process started UTC: `2026-09-20T02:37:51.987929Z`  
1-second metadata polls in this process: **165**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-5.46 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-5.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-5.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-6.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.08 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-6.17 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-6.26 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **329** (n=1434, 2026-09-20T02:40:31.998908Z)
- `FUELINST|fuelType=NPSHYD|generation` = **308** (n=1434, 2026-09-20T02:40:31.998908Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1434, 2026-09-20T02:40:31.998908Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1434, 2026-09-20T02:40:31.998908Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1434, 2026-09-20T02:40:31.998908Z)
- `FUELINST|fuelType=OTHER|generation` = **362** (n=1434, 2026-09-20T02:40:31.998908Z)
- `FUELINST|fuelType=PS|generation` = **-695** (n=1434, 2026-09-20T02:40:31.998908Z)
- `FUELINST|fuelType=WIND|generation` = **15260** (n=1434, 2026-09-20T02:40:31.998908Z)
- `IMBALNGC|TOTAL|imbalance` = **-3755** (n=236, 2026-09-20T02:21:16.829176Z)
- `INDDEM|TOTAL|demand` = **-12197** (n=236, 2026-09-20T02:21:16.829176Z)
- `INDGEN|TOTAL|generation` = **16197** (n=236, 2026-09-20T02:21:16.829176Z)
- `MELNGC|TOTAL|margin` = **37606** (n=236, 2026-09-20T02:19:46.154039Z)
- `NDF|TOTAL|demand` = **19452** (n=241, 2026-09-20T02:17:36.584473Z)
- `TSDF|TOTAL|demand` = **19952** (n=241, 2026-09-20T02:17:36.584473Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T02:41:51.926335Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:50.513222Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:49.092134Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:47.668065Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:46.247447Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:44.778617Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:43.341893Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:41.979110Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:40.545860Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:39.141448Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:37.731139Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:36.071657Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:34.654397Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:33.227525Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:41:31.804410Z` — **MID**: 0 rows; marker `2026-09-20T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
