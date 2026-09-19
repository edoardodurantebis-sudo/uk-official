# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T15:24:09.007232Z`  
Current process started UTC: `2026-09-19T15:20:08.486995Z`  
1-second metadata polls in this process: **132**  
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

- `FUELINST|fuelType=INTVKL|generation` = **702** (n=1298, 2026-09-19T15:20:40.408921Z)
- `FUELINST|fuelType=NPSHYD|generation` = **307** (n=1298, 2026-09-19T15:20:40.408921Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1298, 2026-09-19T15:20:40.408921Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1298, 2026-09-19T15:20:40.408921Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1298, 2026-09-19T15:20:40.408921Z)
- `FUELINST|fuelType=OTHER|generation` = **1187** (n=1298, 2026-09-19T15:20:40.408921Z)
- `FUELINST|fuelType=PS|generation` = **-516** (n=1298, 2026-09-19T15:20:40.408921Z)
- `FUELINST|fuelType=WIND|generation` = **14104** (n=1298, 2026-09-19T15:20:40.408921Z)
- `IMBALNGC|TOTAL|imbalance` = **-3174** (n=213, 2026-09-19T14:54:40.238983Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=213, 2026-09-19T14:54:23.818315Z)
- `INDGEN|TOTAL|generation` = **16778** (n=213, 2026-09-19T14:54:23.818315Z)
- `MELNGC|TOTAL|margin` = **37039** (n=214, 2026-09-19T15:22:01.787811Z)
- `NDF|TOTAL|demand` = **19452** (n=219, 2026-09-19T15:19:13.284533Z)
- `TSDF|TOTAL|demand` = **19952** (n=219, 2026-09-19T15:19:13.284533Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T15:24:07.281487Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:24:05.581988Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:24:03.877796Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:24:02.157823Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:24:00.453268Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:23:58.750402Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:23:57.034028Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:23:55.319105Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:23:53.134397Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:23:51.345934Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:23:49.605142Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:23:47.909032Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:23:46.179684Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:23:44.469113Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:23:42.768187Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
