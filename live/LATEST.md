# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T20:48:37.867841Z`  
Current process started UTC: `2026-09-19T20:44:37.091306Z`  
1-second metadata polls in this process: **201**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=94, delta=-6, z=4.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=-378, z=-0.09 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=92, delta=-14, z=4.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.92 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=4.97 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=0, z=5.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=106, delta=1, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=1, delta=-250, z=-0.07 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=100, delta=4, z=5.22 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=378, delta=4, z=13.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=105, delta=5, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=251, delta=-152, z=6.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=100, delta=1, z=4.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=11.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.84 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1363, 2026-09-19T20:45:25.026025Z)
- `FUELINST|fuelType=NPSHYD|generation` = **475** (n=1363, 2026-09-19T20:45:25.026025Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1363, 2026-09-19T20:45:25.026025Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1363, 2026-09-19T20:45:25.026025Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1363, 2026-09-19T20:45:25.026025Z)
- `FUELINST|fuelType=OTHER|generation` = **646** (n=1363, 2026-09-19T20:45:25.026025Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1363, 2026-09-19T20:45:25.026025Z)
- `FUELINST|fuelType=WIND|generation` = **14349** (n=1363, 2026-09-19T20:45:25.026025Z)
- `IMBALNGC|TOTAL|imbalance` = **-3820** (n=224, 2026-09-19T20:22:42.485438Z)
- `INDDEM|TOTAL|demand` = **-11873** (n=224, 2026-09-19T20:22:26.195138Z)
- `INDGEN|TOTAL|generation` = **16132** (n=224, 2026-09-19T20:22:26.195138Z)
- `MELNGC|TOTAL|margin` = **36251** (n=224, 2026-09-19T20:20:18.046700Z)
- `NDF|TOTAL|demand` = **19452** (n=230, 2026-09-19T20:47:50.435946Z)
- `TSDF|TOTAL|demand` = **19952** (n=230, 2026-09-19T20:47:50.435946Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T20:48:36.845103Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:35.838927Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:34.818347Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:33.814057Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:32.784516Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:31.673850Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:30.531920Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:29.484894Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:28.461026Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:27.398914Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:26.352466Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:25.075371Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:22.640286Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:48:22.640286Z` — **FREQ**: 5761 rows; marker `2026-09-19T20:47:45Z`
- `2026-09-19T20:48:21.588891Z` — **MID**: 0 rows; marker `2026-09-19T20:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
