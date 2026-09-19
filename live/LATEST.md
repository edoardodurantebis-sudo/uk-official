# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T15:03:11.020540Z`  
Current process started UTC: `2026-09-19T14:59:10.857678Z`  
1-second metadata polls in this process: **174**  
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

- `FUELINST|fuelType=INTVKL|generation` = **168** (n=1294, 2026-09-19T15:00:32.714504Z)
- `FUELINST|fuelType=NPSHYD|generation` = **273** (n=1294, 2026-09-19T15:00:32.714504Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1294, 2026-09-19T15:00:32.714504Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1294, 2026-09-19T15:00:32.714504Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1294, 2026-09-19T15:00:32.714504Z)
- `FUELINST|fuelType=OTHER|generation` = **1390** (n=1294, 2026-09-19T15:00:32.714504Z)
- `FUELINST|fuelType=PS|generation` = **-546** (n=1294, 2026-09-19T15:00:32.714504Z)
- `FUELINST|fuelType=WIND|generation` = **13572** (n=1294, 2026-09-19T15:00:32.714504Z)
- `IMBALNGC|TOTAL|imbalance` = **-3174** (n=213, 2026-09-19T14:54:40.238983Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=213, 2026-09-19T14:54:23.818315Z)
- `INDGEN|TOTAL|generation` = **16778** (n=213, 2026-09-19T14:54:23.818315Z)
- `MELNGC|TOTAL|margin` = **36925** (n=213, 2026-09-19T14:51:04.797043Z)
- `NDF|TOTAL|demand` = **19452** (n=218, 2026-09-19T14:48:18.199040Z)
- `TSDF|TOTAL|demand` = **19952** (n=218, 2026-09-19T14:48:18.199040Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T15:03:09.757583Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:03:08.456572Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:03:07.067962Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:03:05.871996Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:03:04.700326Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:03:03.496925Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:03:02.254030Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:03:00.966680Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:02:59.781351Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:02:58.182435Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:02:56.989280Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:02:55.786771Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:02:54.606359Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:02:53.416993Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:02:52.218674Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
