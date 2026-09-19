# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:59:00.360180Z`  
Current process started UTC: `2026-09-19T14:55:00.061916Z`  
1-second metadata polls in this process: **226**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=90, delta=-13, z=10.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=12.52 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1293, 2026-09-19T14:55:31.611040Z)
- `FUELINST|fuelType=NPSHYD|generation` = **264** (n=1293, 2026-09-19T14:55:31.611040Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1293, 2026-09-19T14:55:31.611040Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1293, 2026-09-19T14:55:31.611040Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1293, 2026-09-19T14:55:31.611040Z)
- `FUELINST|fuelType=OTHER|generation` = **1376** (n=1293, 2026-09-19T14:55:31.611040Z)
- `FUELINST|fuelType=PS|generation` = **-306** (n=1293, 2026-09-19T14:55:31.611040Z)
- `FUELINST|fuelType=WIND|generation` = **13434** (n=1293, 2026-09-19T14:55:31.611040Z)
- `IMBALNGC|TOTAL|imbalance` = **-3174** (n=213, 2026-09-19T14:54:40.238983Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=213, 2026-09-19T14:54:23.818315Z)
- `INDGEN|TOTAL|generation` = **16778** (n=213, 2026-09-19T14:54:23.818315Z)
- `MELNGC|TOTAL|margin` = **36925** (n=213, 2026-09-19T14:51:04.797043Z)
- `NDF|TOTAL|demand` = **19452** (n=218, 2026-09-19T14:48:18.199040Z)
- `TSDF|TOTAL|demand` = **19952** (n=218, 2026-09-19T14:48:18.199040Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:58:59.372925Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:58.372805Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:57.372682Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:56.372557Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:55.365552Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:54.365417Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:53.365292Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:52.339703Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:51.339572Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:49.772489Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:48.772402Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:47.772284Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:46.772209Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:45.772089Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:58:44.771998Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
