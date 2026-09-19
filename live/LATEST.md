# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T18:33:57.938377Z`  
Current process started UTC: `2026-09-19T18:29:57.889110Z`  
1-second metadata polls in this process: **203**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1336, 2026-09-19T18:30:30.217685Z)
- `FUELINST|fuelType=NPSHYD|generation` = **501** (n=1336, 2026-09-19T18:30:30.217685Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1336, 2026-09-19T18:30:30.217685Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1336, 2026-09-19T18:30:30.217685Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1336, 2026-09-19T18:30:30.217685Z)
- `FUELINST|fuelType=OTHER|generation` = **998** (n=1336, 2026-09-19T18:30:30.217685Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1336, 2026-09-19T18:30:30.217685Z)
- `FUELINST|fuelType=WIND|generation` = **14183** (n=1336, 2026-09-19T18:30:30.217685Z)
- `IMBALNGC|TOTAL|imbalance` = **-3750** (n=220, 2026-09-19T18:22:57.004790Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=220, 2026-09-19T18:22:40.062173Z)
- `INDGEN|TOTAL|generation` = **16202** (n=220, 2026-09-19T18:22:40.062173Z)
- `MELNGC|TOTAL|margin` = **36202** (n=220, 2026-09-19T18:20:22.618497Z)
- `NDF|TOTAL|demand` = **19452** (n=225, 2026-09-19T18:18:14.376223Z)
- `TSDF|TOTAL|demand` = **19952** (n=225, 2026-09-19T18:18:14.376223Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T18:33:56.986815Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:55.986744Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:54.986634Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:53.986558Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:52.986437Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:51.986305Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:50.986190Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:49.986069Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:48.985989Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:47.985878Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:46.985772Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:45.985657Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:44.867246Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:43.347589Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:33:42.347511Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
