# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T20:27:40.386248Z`  
Current process started UTC: `2026-09-19T20:23:40.006271Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=11.75 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.88 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1359, 2026-09-19T20:25:33.694061Z)
- `FUELINST|fuelType=NPSHYD|generation` = **486** (n=1359, 2026-09-19T20:25:33.694061Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3340** (n=1359, 2026-09-19T20:25:33.694061Z)
- `FUELINST|fuelType=OCGT|generation` = **92** (n=1359, 2026-09-19T20:25:33.694061Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1359, 2026-09-19T20:25:33.694061Z)
- `FUELINST|fuelType=OTHER|generation` = **552** (n=1359, 2026-09-19T20:25:33.694061Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1359, 2026-09-19T20:25:33.694061Z)
- `FUELINST|fuelType=WIND|generation` = **14231** (n=1359, 2026-09-19T20:25:33.694061Z)
- `IMBALNGC|TOTAL|imbalance` = **-3820** (n=224, 2026-09-19T20:22:42.485438Z)
- `INDDEM|TOTAL|demand` = **-11873** (n=224, 2026-09-19T20:22:26.195138Z)
- `INDGEN|TOTAL|generation` = **16132** (n=224, 2026-09-19T20:22:26.195138Z)
- `MELNGC|TOTAL|margin` = **36251** (n=224, 2026-09-19T20:20:18.046700Z)
- `NDF|TOTAL|demand` = **19452** (n=229, 2026-09-19T20:17:59.606414Z)
- `TSDF|TOTAL|demand` = **19952** (n=229, 2026-09-19T20:17:59.606414Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T20:27:39.442922Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:38.442812Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:37.442730Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:36.442623Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:35.442503Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:34.435169Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:33.435067Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:32.434959Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:31.434889Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:30.434763Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:29.434685Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:27.997022Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:26.996911Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:25.996795Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:27:24.996677Z` — **MID**: 0 rows; marker `2026-09-19T20:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
