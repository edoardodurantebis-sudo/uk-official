# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T15:07:21.990884Z`  
Current process started UTC: `2026-09-19T15:03:21.963079Z`  
1-second metadata polls in this process: **213**  
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

- `FUELINST|fuelType=INTVKL|generation` = **524** (n=1295, 2026-09-19T15:05:31.865783Z)
- `FUELINST|fuelType=NPSHYD|generation` = **284** (n=1295, 2026-09-19T15:05:31.865783Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1295, 2026-09-19T15:05:31.865783Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1295, 2026-09-19T15:05:31.865783Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1295, 2026-09-19T15:05:31.865783Z)
- `FUELINST|fuelType=OTHER|generation` = **1133** (n=1295, 2026-09-19T15:05:31.865783Z)
- `FUELINST|fuelType=PS|generation` = **-547** (n=1295, 2026-09-19T15:05:31.865783Z)
- `FUELINST|fuelType=WIND|generation` = **13889** (n=1295, 2026-09-19T15:05:31.865783Z)
- `IMBALNGC|TOTAL|imbalance` = **-3174** (n=213, 2026-09-19T14:54:40.238983Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=213, 2026-09-19T14:54:23.818315Z)
- `INDGEN|TOTAL|generation` = **16778** (n=213, 2026-09-19T14:54:23.818315Z)
- `MELNGC|TOTAL|margin` = **36925** (n=213, 2026-09-19T14:51:04.797043Z)
- `NDF|TOTAL|demand` = **19452** (n=218, 2026-09-19T14:48:18.199040Z)
- `TSDF|TOTAL|demand` = **19952** (n=218, 2026-09-19T14:48:18.199040Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T15:07:20.967254Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:19.937993Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:18.937924Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:17.937854Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:16.924057Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:15.903078Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:14.876428Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:13.876361Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:12.835820Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:11.830546Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:10.826435Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:09.825500Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:08.217445Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:07.212816Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:07:06.175880Z` — **MID**: 0 rows; marker `2026-09-19T14:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
