# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T20:10:41.461695Z`  
Current process started UTC: `2026-09-19T20:06:40.525325Z`  
1-second metadata polls in this process: **147**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=1, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=-250, z=-0.07 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=100, delta=4, z=5.22 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=378, delta=4, z=13.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=105, delta=5, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=251, delta=-152, z=6.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=100, delta=1, z=4.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=11.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=11.75 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=404, delta=1, z=12.44 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=13.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.98 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1355, 2026-09-19T20:05:28.092800Z)
- `FUELINST|fuelType=NPSHYD|generation` = **490** (n=1355, 2026-09-19T20:05:28.092800Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1355, 2026-09-19T20:05:28.092800Z)
- `FUELINST|fuelType=OCGT|generation` = **106** (n=1355, 2026-09-19T20:05:28.092800Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1355, 2026-09-19T20:05:28.092800Z)
- `FUELINST|fuelType=OTHER|generation` = **773** (n=1355, 2026-09-19T20:05:28.092800Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1355, 2026-09-19T20:05:28.092800Z)
- `FUELINST|fuelType=WIND|generation` = **13958** (n=1355, 2026-09-19T20:05:28.092800Z)
- `IMBALNGC|TOTAL|imbalance` = **-3790** (n=223, 2026-09-19T19:52:47.570321Z)
- `INDDEM|TOTAL|demand` = **-11873** (n=223, 2026-09-19T19:52:31.555589Z)
- `INDGEN|TOTAL|generation` = **16162** (n=223, 2026-09-19T19:52:47.570321Z)
- `MELNGC|TOTAL|margin` = **36216** (n=223, 2026-09-19T19:50:05.899376Z)
- `NDF|TOTAL|demand` = **19452** (n=228, 2026-09-19T19:48:04.844285Z)
- `TSDF|TOTAL|demand` = **19952** (n=228, 2026-09-19T19:48:04.844285Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T20:10:39.902214Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:38.361515Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:36.808387Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:35.249664Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:33.735204Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:32.187232Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:30.618183Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:27.135357Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:27.135357Z` — **FREQ**: 5761 rows; marker `2026-09-19T20:09:45Z`
- `2026-09-19T20:10:25.571416Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:24.012417Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:22.482275Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:20.934497Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:19.365246Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:10:17.807762Z` — **MID**: 0 rows; marker `2026-09-19T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
