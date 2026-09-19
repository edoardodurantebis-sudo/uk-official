# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T18:46:33.872444Z`  
Current process started UTC: `2026-09-19T18:42:33.640133Z`  
1-second metadata polls in this process: **186**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=92, z=-0.01 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1339, 2026-09-19T18:45:48.071436Z)
- `FUELINST|fuelType=NPSHYD|generation` = **500** (n=1339, 2026-09-19T18:45:48.071436Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1339, 2026-09-19T18:45:48.071436Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1339, 2026-09-19T18:45:48.071436Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1339, 2026-09-19T18:45:48.071436Z)
- `FUELINST|fuelType=OTHER|generation` = **893** (n=1339, 2026-09-19T18:45:48.071436Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1339, 2026-09-19T18:45:48.071436Z)
- `FUELINST|fuelType=WIND|generation` = **14130** (n=1339, 2026-09-19T18:45:48.071436Z)
- `IMBALNGC|TOTAL|imbalance` = **-3750** (n=220, 2026-09-19T18:22:57.004790Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=220, 2026-09-19T18:22:40.062173Z)
- `INDGEN|TOTAL|generation` = **16202** (n=220, 2026-09-19T18:22:40.062173Z)
- `MELNGC|TOTAL|margin` = **36202** (n=220, 2026-09-19T18:20:22.618497Z)
- `NDF|TOTAL|demand` = **19452** (n=225, 2026-09-19T18:18:14.376223Z)
- `TSDF|TOTAL|demand` = **19952** (n=225, 2026-09-19T18:18:14.376223Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T18:46:32.483880Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:30.522353Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:29.300155Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:27.631185Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:26.406431Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:25.163070Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:23.958050Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:22.530792Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:19.839893Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:19.839893Z` — **FREQ**: 5761 rows; marker `2026-09-19T18:45:45Z`
- `2026-09-19T18:46:18.598798Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:17.436447Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:16.234050Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:14.581421Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:46:12.977241Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
